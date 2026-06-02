# Kapitelplan

## Del 1: Att rama in AI-förmågan

### Kapitel 0: Inledning

- Syfte: Beskriva bokens syfte, målgrupp, förkunskaper, scenario och rekommenderad läsordning.
- Läsarens förkunskaper: Erfarenhet av IT-arkitektur och offentlig IT-styrning.
- Nya huvudbegrepp: AI-förmåga, målarkitektur, Tullverket Aurora.
- Praktiskt exempel/scenario: Introduktion till Tullverket Aurora.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Läsarens arkitekturbakgrund.

### Kapitel 1: Från AI-experiment till myndighetsgemensam AI-förmåga

- Syfte: Visa varför isolerade AI-test inte räcker och vad det innebär att etablera en varaktig AI-förmåga.
- Läsarens förkunskaper: Grundläggande förståelse för myndighetsstyrning och arkitektur.
- Nya huvudbegrepp: AI-experiment, AI-förmåga, skalning, styrbarhet.
- Praktiskt exempel/scenario: Tullverket Auroras tidiga AI-test.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Inledningen.

### Kapitel 2: Vad målarkitektur betyder för AI

- Syfte: Förklara skillnaden mellan nuläge, målarkitektur, referensarkitektur, lösningsarkitektur, roadmap och styrande principer.
- Nya huvudbegrepp: Target architecture, reference architecture, roadmap, architecture decision record.
- Praktiskt exempel/scenario: Hur Tullverket Aurora avgränsar sin AI-målarkitektur.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 1.

### Kapitel 3: AI-portföljen: vilka användningsfall ska myndigheten stödja?

- Syfte: Kategorisera AI-användning och visa hur användningsfall påverkar risk, juridik, data och teknikval.
- Nya huvudbegrepp: AI-portfölj, use-case triage, nyttoklassning, risknivå.
- Praktiskt exempel/scenario: Intern kunskapssökning, dokumentgranskning och riskanalys i tullmiljö.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 1–2.

## Del 2: Ramarna innan tekniken

### Kapitel 4: Juridik, ansvar och regelefterlevnad

- Syfte: Behandla AI Act, GDPR, offentlighet och sekretess, arkiv, upphandling, ansvarsfördelning och dokumentation.
- Nya huvudbegrepp: Regelefterlevnad, riskklassning, personuppgiftsbehandling, ansvarskedja.
- Praktiskt exempel/scenario: Juridisk triage av tre AI-användningsfall.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 3.

### Kapitel 5: Informationsklassning, dataskydd och riskstyrning

- Syfte: Visa hur data, användningsfall och AI-komponenter bör klassas innan plattformsval.
- Nya huvudbegrepp: Informationsklassning, dataminimering, skyddsvärde, modellrisk.
- Praktiskt exempel/scenario: Klassning av tulldokument, handläggarstöd och analysdata.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 4.

### Kapitel 6: Arkitekturprinciper för offentlig AI

- Syfte: Formulera principer för säkerhet, rättssäkerhet, mänsklig kontroll, transparens, spårbarhet, interoperabilitet och leverantörsoberoende.
- Nya huvudbegrepp: AI-principer, guardrails, human oversight, explainability.
- Praktiskt exempel/scenario: Principbeslut för Tullverket Aurora.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 4–5.

### Kapitel 7: Governance och beslutsmodell för AI

- Syfte: Beskriva forum, roller, mandat och processer för AI-beslut.
- Nya huvudbegrepp: AI governance board, arkitekturforum, modellägare, informationsägare.
- Praktiskt exempel/scenario: Beslutsvägar för AI-projekt i Tullverket Aurora.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 6.

## Del 3: Målarkitekturens byggblock

### Kapitel 8: Förmågekarta för AI i myndigheten

- Syfte: Ta fram en förmågekarta för AI från idé till avveckling.
- Nya huvudbegrepp: Förmågekarta, capability model, AI lifecycle.
- Praktiskt exempel/scenario: Auroras förmågekarta.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 7.

### Kapitel 9: Dataarkitektur för AI

