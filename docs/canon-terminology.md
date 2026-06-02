# Canon: terminologi

## Huvudbegrepp

| Begrepp | Rekommenderad term | Definition | Kommentar |
|---|---|---|---|
| AI-förmåga | AI-förmåga | Organisationens samlade förmåga att styra, utveckla, driftsätta, använda och förvalta AI. | Används genom hela boken. |
| AI-experiment | AI-experiment | Avgränsad prövning av AI-teknik, användningsfall eller arbetssätt. | Ska inte likställas med produktionsklar lösning. |
| AI-lösning | AI-lösning | Konkret implementation som stödjer ett specifikt användningsfall med AI. | Skilj från bredare AI-förmåga. |
| Use-case triage | Use-case triage | Strukturerad första bedömning av AI-användningsfall utifrån nytta, data, risk och styrkrav. | Engelskt/svenskt hybridbegrepp accepteras. |
| AI-portfölj | AI-portfölj | Samlad mängd AI-initiativ, piloter och produktionssatta lösningar som styrs över tid. | Utvecklas mer i kapitel 3. |
| Användningsfall | Användningsfall | Avgränsad situation där AI skapar nytta för en viss användare, process eller verksamhetsförmåga. | Beskriv från verksamhetsbehov, inte från produktnamn. |
| Nyttoklassning | Nyttoklassning | Bedömning av vilken typ av nytta ett användningsfall förväntas skapa. | Exempel: effektivisering, kvalitet, analysförmåga eller bättre kunskapsstöd. |
| Risknivå | Risknivå | Preliminär bedömning av hur känsligt och konsekvensrikt ett AI-användningsfall är. | Ska inte blandas ihop med teknisk komplexitet. |
| AI-roll | AI-roll | Beskriver om AI används som assistent, kunskapsstöd, beslutsstöd, styrande komponent eller automatiserad aktör. | Påverkar krav på kontroll, dokumentation och ansvar. |
| Målarkitektur | Målarkitektur | Önskat framtida arkitekturläge som styr vägval, prioriteringar och införande. | Kan vid behov kompletteras med engelsk term target architecture. |
| Referensarkitektur | Referensarkitektur | Återanvändbar arkitekturbeskrivning för en typ av lösning eller förmåga. | Skilj från lösningsarkitektur. |
| Lösningsarkitektur | Lösningsarkitektur | Detaljerad arkitektur för ett specifikt användningsfall eller system. | Ska följa målarkitektur och återanvända referensarkitektur där det är möjligt. |
| Roadmap | Roadmap | Stegvis plan från nuläge till målarkitektur. | Används för införandeordning, inte enbart projektplan. |
| Architecture Decision Record | ADR | Kort dokumentation av ett arkitekturbeslut, dess bakgrund, alternativ och konsekvenser. | Kan kallas arkitekturbeslut i löptext. |
| Arkitekturbeslut | Arkitekturbeslut | Spårbart vägval som påverkar arkitektur, teknik, styrning eller drift. | Dokumenteras tidigt och omprövas vid behov. |
| Regelefterlevnad | Regelefterlevnad | Förmågan att visa och säkerställa att AI-användning följer relevanta lagar, regler, avtal och interna styrkrav. | Etableras i kapitel 4 som arkitekturdrivande krav. |
| Riskklassning | Riskklassning | Bedömning av AI-användningsfall utifrån rättslig, verksamhetsmässig, informationsmässig och teknisk risk. | Skilj från enbart teknisk komplexitet. |
| Personuppgiftsbehandling | Personuppgiftsbehandling | All hantering av personuppgifter, till exempel insamling, lagring, analys, överföring, loggning eller radering. | Använd särskilt vid GDPR-relaterade avsnitt. |
| Ansvarskedja | Ansvarskedja | Tydlig fördelning av ansvar mellan verksamhet, informationsägare, systemägare, modellägare, juridik, säkerhet och arkitektur. | AI får inte göra ansvar otydligt. |
| Juridisk triage | Juridisk triage | Tidig sortering av AI-användningsfall utifrån rättsliga frågor, risk, data, påverkan och krav på kontroll. | Bygger vidare på use-case triage. |
| Mänsklig kontroll | Mänsklig kontroll | Designad process där människor förstår, granskar och ansvarar för AI-stödets användning och konsekvenser. | Kan kompletteras med human oversight när AI Act diskuteras. |
| AI-governance | AI governance | Styrning, roller, mandat, principer och kontrollmekanismer för AI. | Engelskt begrepp kan användas. |
| AI-princip | AI-princip | Styrande formulering som påverkar hur AI-användningsfall, teknik, ansvar och driftmodell ska utformas. | Ska vara konkret nog för att påverka beslut. |
| Guardrails | Guardrails | Tekniska, processuella eller organisatoriska skyddsräcken som begränsar otillåten eller riskfylld AI-användning. | Används särskilt vid generativ AI och säkerhetsarkitektur. |
| Human oversight | Mänsklig kontroll | Designad mänsklig granskning och ansvar i AI-stödda processer. | Använd svensk term i brödtext och engelsk term när regelverksbegrepp diskuteras. |
| Explainability | Förklarbarhet | Förmågan att förstå, granska eller motivera hur ett AI-stöd har tagit fram ett resultat. | Ska anpassas till risk och mottagare. |
| Policy enforcement | Policy enforcement | Mekanismer som säkerställer att beslutade regler faktiskt följs i användning och drift. | Kan vara tekniskt, organisatoriskt eller båda. |
| Leverantörsoberoende | Leverantörsoberoende | Förmågan att hantera eller byta leverantör, modell eller plattform utan okontrollerad risk. | Ska bedömas riskbaserat, inte absolut. |
| Modulär AI-arkitektur | Modulär AI-arkitektur | Arkitektur där modell, index, orkestrering och driftkomponenter kan bytas med kontrollerade konsekvenser. | Viktigt för långsiktig myndighetsförvaltning. |
| RAG | Retrieval-augmented generation | Mönster där en språkmodell kompletteras med hämtad information från kontrollerade kunskapskällor. | Förklara första gången. |
| MLOps | MLOps | Arbetssätt och verktyg för livscykelhantering av maskininlärningsmodeller. | |
| LLMOps | LLMOps | Livscykelhantering, drift och kvalitetssäkring av lösningar baserade på stora språkmodeller. | |
| AI-gateway | AI-gateway | Kontrollerad åtkomstpunkt mellan applikationer, användare och AI-modeller. | Används som arkitekturbyggblock. |
| Guardrails | Guardrails | Tekniska och organisatoriska skyddsräcken som styr och begränsar AI-användning. | Engelskt begrepp är vedertaget. |
| Sovereign cloud | Sovereign cloud | Molnlösning med särskilt fokus på jurisdiktion, kontroll, datalokalisering och operationell suveränitet. | Förklara i driftkapitlet. |

