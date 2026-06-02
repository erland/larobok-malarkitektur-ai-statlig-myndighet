# Appendix A: Kommersiella AI-plattformar och molntjänster

## Syfte med appendixet

Detta appendix kompletterar kapitel 14. Huvudkapitlet beskriver hur en statlig myndighet bör resonera om plattformar, produkter och ramverk som arkitekturfråga. Appendixet är mer konkret: det ger en översikt över kommersiella alternativ som ofta blir aktuella när en större myndighet ska etablera AI-förmåga.

Syftet är inte att rekommendera en leverantör. Syftet är att ge arkitekten ett praktiskt underlag för att förstå:

- vad olika produktkategorier tillför i målarkitekturen,
- när de är lämpliga att överväga,
- vilka frågor som behöver besvaras före beslut,
- vilka risker som behöver hanteras,
- vilka alternativ som bör jämföras med open source och egen drift i Appendix B.

Appendixet är medvetet separerat från huvudkapitlen. Produkter, licensmodeller, regioner, dataskyddsvillkor, säkerhetsfunktioner och modellutbud förändras snabbt. En myndighet bör därför se detta som en uppdateringsbar katalog, inte som en statisk rekommendation.

## Så ska appendixet användas

När en myndighet ska välja tekniska byggblock bör appendixet användas efter att följande redan är gjort:

- användningsfallet är beskrivet,
- informationsklassning är genomförd,
- juridiska och säkerhetsmässiga ramar är bedömda,
- driftspår är valt eller preliminärt avgränsat,
- arkitekturprinciper och kontrollpunkter är kända.

Om organisationen börjar här, i produktlistan, är risken stor att tekniken driver arkitekturen i stället för tvärtom. Appendixet bör därför användas som jämförelsestöd, inte som inköpslista.

För varje plattform eller produktkategori bör arkitekten ställa fem frågor:

1. Vilken förmåga tillför detta i målarkitekturen?
2. Vilka data, användare och processer kommer den åt?
3. Vilken kontroll får myndigheten över identitet, loggning, region, kryptering, modellval och livscykel?
4. Vilka delar blir beroende av leverantörens villkor, roadmap och driftsmodell?
5. Vilket alternativ finns om lösningen måste bytas ut, avgränsas eller tas hem?

## Översikt över produktkategorier

| Kategori | Typisk nytta | Typisk risk |
|---|---|---|
| Produktivitetsassistenter | Snabb nytta för låg- och medelriskarbete | Otydlig användning, dataläckage, svår kontroll över beteende |
| Hyperscalerplattformar | Brett modellutbud, snabb utveckling, integrationsstöd | Leverantörsberoende, regionval, komplex kostnadsstyrning |
| Data- och analysplattformar med AI | AI nära data och befintlig analysmiljö | Plattformsspecifik arkitektur och svåra exitfrågor |
| Modell- och API-leverantörer | Direkt åtkomst till starka modeller | Extern behandling, avtalsvillkor, datalagring och regulatorisk prövning |
| Kommersiella RAG- och söktjänster | Snabbare kunskapsstöd och semantisk sökning | Felaktig åtkomstmodell, bristande spårbarhet, kvalitetsproblem |
| Kommersiell AI-infrastruktur | Kontrollerad drift, GPU-stöd, enterprise support | Kostnad, kapacitetsplanering, teknisk komplexitet |
| AI-governance och riskverktyg | Stöd för dokumentation, policy och modellkontroll | Risk att verktyget ersätter verklig ansvarsfördelning |
| Verksamhetsplattformar med AI-agenter | AI i befintliga arbetsflöden | Agentbehörigheter, indirekt prompt injection och svår revisionsbarhet |

## Microsoft Azure AI Foundry och Azure OpenAI

### Vad plattformen tillför

Microsofts AI-erbjudande är ofta relevant i myndigheter som redan använder Microsoft 365, Entra ID, Azure, Purview, Defender, Sentinel eller andra delar av Microsofts ekosystem. Azure AI Foundry kan fungera som en samlande plattform för att hitta, testa, bygga, driftsätta och styra AI-applikationer och agenter. Azure OpenAI och andra modeller i modellkatalogen kan användas för generativ AI, sammanfattning, klassificering, kodstöd, RAG och andra språkbaserade funktioner.

I målarkitekturen kan plattformen bidra med:

- modellåtkomst och modellkatalog,
- API-baserad generativ AI,
- stöd för agent- och applikationsutveckling,
- koppling till Azure AI Search för RAG,
- identitets- och behörighetsintegration med Microsoft-miljö,
- säkerhets- och övervakningskopplingar till övrig Azure-plattform,
- enterprise-funktioner för styrning, policy och drift.

För en myndighet kan detta vara aktuellt för ett första kontrollerat spår för intern kunskapssökning, sammanfattning av styrdokument, stödfunktioner för arkitekturteam och kontrollerade pilotlösningar där myndigheten redan har Azure som godkänd plattform.

### När det är lämpligt

Plattformen bör övervägas när myndigheten redan har en etablerad Microsoft- och Azure-strategi, när identitetsintegration med Entra ID är central och när man vill kombinera generativ AI med övriga Azure-tjänster. Den är särskilt relevant när myndigheten behöver en bred enterprise-plattform snarare än en isolerad modell-API-tjänst.

