# Omslagskompatibilitet

## Status

Omslaget är godkänt av användaren och har lagts in i projektet.

Ingen ny bild har genererats. Den godkända bilden har endast formats om tekniskt för bättre kompatibilitet med vanliga bokplattformar.

## Filer

| Fil | Syfte | Format | Färgrymd | Storlek |
|---|---|---|---|---|
| `assets/cover/cover.png` | Inbäddat omslag för EPUB/PDF-export | PNG | RGB | 1600 × 2400 px |
| `assets/cover/cover-marketplace.jpg` | Alternativ uppladdnings-/marknadsfil | JPEG | RGB | 1600 × 2400 px |

## Kontroll mot Apple Books

Apple Books anger att omslagsbild ska vara PNG eller JPEG, i RGB-färgrymd och minst 1400 pixlar på den kortaste sidan.

Resultat:

- Format: PNG och JPEG finns.
- Färgrymd: RGB.
- Kortaste sida: 1600 px.
- Status: godkänd teknisk kompatibilitet enligt angivna krav.

## Kontroll mot Google Play Books / Google Books

Google Play Books anger för e-böcker att omslag kan vara PNG eller JPG, minst 1024 pixlar och högst 7200 pixlar i höjd och bredd.

Resultat:

- Format: PNG och JPEG finns.
- Pixelmått: 1600 × 2400 px.
- Både höjd och bredd ligger inom intervallet 1024–7200 px.
- Status: godkänd teknisk kompatibilitet enligt angivna krav.

## Metadata

`docs/export-metadata.yaml` pekar på:

```yaml
cover_image: assets/cover/cover.png
cover_image_marketplace: assets/cover/cover-marketplace.jpg
```

`book.yaml` pekar på:

```yaml
cover_image: assets/cover/cover.png
```

## Kommentar

Omslaget är i stående 2:3-format. Google anger att kvadratiska omslag rekommenderas i vissa hjälpsidor för särskilda flöden, men deras generella e-bokskrav accepterar PNG/JPG inom 1024–7200 pixlar. För denna bok används därför ett traditionellt stående bokomslag.