| Beslutsmatris | Beslutsmatris | Strukturerad jämförelse av arkitekturalternativ mot gemensamma kriterier. | Använd som beslutsstöd, inte som mekanisk poängmaskin. |
| Tradeoff | Tradeoff | Avvägning där ett alternativ ger vissa fördelar men samtidigt skapar nackdelar eller risker. | Används särskilt i vägvalskapitel. |
| Modellkatalog | Modellkatalog | Styrd lista över godkända modeller, modellspår och användningsvillkor. | Ska kopplas till informationsklass och användningsfall. |
| Arkitekturspår | Arkitekturspår | Godkänt mönster för en kategori AI-användningsfall, med tillhörande kontroller, driftmodell och beslut. | Hjälper myndigheten undvika både övercentralisering och fragmentering. |

## Språkregler

- Skriv på svenska.
- Använd engelska begrepp när de är vedertagna och svensk översättning skulle bli otydlig.
- Introducera svensk term och engelsk term tillsammans första gången när det hjälper läsaren.
- Var konsekvent med Tullverket Aurora som scenarionamn.
| Informationsklassning | Informationsklassning | Bedömning av informationens skyddsbehov, vanligtvis utifrån konfidentialitet, riktighet och tillgänglighet. | I AI-flöden ska även promptar, svar, embeddings och loggar ingå. |
| Dataskyddsbedömning | Dataskyddsbedömning | Bedömning av personuppgiftsbehandling, ändamål, rättslig grund, ansvar och skyddsåtgärder. | Skilj från generell informationsklassning. |
| AI-riskbedömning | AI-riskbedömning | Bedömning av risk kopplad till användningsfall, data, AI-roll, automatiseringsgrad och konsekvens. | Risk uppstår inte enbart av modelltyp. |
| Embeddings | Embeddings | Vektorrepresentationer av text eller annan data som används för semantisk sökning och retrieval. | Klassa efter informationen de representerar. |
| Vektorindex | Vektorindex | Sökbart index av embeddings som gör det möjligt att hitta relevant kontext. | Ska skyddas som härledd information. |
| Driftmodell | Driftmodell | Beslut om var och hur en AI-lösning körs och förvaltas, exempelvis moln, hybrid, on-premises eller isolerat. | Ska följa klassning och riskprofil. |
| Policy enforcement | Policy enforcement | Teknisk eller processuell kontroll som säkerställer att regler följs före, under eller efter AI-anrop. | Återkommer i referensarkitekturen. |

