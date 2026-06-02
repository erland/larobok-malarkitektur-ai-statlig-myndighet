# Projektstatus

## Bok

Titel: Målarkitektur för AI i statlig myndighet
Språk: Svenska
Författare: Erland Lindmark
Version: 3.3

## Nuvarande fas

- Start/intervju: Klar
- Bokspecifikation: Klar
- Kapitelplan: Klar
- Kapitelgenerering: Klar
- Granskning: Faktaverifierad, slutredigerad och faktakompletteringar integrerade i kapiteltexten
- Export: EPUB genererad tidigare. PDF genererad med Pandoc/XeLaTeX, omslag, centrerad titelsida, klickbar innehållsförteckning före inledningen och TOC på översta kapitelnivån.

## Kapitelstatus

| Kapitel | Titel | Status | Kommentar |
|---|---|---|---|
| 0 | Inledning | Granskat utkast | Skapad som starttext |
| 1 | Från AI-experiment till myndighetsgemensam AI-förmåga | Granskat utkast | Skapat i version 0.2 |
| 2 | Vad målarkitektur betyder för AI | Granskat utkast | Skapat i version 0.3 |
| 3 | AI-portföljen: vilka användningsfall ska myndigheten stödja? | Granskat utkast | Skapat i version 0.4 |
| 4 | Juridik, ansvar och regelefterlevnad | Faktaverifierat och integrerat utkast | Faktakomplettering integrerad i kapiteltext 2026-06-02 |
| 5 | Informationsklassning, dataskydd och riskstyrning | Faktaverifierat och integrerat utkast | Faktakomplettering integrerad i kapiteltext 2026-06-02 |
| 6 | Arkitekturprinciper för offentlig AI | Granskat utkast | Skapat i version 0.7 |
| 7 | Governance och beslutsmodell för AI | Granskat utkast | Skapat i version 0.8 |
| 8 | Förmågekarta för AI i myndigheten | Granskat utkast | Skapat i version 0.9 |
| 9 | Dataarkitektur för AI | Granskat utkast | Skapat i version 1.0 |
| 10 | Teknisk referensarkitektur | Granskat utkast | Skapat i version 1.1 |
| 11 | Generativ AI, RAG och kunskapsstöd | Granskat utkast | Skapat i version 1.2 |
| 12 | MLOps, LLMOps och livscykelhantering | Granskat utkast | Skapat i version 1.3 |
| 13 | Moln, on-premises och hybrid: en beslutsmodell | Faktaverifierat och integrerat utkast | Faktakomplettering integrerad i kapiteltext 2026-06-02 |
| 14 | Plattformar, produkter och ramverk att överväga | Faktaverifierat och integrerat utkast | Faktakomplettering integrerad i kapiteltext 2026-06-02 |
| 15 | När man väljer vad | Granskat utkast | Skapat i version 1.6 |
| 16 | Säkerhetsarkitektur för AI | Faktaverifierat och integrerat utkast | Faktakomplettering integrerad i kapiteltext 2026-06-02 |
| 17 | Upphandling och leverantörsstyrning | Faktaverifierat och integrerat utkast | Faktakomplettering integrerad i kapiteltext 2026-06-02 |
| 18 | Roadmap: från nuläge till etablerad AI-förmåga på 24 månader | Granskat utkast | Skapat i version 1.9 |
| 19 | Målarkitektur för Tullverket Aurora | Granskat utkast | Skapat i version 2.0 |
| 20 | Vanliga misstag och anti-patterns | Granskat utkast | Skapat i version 2.1 |
| 21 | Arkitektens checklistor och beslutsmallar | Granskat utkast | Skapat i version 2.2 |
| Appendix A | Kommersiella AI-plattformar och molntjänster | Utkast | Skapat i version 3.0 som uppdateringsbar produkt- och leverantörsöversikt |

## Introducerade begrepp

