# EPUB-export

## Resultat

EPUB har skapats med Pandoc 3.1.11.1.

## Skapad fil

- `exports/malarkitektur-ai-statlig-myndighet.epub`

## Kontroller

- EPUB-filen innehåller korrekt `mimetype`: `application/epub+zip`.
- EPUB-filen innehåller `EPUB/content.opf`.
- Titel, författare och språk finns i EPUB-metadata.
- Omslaget är inbäddat som `EPUB/media/cover.png`.
- EPUB-filen använder projektets `styles/epub.css`.
- Exporten använder kapitelordningen från `docs/export-metadata.yaml`.

## Metadata

- Titel: Målarkitektur för AI i statlig myndighet
- Författare: Erland Lindmark
- Språk: sv-SE


## Justering efter läsarkontroll

EPUB-exporten har justerats efter granskning i läsare:

- Titelsidan visar nu titel, undertitel och författare.
- Titelsidans titel, undertitel och författare centreras via EPUB-CSS.
- Innehållsförteckningen exporteras med `--toc-depth=1`, vilket innebär endast översta kapitelnivån.
- EPUB-CSS tvingar inte längre `page-break-before` på H1-rubriker i separata kapitelfiler, för att undvika tom sida före kapitel vid navigering.
