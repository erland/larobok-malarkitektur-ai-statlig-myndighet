#!/usr/bin/env python3
import argparse
import os
import re
import subprocess
import sys
import tempfile
import zipfile
import shutil
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "docs" / "export-metadata.yaml"
BUILD_DIR = ROOT / "build"
EXPORTS_DIR = ROOT / "exports"


def fail(message: str) -> None:
    print(f"Fel: {message}", file=sys.stderr)
    sys.exit(1)


def warn(message: str) -> None:
    print(f"Varning: {message}")


def read_metadata() -> dict:
    if not METADATA_PATH.exists():
        fail("docs/export-metadata.yaml saknas.")
    if yaml is None:
        fail("Python-paketet PyYAML saknas. Installera med: pip install pyyaml")
    data = yaml.safe_load(METADATA_PATH.read_text(encoding="utf-8")) or {}
    for key in ["title", "author", "language", "chapters"]:
        if not data.get(key):
            fail(f"Metadatafältet '{key}' saknas eller är tomt.")
    cover_image = data.get("cover_image")
    if cover_image and not (ROOT / cover_image).exists():
        fail(f"Metadatafältet 'cover_image' pekar på saknad fil: {cover_image}")
    return data


def count_table_cells(line: str) -> int:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return -1
    return len([part for part in stripped.split("|")[1:-1]])


def validate_markdown(path: Path, text: str) -> None:
    lines = text.splitlines()
    in_code = False
    fence_count = 0
    for idx, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            in_code = not in_code
            fence_count += 1
        if not in_code and re.match(r"^#{4,}\s+", line):
            fail(f"{path}: rad {idx} använder H4 eller djupare rubrik.")
        if not in_code and re.search(r"<(script|iframe|style)\b", line, re.IGNORECASE):
            fail(f"{path}: rad {idx} innehåller otillåten rå HTML.")
    if fence_count % 2 != 0:
        fail(f"{path}: kodblock verkar sakna avslutande fence.")

    for idx, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip().endswith("|"):
            if idx + 1 < len(lines):
                next_line = lines[idx + 1].strip()
                if re.match(r"^\|[\s:\-|\t]+\|$", next_line):
                    expected = count_table_cells(line)
                    j = idx + 2
                    while j < len(lines) and lines[j].strip().startswith("|") and lines[j].strip().endswith("|"):
                        if count_table_cells(lines[j]) != expected:
                            fail(f"{path}: tabellrad {j + 1} har annat antal celler än rubriken.")
                        j += 1

    for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1)
        if target.startswith(("http://", "https://")):
            continue
        image_path = (path.parent / target).resolve()
        if not image_path.exists():
            fail(f"{path}: bildreferens saknar fil: {target}")


def build_book(metadata: dict) -> Path:
    BUILD_DIR.mkdir(exist_ok=True)
    parts = []
    for chapter in metadata["chapters"]:
        chapter_path = ROOT / chapter
        if not chapter_path.exists():
            fail(f"Kapitel saknas: {chapter}")
        text = chapter_path.read_text(encoding="utf-8")
        validate_markdown(chapter_path, text)
        parts.append(text.strip() + "\n")
    merged = "\n\n".join(parts)
    out = BUILD_DIR / "book.md"
    out.write_text(merged, encoding="utf-8")
    return out


def require_pandoc() -> None:
    try:
        subprocess.run(["pandoc", "--version"], check=True, stdout=subprocess.DEVNULL)
    except Exception:
        fail("Pandoc saknas. Installera Pandoc och försök igen.")


def require_xelatex() -> None:
    try:
        subprocess.run(["xelatex", "--version"], check=True, stdout=subprocess.DEVNULL)
    except Exception:
        fail("xelatex saknas. Installera en LaTeX-motor, exempelvis TinyTeX eller TeX Live.")


def _zip_epub_dir(src_dir: Path, output_path: Path) -> None:
    temp_output = output_path.with_suffix(output_path.suffix + ".tmp")
    if temp_output.exists():
        temp_output.unlink()
    mimetype = src_dir / "mimetype"
    with zipfile.ZipFile(temp_output, "w") as zf:
        if mimetype.exists():
            zf.write(mimetype, "mimetype", compress_type=zipfile.ZIP_STORED)
        for path in sorted(src_dir.rglob("*")):
            if path.is_file():
                rel = path.relative_to(src_dir).as_posix()
                if rel == "mimetype":
                    continue
                zf.write(path, rel, compress_type=zipfile.ZIP_DEFLATED)
    temp_output.replace(output_path)