| Begrepp | Kapitel | Kort definition |
|---|---|---|
| AI-förmåga | 0 | Organisationens samlade förmåga att styra, utveckla, driftsätta och förvalta AI på ett säkert och nyttoskapande sätt. |
| AI-experiment | 1 | Avgränsad prövning som visar om en AI-idé kan fungera, utan att bevisa produktionsbarhet. |
| AI-lösning | 1 | Konkret implementation för ett specifikt AI-användningsfall. |
| Use-case triage | 1 | Gemensam bedömning av AI-användningsfall utifrån nytta, risk, data och styrkrav. |
| Målarkitektur | 0 | Beskrivning av önskat framtida arkitekturläge och de vägval som krävs för att nå dit. |
| Tullverket Aurora | 0 | Fiktiv tullmyndighet som används som återkommande scenario. |
| Target architecture | 2 | Engelsk term för målarkitektur; används när internationella arkitekturbegrepp jämförs. |
| Referensarkitektur | 2 | Återanvändbar arkitekturbeskrivning för en typ av lösning eller förmåga. |
| Lösningsarkitektur | 2 | Detaljerad arkitektur för ett specifikt användningsfall eller system. |
| Roadmap | 2 | Stegvis plan som visar hur organisationen rör sig från nuläge till målarkitektur. |
| Architecture Decision Record | 2 | Dokumenterat arkitekturbeslut med bakgrund, alternativ, konsekvenser och omprövningspunkt. |
| Arkitekturbeslut | 2 | Spårbart vägval som påverkar målarkitektur, referensarkitektur eller lösningsarkitektur. |
| AI-portfölj | 3 | Samlad mängd AI-initiativ, piloter och produktionssatta lösningar som styrs över tid. |
| Användningsfall | 3 | Avgränsad situation där AI skapar nytta för en viss användare eller process. |
| Nyttoklassning | 3 | Bedömning av vilken typ av nytta ett AI-användningsfall förväntas skapa. |
| Risknivå | 3 | Preliminär bedömning av hur känsligt och konsekvensrikt ett AI-användningsfall är. |
| AI-roll | 3 | Beskrivning av om AI används som assistent, kunskapsstöd, beslutsstöd, styrande komponent eller automatiserad aktör. |
| Regelefterlevnad | 4 | Förmågan att visa och säkerställa att AI-användning följer relevanta lagar, regler, avtal och interna styrkrav. |
| Riskklassning | 4 | Bedömning av AI-användningsfall utifrån rättslig, verksamhetsmässig, informationsmässig och teknisk risk. |
| Personuppgiftsbehandling | 4 | All hantering av personuppgifter, till exempel insamling, lagring, analys, överföring, loggning eller radering. |
| Ansvarskedja | 4 | Tydlig fördelning av ansvar mellan verksamhet, informationsägare, systemägare, modellägare, juridik, säkerhet och arkitektur. |
| Juridisk triage | 4 | Tidig sortering av AI-användningsfall utifrån rättsliga frågor, risk, data, påverkan och krav på kontroll. |
| Mänsklig kontroll | 4 | Designad process där människor förstår, granskar och ansvarar för AI-stödets användning och konsekvenser. |
| Informationsklassning | 5 | Bedömning av informationens skyddsbehov, särskilt konfidentialitet, riktighet och tillgänglighet. |
| Dataskyddsbedömning | 5 | Bedömning av hur personuppgifter behandlas och vilka krav som följer av dataskyddsregler. |
| AI-riskbedömning | 5 | Bedömning av risk utifrån användningsfall, data, AI-roll, process och möjlig påverkan. |
| Embeddings | 5 | Vektorrepresentationer av text eller annan information som behöver skyddas utifrån sitt informationsinnehåll. |
| Driftmodell | 5 | Val av var och hur AI-lösningen körs, exempelvis moln, hybrid, on-premises eller isolerad miljö. |
| AI-princip | 6 | Styrande formulering som påverkar hur AI-användningsfall, teknik, ansvar och driftmodell ska utformas. |
| Guardrails | 6 | Tekniska, processuella eller organisatoriska skyddsräcken som begränsar otillåten eller riskfylld AI-användning. |
| Human oversight | 6 | Engelsk term för mänsklig kontroll; designad mänsklig granskning och ansvar i AI-stödda processer. |
| Explainability | 6 | Förklarbarhet; förmågan att förstå, granska eller motivera hur ett AI-stöd har tagit fram ett resultat. |
| Policy enforcement | 6 | Tekniska eller organisatoriska mekanismer som säkerställer att beslutade regler faktiskt följs i användning och drift. |
| Leverantörsoberoende | 6 | Förmågan att hantera eller byta leverantör, modell eller plattform utan okontrollerad verksamhets- eller arkitekturrisk. |

