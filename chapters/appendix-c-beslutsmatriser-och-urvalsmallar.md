# Appendix C: Beslutsmatriser och urvalsmallar

## Varför detta appendix finns

Kapitel 14 beskriver plattformar, produkter och ramverk som arkitekturfrågor. Appendix A ger exempel på kommersiella AI-plattformar och molntjänster. Appendix B ger exempel på open source-modeller, ramverk och egen drift. Detta appendix kompletterar dem med beslutsmatriser och urvalsmallar.

Syftet är att göra produkt- och plattformsdiskussionen användbar i praktiskt arkitekturarbete. En större statlig myndighet behöver inte bara veta vilka alternativ som finns. Den behöver också kunna förklara varför ett alternativ är lämpligt, vilka risker som finns, vilka kontroller som krävs och när beslutet bör omprövas.

Appendixet kan användas i arkitekturforum, inför upphandling, vid riskklassning av användningsfall, i dialog mellan verksamhet och IT samt när arkitekturbeslut ska dokumenteras.

## Så ska appendixet användas

Appendixet är inte en poängmodell som automatiskt väljer produkt. Det är ett beslutsstöd. Arkitekten bör använda matriserna för att göra antaganden synliga, fånga beroenden och skapa spårbarhet mellan användningsfall, juridik, säkerhet, driftmodell och teknikval.

Ett bra arbetssätt är:

1. Beskriv användningsfallet.
2. Klassificera information, process och risk.
3. Välj preliminärt arkitekturspår.
4. Använd relevant beslutsmatris.
5. Dokumentera beslut, antaganden och osäkerheter.
6. Sätt kontrollpunkter för omprövning.
7. För in beslutet i målarkitekturen och plattformskartan.

För en myndighet innebär det att varje större AI-val kopplas till ett tydligt arkitekturbeslut, inte till en generell produktpreferens.

## Urvalsmall för AI-byggblock

Denna mall kan användas för varje produkt, plattform, ramverk eller tekniskt byggblock som övervägs.

| Fråga | Svar att dokumentera |
|---|---|
| Vilket byggblock gäller beslutet? | Exempelvis AI-gateway, modellplattform, RAG-lager, vektordatabas, agentramverk eller observability. |
| Vilket användningsfall driver behovet? | Ange konkret verksamhetsbehov och om det gäller experiment, pilot eller produktion. |
| Vilken informationsklass berörs? | Ange om lösningen hanterar öppna data, interna data, personuppgifter, sekretess eller särskilt skyddsvärd information. |
| Vilket driftspår är aktuellt? | SaaS, publikt moln, sovereign cloud, privat moln, on-premises eller hybrid. |
| Vilken förmåga tillför lösningen? | Beskriv konkret arkitekturförmåga, inte bara produktfunktion. |
| Vilka kontroller krävs? | Identitet, loggning, kryptering, region, DLP, behörighet, policy enforcement, mänsklig kontroll och incidenthantering. |
| Vilka beroenden skapas? | Leverantör, licens, modellvillkor, API, dataformat, kompetens, infrastruktur och driftorganisation. |
| Vilka alternativ har bedömts? | Ange minst ett kommersiellt alternativ och, där rimligt, ett open source- eller egen drift-alternativ. |
| När ska beslutet omprövas? | Vid ny informationsklass, större användningsökning, förändrat regelverk, ny leverantörsvillkor eller säkerhetsincident. |

## Matris 1: SaaS, plattform eller egen drift

Den första frågan är ofta om myndigheten ska använda en färdig SaaS-lösning, en bred AI-plattform eller bygga och drifta mer själv.

