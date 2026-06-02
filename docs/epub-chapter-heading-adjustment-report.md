# EPUB-justering: kapitelrubriker

Datum: 2026-06-02

## Genomförd ändring

Kapitelrubriker i EPUB-renderingen har justerats så att rubriken i respektive kapitel visas på två centrerade rader:

```text
Kapitel N
Kapitelns titel
```

Innehållsförteckningen behåller samma text som tidigare, till exempel:

```text
Kapitel 1: Från AI-experiment till myndighetsgemensam AI-förmåga
```

## Teknisk lösning

- Källkapitlens markdownrubriker behålls oförändrade för stabil kapitelordning och TOC-generering.
- EPUB-filen postprocessas efter Pandoc-export.
- I kapitel-XHTML delas H1-rubriker av typen `Kapitel N: Titel` visuellt upp i två `span`-element.
- `styles/epub.css` styr centrerad rubrik, radbrytning och reducerade marginaler ovanför/under rubriken.
- TOC genereras fortsatt med `--toc-depth=1`.

## Kontroller

- Innehållsförteckningen är oförändrad i textnivå.
- Kapitelrubrikerna i själva kapitlen är centrerade.
- Kapitelnumret visas på egen rad.
- Kapitelrubrikens titel visas på raden under.
- Ingen extra H2/H3-nivå har lagts till.
