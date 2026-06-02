# Målarkitektur för AI i statlig myndighet

**En praktisk handbok för att etablera säker, styrd och skalbar AI-förmåga**

Författare: Erland Lindmark

Detta är ett standardiserat bokprojekt för en praktisk handbok med lärobokskaraktär.

## Projektstruktur

- `chapters/` innehåller manuskapitel.
- `docs/` innehåller bokspecifikation, kapitelplan, canon, projektstatus, exportmetadata och illustrationsplan.
- `assets/` innehåller omslag, bildprompter och eventuella bilder.
- `styles/` innehåller CSS för EPUB och PDF.
- `scripts/` innehåller lokal exportpipeline.
- `exports/` är målplats för genererade EPUB/PDF/DOCX/Markdown-filer.

## Rekommenderat arbetsflöde

1. Granska `docs/book-specification.md`.
2. Granska `docs/chapter-plan.md`.
3. Fortsätt med kapitel 1 enligt planen.
4. Uppdatera canon- och statusfiler när innehållet växer.
5. Exportera lokalt med `scripts/export-book.sh` när manus är redo.

## Lokal export

Exportscriptet förutsätter Python 3 och rekommenderar Pandoc för EPUB/PDF.

```bash
bash scripts/export-book.sh --format epub
bash scripts/export-book.sh --format pdf
```