| Val | När det kan vara lämpligt | När det kräver särskild försiktighet |
|---|---|---|
| Färdig SaaS-assistent | När användningsfallet är låg- till medelrisk, nyttan är tydlig, integrationerna är begränsade och myndigheten kan styra användning med policy, behörighet och dataskydd. | När lösningen hanterar sekretess, känsliga personuppgifter, beslutspåverkande processer eller dataflöden som inte kan kontrolleras tillräckligt. |
| Kommersiell AI-plattform | När myndigheten behöver modellkatalog, API:er, RAG-stöd, agentfunktioner, MLOps, säkerhetsfunktioner och snabbare etablering än egen plattform. | När plattformen skapar stark inlåsning, otydliga datavillkor, begränsad transparens eller svårigheter att uppfylla krav på portabilitet och revision. |
| Egen drift eller kontrollerad open source-stack | När myndigheten behöver hög kontroll, särskild datalokalitet, egen modellservering, insyn, portabilitet eller drift i skyddad miljö. | När organisationen saknar driftkompetens, säkerhetsförmåga, GPU-kapacitet, modellvalidering, patchning, övervakning eller livscykelprocesser. |
| Hybrid | När flera risknivåer, verksamhetsbehov och informationsklasser måste stödjas samtidigt. | När hybridmodellen blir otydlig, duplicerar plattformar eller saknar gemensamma styrprinciper och integrationsmönster. |

För en myndighet blir svaret sällan ett enda val. Myndigheten kan använda en styrd SaaS-assistent för lågklassad produktivitet, en kommersiell AI-plattform för kontrollerade RAG-tillämpningar och egen drift för särskilt känsliga användningsfall.

## Matris 2: Publikt moln, sovereign cloud, privat moln eller on-premises

Driftmiljö bör väljas utifrån risk och kontrollbehov, inte utifrån generell molnpreferens.

| Driftval | När det bör övervägas | Kontrollfrågor |
|---|---|---|
| Publikt moln | När användningsfallet kräver skalbarhet, snabb tillgång till modeller, managed services och integration med befintlig molnstrategi. | Vilka regioner används, hur hanteras underbiträden, hur loggas åtkomst, vilka data får lämna myndighetens miljö och vilka exitmöjligheter finns? |
| Sovereign cloud eller reglerad molnvariant | När myndigheten behöver mer kontroll över drift, datalokalitet, jurisdiktion, supportmodell eller administrativ åtkomst än standardmoln ger. | Vilka garantier är faktiska och avtalade, vilka tjänster ingår, vilka modeller är tillgängliga och vilka beroenden kvarstår? |
| Privat moln | När myndigheten redan har privat moln, stark intern driftförmåga och behov av kontrollerad plattform med viss skalbarhet. | Kan miljön hantera GPU, modellservering, livscykel, patchning, observability och kostnadskontroll över tid? |
| On-premises | När informationen, lagkraven, säkerhetskraven eller operativa kraven gör extern drift olämplig. | Finns tillräcklig kapacitet, redundans, kompetens, säkerhetsövervakning, modelluppdatering och incidentförmåga? |
| Hybrid | När olika informationsklasser och användningsfall kräver olika driftspår men ska styras av samma målarkitektur. | Finns gemensam identitet, loggning, policy, arkitekturbeslut, dataflödeskontroll och livscykelstyrning? |

## Matris 3: RAG, fine-tuning eller egen modellservering

För generativ AI är det viktigt att skilja på kunskapsförankring, modellbeteende och driftkontroll.

| Val | Vad det löser | När det är lämpligt | När det inte räcker |
|---|---|---|---|
| Promptning | Ger snabb styrning av modellens uppgift och ton. | Vid enkla uppgifter, prototyper, sammanfattning, klassificering och låg risk. | När modellen behöver åtkomst till myndighetens aktuella kunskap, spårbarhet eller mer kontrollerad kontext. |
| RAG | Kopplar modellen till dokument, kunskapsbaser och sökindex utan att ändra modellens vikter. | När myndigheten vill ge svar baserade på interna källor, styrdokument, handböcker eller regelverk. | När problemet kräver ny modellförmåga, avancerad domänanpassning eller mycket låg latens i särskild driftmiljö. |
| Fine-tuning | Anpassar modellens beteende, format eller domänmönster. | När många exempel finns, uppgiften är återkommande och RAG inte räcker för önskat beteende. | När behovet främst handlar om aktuell kunskap, källhänvisning eller åtkomst till dokument. |
| Egen modellservering | Ger mer kontroll över drift, dataflöden, latens, modellval och isolering. | När informationsklass, säkerhet, kostnad, prestanda eller portabilitet motiverar egen inferens. | När organisationen saknar kapacitet att hantera modelluppdateringar, övervakning, patchning och säker drift. |
| Hybridmodell | Kombinerar flera mönster för olika risknivåer. | När myndigheten har både lågklassade och känsliga användningsfall. | När arkitekturen saknar tydliga regler för vilka spår som får användas när. |