## Tillägg från kapitel 7

| Begrepp | Rekommenderad term | Definition | Kommentar |
|---|---|---|---|
| AI-governance | AI-governance | Styrmodell för hur AI-initiativ beslutas, prioriteras, granskas, driftsätts, följs upp och avvecklas. | Introduceras i kapitel 7. |
| Styrklass | Styrklass | Klassning som avgör vilken beslutsnivå, dokumentation och granskning ett AI-användningsfall kräver. | Används för proportionerlig governance. |
| AI-styrgrupp | AI-styrgrupp | Ledningsnära forum för strategiska AI-beslut, riskaptit, prioriteringar och investeringar. | Ska inte detaljstyra teknisk design. |
| AI-governanceforum | AI-governanceforum | Taktiskt forum som bedömer AI-användningsfall, hanterar portfölj, villkor, undantag och eskalering. | Binder samman verksamhet, juridik, säkerhet, dataskydd och arkitektur. |
| Produktionsgodkännande | Produktionsgodkännande | Beslutspunkt innan en AI-lösning får användas i produktion. | Ska inkludera ansvar, risk, loggning, uppföljning och incidenthantering. |
| AI-community | AI-community | Lärande forum för praktiker som delar mönster, erfarenheter, incidenter och återanvändbara lösningar. | Inte primärt ett beslutsforum. |

## Tillägg från kapitel 8

| Begrepp | Rekommenderad term | Definition | Kommentar |
|---|---|---|---|
| Förmågekarta | Förmågekarta | Strukturerad beskrivning av vad myndigheten behöver kunna göra för att etablera, använda och förvalta AI. | Ska inte blandas ihop med systemkarta eller organisationsschema. |
| Capability model | Capability model | Engelsk term för förmågemodell eller förmågekarta. | Används vid koppling till etablerade arkitekturmetoder. |
| AI lifecycle | AI lifecycle | Livscykeln för en AI-lösning från idé, triage och design till drift, uppföljning och avveckling. | Behåll engelsk term där den är vedertagen. |
| Gemensam förmåga | Gemensam förmåga | Förmåga som bör etableras myndighetsgemensamt och återanvändas av flera AI-lösningar. | Exempel: AI-gateway, modellregister och produktionsgodkännande. |
| Federerad förmåga | Federerad förmåga | Förmåga som följer gemensamma regler men utförs nära verksamhetsområde eller produktteam. | Exempel: verksamhetsvalidering och domänspecifika promptmönster. |
| Lokal förmåga | Lokal förmåga | Förmåga som kan hanteras lokalt av ett team inom fastställda styr- och säkerhetsramar. | Får inte kringgå gemensamma miniminivåer. |
| Förmågemognad | Förmågemognad | Bedömning av om en förmåga saknas, är fragmenterad, definierad, etablerad eller förvaltad. | Används som underlag för roadmap. |

