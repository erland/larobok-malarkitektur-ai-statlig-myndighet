# Granskningsrapport

## Sammanfattning

Projektet har granskats efter att inledning och kapitel 1–21 skapats.

Resultat: manus är sammanhängande, kapitelordningen är komplett och projektet är redo för redaktionell slutputs samt därefter EPUB/PDF-export. Den tekniska markdownvalideringen är godkänd för lokal markdown-export.

## Omfattning

- Titel: Målarkitektur för AI i statlig myndighet
- Författare: Erland Lindmark
- Språk: Svenska
- Kapitel: 22 filer inklusive inledning
- Ungefärligt ordantal: 74199
- Granskningsdatum: 2026-06-02

## Kontroller som genomförts

| Kontroll | Resultat | Kommentar |
|---|---|---|
| Kapitelordning enligt metadata | Godkänd | `chapters/00-inledning.md` ligger först och kapitel 1–21 följer i rätt ordning. |
| Saknade kapitel | Godkänd | Inga planerade kapitel saknas. |
| H1 per kapitel | Godkänd | Varje kapitel har exakt en H1-rubrik. |
| H4 eller djupare rubriker | Godkänd | Inga otillåtna H4-rubriker hittades. |
| Kodblock | Godkänd | Inga obalanserade kodblock hittades. |
| Tabellstruktur | Godkänd | Inga uppenbara tabellfel hittades vid maskinell kontroll. |
| Bildreferenser i kapitel | Godkänd | Inga saknade inre bildreferenser hittades. |
| Övningar | Godkänd | Traditionella övningar har inte lagts in som standardmoment. |
| Lokal markdown-export | Godkänd | `scripts/export-book.py --format markdown` kunde skapa sammanslagen markdown i `exports/`. |

## Progression

Bokens progression är logisk:

1. Den börjar med behovet av AI-förmåga och målarkitektur.
2. Den går vidare till användningsfall, juridik, informationsklassning, risk och governance.
3. Den introducerar därefter förmågekarta, dataarkitektur och teknisk referensarkitektur.
4. Den fördjupar vägval kring RAG, MLOps/LLMOps, moln, on-premises, hybrid, produkter och säkerhet.
5. Den avslutar med upphandling, roadmap, samlat scenario, anti-patterns och checklistor.

Detta passar målgruppen erfarna IT-arkitekter eftersom boken bygger runt avvägningar, styrning, principer, vägval och konsekvenser snarare än grundläggande AI-teori.

## Terminologi och canon

Terminologin är tillräckligt konsekvent för fortsatt redigering. Följande begrepp är bärande och bör behållas konsekvent genom hela boken:

- AI-förmåga
- målarkitektur
- referensarkitektur
- AI-portfölj
- use-case triage
- informationsklassning
- riskstyrning
- AI-gateway
- RAG
- MLOps och LLMOps
- guardrails
- Tullverket Aurora

## Återkommande scenario

Scenariot med Tullverket Aurora fungerar som röd tråd och är särskilt starkt i kapitel där målarkitektur, användningsfall, tekniska vägval, roadmap och samlad målbild behandlas.

Rekommendation inför slutredigering: förstärk gärna scenariokopplingen i de mest juridiska och tekniska kapitlen med korta exempelrutor om samma användningsfall återkommer.

## Exportberedskap

Projektet har metadata, kapitelordning, styles och exportscript. Markdown-exporten har testats.

Kvar före EPUB/PDF:

- Generera eller lägg till `assets/cover/cover.png` om omslag ska ingå.
- Gör en sista faktakontroll av regulatoriska påståenden, särskilt AI Act, GDPR, upphandling och svenska myndighetsriktlinjer.
- Kör lokal EPUB/PDF-export i en miljö med Pandoc och PDF-motor installerad.
- Kontrollera visuellt att listor, tabeller, rubriker och innehållsförteckning renderas korrekt.

## Rekommenderad nästa åtgärd

Nästa steg bör vara slutredigering av stil och konsekvens, alternativt att generera omslaget innan EPUB/PDF-export.


## Slutredigering av stil, konsekvens och scenariokoppling

Datum: 2026-06-02

Följande redaktionella justeringar har genomförts efter den första granskningen:

- Tullverket Aurora har förstärkts som återkommande scenario i kapitel där exempelkopplingen var svagare.
- Flera kapitel har kompletterats med vägvalsfrågor för att stärka bokens karaktär av praktisk arkitekturhandbok.
- Kapitel 20 och 21 har kompletterats med fallgropar för att ge mer enhetlig kapitelstruktur.
- Kapitel 19 har fått tydligare koppling till målarkitekturen eftersom det fungerar som bokens sammanhållna tillämpningsexempel.
- Kapitel 1–18 har fått övergångar som binder ihop progressionen från AI-förmåga till juridik, data, teknik, drift, upphandling och införande.
- Manus har fortsatt inga traditionella övningar, i linje med författarens önskemål.

Resultat: manus är mer konsekvent och scenariot är tydligare integrerat. Rekommenderat nästa steg är faktaverifiering av aktuella regulatoriska och produktrelaterade kapitel innan EPUB/PDF-export.