Den kan också vara lämplig när organisationen vill införa flera olika arkitekturspår men ändå ha gemensamma kontroller för åtkomst, loggning, nätverk, region, nyckelhantering och kostnadsuppföljning.

### När den kräver särskild analys

För högklassad information behöver region, databehandling, loggning, supportåtkomst, underleverantörer och avtalsvillkor granskas noggrant. Det räcker inte att en funktion finns i Azure; den måste vara tillgänglig i rätt region, med rätt villkor och rätt tekniska kontroller.

Myndigheten bör också undvika att låta plattformens modellkatalog bli synonym med målarkitektur. Målarkitekturen ska definiera vilka egenskaper en modell- och applikationsplattform måste ha, inte bara vilka modeller som råkar finnas i katalogen.

### Typiska arkitekturfrågor

- Vilka Azure-regioner är godkända för respektive informationsklass?
- Hur styrs modellval och modellversioner?
- Hur separeras experiment, test och produktion?
- Vilka promptar, svar och loggar lagras, var och hur länge?
- Hur integreras plattformen med myndighetens SIEM, IAM, DLP och datakatalog?
- Hur undviker myndigheten att RAG-index byggs utan korrekt behörighetsmodell?

## Microsoft 365 Copilot och Copilot Chat

### Vad plattformen tillför

Microsoft 365 Copilot och Copilot Chat är relevanta som produktivitets- och kunskapsassistenter i organisationer som redan använder Microsoft 365. De kan ge snabb nytta i arbetsflöden som e-post, möten, dokument, sammanfattningar, informationssökning och intern produktion av text.

I målarkitekturen bör de inte behandlas som samma sak som en generell AI-plattform. De är snarare en användarnära AI-kanal med stark koppling till Microsoft 365-data och behörigheter.

För en myndighet kan detta vara aktuellt för låg- och medelriskarbete, exempelvis mötessammanfattningar, utkast till interna dokument, stöd för projektkommunikation och personlig produktivitet. Det bör däremot inte införas brett för sekretessbelagda, operativa eller rättsligt känsliga uppgifter utan tydlig policy, utbildning och kontroll.

### När det är lämpligt

Det är lämpligt när syftet är att snabbt höja produktiviteten i befintliga kontorsflöden och när myndigheten har god ordning på behörigheter, informationsklassning, dokumentstruktur, känslighetsetiketter och livscykelhantering i Microsoft 365.

En viktig poäng är att Copilot kan exponera befintliga behörighetsproblem. Om en användare redan har för bred åtkomst till dokument kan en AI-assistent göra problemet mer synligt och mer effektivt, inte skapa det från grunden.

### När det kräver särskild analys

Införande bör föregås av en särskild bedömning av informationshantering. Myndigheten behöver veta vilka datakällor assistenten kan nå, hur känsliga dokument märks upp, hur delning begränsas, hur användare utbildas och hur incidenter hanteras.

Det krävs också tydliga regler för när svar från assistenten får användas i beslutsunderlag, externa handlingar, rättsliga bedömningar eller ärendehantering.

### Typiska arkitekturfrågor

- Är behörighetsmodellen i Microsoft 365 tillräckligt korrekt?
- Finns fungerande känslighetsetiketter och retention-policyer?
- Är användarna utbildade i vad som inte får matas in?
- Hur följs användning, risker och incidenter upp?
- Vilka användningsfall är uttryckligen förbjudna?
- Är detta ett produktivitetsverktyg, ett verksamhetssystem eller ett beslutsstöd?

## Amazon Bedrock

### Vad plattformen tillför

Amazon Bedrock är en kommersiell AI-plattform för att bygga generativa AI-applikationer med flera olika foundation models, inklusive stöd för RAG via Knowledge Bases, agentfunktioner och guardrails. För organisationer som redan använder AWS kan Bedrock vara ett naturligt AI-lager i en större molnarkitektur.

I målarkitekturen kan Bedrock bidra med:

- åtkomst till flera modellfamiljer via en gemensam tjänst,
- RAG-mönster via Knowledge Bases,
- agentliknande arbetsflöden,
- guardrails och säkerhetskontroller,
- integration med övriga AWS-tjänster,
- möjlighet att bygga AI-applikationer nära data som redan finns i AWS.

För en myndighet kan Bedrock vara relevant om myndigheten har ett etablerat AWS-spår eller om ett särskilt användningsfall kräver modellbredd, RAG-komponenter och integrationsmönster som passar AWS-miljön.

### När det är lämpligt

Bedrock bör övervägas när myndigheten redan har AWS-kompetens, governance och säkerhetsmönster på plats. Det är särskilt relevant för applikationsdriven generativ AI där utvecklingsteam behöver bygga egna tjänster och inte bara använda en färdig assistent.

Det kan också vara lämpligt när myndigheten vill kunna jämföra flera modellleverantörer inom samma plattform, under gemensamma IAM-, loggnings- och nätverkskontroller.

### När det kräver särskild analys

Arkitekten behöver analysera regionstöd, modellvillkor, loggning, databehandling och integration med befintliga säkerhetsverktyg. Knowledge Bases och Agents kan sänka utvecklingströskeln, men de löser inte automatiskt informationsklassning, källkvalitet, åtkomstkontroll eller ansvarsfrågor.