| Dataarkitektur | Dataarkitektur | Beskrivning av hur data struktureras, ägs, kvalitetssäkras, skyddas, spåras och används över tid. | Kapitel 9 etablerar dataarkitektur som eget arkitekturperspektiv för AI. |
| Informationsägarskap | Informationsägarskap | Ansvar för informationens kvalitet, klassning, tillgänglighet, användning och livscykel. | Ska kopplas till auktoritativa källor och produktionsgodkända AI-index. |
| Metadata | Metadata | Data om data som kan beskriva källa, version, informationsklass, åtkomstregel, giltighet och ansvar. | I AI-arkitekturen används metadata även som styrningsmekanism. |
| Data lineage | Data lineage | Spårbarhet från källa genom transformationer, index, retrieval, modellinteraktion och AI-svar. | Viktigt vid revision, incidenter, kvalitetssäkring och förvaltning. |
| Embeddings | Embeddings | Numeriska representationer av text, bild eller annan information som möjliggör semantisk sökning. | Ska behandlas som skyddsvärda utifrån källmaterial och användningsfall. |
| Vektordatabas | Vektordatabas | Databas som lagrar embeddings och stödjer semantisk sökning. | Ska omfattas av informationsklassning, åtkomstkontroll, loggning och driftkrav. |
| Chunking | Chunking | Uppdelning av dokument i mindre textstycken för indexering och retrieval. | Påverkar kvalitet, kontext, spårbarhet och risken för lösryckta svar. |
| Behörighetsmedveten retrieval | Behörighetsmedveten retrieval | Hämtning av kontext där resultat filtreras utifrån användarens behörighet, roll och informationsklass. | Grundkrav för RAG i myndighetsmiljö med blandade informationsklasser. |

| Teknisk referensarkitektur | Teknisk referensarkitektur | Återanvändbar teknisk arkitekturbeskrivning som visar AI-byggblock, ansvar, relationer och styrande integrationsmönster. | Etableras i kapitel 10 som karta för tekniska vägval. |
| AI-gateway | AI-gateway | Kontrollerat åtkomstlager mellan applikationer och AI-tjänster. | Hanterar exempelvis policy, loggning, modellval, kvoter och behörighet. |
| Modellplattform | Modellplattform | Teknisk miljö där modeller görs tillgängliga, körs, versioneras, övervakas och förvaltas. | Kan vara molnbaserad, intern eller hybrid. |
| Inferens | Inferens | Körning där en tränad modell tar emot indata och producerar utdata. | Används för både generativa modeller och prediktiva modeller. |
| Orkestrering | Orkestrering | Samordning av flera steg i ett AI-flöde. | Exempel: retrieval, promptkonstruktion, modellkörning och policykontroll. |
| Policy enforcement | Policy enforcement | Teknisk tillämpning av policyregler i systemflödet. | Ska inte reduceras till styrdokument; regler ska kunna verkställas tekniskt. |
| Observability | Observability | Förmåga att förstå drift, användning, kvalitet, kostnad och avvikelser genom loggar, mätvärden och spårning. | Viktigt för AI-drift, incidenthantering och nyttostyrning. |
| Guardrails | Guardrails | Tekniska och processuella skydd som begränsar användning och beteende i en AI-lösning. | Omfattar inte bara filter utan även verktygsbegränsning, källkrav och mänsklig granskning. |
| Agentmönster | Agentmönster | AI-mönster där en modell eller orkestrering kan välja verktyg, anropa API:er eller genomföra flera steg. | Ska användas försiktigt i myndighetsmiljö och kräver stark kontroll. |
| Prompt | Prompt | Instruktion och kontext som skickas till en språkmodell. | Ska hanteras som del av informationsflödet och kan innehålla skyddsvärd information. |
| Promptning | Promptning | Styrning av modellens beteende genom instruktioner och kontext utan att träna om modellen. | Räcker för enklare produktivitetsstöd men inte för styrt myndighetskunskapsstöd. |
| Grounding | Grounding | Koppling mellan modellens svar och specifika källor, data eller regler. | Viktigt för källhänvisning, granskning och tillit. |
| Hallucination | Hallucination | Svar som verkar trovärdigt men inte är korrekt, inte följer källorna eller hittar på information. | Ska hanteras med källstyrning, testning, osäkerhetsmarkering och mänsklig kontroll. |
| Finjustering | Finjustering | Vidareträning av en modell för att påverka beteende, format, stil eller återkommande mönster. | Ska inte användas som ersättning för aktuella styrda källor. |
| Produktivitetsstöd | Produktivitetsstöd | Generativt stöd för lågklassade arbetsuppgifter som formulering, strukturering eller sammanfattning. | Har normalt lägre risk än ärendenära och beslutsnära stöd. |
| Kunskapsstöd | Kunskapsstöd | AI-stöd som hjälper användaren att hitta, sammanfatta och förstå styrda källor. | Auroras första RAG-produkt är ett internt kunskapsstöd. |
| Ärendenära stöd | Ärendenära stöd | AI-stöd som använder eller sammanfattar information kopplad till ett konkret ärende. | Kräver högre kontroll, loggning och tydlig mänsklig granskning. |
| Beslutsnära stöd | Beslutsnära stöd | AI-stöd som ligger nära bedömning, prioritering eller rekommendation i ett beslutsflöde. | Kräver särskild riskprövning och stark governance. |