- Syfte: Behandla datakällor, metadata, informationsägarskap, datakvalitet, åtkomstkontroll, lineage, sökindex och vektordatabaser.
- Nya huvudbegrepp: Data lineage, metadata, embeddings, vektordatabas.
- Praktiskt exempel/scenario: Regelverk och ärendedokument som kunskapsbas.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 5 och 8.

### Kapitel 10: Teknisk referensarkitektur

- Syfte: Beskriva målarkitekturens centrala komponenter.
- Nya huvudbegrepp: AI-gateway, modellplattform, RAG-lager, policy enforcement, observability.
- Praktiskt exempel/scenario: Referensarkitektur för Auroras AI-plattform.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 8–9.

### Kapitel 11: Generativ AI, RAG och kunskapsstöd

- Syfte: Visa när promptning räcker, när RAG är rätt, när finjustering är relevant och när egen modellservering behövs.
- Nya huvudbegrepp: RAG, fine-tuning, prompt engineering, retrieval, hallucination.
- Praktiskt exempel/scenario: Intern kunskapssökning i regelverk och handböcker.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 9–10.

### Kapitel 12: MLOps, LLMOps och livscykelhantering

- Syfte: Gå igenom modellregister, versionering, test, validering, deployment, drift, mätning, incidenter och avveckling.
- Nya huvudbegrepp: MLOps, LLMOps, modellregister, driftövervakning, modellavveckling.
- Praktiskt exempel/scenario: Livscykel för Auroras handläggarstöd.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 10–11.

## Del 4: Plattformar, drift och vägval

### Kapitel 13: Moln, on-premises och hybrid: en beslutsmodell

- Syfte: Ge en praktisk modell för val mellan SaaS, publikt moln, sovereign cloud, privat moln, on-premises och hybrid.
- Nya huvudbegrepp: Sovereign cloud, privat moln, hybridarkitektur, datalokalisering.
- Praktiskt exempel/scenario: Driftmodeller för tre AI-användningsfall.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 5, 10 och 12.

### Kapitel 14: Plattformar, produkter och ramverk att överväga

- Syfte: Behandla produkt- och plattformskategorier utan att bli en produktmanual.
- Nya huvudbegrepp: AI-assistent, hyperscalerplattform, open source-modell, inferensplattform, orkestreringsramverk.
- Praktiskt exempel/scenario: Auroras plattformsutvärdering.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 13.

### Kapitel 15: När man väljer vad

- Syfte: Samla arkitekturbeslut om köpa eller bygga, central eller federerad plattform, RAG eller fine-tuning, moln eller on-premises.
- Nya huvudbegrepp: Architecture decision record, beslutsmatris, tradeoff.
- Praktiskt exempel/scenario: Beslutslogg för Auroras målarkitektur.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 13–14.

### Kapitel 16: Säkerhetsarkitektur för AI

- Syfte: Behandla hot, skyddsåtgärder och driftsäkerhet i AI-lösningar.
- Nya huvudbegrepp: Prompt injection, data leakage, red teaming, guardrails, content filtering.
- Praktiskt exempel/scenario: Säkerhetskrav för ett RAG-baserat kunskapsstöd.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Kapitel 10–15.

### Kapitel 17: Upphandling och leverantörsstyrning

- Syfte: Ta upp kravställning, datalokalisering, exitstrategi, transparens, revision, SLA, modellvillkor och öppna standarder.
- Nya huvudbegrepp: Exitstrategi, leverantörsrisk, underbiträde, revisionsrätt.
- Praktiskt exempel/scenario: Kravbilaga för Auroras AI-plattform.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 13–16.

## Del 5: Införande och praktisk målarkitektur

### Kapitel 18: Roadmap: från nuläge till etablerad AI-förmåga på 24 månader

- Syfte: Föreslå en stegvis införandeplan från nuläge till förvaltad AI-förmåga.
- Nya huvudbegrepp: Roadmap, mognadssteg, pilotportfölj, produktionssättning.
- Praktiskt exempel/scenario: Auroras 24-månadersplan.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 1–17.

### Kapitel 19: Målarkitektur för Tullverket Aurora

- Syfte: Samla bokens delar i ett sammanhängande exempel.
- Nya huvudbegrepp: Målbild, byggblock, säkerhetszoner, integrationsmönster, arkitekturbeslut.
- Praktiskt exempel/scenario: Komplett målarkitekturskiss för Aurora.
- Svårighetsgrad: Avancerad.
- Bygger vidare på: Hela boken.