def _add_class_to_h1(opening_tag: str, class_name: str) -> str:
    if "class=" in opening_tag:
        return re.sub(r'class="([^"]*)"', lambda m: f'class="{m.group(1)} {class_name}"', opening_tag, count=1)
    return opening_tag[:-1] + f' class="{class_name}">'


def post_process_epub(output: Path, metadata: dict) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        with zipfile.ZipFile(output, "r") as zf:
            zf.extractall(tmp)

        title_page = tmp / "EPUB" / "text" / "title_page.xhtml"
        if title_page.exists():
            title = metadata.get("title", "")
            subtitle = metadata.get("subtitle", "")
            author = metadata.get("author", "")
            title_page.write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="sv-SE" xml:lang="sv-SE">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <title>{title}</title>
  <link rel="stylesheet" type="text/css" href="../styles/stylesheet1.css" />
</head>
<body epub:type="frontmatter">
<section epub:type="titlepage" class="titlepage">
  <h1 class="title">{title}</h1>
  <p class="subtitle">{subtitle}</p>
  <p class="author">{author}</p>
</section>
</body>
</html>
""", encoding="utf-8")

        h1_pattern = re.compile(r'(<h1\b[^>]*>)((?:Kapitel\s+\d+|Appendix\s+[A-ZÅÄÖ])):\s*(.*?)(</h1>)', re.DOTALL)
        for xhtml in (tmp / "EPUB" / "text").glob("*.xhtml"):
            text = xhtml.read_text(encoding="utf-8")

            def repl(match: re.Match) -> str:
                opening = _add_class_to_h1(match.group(1), "chapter-heading")
                number = match.group(2).strip()
                heading_title = match.group(3).strip()
                return (
                    f'{opening}<span class="chapter-number">{number}</span>'
                    f'<span class="chapter-title">{heading_title}</span>{match.group(4)}'
                )

            updated = h1_pattern.sub(repl, text)
            if updated != text:
                xhtml.write_text(updated, encoding="utf-8")

        _zip_epub_dir(tmp, output)


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def slug(text: str) -> str:
    value = text.lower().replace("å", "a").replace("ä", "a").replace("ö", "o")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")[:60] or "chapter"


def transform_chapter_for_pdf(text: str) -> str:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if not match:
            continue
        heading = match.group(1).strip()
        anchor = slug(heading)
        split = re.match(r"^(Kapitel\s+\d+|Appendix\s+[A-ZÅÄÖ]):\s*(.+)$", heading)
        if split:
            prefix, heading_title = split.group(1), split.group(2)
            replacement = rf"""
\clearpage
\phantomsection
\pdfbookmark[1]{{{latex_escape(heading)}}}{{{anchor}}}
\addcontentsline{{toc}}{{section}}{{{latex_escape(heading)}}}
\begin{{center}}
{{\Large\bfseries {latex_escape(prefix)}\par}}
\vspace{{0.20em}}
{{\Huge\bfseries {latex_escape(heading_title)}\par}}
\end{{center}}
\vspace{{0.75em}}
"""
        else:
            replacement = rf"""
\clearpage
\phantomsection
\pdfbookmark[1]{{{latex_escape(heading)}}}{{{anchor}}}
\addcontentsline{{toc}}{{section}}{{{latex_escape(heading)}}}
\begin{{center}}
{{\Huge\bfseries {latex_escape(heading)}\par}}
\end{{center}}
\vspace{{0.75em}}
"""
        lines[idx] = replacement.strip()
        break
    return "\n".join(lines)


def ensure_pdf_header() -> Path:
    path = ROOT / "styles" / "pdf-pandoc-header.tex"
    if path.exists():
        return path
    path.write_text(r"""