| Publikt moln | Publikt moln | Extern molninfrastruktur eller molntjänst som delas mellan många kunder genom teknisk separation. | Bedöms utifrån faktisk datahantering, kontroll och leverantörsvillkor. |
| SaaS | SaaS | Färdig applikation eller tjänst där leverantören ansvarar för större delen av applikation och plattform. | Kan vara lämpligt för lågklassat produktivitetsstöd men kräver tydliga villkor. |
| PaaS | PaaS | Plattformstjänst där myndigheten bygger egna lösningar ovanpå leverantörens plattform. | Relevant för AI-plattformar, modell-API:er, RAG och MLOps-tjänster. |
| IaaS | IaaS | Grundläggande molninfrastruktur som virtuella maskiner, nätverk och lagring. | Ger mer kontroll än SaaS men kräver mer eget ansvar. |
| Sovereign cloud | Sovereign cloud | Molnerbjudande med särskilda löften eller mekanismer för datalokalisering, jurisdiktion, åtkomst eller kontroll. | Ska konkretiseras i verifierbara krav; etiketten räcker inte. |
| On-premises | On-premises | Drift i myndighetens egen eller särskilt kontrollerade infrastruktur. | Kan ge kontroll men kräver kapacitet, säkerhet och livscykelförmåga. |
| Privat moln | Privat moln | Molnliknande plattform för en organisation eller avgränsad grupp, driven internt eller av leverantör. | Kan kombinera molnliknande arbetssätt med högre kontroll. |
| Hybridarkitektur | Hybridarkitektur | Arkitektur där olika delar av AI-förmågan körs i olika miljöer och binds samman genom styrda gränssnitt. | Auroras realistiska målbild, men kräver tydliga gränser och ansvar. |
| Driftmodell | Driftmodell | Val och styrning av var och hur AI-komponenter körs, förvaltas, säkras och integreras. | Ska väljas per användningsfall, informationsflöde och AI-roll. |
| Exitstrategi | Exitstrategi | Plan för att kunna lämna eller byta leverantör, modell, plattform eller driftmodell utan oacceptabel risk. | Ska ingå i viktiga drift- och plattformsbeslut. |

| AI-stack | AI-stack | Det samlade tekniklagret för en AI-lösning eller AI-förmåga: data, modellåtkomst, orkestrering, applikation, säkerhet, observability och drift. | Etableras i kapitel 14. |
| Plattformskarta | Plattformskarta | Arkitekturkarta som visar vilka produkt- och plattformskategorier som får användas i vilka byggblock och driftspår. | Används för att undvika produktval utan arkitekturstyrning. |
| Modellhub | Modellhub | Styrd katalog eller åtkomstpunkt för godkända modeller, modellversioner, användningsfall och informationsklasser. | Kan vara del av AI-gateway, modellplattform eller modellregister. |
| Sovereign cloud | Sovereign cloud | Molnerbjudande med särskilda kontroller för datalokalisering, drift, åtkomst och jurisdiktion. | Ska inte användas som garanti; bedöm alltid konkret. |
| Agentramverk | Agentramverk | Ramverk för att bygga AI-flöden där modeller kan orkestrera steg, verktyg, minne eller mänsklig kontroll. | Kräver tydlig loggning, testbarhet och styrning i myndighetsmiljö. |
| Guardrail-komponent | Guardrail-komponent | Teknisk kontroll som begränsar, filtrerar eller övervakar AI-anrop och AI-svar. | Får inte beskrivas som ensam risklösning. |