| AI-governance | 7 | Styrmodell för hur AI-initiativ beslutas, prioriteras, granskas, driftsätts och följs upp. |
| Styrklass | 7 | Klassning som avgör vilken beslutsnivå, dokumentation och granskning ett AI-användningsfall kräver. |
| AI-styrgrupp | 7 | Ledningsnära forum för strategiska AI-beslut, riskaptit, prioriteringar och investeringar. |
| AI-governanceforum | 7 | Taktiskt forum som bedömer AI-användningsfall, hanterar portfölj, villkor och eskalering. |
| Produktionsgodkännande | 7 | Beslutspunkt innan en AI-lösning får användas i produktion. |

| Förmågekarta | 8 | Strukturerad beskrivning av vad myndigheten behöver kunna göra för att etablera och förvalta AI-förmåga. |
| Capability model | 8 | Engelsk term för förmågemodell eller förmågekarta. |
| AI lifecycle | 8 | Livscykeln för en AI-lösning från idé och triage till drift, uppföljning och avveckling. |
| Gemensam förmåga | 8 | Förmåga som bör etableras myndighetsgemensamt och återanvändas av flera AI-lösningar. |
| Federerad förmåga | 8 | Förmåga som följer gemensamma regler men utförs nära verksamhetsområde eller produktteam. |
| Lokal förmåga | 8 | Förmåga som kan lösas av ett enskilt team inom fastställda ramar. |
| Dataarkitektur | 9 | Beskrivning av hur data struktureras, ägs, kvalitetssäkras, skyddas, spåras och används över tid. |
| Informationsägarskap | 9 | Ansvar för informationens kvalitet, klassning, tillgänglighet, användning och livscykel. |
| Metadata | 9 | Data om data som kan styra åtkomst, kvalitet, giltighet, sökning och spårbarhet. |
| Data lineage | 9 | Spårbarhet från källdata genom transformationer, index, retrieval, modellinteraktion och AI-svar. |
| Vektordatabas | 9 | Databas som lagrar embeddings och möjliggör semantisk sökning. |
| Behörighetsmedveten retrieval | 9 | Hämtning av kontext där resultat filtreras utifrån användarens behörighet och informationsklass. |

| Teknisk referensarkitektur | 10 | Återanvändbar teknisk arkitekturbeskrivning som visar AI-byggblock, ansvar, relationer och styrande integrationsmönster. |
| AI-gateway | 10 | Kontrollerat åtkomstlager mellan applikationer och AI-tjänster för exempelvis policy, loggning, modellval och behörighet. |
| Modellplattform | 10 | Teknisk miljö där modeller görs tillgängliga, körs, versioneras, övervakas och förvaltas. |
| Inferens | 10 | Körning där en tränad modell tar emot indata och producerar utdata. |
| Orkestrering | 10 | Samordning av flera steg i ett AI-flöde, exempelvis retrieval, promptkonstruktion, modellkörning och policykontroll. |
| Policy enforcement | 10 | Teknisk tillämpning av regler i systemflödet, exempelvis åtkomst, modellval, loggning och spärrar. |
| Observability | 10 | Förmåga att förstå drift, användning, kvalitet, kostnad och avvikelser genom loggar, mätvärden och spårning. |
| Guardrails | 10 | Tekniska och processuella skydd som begränsar hur AI-lösningen får användas och vilket beteende den får uppvisa. |