Guardrails ska ses som ett tekniskt kontrollager, inte som garanti för rättssäkert eller korrekt AI-beteende.

### Typiska arkitekturfrågor

- Vilka modeller får användas för vilken informationsklass?
- Hur kontrolleras datakällor i Knowledge Bases?
- Hur mappas behörigheter från källsystem till RAG-svar?
- Vilken observability finns för agentsteg och verktygsanrop?
- Hur hanteras kostnader vid många modell- och retrieval-anrop?
- Hur dokumenteras modellval och guardrail-konfigurationer?

## Google Vertex AI och Gemini Enterprise

### Vad plattformarna tillför

Google Vertex AI är en AI- och ML-plattform som omfattar modellutveckling, modellkatalog, generativ AI, driftsättning, utvärdering och integration med Googles molntjänster. Model Garden används för att upptäcka, testa, anpassa och driftsätta modeller. Vertex AI Agent Builder och närliggande Gemini Enterprise-funktioner är relevanta för organisationer som vill bygga eller använda agent- och kunskapslösningar över verksamhetsdata.

Gemini Enterprise kan betraktas som en mer användarnära plattform för intranätsökning, AI-assistenter och agentiska arbetsflöden med koppling till verksamhetens informationskällor.

I målarkitekturen kan Google-spåret bidra med:

- modellkatalog och generativa modeller,
- AI-applikations- och agentbyggande,
- enterprise-sökning och åtkomst till verksamhetsdata,
- koppling till Google Cloud-data och analys,
- produktivitetsintegration för organisationer som använder Google Workspace.

### När det är lämpligt

Google-plattformar bör övervägas när myndigheten redan har Google Cloud eller Google Workspace som strategisk miljö, eller när ett specifikt användningsfall passar Googles styrkor inom sök, dataanalys, multimodala modeller och AI-applikationsutveckling.

De kan också vara relevanta i ett jämförande upphandlings- eller marknadsanalysarbete där myndigheten vill förstå alternativ till Microsoft- och AWS-spår.

### När det kräver särskild analys

Som för andra molnplattformar krävs noggrann analys av regioner, databehandling, åtkomst, loggning, support, kontraktsvillkor och integration med myndighetens befintliga säkerhetsarkitektur. För agent- och enterprise-sökfunktioner behöver särskild uppmärksamhet läggas på vilka datakällor som kopplas in och hur behörigheter respekteras.

### Typiska arkitekturfrågor

- Vilka datakällor får en enterprise-assistent indexera?
- Hur säkerställs permissions-aware sökning?
- Hur styrs vilka modeller och agenter som får användas?
- Hur separeras experiment från produktion?
- Vilka loggar behövs för revision, incidenthantering och felsökning?
- Hur passar plattformen med myndighetens befintliga IAM- och SIEM-miljö?

## NVIDIA AI Enterprise och NVIDIA NIM

### Vad plattformen tillför

NVIDIA AI Enterprise och NVIDIA NIM är relevanta när myndigheten behöver kommersiellt supportad AI-infrastruktur, modellservering och GPU-baserad inferens, särskilt i privat moln, on-premises eller hybridmiljö. NIM tillhandahåller paketerade inference-mikrotjänster för olika typer av modeller, medan AI Enterprise fungerar som ett bredare enterprise-lager för utveckling, driftsättning och hantering av AI-applikationer.

I målarkitekturen kan detta bidra med:

- standardiserad modellservering,
- bättre kontroll över driftmiljö,
- stöd för on-premises och hybridarkitektur,
- kommersiell support för AI-runtime och inferens,
- möjlighet att köra öppna eller kommersiellt licensierade modeller nära känsliga data.

För en myndighet kan detta vara aktuellt när vissa användningsfall inte kan placeras i publikt moln men ändå behöver modern modellservering och skalbar inferens.

### När det är lämpligt

Det är lämpligt när myndigheten har krav på egen drift, låg latens, särskild datakontroll eller behov av GPU-accelererad inferens i kontrollerade miljöer. Det kan också vara relevant om myndigheten redan har en Kubernetes-, virtualiserings- eller privat moln-strategi där AI-funktioner ska placeras.

### När det kräver särskild analys

Den stora frågan är inte bara teknisk. Myndigheten behöver kunna planera kapacitet, drifta GPU-resurser, hantera kostnader, uppdatera modeller, övervaka prestanda och säkra runtime-miljön. Egen eller nära egen drift ger mer kontroll men också mer ansvar.

### Typiska arkitekturfrågor

- Vilka modeller ska köras i egen miljö och varför?
- Är kostnaden för GPU-kapacitet motiverad av risk- eller prestandakrav?
- Hur uppdateras inference-containrar och modeller?
- Hur integreras modellservering med AI-gateway, IAM, loggning och policy?
- Vilken fallback finns om kapaciteten inte räcker?
- Vilka delar ska vara kommersiellt supportade och vilka kan vara open source?

## Red Hat OpenShift AI

### Vad plattformen tillför

Red Hat OpenShift AI är relevant för organisationer som redan använder OpenShift eller vill etablera AI-förmåga på en containerplattform med hybrid cloud-orientering. Plattformen riktar sig mot utveckling, träning, modellhantering, MLOps och driftsättning av AI-arbetslaster i en enterprise-Kubernetes-miljö.