## Kapitel 16: Säkerhetsarkitektur för AI

| Begrepp | Rekommenderad användning |
|---|---|
| Prompt injection | Används för attacker där instruktioner försöker styra modellen på otillåtet sätt. Förklara både direkt och indirekt variant. |
| Indirekt prompt injection | Används när instruktionen kommer via dokument, webbsida, e-post, bilaga eller annan hämtad kontext. |
| Data leakage | Används för otillåten informationsspridning via prompt, retrieval, modellutdata, logg eller integration. |
| Guardrails | Används som samlingsbegrepp för tekniska och processuella begränsningar som styr vad AI-lösningen får göra. |
| Content filtering | Används för kontroller som blockerar eller flaggar riskfyllt innehåll. |
| Red teaming | Används för AI-specifik säkerhetstestning med realistiska angreppsscenarier. |
| AI-gateway | Används som kontrollplan mellan applikationer och modell- eller AI-tjänster. |
| Säkerhetszon | Används för avgränsad AI-miljö med definierade dataklasser, driftregler och säkerhetskrav. |

## Kapitel 17: Upphandling och leverantörsstyrning

| Begrepp | Rekommenderad användning |
|---|---|
| AI-upphandling | Används för anskaffning av AI-relaterade tjänster, produkter, plattformar och stöd där AI-specifika krav måste hanteras. |
| Anskaffningsstrategi | Används för det samlade valet av avtalsspår, ramavtal, ny upphandling, intern utveckling, konsultstöd eller plattformsspår. |
| Leverantörsstyrning | Används för löpande uppföljning av leverantör, underleverantörer, villkor, säkerhet, kvalitet, kostnad och förändringar. |
| AI-villkor | Används för produkt-, API- och tjänstevillkor som reglerar dataanvändning, loggning, modellträning, underleverantörer och ändringar. |
| Underleverantörskedja | Används för den kedja av aktörer som tillhandahåller eller behandlar delar av AI-tjänsten. |
| Portabilitet | Används för förmågan att flytta data, konfiguration, promptmallar, integrationer och verksamhetslogik. |
| Exitstrategi | Används fortsatt som plan för att kunna lämna eller ersätta leverantör, modell, plattform eller driftmodell. |
| Kritisk inlåsning | Används när en AI-lösning blir verksamhetskritisk utan rimlig insyn, export, ersättningsmöjlighet eller alternativ drift. |

## Kapitel 18: Roadmap från nuläge till etablerad AI-förmåga

| Begrepp | Rekommenderad användning |
|---|---|
| AI-roadmap | Används för den arkitekturella införandeplanen från nuläge till etablerad AI-förmåga. Ska omfatta styrning, teknik, data, juridik, säkerhet, användningsfall och förvaltning. |
| Sandlåda | Används för kontrollerad testmiljö, inte som synonym till produktion. Skriv tydligt vilka data, modeller och användare som är tillåtna. |
| Styrd pilot | Används för pilot som prövar ett användningsfall under realistiska villkor med ansvar, kontroller och mätpunkter. |
| Produktionskriterier | Används för krav som måste uppfyllas före produktionssättning, exempelvis ägare, riskbedömning, loggning, support och incidentprocess. |
| Införandefas | Används för period i roadmapen med särskilt fokus, exempelvis nuläge, sandlåda, pilot, produktion, skalning eller mognad. |
| Mognadsmodell | Används för att mäta om AI-förmågan är styrbar, återanvändbar, säker och förvaltad, inte bara hur många AI-lösningar som finns. |
| Omprövningsdatum | Används för planerad tidpunkt när en AI-lösning, modell, datakälla eller arkitekturbeslut ska granskas på nytt. |

