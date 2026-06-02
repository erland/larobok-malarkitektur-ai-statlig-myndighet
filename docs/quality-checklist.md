# Kvalitetschecklista

## Språk och målgrupp

- Är texten skriven på svenska?
- Används engelska begrepp endast när de är vedertagna eller mer precisa?
- Matchar nivån erfarna IT-arkitekter?
- Undviks nybörjarförklaringar som bromsar tempot?
- Förklaras AI-specifika begrepp när de först används?

## Pedagogik

- Har kapitlet ett tydligt arkitekturproblem?
- Finns ett rekommenderat angreppssätt?
- Finns exempel från Tullverket Aurora?
- Finns vägvalsfrågor?
- Finns checklista?
- Finns vanliga fallgropar?

## Progression

- Introduceras begrepp i rätt ordning?
- Bygger kapitlet vidare på tidigare beslut?
- Återknyter kapitlet till målarkitekturen?
- Undviks stora hopp från juridik direkt till teknik utan risk- och principresonemang?

## Teknik och fakta

- Är tekniska antaganden tydligt markerade?
- Är aktuella rättsliga eller regulatoriska fakta markerade för verifiering vid slutredigering?
- Beskrivs produktkategorier neutralt och beslutsorienterat?
- Undviks leverantörslåsning i språket?

## Export

- Finns metadata?
- Finns författare?
- Är kapitelordningen stabil?
- Används endast H1-H3 i kapitel?
- Finns inga traditionella övningar om användaren inte ber om det?

## Granskningsresultat 2026-06-02

- Kapitelordning: Godkänd.
- Metadata: Godkänd för fortsatt exportförberedelse.
- Markdownnivåer: Godkänd, inga H4-rubriker hittades.
- Kapitelstruktur: Godkänd för praktisk handbok med lärobokskaraktär.
- Övningar: Godkänd, traditionella övningar har inte lagts in.
- Scenario: Godkänd, Tullverket Aurora används som återkommande exempel.
- Exportvalidering: Markdown-export testad och godkänd.
- Kvar inför slutexport: omslagsbild, visuell EPUB/PDF-kontroll och slutlig faktaverifiering av aktuella regelverk.



## Slutredigeringsresultat 2026-06-02

- Stil: Jämnad mot praktisk handbok med lärobokskaraktär.
- Scenario: Tullverket Aurora har stärkts som röd tråd i kapitel där kopplingen var svagare.
- Kapitelstruktur: Vägvalsfrågor, fallgropar, checklistor och målarkitekturkoppling har harmoniserats.
- Progression: Övergångar mellan kapitel 1–18 har lagts till.
- Övningar: Fortsatt utelämnade enligt författarens instruktion.
- Export: Sammanslagen markdown bör uppdateras före EPUB/PDF-export.


## Faktaverifiering 2026-06-02

- Kapitel 4, 5, 13, 14, 16 och 17 är faktaverifierade mot aktuella källor.
- Faktakompletteringar har integrerats i respektive kapitel och ligger inte kvar som separata manusavsnitt.
- Separat rapport finns i `docs/fact-verification-report.md`.
- AI Act-formuleringar är justerade för stegvis tillämpning och pågående förenklingsarbete.
- GDPR-formuleringar är förtydligade för personuppgifter i hela AI-flödet.
- Moln- och upphandlingsavsnitt är kompletterade med svensk offentlig vägledning.
- Säkerhetsavsnittet är kompletterat med OWASP/ENISA-perspektiv.


## Omslag och plattformskompatibilitet

- Omslag inlagt i `assets/cover/cover.png`.
- Alternativ JPEG-fil skapad i `assets/cover/cover-marketplace.jpg`.
- Omslaget är RGB och 1600 × 2400 px.
- Apple Books-kompatibilitet kontrollerad mot PNG/JPEG, RGB och minst 1400 px kortaste sida.
- Google Books-kompatibilitet kontrollerad mot PNG/JPG och 1024–7200 px.

## EPUB-kontroll efter integrering

- Sektionen `Faktagranskad komplettering 2026-06-02` förekommer inte längre i kapitelmanus.
- EPUB ska byggas om efter integrering.
- Innehållsförteckningen ska fortsatt visa endast översta kapitelnivån.
- Kapitelrubriker ska fortsatt visas centrerade på två rader i kapitelvyn.


## Appendix A-kontroll 2026-06-02

- Appendix A är skapat som uppdateringsbar katalog, inte som statisk rekommendation.
- Kapitel 14 innehåller hänvisning till Appendix A.
- Metadata och kapitelordning är uppdaterade.
- EPUB har inte byggts om i detta steg enligt användarens instruktion.


## Appendix B-kontroll 2026-06-02

- Appendix B är skapat som uppdateringsbar översikt över open source-modeller, ramverk och egen drift.
- Appendixet är placerat efter Appendix A och före kommande Appendix C.
- Kapitel 14 hänvisar nu till både Appendix A och Appendix B.
- Appendix B använder samma beslutsorienterade struktur som övriga boken: vad komponenten tillför, när den är lämplig, när den kräver särskild analys och typiska arkitekturfrågor.
- EPUB har inte byggts om ännu, enligt instruktion att vänta tills alla appendix är skapade.


## Appendix C-kontroll 2026-06-02

- Appendix C är skapat som beslutsstöd snarare än produktkatalog.
- Appendix C använder samma scenario, Tullverket Aurora, som övriga boken.
- Appendix C innehåller beslutsmatriser för SaaS, plattform, egen drift, moln/on-premises, RAG/fine-tuning, central/federerad modell, open source/kommersiellt, vektordatabaser, agentfunktioner och guardrails.
- Appendix C innehåller mallar för arkitekturbeslut, AI-use-case canvas och leverantörs-/ramverksbedömning.
- Appendix C använder endast H1-H3 och strikt markdown.
- EPUB har inte byggts om i detta steg.

## EPUB-export med appendix

- [x] Appendix A–C ingår i kapitelordningen.
- [x] EPUB är skapad med Pandoc.
- [x] Omslag är inbäddat.
- [x] TOC använder översta kapitelnivån.
- [x] Titelsidan innehåller titel, undertitel och författare.

## Appendixkontroll 2026-06-02

- Appendix A–C kontrollerade efter redaktionell justering.
- Scenariobundna Aurora-avsnitt har tagits bort ur appendixdelen.
- Appendixrubriker renderas i EPUB med samma tvådelade rubrikformat som kapitelrubrikerna.


## PDF-exportkontroll 2026-06-02

- [x] PDF innehåller omslag.
- [x] PDF innehåller centrerad titelsida med titel, undertitel och författare.
- [x] PDF har klickbar innehållsförteckning före inledningen.
- [x] PDF-innehållsförteckningen använder endast översta kapitelnivån.
- [x] Kapitel- och appendixrubriker visas centrerat på två rader.
- [x] PDF skapades med Pandoc och XeLaTeX.
- [x] PDF renderades till bildsidor för visuell kontroll.
