# PDF-exportrapport

Datum: 2026-06-02

## Resultat

PDF har skapats som `exports/malarkitektur-ai-statlig-myndighet.pdf`.

## Exportprofil

- Verktyg: Pandoc 3.1.11.1 och XeLaTeX.
- Sidformat: A4.
- Omslag: första sidan i PDF.
- Titelsida: centrerad titel, undertitel och författare.
- Innehållsförteckning: ligger före inledningen i själva PDF:en.
- Innehållsförteckningens nivå: endast översta kapitelnivån.
- Länkar: innehållsförteckningen är klickbar.
- Kapitelrubriker: kapitel och appendix renderas centrerat på två rader.
- Brödtext: markdown har renderats semantiskt via Pandoc.

## Kontroll

PDF:en har inspekterats och renderats till bildsidor enligt PDF-arbetsflödet. Inspektionen visade:

- PDF är inte krypterad.
- PDF har A4-format.
- PDF innehåller länkannotationer från innehållsförteckningen.
- Metadata innehåller titel och författare.

## Reproducerbarhet

Projektets `scripts/export-book.py --format pdf` har uppdaterats så att samma PDF-profil kan byggas lokalt med Pandoc och XeLaTeX.