## Kapitel 19: Målarkitektur för Tullverket Aurora

| Begrepp | Rekommenderad användning |
|---|---|
| Arkitekturspår | Används som fördefinierat vägval för en viss typ av AI-användning, med kopplade regler för data, drift, säkerhet, modellval och förvaltning. |
| AI-gateway | Används som gemensam kontrollerad åtkomstpunkt för modellåtkomst, policy, routing, loggning och kostnadsuppföljning. Ska inte beskrivas som en specifik produkt. |
| Modellkatalog | Används som register över godkända modeller, deras villkor, begränsningar, miljöer och användningsområden. |
| RAG-målarkitektur | Används för målbilden som binder samman dokument, metadata, retrieval, modellåtkomst, källhänvisning och uppföljning för kunskapsstöd. |
| Driftspår | Används för att beskriva var och hur ett AI-användningsfall får köras utifrån klassning, risk och kontrollbehov. |
| Dokumentpaket | Används för uppdelning av målarkitekturen i styrande dokument, fördjupningar och operativa mallar. |

| Anti-pattern | Anti-pattern | Återkommande arbetssätt eller arkitekturval som ser rimligt ut kortsiktigt men ofta skapar problem över tid. | Används i kapitel 20 för att beskriva mönster som bör undvikas. |
| Teknisk skuld | Teknisk skuld | Tekniska genvägar som gör en lösning svårare att ändra, säkra eller förvalta. | Skilj från dataskuld och styrningsskuld. |
| Styrningsskuld | Styrningsskuld | Brister i mandat, roller, beslut och ansvar som gör AI-förmågan svår att styra. | Särskilt relevant vid decentraliserad AI-användning. |
| Dataskuld | Dataskuld | Brister i datakvalitet, metadata, ägarskap, åtkomst eller spårbarhet som försämrar AI-lösningar. | Kopplas till dataarkitektur och RAG. |
| Säkerhetsskuld | Säkerhetsskuld | Brister i skydd, loggning, behörighet, segmentering eller incidentförmåga. | Används för att beskriva ackumulerad säkerhetsrisk. |
| Skugg-AI | Skugg-AI | AI-användning som sker utanför myndighetens godkända styrning, verktyg och riskbedömning. | Ska undvikas genom gemensamma guardrails och godkända sandlådor. |
| AI-use-case canvas | AI-use-case canvas | Strukturerad första beskrivning av ett AI-användningsfall med problem, användare, AI-roll, data, risk, nytta och nästa beslut. | Introduceras i kapitel 21 som praktisk mall. |
| Triagechecklista | Triagechecklista | Tidig checklista som hjälper organisationen att sortera ett användningsfall till rätt process. | Skilj från fullständig juridisk eller säkerhetsmässig granskning. |
| Beslutschecklista | Beslutschecklista | Checklista som stödjer ett konkret arkitekturbeslut, exempelvis driftmodell eller RAG-val. | Bör kopplas till ADR. |
| Produktionsberedskap | Produktionsberedskap | Bedömning av om en AI-lösning är redo för produktion utifrån ägarskap, data, juridik, säkerhet, test, drift och förvaltning. | Används som gate mellan pilot och produktion. |
| Omprövningspunkt | Omprövningspunkt | Datum eller händelse som anger när ett arkitekturbeslut ska granskas på nytt. | Viktigt eftersom AI-teknik, risk och villkor förändras. |


## Redaktionella termer

| Begrepp | Rekommenderad term | Definition | Kommentar |
|---|---|---|---|
| Scenarioankare | Tullverket Aurora | Det återkommande fiktiva exemplet som används för att konkretisera vägval. | Används för att göra boken sammanhållen och praktisk. |
| Vägvalsfrågor | Vägvalsfrågor | Frågor som hjälper arkitekten att omsätta kapitlets resonemang i beslut. | Ersätter traditionella övningar. |
| Övergång till nästa kapitel | Övergång till nästa kapitel | Kort redaktionell brygga som visar hur kapitlet leder vidare. | Används för bättre progression. |