I målarkitekturen kan den bidra med:

- en gemensam plattform för AI-team,
- stöd för hybrid och self-managed drift,
- integration med containerbaserade driftmönster,
- modellregister och modellservering,
- styrning via befintliga Kubernetes- och OpenShift-mekanismer.

För en myndighet kan detta vara aktuellt om myndigheten redan har OpenShift som strategisk applikationsplattform och vill undvika att AI blir en separat parallell infrastruktur.

### När det är lämpligt

Plattformen är lämplig när myndigheten har stark container- och plattformskompetens och vill bygga AI-förmåga på samma grund som övriga moderna applikationer. Den passar särskilt bra där hybridarkitektur, standardiserad runtime, intern plattformsförvaltning och kontroll över driftmiljö är viktiga.

### När det kräver särskild analys

OpenShift AI ger inte i sig en färdig myndighetsgemensam AI-förmåga. Det är en plattformskomponent som kräver komplettering med dataarkitektur, modellpolicy, RAG-komponenter, AI-gateway, observability, säkerhetskontroller och tydlig förvaltning.

### Typiska arkitekturfrågor

- Är OpenShift redan godkänd och etablerad som strategisk plattform?
- Finns team som kan drifta AI-arbetslaster på Kubernetes?
- Hur hanteras GPU-noder, modellversioner och inferensskalning?
- Vilka delar ska byggas internt och vilka ska köpas som tjänst?
- Hur kopplas plattformen till myndighetens datakällor och säkerhetszoner?

## Databricks Mosaic AI

### Vad plattformen tillför

Databricks Mosaic AI är relevant för myndigheter som redan använder Databricks som data- och analysplattform eller som överväger en lakehouse-orienterad AI-arkitektur. Plattformen kan bidra med modellträning, modellservering, vektorsökning, feature- och datahantering, experiment, governance och generativa AI-arbetsflöden nära data.

I målarkitekturen kan Databricks-spåret tillföra:

- AI nära data- och analysplattformen,
- vektorsökning och RAG-komponenter,
- modellservering,
- koppling mellan klassisk ML, generativ AI och data engineering,
- governance via plattformens data- och behörighetslager.

För en myndighet kan detta vara relevant för analysnära användningsfall, riskmodeller, prediktiv analys och RAG över data som redan hanteras i en kontrollerad data- och analysmiljö.

### När det är lämpligt

Det är lämpligt när AI-förmågan är tätt kopplad till myndighetens dataplattform och när verksamheten behöver kombinera strukturerad analys, maskininlärning, generativ AI och datastyrning.

Det passar särskilt väl när data engineering, ML och analys redan sker i Databricks och när myndigheten vill undvika att bygga separata AI-pipelines vid sidan av dataplattformen.

### När det kräver särskild analys

Risken är att lösningen blir starkt plattformsspecifik. Arkitekten behöver analysera exit, portabilitet, kostnad, integration med verksamhetssystem, juridisk lämplighet och hur plattformens governance motsvarar myndighetens krav.

### Typiska arkitekturfrågor

- Vilka AI-användningsfall hör naturligt hemma nära dataplattformen?
- Ska RAG byggas mot dokument, tabeller eller båda?
- Hur separeras experiment, analys och produktion?
- Hur dokumenteras modell- och datapipelinebeslut?
- Hur integreras plattformen med övrig AI-gateway och central policy?

## Snowflake Cortex AI

### Vad plattformen tillför

Snowflake Cortex AI är relevant där myndigheten redan använder Snowflake som dataplattform eller där AI-funktioner ska placeras nära strukturerad och semistrukturerad data i Snowflake. Cortex Analyst kan användas för naturligt språk mot strukturerad data, medan Cortex Search och andra funktioner kan stödja sök- och AI-mönster i plattformens datamiljö.

I målarkitekturen kan Snowflake-spåret bidra med:

- AI-funktioner nära befintliga data,
- naturligt språk mot analytiska datamängder,
- sök- och RAG-liknande mönster,
- integrerad datastyrning inom Snowflake-miljön,
- minskad datarörelse för vissa analysfall.

### När det är lämpligt

Det är lämpligt när användningsfallen är nära dataanalys, rapportering, beslutsstöd och strukturerade informationsmängder som redan finns i Snowflake. Det kan vara särskilt relevant för verksamhetsanalys, kontrolluppföljning, prognoser och interna beslutsunderlag.

### När det kräver särskild analys

Det är mindre lämpligt som generell AI-plattform för alla typer av AI-användning. Arkitekten bör bedöma om användningsfallet faktiskt hör hemma i dataplattformen eller om det bör ligga i ett annat applikations- eller AI-lager.

### Typiska arkitekturfrågor

- Är den aktuella informationen redan förvaltad i Snowflake?
- Är användningsfallet analytiskt eller operativt?
- Hur styrs semantiska modeller och metadata?
- Hur granskas svar som bygger på naturligt språk mot data?
- Hur loggas frågor och svar för revision och felsökning?

## OpenAI API, ChatGPT Enterprise och ChatGPT Business

### Vad plattformarna tillför

