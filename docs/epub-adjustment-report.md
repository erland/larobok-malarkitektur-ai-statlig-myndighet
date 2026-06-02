# EPUB-justeringsrapport

## Syfte

EPUB-exporten har justerats enligt följande önskemål:

- titelsidan ska visa titel, undertitel och författare
- titelsidans text ska vara centrerad
- innehållsförteckningen ska länka direkt till kapitlens första sida utan att skapa en tom sida före kapitlet
- innehållsförteckningen ska endast innehålla översta kapitelnivån

## Genomförda ändringar

- `scripts/export-book.py` skickar nu med `subtitle` till Pandoc vid EPUB-export.
- EPUB-exporten använder nu `--toc-depth=1`.
- `styles/epub.css` har justerats så att H1-rubriker inte tvingar fram sidbrytning inne i varje XHTML-fil.
- Titelsidans CSS har fått centrerad layout för titel, undertitel och författare.

## Kontroll

Den exporterade EPUB-filen har kontrollerats genom att den packats upp och granskats:

- `EPUB/text/title_page.xhtml` innehåller titel, undertitel och författare.
- `EPUB/nav.xhtml` innehåller endast H1-/kapitelnivån.
- TOC-länkarna pekar direkt till respektive kapitelfil, till exempel `text/ch002.xhtml`.
- Omslaget ligger kvar inbäddat i EPUB-filen.