## Matris 4: Central plattform eller federerad modell

En större myndighet behöver ofta balansera gemensam kontroll med lokal verksamhetsförmåga.

| Modell | När den passar | Risker att hantera |
|---|---|---|
| Central AI-plattform | När myndigheten behöver gemensam styrning, standardiserade säkerhetskontroller, återanvändbara komponenter och samlad kostnadskontroll. | Plattformsteamet kan bli flaskhals, verksamheter kan kringgå plattformen och generella lösningar kan missa lokala behov. |
| Federerad modell | När flera verksamhetsområden har olika behov, tempo och systemmiljöer men kan följa gemensamma principer. | Fragmentering, dubbla lösningar, svag loggning, olika säkerhetsnivåer och svårare leverantörsstyrning. |
| Hub-and-spoke | När myndigheten vill kombinera central styrning med distribuerade produktteam. | Kräver tydliga gränssnitt, arkitekturforum, plattformskarta, beslutsmandat och gemensamma kontroller. |
| Lokal lösning per användningsfall | När användningsfallet är isolerat, experimentellt eller mycket specialiserat. | Riskerar att skapa skugg-AI, duplicering, svag förvaltning och svår avveckling. |

För en myndighet är hub-and-spoke oftast mest realistiskt. Ett centralt plattformsteam tillhandahåller gemensamma byggblock, medan verksamhetsnära team utvecklar lösningar inom tydliga ramar.

## Matris 5: Kommersiellt, open source eller blandat ekosystem

Kommersiella lösningar och open source bör inte behandlas som ideologiska motsatser. De är olika sätt att fördela ansvar, kontroll, kostnad och tempo.

| Val | Vad myndigheten får | Vad myndigheten måste ta ansvar för |
|---|---|---|
| Kommersiell helhetsplattform | Snabb etablering, managed services, support, säkerhetsfunktioner, modellkatalog och integrationsstöd. | Leverantörsstyrning, avtalsrisker, datavillkor, kostnadskontroll, exitplan och beroende av roadmap. |
| Open source-stack | Kontroll, insyn, portabilitet, möjlighet till egen drift och lägre inlåsning. | Drift, säkerhet, patchning, licensgranskning, modellvalidering, kompetens och supportmodell. |
| Blandat ekosystem | Möjlighet att använda managed services där det ger värde och open source där kontroll behövs. | Arkitekturdisciplin, integrationsmönster, gemensam observability och tydliga regler för vad som får blandas. |
| Leverantörsoberoende abstraktionslager | Minskad direktkoppling till en modell eller leverantör. | Risk för extra komplexitet, lägsta gemensamma nämnare och svårare felsökning. |

## Matris 6: Vektordatabas och sökplattform

RAG och kunskapsstöd kräver inte alltid en specialiserad vektordatabas. Valet bör styras av datamängd, sökkvalitet, driftmodell och förvaltningsförmåga.

| Alternativ | När det kan passa | Frågor att ställa |
|---|---|---|
| Befintlig sökplattform med vektorstöd | När myndigheten redan har etablerad sökdrift, kompetens, säkerhet och integrationer. | Räcker prestanda, hybrid search, åtkomstkontroll, metadatahantering och filtrering på dokumentnivå? |
| Specialiserad vektordatabas | När användningsfallet kräver hög skalbarhet, semantisk sökning, låg latens eller avancerad indexhantering. | Hur hanteras behörigheter, backup, region, kryptering, observability, dataradering och driftansvar? |
| Databas med vektorutökning | När volymen är måttlig och myndigheten vill hålla arkitekturen enkel nära befintlig dataplattform. | Är sökkvalitet, indexering, metadata, filtrering och livscykel tillräcklig för användningsfallet? |
| Managed knowledge base-tjänst | När snabb etablering och integrering med modellplattform är viktigare än maximal kontroll. | Vilken kontroll finns över chunking, embeddings, källor, åtkomst, loggning och export? |

## Matris 7: Agentfunktioner och automatiserade arbetsflöden