\usepackage[a4paper,margin=22mm,bottom=24mm]{geometry}
\usepackage{fontspec}
\setmainfont{Noto Serif}
\setsansfont{Noto Sans}
\usepackage{microtype}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{eso-pic}
\usepackage{setspace}
\setstretch{1.08}
\usepackage{enumitem}
\setlist{itemsep=0.2em, topsep=0.3em}
\usepackage{titlesec}
\titleformat{\section}{\Large\bfseries\color{black}}{}{0em}{}
\titlespacing*{\section}{0pt}{1.3em}{0.5em}
\titleformat{\subsection}{\large\bfseries\color{black}}{}{0em}{}
\titlespacing*{\subsection}{0pt}{1.0em}{0.35em}
\titleformat{\subsubsection}{\normalsize\bfseries\color{black}}{}{0em}{}
\titlespacing*{\subsubsection}{0pt}{0.8em}{0.25em}
\usepackage{tocloft}
\renewcommand{\contentsname}{Innehåll}
\setcounter{tocdepth}{1}
\setlength{\cftbeforesecskip}{0.38em}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0pt}
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor={teal!50!black},
  urlcolor={teal!50!black},
  citecolor={teal!50!black}
}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{fvextra}
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
\usepackage{framed}
\definecolor{shadecolor}{RGB}{241,245,249}
""", encoding="utf-8")
    return path


def build_pdf_markdown(metadata: dict) -> Path:
    BUILD_DIR.mkdir(exist_ok=True)
    title = metadata.get("title", "")
    subtitle = metadata.get("subtitle", "")
    author = metadata.get("author", "")
    cover = metadata.get("cover_image", "assets/cover/cover.png")

    front = rf"""
```{{=latex}}
\pagenumbering{{gobble}}
\thispagestyle{{empty}}
\AddToShipoutPictureBG*{{\AtPageLowerLeft{{\includegraphics[width=\paperwidth,height=\paperheight]{{{cover}}}}}}}
\null
\clearpage

\thispagestyle{{empty}}
\vspace*{{0.28\textheight}}
\begin{{center}}
{{\Huge\bfseries {latex_escape(title)}\par}}
\vspace{{0.8cm}}
{{\Large {latex_escape(subtitle)}\par}}
\vspace{{1.5cm}}
{{\large {latex_escape(author)}\par}}
\end{{center}}
\clearpage

\pagenumbering{{roman}}
\phantomsection
\pdfbookmark[1]{{Innehåll}}{{toc}}
\tableofcontents
\clearpage
\pagenumbering{{arabic}}
```
""".strip()

    parts = [front]
    for chapter in metadata["chapters"]:
        path = ROOT / chapter
        text = path.read_text(encoding="utf-8")
        validate_markdown(path, text)
        parts.append(transform_chapter_for_pdf(text).strip())

    out = BUILD_DIR / "book-pdf.md"
    out.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    return out


def run_export(fmt: str, metadata: dict, book_md: Path) -> None:
    EXPORTS_DIR.mkdir(exist_ok=True)
    safe_name = metadata.get("project_slug") or "book"
    title = metadata["title"]
    subtitle = metadata.get("subtitle", "")
    author = metadata["author"]
    lang = "sv-SE" if metadata.get("language") == "sv" else "en"

    if fmt == "markdown":
        output = EXPORTS_DIR / f"{safe_name}.md"
        output.write_text(book_md.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Skapade {output}")
        return

    if fmt == "epub":
        require_pandoc()
        output = EXPORTS_DIR / f"{safe_name}.epub"
        cmd = [
            "pandoc", str(book_md),
            "--from=gfm",
            "--to=epub3",
            "--metadata", f"title={title}",
            "--metadata", f"subtitle={subtitle}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--toc-depth=1",
            "--css", str(ROOT / "styles" / "epub.css"),
        ]
        if metadata.get("cover_image"):
            cmd.extend(["--epub-cover-image", str(ROOT / metadata["cover_image"])])
        cmd.extend(["--output", str(output)])
        print("Kör:", " ".join(cmd))
        subprocess.run(cmd, check=True)
        post_process_epub(output, metadata)
        print(f"Skapade {output}")
        return

    if fmt == "pdf":
        require_pandoc()
        require_xelatex()
        pdf_md = build_pdf_markdown(metadata)
        header = ensure_pdf_header()
        output = EXPORTS_DIR / f"{safe_name}.pdf"
        cmd = [
            "pandoc", str(pdf_md),
            "--from=markdown+raw_tex+pipe_tables",
            "--pdf-engine=xelatex",
            "--toc-depth=1",
            "--include-in-header", str(header),
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--output", str(output),
        ]
        print("Kör:", " ".join(cmd))
        subprocess.run(cmd, check=True, cwd=ROOT)
        print(f"Skapade {output}")
        return

    fail(f"Okänt format: {fmt}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Exportera bokprojekt till EPUB/PDF/Markdown.")
    parser.add_argument("--format", choices=["epub", "pdf", "markdown", "all"], default="markdown")
    args = parser.parse_args()

    metadata = read_metadata()
    book_md = build_book(metadata)

    formats = ["markdown", "epub", "pdf"] if args.format == "all" else [args.format]
    for fmt in formats:
        run_export(fmt, metadata, book_md)


if __name__ == "__main__":
    main()