### Kapitel 20: Vanliga misstag och anti-patterns

- Syfte: Visa återkommande fallgropar och hur de undviks.
- Nya huvudbegrepp: Anti-pattern, teknisk skuld, styrningsskuld, dataskuld.
- Praktiskt exempel/scenario: Felaktiga vägval i Aurora och hur de korrigeras.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Hela boken.

### Kapitel 21: Arkitektens checklistor och beslutsmallar

- Syfte: Samla praktiska mallar och beslutsstöd.
- Nya huvudbegrepp: AI-use-case canvas, moln/on-prem-beslutsmatris, plattformschecklista.
- Praktiskt exempel/scenario: Mallar ifyllda med Aurora-exempel.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Hela boken.

## Progressionskontroll

- Begrepp introduceras i rätt ordning: Ja. Boken börjar med behov och målbild, går vidare till juridik och risk, därefter arkitektur, plattformar och införande.
- För svåra hopp: Kapitlen om juridik, informationsklassning, referensarkitektur och plattformsval bör skrivas med tydliga vägvalsramar för att undvika för branta hopp.
- Repetitionstillfällen: Kapitel 7, 10, 15, 18 och 21 återknyter till tidigare principer och beslut.
- Slutprojekt eller sammanfattande moment: Kapitel 19 fungerar som sammanhållet arkitekturexempel och kapitel 21 som praktisk mallbank.


## Appendix

### Appendix A: Kommersiella AI-plattformar och molntjänster

- Syfte: Ge en konkret och uppdateringsbar översikt över kommersiella AI-plattformar, molntjänster och leverantörserbjudanden som kan vara relevanta för en större statlig myndighet.
- Läsarens förkunskaper: Läsaren bör ha läst kapitel 14 eller ha motsvarande förståelse för AI-plattformar som arkitekturfråga.
- Nya huvudbegrepp: Produktivitetsassistent, hyperscalerplattform, modell-API, kommersiellt RAG-lager, AI-governanceverktyg, verksamhetsagent.
- Praktiskt exempel/scenario: Tullverket Aurora använder appendixet för att jämföra kommersiella alternativ per arkitekturspår.
- Svårighetsgrad: Erfaren.
- Bygger vidare på: Kapitel 14 och kapitel 15.


### Appendix B: Open source-modeller, ramverk och egen drift

- Syfte: Ge en konkret och uppdateringsbar översikt över öppna modellfamiljer, open source-ramverk, vektordatabaser, serveringslösningar och driftmönster för egen eller kontrollerad AI-drift.
- Läsarens förkunskaper: Läsaren bör ha läst kapitel 14 och Appendix A eller ha motsvarande förståelse för plattformsval, driftmodeller och AI-livscykel.
- Nya huvudbegrepp: Öppna modellvikter, modellhub, egen inferens, RAG-ramverk, vektordatabas, LLMOps, evalueringsramverk, policy som kod.
- Praktiskt exempel/scenario: Tullverket Aurora använder appendixet för att bedöma när open source är lämpligt som experimentspår, produktionsspår eller alternativ till kommersiell plattform.
- Svårighetsgrad: Erfaren till avancerad.
- Bygger vidare på: Kapitel 14, kapitel 15 och Appendix A.


### Appendix C: Beslutsmatriser och urvalsmallar

- Syfte: Ge praktiska beslutsmatriser och urvalsmallar för att jämföra SaaS, kommersiella plattformar, open source, egen drift, RAG, fine-tuning, agentfunktioner, vektordatabaser och driftspår.
- Läsarens förkunskaper: Läsaren bör ha läst kapitel 14, kapitel 15 samt Appendix A och B.
- Nya huvudbegrepp: Beslutsmatris, urvalsmall, arkitekturbeslut, omprövningspunkt, driftspår, kontrollnivå och AI-use-case canvas.
- Praktiskt exempel/scenario: Tullverket Aurora använder appendixet för att fatta och dokumentera plattformsval som spårbara arkitekturbeslut.
- Svårighetsgrad: Erfaren till avancerad.
- Bygger vidare på: Kapitel 14, kapitel 15, Appendix A och Appendix B.