| Prompt | 11 | Instruktion och kontext som skickas till en språkmodell. |
| Promptning | 11 | Styrning av modellens beteende genom instruktioner och kontext utan att träna om modellen. |
| Grounding | 11 | Koppling mellan modellens svar och specifika källor, data eller regler. |
| Hallucination | 11 | Svar som verkar trovärdigt men inte är korrekt, inte följer källorna eller hittar på information. |
| Finjustering | 11 | Vidareträning av en modell för att påverka beteende, format, stil eller återkommande klassificeringsmönster. |
| Produktivitetsstöd | 11 | Generativt stöd för lågklassade arbetsuppgifter som formulering, strukturering eller sammanfattning. |
| Kunskapsstöd | 11 | AI-stöd som hjälper användaren att hitta, sammanfatta och förstå styrda källor. |
| Ärendenära stöd | 11 | AI-stöd som använder eller sammanfattar information kopplad till ett konkret ärende. |
| Beslutsnära stöd | 11 | AI-stöd som ligger nära bedömning, prioritering eller rekommendation i ett beslutsflöde. |
| MLOps | 12 | Förmågan att utveckla, testa, driftsätta, övervaka och förvalta maskininlärningsmodeller kontrollerat. |
| LLMOps | 12 | Livscykelhantering för stora språkmodeller, promptar, RAG-flöden, utvärderingar och modellinteraktioner. |
| Modellregister | 12 | Kontrollerad katalog över modeller, modellversioner, status, ansvar, risk och godkänd användning. |
| Modellkort | 12 | Dokumentation av en modell, dess syfte, begränsningar, mätvärden och lämpliga användningsområden. |
| Systemkort | 12 | Dokumentation av en AI-lösning i sitt organisatoriska och tekniska sammanhang. |
| Utvärderingsdataset | 12 | Styrd samling testfrågor, förväntade källor och kvalitetskriterier för AI-utvärdering. |
| Modellövervakning | 12 | Uppföljning av modellbeteende, kvalitet, drift, bias, användning och avvikelser över tid. |
| AI-releaseprocess | 12 | Riskbaserad process för att godkänna och produktionssätta ändringar i modeller, promptar, RAG-index och AI-tjänster. |

| Publikt moln | 13 | Extern molninfrastruktur eller molntjänst som delas mellan många kunder genom teknisk separation. |
| SaaS | 13 | Färdig applikation eller tjänst som används utan att myndigheten själv driftar underliggande plattform. |
| PaaS | 13 | Plattformstjänst där myndigheten bygger egna lösningar ovanpå leverantörens plattform. |
| IaaS | 13 | Grundläggande molninfrastruktur som virtuella maskiner, nätverk och lagring. |
| Sovereign cloud | 13 | Molnerbjudande med särskilda löften eller mekanismer för datalokalisering, jurisdiktion, åtkomst eller kontroll. |
| On-premises | 13 | Drift i myndighetens egen eller särskilt kontrollerade infrastruktur. |
| Privat moln | 13 | Molnliknande plattform för en organisation eller avgränsad grupp, driven internt eller av leverantör. |
| Hybridarkitektur | 13 | Arkitektur där olika delar av AI-förmågan körs i olika miljöer och binds samman genom styrda gränssnitt. |
| Driftmodell | 13 | Val och styrning av var och hur AI-komponenter körs, förvaltas, säkras och integreras. |
| Exitstrategi | 13 | Plan för att kunna lämna eller byta leverantör, modell, plattform eller driftmodell utan oacceptabel risk. |