OpenAI:s kommersiella erbjudanden kan vara relevanta både som direkt modell-API och som färdiga arbetsmiljöer för generativ AI. API-plattformen används för att bygga egna AI-applikationer, medan ChatGPT Enterprise och Business är mer användarnära miljöer för kunskapsarbete och interna arbetsflöden.

I målarkitekturen kan de bidra med:

- åtkomst till starka generativa modeller,
- snabb prototypframtagning,
- API-baserade AI-funktioner i egna applikationer,
- användarnära arbetsyta för kontrollerad generativ AI,
- möjligheter till integrations- och administrationskontroller beroende på avtal och tjänst.

### När det är lämpligt

Direkt modell-API är lämpligt när myndigheten vill bygga egna applikationer och kan hantera integration, loggning, säkerhet, dataskydd och livscykel själv. En färdig enterprise-chatmiljö kan vara lämplig för avgränsade produktivitets- och kunskapsfall, förutsatt att dataskydds- och avtalsvillkor är tydligt godkända.

### När det kräver särskild analys

För offentlig sektor krävs särskild granskning av personuppgifter, sekretess, datalagring, supportåtkomst, modellträning, retention, geografisk behandling och underleverantörer. Det är också viktigt att skilja mellan konsumenttjänster och enterprise-/API-tjänster; de har olika villkor och kontrollnivåer.

### Typiska arkitekturfrågor

- Vilken tjänst används: konsument, business, enterprise eller API?
- Vilka data får skickas till tjänsten?
- Hur hanteras retention och loggar?
- Vilka avtal och personuppgiftsbiträdesvillkor gäller?
- Kan tjänsten användas via en central AI-gateway?
- Finns alternativ för känsligare användningsfall?

## Anthropic Claude

### Vad plattformen tillför

Anthropic Claude är en kommersiell modell- och assistentplattform som ofta övervägs för språkförståelse, analys, sammanfattning, kodstöd, längre kontexter och agentliknande arbetsflöden. Den kan användas direkt via leverantörens egna erbjudanden eller indirekt via plattformar som gör Claude-modeller tillgängliga.

I målarkitekturen är Claude främst relevant som modell- och assistentalternativ, inte som fullständig myndighetsplattform. Den kan ge hög kvalitet i språkintensiva användningsfall men behöver placeras bakom samma kontroller som andra externa modellleverantörer.

### När det är lämpligt

Claude bör övervägas när användningsfallet kräver stark språkförståelse, analys av längre dokument, sammanfattning, resonemang eller kodstöd och när myndigheten har ett godkänt avtals- och driftspår för leverantören eller för den plattform som tillhandahåller modellen.

### När det kräver särskild analys

Som för andra externa modellleverantörer behöver dataskydd, retention, geografisk behandling, avtalsvillkor, supportåtkomst, loggning och modelluppdateringar granskas. Om Claude används via en annan plattform, till exempel en hyperscaler, behöver både modellleverantörens och plattformsleverantörens villkor förstås.

### Typiska arkitekturfrågor

- Används Claude direkt eller via en annan plattform?
- Vilka data skickas och vilken retention gäller?
- Hur påverkas myndigheten av modelluppdateringar?
- Hur dokumenteras modellval i arkitekturbeslut?
- Hur jämförs Claude med andra modeller för samma användningsfall?

## Mistral AI

### Vad plattformen tillför

Mistral AI är särskilt intressant i europeisk kontext eftersom leverantören erbjuder både kommersiella modeller, öppna modellalternativ och olika distributionsformer. Mistral kan vara relevant när myndigheten vill jämföra europeiska modellalternativ med amerikanska hyperscaler- eller modellleverantörer.

I målarkitekturen kan Mistral vara aktuellt som:

- modellleverantör via API,
- leverantör av öppna eller öppenviktsmodeller för egen drift,
- komponent i ett europeiskt eller suveränitetsorienterat AI-spår,
- alternativ för språkmodeller, kodmodeller, agentlösningar och multimodala användningsfall beroende på tjänst.

### När det är lämpligt

Mistral bör övervägas när europeisk leverantörsstrategi, öppenhet, portabilitet eller egen drift är viktiga jämförelsekriterier. Det kan också vara relevant när myndigheten vill testa modeller som kan användas både via kommersiell tjänst och i mer kontrollerade driftformer.

### När det kräver särskild analys

Begrepp som europeisk, öppen, suverän eller självhostad får inte ersätta konkret juridisk och teknisk prövning. Myndigheten behöver fortfarande bedöma licenser, driftplats, support, säkerhetskontroller, modellkvalitet, språkstöd och långsiktig förvaltning.

### Typiska arkitekturfrågor

- Ska modellen användas via API eller egen drift?
- Vilken licens gäller för aktuell modell?
- Vilka svenska och myndighetsspecifika språkbehov finns?
- Hur jämförs modellen mot andra alternativ i kvalitet, kostnad och risk?
- Vilka krav finns på support, uppdateringar och säkerhetsfixar?

## Cohere

### Vad plattformen tillför

Cohere är relevant främst som kommersiell modell- och retrieval-leverantör med särskild tyngd inom enterprise search, embeddings och reranking. Reranking är ofta en viktig komponent i RAG-lösningar eftersom den hjälper systemet att prioritera de mest relevanta dokumentpassagerna innan de skickas till språkmodellen.