Agentfunktioner bör införas försiktigt i myndighetsmiljö. Ju mer en AI-komponent får agera, desto viktigare blir kontroll, spårbarhet och mänsklig godkännandeprocess.

| Agentnivå | Beskrivning | Rekommenderad kontroll |
|---|---|---|
| Assisterande svar | AI föreslår text, sammanfattning eller analys men utför inga åtgärder. | Användarpolicy, loggning, källhänvisning och tydlig markering av AI-genererat stöd. |
| Verktygsanrop med godkännande | AI kan föreslå eller förbereda åtgärder, men människa godkänner innan något ändras. | Behörighetskontroll, transaktionslogg, rollback, mänsklig kontroll och testade verktygsgränssnitt. |
| Begränsad automation | AI utför avgränsade åtgärder inom tydliga regler och låg risk. | Policy enforcement, driftövervakning, incidentprocess, rate limits, evalueringsdata och regelbunden granskning. |
| Hög autonomi | AI planerar och genomför flera steg med begränsad mänsklig kontroll. | Bör normalt undvikas i känsliga myndighetsprocesser tills risk, juridik, säkerhet och kontroll är mycket väl etablerade. |

## Matris 8: Säkerhets- och guardrails-nivå

Guardrails är inte en enskild produkt. Det är en kombination av design, policy, kontroller, testning och övervakning.

| Risknivå | Exempel | Minsta kontrollnivå |
|---|---|---|
| Låg | Allmän textbearbetning med icke-känsliga data. | Användarpolicy, grundläggande loggning, tydliga instruktioner och informationsklassningsregler. |
| Medel | Intern kunskapssökning, sammanfattning av interna dokument eller handläggarstöd utan beslutsautomation. | Åtkomstkontroll, källhänvisning, RAG-filtrering, promptskydd, loggning, kvalitetstest och användarutbildning. |
| Hög | Sekretessnära data, beslutspåverkan, verksamhetskritiska analyser eller integration med ärendesystem. | Separat riskbedömning, juridisk granskning, mänsklig kontroll, red teaming, policy enforcement, incidentplan, kontinuerlig övervakning och tydligt modellansvar. |
| Mycket hög | Säkerhetskänslig verksamhet, automatiserade ingripanden eller påverkan på individers rättigheter. | Bör kräva särskild styrning, stark isolering, formell godkännandeprocess, omfattande dokumentation och ofta mycket restriktiv användning. |

## Mall: Arkitekturbeslut för AI-val

Denna mall kan användas som ADR, arkitekturbeslut eller bilaga till målarkitekturen.

| Fält | Innehåll |
|---|---|
| Besluts-ID | Exempelvis AI-ADR-014. |
| Beslut | Kort formulering av vad som beslutas. |
| Status | Föreslaget, beslutat, ersatt eller avvecklat. |
| Kontext | Vilket problem, användningsfall och vilka ramar beslutet gäller. |
| Alternativ | Vilka alternativ som jämförts. |
| Vald lösning | Vilket alternativ som väljs och varför. |
| Informationsklass | Vilken typ av information lösningen får hantera. |
| Driftspår | SaaS, publikt moln, sovereign cloud, privat moln, on-premises eller hybrid. |
| Juridiska antaganden | Dataskydd, sekretess, upphandling, AI Act-klassning och avtalade villkor. |
| Säkerhetskontroller | Identitet, åtkomst, loggning, kryptering, DLP, guardrails, övervakning och incidenthantering. |
| Beroenden | Leverantörer, modeller, ramverk, infrastruktur, kompetens och dataflöden. |
| Konsekvenser | Nytta, risk, kostnad, förvaltning, inlåsning och förändringsbarhet. |
| Omprövning | När beslutet ska ses över. |
| Ägare | Funktion eller roll som ansvarar för beslutets livscykel. |

## Mall: AI-use-case canvas för plattformsval

Denna mall hjälper arkitekten att hålla produktvalet kopplat till verksamhetsnytta och risk.