| AI-stack | 14 | Det samlade tekniklagret för data, modellåtkomst, orkestrering, applikation, säkerhet, observability och drift. |
| Plattformskarta | 14 | Arkitekturkarta som kopplar produkt- och plattformskategorier till målarkitekturens byggblock och driftspår. |
| Modellhub | 14 | Styrd åtkomstpunkt eller katalog för godkända modeller, modellversioner och tillåtna användningsfall. |
| Sovereign cloud | 14 | Molnerbjudande med särskilda kontroller för datalokalisering, drift, åtkomst och jurisdiktion; måste alltid bedömas konkret. |
| Agentramverk | 14 | Ramverk för att orkestrera AI-flöden där modeller kan använda verktyg, minne, arbetssteg eller mänsklig kontroll. |

| Beslutsmatris | 15 | Strukturerad jämförelse av arkitekturalternativ mot gemensamma kriterier. |
| Tradeoff | 15 | Avvägning där ett alternativ ger vissa fördelar men samtidigt skapar nackdelar eller risker. |
| Modellkatalog | 15 | Styrd lista över godkända modeller, modellspår och användningsvillkor. |
| Arkitekturspår | 15 | Godkänt mönster för en kategori AI-användningsfall, med tillhörande kontroller, driftmodell och beslut. |
| Prompt injection | 16 | Angrepp där instruktioner i prompt eller hämtad kontext försöker påverka modellens beteende. |
| Indirekt prompt injection | 16 | Prompt injection som kommer via dokument, webbsidor eller annan kontext som modellen hämtar och tolkar. |
| Data leakage | 16 | Otillåten exponering av känslig information via promptar, retrieval, modellutdata, loggar eller verktygsanrop. |
| Red teaming | 16 | Strukturerad säkerhetstestning där lösningen utsätts för realistiska angrepp och missbruksscenarier. |
| Content filtering | 16 | Kontroll som blockerar, flaggar eller begränsar otillåtet eller riskfyllt innehåll i indata eller utdata. |
| AI-gateway | 16 | Kontrollerad passage mellan applikationer och modeller där policy, loggning och modellval kan styras. |
| Säkerhetszon | 16 | Avgränsad miljö med definierade regler för dataklass, drift, åtkomst, loggning och tillåtna AI-funktioner. |

| AI-upphandling | 17 | Anskaffning av AI-relaterade tjänster, produkter och stöd där krav på data, säkerhet, ansvar, transparens och livscykel är centrala. |
| Leverantörsstyrning | 17 | Löpande styrning och uppföljning av externa leverantörer, underleverantörer, villkor, förändringar, kvalitet, säkerhet och kostnad. |
| Portabilitet | 17 | Förmåga att flytta data, konfiguration, logik och integrationer mellan leverantörer eller driftmiljöer utan oacceptabel risk. |
| Underleverantörskedja | 17 | Kedja av aktörer som direkt eller indirekt behandlar data eller tillhandahåller komponenter i en AI-tjänst. |
| AI-villkor | 17 | Produkt-, API- eller tjänstevillkor som reglerar hur AI-tjänsten använder data, modeller, loggar, underleverantörer och ändringar. |

| AI-roadmap | 18 | Arkitekturell införandeplan som binder samman nuläge, målbild, beslut, beroenden och införandesteg för AI-förmågan. |
| Sandlåda | 18 | Kontrollerad miljö där godkända AI-användningsfall kan testas med definierade data, verktyg och regler. |
| Styrd pilot | 18 | Avgränsad prövning av ett AI-användningsfall under realistiska villkor med dokumenterade kontroller, ansvar och mätpunkter. |
| Produktionskriterier | 18 | Krav som måste vara uppfyllda innan ett AI-användningsfall får gå från pilot till produktion. |
| Arkitekturspår | 18 | Godkänt införandemönster för en viss typ av AI-användning, med regler för data, drift, säkerhet, modellval och förvaltning. |
| Mognadsmodell | 18 | Modell för att mäta hur stabil, styrbar och återanvändbar myndighetens AI-förmåga är över tid. |