I målarkitekturen kan Cohere tillföra:

- embeddings för semantisk sökning,
- reranking för bättre RAG-kvalitet,
- språkmodeller för enterprise-användning,
- komponenter som kan kombineras med andra sök- och datalager.

### När det är lämpligt

Cohere bör övervägas när myndigheten har RAG-användningsfall där retrieval-kvalitet är avgörande och där vanliga vektorsökresultat inte ger tillräcklig precision. Det kan vara särskilt relevant i dokumenttunga miljöer där många liknande dokument gör det svårt att hitta rätt underlag.

### När det kräver särskild analys

Som extern modell- eller API-leverantör kräver Cohere samma prövning som andra kommersiella AI-tjänster. Särskild uppmärksamhet bör läggas på vilka dokumentpassager som skickas till tjänsten vid reranking och hur detta förhåller sig till informationsklassning och sekretess.

### Typiska arkitekturfrågor

- Vilka textpassager skickas till reranking?
- Behöver reranking ske i egen miljö?
- Hur mäts förbättrad sökkvalitet?
- Hur påverkas kostnad och latens?
- Kan komponenten bytas ut om kravbilden förändras?

## Azure AI Search och kommersiella söktjänster

### Vad tjänsterna tillför

Azure AI Search är ett exempel på kommersiell sök- och retrieval-tjänst som kan användas för hybrid sökning, vektorsökning, semantisk sökning och RAG-mönster. Motsvarande kommersiella sökfunktioner finns även i andra plattformar och dataekosystem.

I målarkitekturen är sök- och retrieval-lagret centralt eftersom det avgör vilka källor en generativ AI-lösning faktiskt använder. En stark språkmodell kompenserar inte för dålig retrieval.

### När det är lämpligt

Kommersiella söktjänster är lämpliga när myndigheten vill bygga RAG över dokument, styrande material, handböcker, FAQ, ärendeunderlag eller andra textkällor och behöver enterprise-funktioner för skalning, indexering, hybrid sökning och integration.

### När det kräver särskild analys

Den största risken är ofta behörighetsmodellen. Om indexet inte respekterar källsystemens åtkomstregler kan RAG-lösningen exponera information på fel sätt. Myndigheten behöver också hantera dokumentversioner, metadata, gallring, källhänvisningar och kvalitetssäkring.

### Typiska arkitekturfrågor

- Hur mappas källsystemens behörigheter till sökindexet?
- Vilka metadata behövs för spårbarhet?
- Hur hanteras borttagna eller ändrade dokument?
- Vilken kombination av keyword, vector och semantic search ska användas?
- Hur mäts precision, recall och svarskvalitet?
- Hur undviks att gamla styrdokument används som aktuell sanning?

## Pinecone och andra kommersiella vektordatabaser

### Vad de tillför

Pinecone är ett exempel på en fullt hanterad vektordatabas för AI-applikationer i produktion. Kommersiella vektordatabaser kan ge snabb väg till skalbar semantisk sökning, särskilt när organisationen inte vill bygga och drifta vektorindex själv.

I målarkitekturen kan en vektordatabas bidra med:

- lagring och sökning av embeddings,
- låg latens för similarity search,
- skalning för stora dokumentmängder,
- separation mellan AI-applikationslager och källdatalager.

### När det är lämpligt

Det är lämpligt när vektorsökning är en central och återkommande förmåga och när myndigheten behöver en specialiserad, hanterad tjänst med tydliga prestanda- och skalningsegenskaper.

### När det kräver särskild analys

En vektordatabas innehåller inte nödvändigtvis ursprungsdokumenten, men embeddings och metadata kan ändå vara känsliga. Myndigheten behöver bedöma om embeddings kan läcka information, hur metadata skyddas, hur åtkomst styrs och hur radering fungerar.

### Typiska arkitekturfrågor

- Är embeddings och metadata informationsklassade?
- Ska vektordatabasen vara fristående eller integrerad i befintlig dataplattform?
- Hur hanteras tenant-separation, behörigheter och radering?
- Vilket krav finns på hybrid sökning?
- Hur undviks inlåsning i ett specifikt indexformat eller API?

## Elasticsearch, MongoDB Atlas Vector Search och integrerade vektorfunktioner

### Vad de tillför

Många befintliga data- och sökplattformar har integrerat vektorsökning. Elasticsearch kan användas för hybrid sökning och vektorsökning i sökdrivna lösningar. MongoDB Atlas Vector Search kan vara relevant när dokumentdata redan finns i MongoDB. Databricks AI Search och Snowflake Cortex Search är andra exempel på integrerade sök- och vektorfunktioner nära befintliga data.

I målarkitekturen är detta viktigt eftersom det inte alltid är bäst att införa en separat vektordatabas. Ibland är det bättre att använda vektorfunktioner där data, governance och förvaltning redan finns.

### När det är lämpligt

Integrerade vektorfunktioner är lämpliga när myndigheten redan har en etablerad plattform, när datan naturligt hör hemma där och när sökfunktionen inte kräver specialiserad separat vektordatabas.

### När det kräver särskild analys

Arkitekten behöver säkerställa att den integrerade lösningen klarar krav på prestanda, skala, hybrid sökning, filtrering, behörigheter, indexuppdatering, observability och återställning. Att en plattform har vektorsökning betyder inte att den passar alla RAG-behov.