| Område | Frågor |
|---|---|
| Verksamhetsnytta | Vilket problem löser användningsfallet och för vem? |
| Beslutspåverkan | Påverkar AI-stödet beslut, prioriteringar, riskbedömningar eller individers rättigheter? |
| Data | Vilka datakällor används, vilken informationsklass har de och vem äger dem? |
| Användare | Vilka roller får använda lösningen och vilka behörigheter krävs? |
| AI-mönster | Är det promptning, RAG, klassificering, prediktion, agentflöde, automation eller modellservering? |
| Driftspår | Vilken miljö är preliminärt lämplig och varför? |
| Kontrollkrav | Vilka loggar, tester, guardrails, källhänvisningar och manuella godkännanden krävs? |
| Förvaltning | Vem ansvarar för modell, data, promptar, index, integrationer, kostnad och incidenter? |
| Mätning | Hur mäts kvalitet, nytta, risk, fel, användning och kostnad? |
| Avveckling | Hur tas lösningen bort eller ersätts om den inte längre är lämplig? |

## Mall: Leverantörs- och ramverksbedömning

Denna mall kan användas både för kommersiella alternativ i Appendix A och open source-alternativ i Appendix B.

| Bedömningsområde | Frågor |
|---|---|
| Förmåga | Vilken arkitekturförmåga tillför alternativet? |
| Mognad | Är alternativet produktionsmoget för myndighetens risknivå? |
| Säkerhet | Finns stöd för identitet, åtkomst, kryptering, loggning, isolering och incidenthantering? |
| Dataskydd | Hur hanteras personuppgifter, promptar, träningsdata, loggar, retention och radering? |
| Transparens | Går det att förstå modellval, dataflöden, underleverantörer, driftmiljö och begränsningar? |
| Portabilitet | Går det att byta modell, exportera data, flytta index eller ersätta komponenten? |
| Integration | Passar alternativet med IAM, nätverk, SIEM, ärendesystem, dataplattform och DevSecOps? |
| Kompetens | Har myndigheten eller leverantören tillräcklig kompetens för drift och utveckling? |
| Kostnad | Hur ser kostnadsdrivare ut över tid, inklusive användning, lagring, inferens, drift och support? |
| Avtal och licens | Finns villkor som påverkar offentlig sektor, datalokalitet, revision, exit eller kommersiell användning? |
| Livscykel | Hur hanteras uppgraderingar, modellbyten, sårbarheter, incidenter och avveckling? |

## Samlad checklista före produktbeslut

Innan en produkt, plattform eller ramverk förs in i målarkitekturen bör arkitekten kunna svara ja på följande:

- Är användningsfallet beskrivet och prioriterat?
- Är informationsklassning genomförd?
- Är juridiska och dataskyddsmässiga ramar bedömda?
- Är driftspår valt eller avgränsat?
- Är säkerhetskontroller definierade?
- Är ansvarig ägare utsedd?
- Är minst två alternativ bedömda?
- Är kostnad och kompetens analyserade?
- Är exit och portabilitet hanterade?
- Är beslutet dokumenterat som arkitekturbeslut?
- Är omprövningspunkt satt?
- Är kopplingen till målarkitekturen tydlig?

## Vanliga fallgropar

- **Att använda poängmatriser som facit.** En matris kan strukturera bedömningen, men ersätter inte arkitektoniskt omdöme.

- **Att jämföra produkter utan användningsfall.** Utan tydlig verksamhetskontext blir jämförelsen ofta en lista med funktioner.

- **Att underskatta driftansvaret för open source.** Fri tillgång till kod eller modellvikter betyder inte fri produktion.

- **Att övervärdera leverantörens standardkontroller.** Managed services minskar vissa bördor men tar inte bort myndighetens ansvar.

- **Att glömma avveckling.** Varje AI-komponent bör ha en plan för byte, avveckling eller återgång till manuell process.

- **Att blanda risknivåer i samma lösning.** En lågklassad lösning bör inte gradvis få hantera högre risk utan nytt beslut.

## Koppling till målarkitekturen

Appendix C bör användas som ett praktiskt verktyg när målarkitekturen omsätts i beslut. Det hjälper myndigheten att hålla ihop verksamhetsnytta, juridik, säkerhet, data, drift och leverantörsval.

I en mogen AI-förmåga är det inte produktlistan som är viktigast. Det viktiga är att myndigheten har en repeterbar beslutsmodell som gör det möjligt att välja rätt lösning för rätt användningsfall, ompröva beslut när förutsättningarna ändras och undvika att teknikval driver arkitekturen i fel riktning.