| Arkitekturspår | 19 | Fördefinierat vägval för en viss typ av AI-användning, med kopplade regler för data, drift, säkerhet, modellval och förvaltning. |
| AI-gateway | 19 | Gemensam kontrollerad åtkomstpunkt för modellåtkomst, policy, routing, loggning och kostnadsuppföljning. |
| Modellkatalog | 19 | Register över godkända modeller, deras villkor, begränsningar, miljöer och användningsområden. |
| RAG-målarkitektur | 19 | Samlad målbild för hur dokument, metadata, retrieval, modellåtkomst, källhänvisning och uppföljning används för kunskapsstöd. |
| Driftspår | 19 | Beslutsbar kategori för var och hur ett AI-användningsfall får köras utifrån klassning, risk och kontrollbehov. |
| ADR | 19 | Architecture Decision Record; kort spårbar dokumentation av ett arkitekturbeslut, alternativ och konsekvenser. |

| Anti-pattern | 20 | Återkommande arbetssätt eller arkitekturval som ser rimligt ut kortsiktigt men ofta skapar problem över tid. |
| Teknisk skuld | 20 | Tekniska genvägar som gör en lösning svårare att ändra, säkra eller förvalta. |
| Styrningsskuld | 20 | Brister i mandat, roller, beslut och ansvar som gör AI-förmågan svår att styra. |
| Dataskuld | 20 | Brister i datakvalitet, metadata, ägarskap, åtkomst eller spårbarhet som försämrar AI-lösningar. |
| Säkerhetsskuld | 20 | Brister i skydd, loggning, behörighet, segmentering eller incidentförmåga. |
| Skugg-AI | 20 | AI-användning som sker utanför myndighetens godkända styrning, verktyg och riskbedömning. |

| AI-use-case canvas | 21 | Strukturerad första beskrivning av ett AI-användningsfall med problem, användare, AI-roll, data, risk, nytta och nästa beslut. |
| Triagechecklista | 21 | Tidig kontrollista som sorterar ett användningsfall till rätt process och visar vilka fördjupningar som behövs. |
| Beslutschecklista | 21 | Stöd för att fatta och dokumentera ett konkret arkitekturbeslut. |
| Produktionsberedskap | 21 | Bedömning av om en AI-lösning har ägarskap, kontroller, test, drift, support och förvaltning inför produktion. |
| Omprövningspunkt | 21 | Tidpunkt eller händelse som kräver att ett tidigare arkitekturbeslut granskas på nytt. |

## Öppna beslut

- Exakt omslagsstil ska väljas.
- Eventuella inre illustrationer är inte aktiverade.

## Nästa rekommenderade steg

- Granska helheten: progression, terminologi, konsekvent användning av Tullverket Aurora och exportberedskap.

## Granskningsnotering

Första kvalitetsgranskning genomförd 2026-06-02. Manus är komplett enligt kapitelplanen och teknisk markdownvalidering är godkänd. Kvar inför slutexport är omslagsbild, slutlig faktaverifiering av aktuella regelverk samt visuell kontroll av EPUB/PDF.

## Nästa rekommenderade steg

- Slutredigera språk och konsekvens i hela manus.
- Generera eller lägg till omslagsbild i `assets/cover/cover.png`.
- Kör lokal EPUB/PDF-export och granska rendering.


## Slutredigering 2026-06-02

Genomförd redaktionell slutredigering med fokus på stil, konsekvens och scenariokoppling.

- Kapitel 1–21 har fått tydligare eller jämnare koppling till Tullverket Aurora där det saknades.
- Vägvalsfrågor har kompletterats i kapitel där beslutsstödet var svagare.
- Kapitel 20 och 21 har kompletterats med vanliga fallgropar för att harmonisera med övrig kapitelstruktur.
- Kapitel 19 har kompletterats med tydligare koppling till målarkitekturen.
- Övergångar mellan kapitel 1–18 har lagts in för bättre progression.
- Ingen traditionell övningsstruktur har lagts till.