### Typiska arkitekturfrågor

- Är vektorsökning en kärnförmåga eller stödfunktion?
- Var finns datan redan i dag?
- Vilken plattform har bäst governance för just denna datamängd?
- Behövs avancerad filtrering och behörighetsstyrning vid sökning?
- Hur mäts kvalitet jämfört med specialiserad vektordatabas?

## IBM watsonx och watsonx.governance

### Vad plattformen tillför

IBM watsonx är ett kommersiellt AI- och dataplattformserbjudande där watsonx.governance är särskilt relevant för styrning, dokumentation, övervakning och hantering av AI-risker. För myndigheter som behöver formalisera modellansvar, dokumentation och riskkontroll kan governance-lagret vara intressant.

I målarkitekturen kan watsonx.governance eller liknande verktyg bidra med:

- registrering av AI-användningsfall,
- dokumentation av modeller och risker,
- övervakning av modell- och AI-tillgångar,
- stöd för transparens och ansvarsfördelning,
- koppling mellan teknisk modellhantering och organisatorisk governance.

### När det är lämpligt

Det är lämpligt när myndigheten behöver ett mer strukturerat verktygsstöd för AI-styrning än vad den befintliga arkitektur- eller GRC-plattformen ger. Det kan vara relevant för högre risknivåer, många modeller, många team eller krav på central uppföljning.

### När det kräver särskild analys

Ett governance-verktyg ersätter inte styrning. Om roller, beslut, riskklassning och ansvar är oklara kommer verktyget bara dokumentera oklarheten. Arkitekten bör därför koppla sådana verktyg till faktiska processer, beslutspunkter och ansvariga roller.

### Typiska arkitekturfrågor

- Vilka AI-tillgångar ska registreras?
- Hur kopplas verktyget till AI-portföljen?
- Hur integreras det med modellregister, ärendehantering, riskhantering och arkitekturbeslut?
- Vilka krav från AI Act, GDPR och intern styrning ska stödjas?
- Vem äger uppdatering och kvalitet i registren?

## ServiceNow AI Agents och Now Assist

### Vad plattformen tillför

ServiceNow är relevant där myndigheten redan använder plattformen för ITSM, ärendehantering, HR, kundtjänst, arbetsflöden eller intern service. AI-funktioner och agenter i ServiceNow kan ge automation och assistans i befintliga processer.

I målarkitekturen är detta inte en generell AI-plattform utan ett verksamhetsnära AI-lager inuti en arbetsflödesplattform.

### När det är lämpligt

Det är lämpligt när användningsfallet är tätt kopplat till processer som redan finns i ServiceNow, till exempel intern support, ärendeklassificering, kunskapsartiklar, uppgiftsrouting eller sammanfattning av ärenden.

### När det kräver särskild analys

Agentfunktioner i arbetsflödesplattformar kräver särskild kontroll över behörigheter, verktygsanrop, eskalering, audit trails och mänsklig kontroll. Ju mer agenten får göra, desto mer liknar den en aktör i processen snarare än ett passivt stöd.

### Typiska arkitekturfrågor

- Vilka processer får AI-agenten påverka?
- Vilka verktyg och system får agenten anropa?
- Vilka beslut kräver mänsklig bekräftelse?
- Hur loggas agentens steg?
- Hur förhindras prompt injection via ärendetext, e-post eller kunskapsartiklar?

## Salesforce Agentforce och andra CRM-/verksamhetsplattformar

### Vad plattformarna tillför

Salesforce Agentforce är ett exempel på AI-agenter inuti en större verksamhetsplattform. För myndigheter som använder CRM-, kontaktcenter- eller ärendeplattformar kan liknande agentfunktioner vara relevanta för kundmöten, ärendeberedning, intern handläggning och serviceflöden.

I målarkitekturen ska sådana plattformar behandlas som AI i verksamhetssystem, inte som fristående experiment.

### När det är lämpligt

Det är lämpligt när användningsfallet ligger nära en befintlig process i plattformen och där datamodell, behörighet, arbetsflöden och uppföljning redan är etablerade. Det kan ge snabb nytta eftersom AI-funktionen arbetar i samma kontext som användarna.

### När det kräver särskild analys

Risken är att AI-agenten får för stort handlingsutrymme i en process som har rättsliga eller servicekritiska konsekvenser. Myndigheten måste analysera om agenten bara assisterar, föreslår, bereder eller faktiskt initierar åtgärder.

### Typiska arkitekturfrågor

- Vilken process påverkas?
- Vilka data använder agenten?
- Är agenten rådgivande eller handlande?
- Hur syns agentens bidrag i ärendehistoriken?
- Hur kan beslut spåras och förklaras i efterhand?

## Europeiska och suveränitetsorienterade kommersiella alternativ

### Vad kategorin tillför

I offentlig sektor uppstår ofta behov av europeiska, nationella eller suveränitetsorienterade alternativ. Det kan gälla molnplattform, modellleverantör, driftpartner, datacenter, supportorganisation eller avtalad kontroll över data och åtkomst.

Det viktiga är att suveränitet inte är en etikett utan en uppsättning konkreta egenskaper:

- var data behandlas,
- vilka rättsordningar som kan påverka åtkomst,
- vem som har administrativ kontroll,
- hur support och drift bemannas,
- vilka underleverantörer som används,
- hur exit och portabilitet fungerar,
- vilka tekniska kontroller myndigheten själv kan utöva.

### När det är lämpligt

Sådana alternativ bör övervägas när informationsklassning, sekretess, samhällskritisk verksamhet, politisk styrning eller strategisk försörjningsförmåga gör att vanliga publika molnspår inte är tillräckliga.

### När det kräver särskild analys

Ett europeiskt eller suveränt alternativ kan ge bättre kontroll i vissa avseenden men sämre modellutbud, högre kostnad, lägre mognad eller mer begränsad skalbarhet. Arkitekten måste därför väga kontroll mot funktion, tempo, kompetens och långsiktig förvaltning.

### Typiska arkitekturfrågor

- Vilken konkret risk reduceras av detta alternativ?
- Vilka tekniska och juridiska kontroller är verifierbara?
- Vilket modellutbud finns och hur uppdateras det?
- Finns tillräcklig support och kapacitet?
- Är lösningen portabel eller skapar den ny inlåsning?

## Kommersiella guardrails, content safety och AI-säkerhetslager

### Vad de tillför

Kommersiella guardrails- och content safety-tjänster kan bidra med filtrering, policykontroll, klassificering, PII-detektion, blockering av vissa svarstyper, kontroll av promptar och övervakning av AI-applikationer. Exempel finns hos hyperscalers och specialiserade AI-säkerhetsleverantörer.

I målarkitekturen bör detta ses som ett kontrollager runt AI-applikationen, inte som en garanti för säkerhet.

### När det är lämpligt

Det är lämpligt när myndigheten bygger generativa AI-tjänster som ska användas av många användare, när svar kan påverka verksamhetsprocesser eller när det finns risk för otillåten dataexponering, skadligt innehåll, hallucinationer eller prompt injection.

### När det kräver särskild analys

Guardrails kan ge falska positiva och falska negativa. De kan också vara svåra att anpassa till svenska myndighetsbegrepp, juridiska formuleringar och verksamhetsspecifik kontext. Myndigheten behöver därför testa dem mot egna scenarier.

### Typiska arkitekturfrågor

- Vilka risker ska guardrails faktiskt reducera?
- Sker kontroll före modellen, efter modellen eller båda?
- Hur loggas blockerade och tillåtna interaktioner?
- Hur hanteras svenska, engelska och blandade texter?
- Hur testas kontrollagret mot prompt injection och dataläckage?
- Vem får ändra policyregler?

## Minsta beslutsunderlag före val av kommersiell plattform

Innan myndigheten väljer en kommersiell AI-plattform bör följande finnas dokumenterat:

- användningsfall och målgrupp,
- informationsklassning,
- rättslig grund och dataskyddsbedömning där det behövs,
- krav på region, datalagring och supportåtkomst,
- krav på identitet och åtkomst,
- krav på loggning, spårbarhet och revision,
- krav på modellval och modellversioner,
- krav på RAG-källor och behörighetsmodell,
- krav på guardrails och incidenthantering,
- kostnadsmodell och kapacitetsantaganden,
- exitstrategi och portabilitet,
- ansvarig produktägare och förvaltningsmodell.

## Vanliga misstag

- Att jämföra modellkataloger i stället för arkitekturförmågor.
- Att införa en produktivitetsassistent utan att först städa behörigheter.
- Att anta att “enterprise” automatiskt betyder att tjänsten är godkänd för sekretessbelagd information.
- Att använda RAG utan permissions-aware indexering.
- Att placera guardrails efteråt som en kosmetisk säkerhetsåtgärd.
- Att välja en vektordatabas utan att förstå metadata, radering och åtkomstkontroll.
- Att köpa AI-governanceverktyg innan governanceprocessen är definierad.
- Att låta varje avdelning välja egen AI-tjänst utan gemensam AI-gateway och policy.
- Att blanda låg- och högriskanvändning i samma tekniska spår.
- Att sakna exitstrategi för modeller, data, index och promptflöden.

## Källor för framtida verifiering

Denna översikt bör uppdateras regelbundet mot leverantörernas officiella dokumentation. Vid senaste uppdateringen användes bland annat följande källtyper:

- Microsoft Learn: Azure AI Foundry, Azure AI Search och Microsoft 365 Copilot.
- AWS Documentation: Amazon Bedrock, Knowledge Bases, Agents och Guardrails.
- Google Cloud Documentation: Vertex AI, Model Garden, Agent Builder och Gemini Enterprise.
- NVIDIA Documentation: NVIDIA AI Enterprise och NIM.
- Red Hat Documentation: Red Hat OpenShift AI.
- Databricks Documentation: Mosaic AI, Model Serving och AI Search.
- Snowflake Documentation: Cortex AI, Cortex Analyst och Cortex Search.
- OpenAI: Enterprise privacy och business data controls.
- Mistral AI Documentation: modeller och distributionsalternativ.
- Cohere Documentation: embeddings, reranking och enterprise retrieval.
- MongoDB Documentation: Atlas Vector Search.
- IBM Documentation: watsonx.governance.
- Leverantörsdokumentation för ServiceNow och Salesforce där AI-agenter är relevanta.