## Faktaverifiering 2026-06-02

Kapitel 4, 5, 13, 14, 16 och 17 har faktaverifierats mot aktuella offentliga och etablerade källor. Faktakompletteringar har lagts in i respektive kapitel och en separat rapport finns i `docs/fact-verification-report.md`.

## Nästa rekommenderade steg

- Skapa och granska omslagsbild.
- Kör EPUB/PDF-export.
- Gör visuell slutkontroll av rubriker, listor, tabeller, innehållsförteckning, sidbrytningar och omslag.


## Omslag

Status: Godkänt av användaren, tekniskt anpassat till RGB och 1600 × 2400 px, inlagt i `assets/cover/cover.png`.

Alternativ marknadsfil: `assets/cover/cover-marketplace.jpg`.

Kompatibilitetskontroll: dokumenterad i `docs/cover-compatibility-check.md`.

## Exportstatus
- EPUB skapad med Pandoc: `exports/malarkitektur-ai-statlig-myndighet.epub`
- Omslag inbäddat via `assets/cover/cover.png`.
- Exportdatum: 2026-06-02.


## EPUB-justering

- Titelsida kompletterad med undertitel och centrerad layout.
- Innehållsförteckning begränsad till översta kapitelnivån.
- EPUB-CSS justerad för att undvika tom sida före kapitel vid navigering.


## EPUB-justering: kapitelrubriker

- Kapitelrubriker i EPUB-renderingen visas nu på två centrerade rader: kapitelnummer på första raden och kapiteltitel på andra raden.
- Markdownkällorna behåller sina ursprungliga H1-rubriker så att innehållsförteckningen i EPUB förblir oförändrad.
- Exportscriptet postprocessar EPUB efter Pandoc-export och applicerar särskild CSS för kapitelrubriker.


## Redaktionell åtgärd 2026-06-02

Sektioner med rubriken `Faktagranskad komplettering 2026-06-02` har tagits bort som egna kapitelavsnitt. Relevanta delar har i stället integrerats i kapitlens ordinarie avsnitt, särskilt i kapitel 4, 5, 13, 14, 16 och 17. EPUB-exporten har därefter byggts om.

## Appendixstatus

| Appendix | Titel | Status | Kommentar |
|---|---|---|---|
| A | Kommersiella AI-plattformar och molntjänster | Utkast | Skapat 2026-06-02 |
| B | Open source-modeller, ramverk och egen drift | Utkast | Skapat 2026-06-02 |
| C | Beslutsmatriser och urvalsmallar | Utkast | Skapat 2026-06-02 |


## Nästa rekommenderade steg efter Appendix C

- Granska Appendix A–C som samlad appendixdel.
- Bygg om EPUB när appendixdelen är godkänd.
- Gör visuell kontroll av innehållsförteckning, kapitelrubriker, tabeller och appendixlänkar.

## EPUB-export 2026-06-02

EPUB har skapats efter att Appendix A–C lagts till. Exporten finns i `exports/malarkitektur-ai-statlig-myndighet.epub`. Tidigare layoutjusteringar för omslag, titelsida, TOC och kapitelrubriker är bevarade.

## Appendixjustering 2026-06-02

- Appendix A–C har rensats från särskilda Tullverket Aurora-sektioner.
- Appendix A:s sektion `Koppling till Appendix B och C` har tagits bort.
- EPUB-scriptet stödjer nu tvådelade, centrerade appendixrubriker.


## PDF-export 2026-06-02

- PDF skapad med Pandoc och XeLaTeX.
- Omslag ligger först i PDF:en.
- Titelsidan innehåller titel, undertitel och författare, centrerat.
- Klickbar innehållsförteckning ligger före inledningen.
- Innehållsförteckningen innehåller endast översta kapitelnivån.
- Kapitel- och appendixrubriker visas centrerat på två rader.
- Första sidorna har renderats som kontroll enligt PDF-arbetsflödet.
