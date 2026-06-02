# Kapitel 14: Plattformar, produkter och ramverk att överväga

## Varför detta kapitel finns

När driftmodellen är formulerad kommer nästa fråga nästan omedelbart: vilka plattformar, produkter och ramverk bör myndigheten överväga?

Det är en rimlig fråga, men den är också riskabel. Om den ställs för tidigt förvandlas målarkitekturen lätt till en produktjämförelse. Då börjar diskussionen handla om vilken leverantör som har flest modeller, bäst demo, mest imponerande agentfunktioner eller mest attraktiv licensmodell. För en större statlig myndighet är det fel startpunkt.

En AI-plattform ska inte väljas bara för att den kan generera text, skapa embeddings, hantera agenter eller kopplas till en vektordatabas. Den ska passa myndighetens användningsfall, informationsklassning, rättsliga ramar, säkerhetskrav, integrationsmiljö, driftmodell, kompetens och långsiktiga förvaltningsförmåga.

Detta kapitel behandlar därför produkt- och ramverksval som en arkitekturfråga, inte som en inköpslista. Målet är att ge en strukturerad karta över vilka typer av plattformar och komponenter som är relevanta, när de bör övervägas och vilka frågor arkitekten bör ställa innan ett vägval görs.

Kapitlet bygger vidare på kapitel 10 om teknisk referensarkitektur, kapitel 11 om generativ AI och RAG, kapitel 12 om MLOps och LLMOps samt kapitel 13 om moln, on-premises och hybrid. Där etablerades att myndigheten bör definiera arkitekturspår innan den väljer produkter. Här översätts den principen till en mer konkret marknads- och teknikbild.

Kapitlet är avsiktligt skrivet som ett vägvals- och arkitekturkapitel, inte som en produktkatalog. Konkreta exempel på kommersiella plattformar, molntjänster och leverantörer hålls därför i **Appendix A: Kommersiella AI-plattformar och molntjänster**. Konkreta exempel på öppna modeller, open source-ramverk och egen drift hålls i **Appendix B: Open source-modeller, ramverk och egen drift**. Beslutsmatriser och urvalsmallar hålls i **Appendix C: Beslutsmatriser och urvalsmallar**. Det gör produkt- och ramverksöversikterna samt beslutsstödet enklare att uppdatera utan att huvudkapitlets arkitekturresonemang behöver skrivas om.


## Arkitekturproblemet

Tullverket Aurora har efter de tidigare kapitlens arbete en tydligare målbild. Myndigheten vill kunna stödja flera typer av AI-användning:

- lågklassad personlig produktivitet,
- intern kunskapssökning i styrdokument och handböcker,
- sammanfattning av ärendehandlingar,
- verksamhetsnära analysstöd,
- kontrollerade prediktiva modeller,
- framtida agentliknande arbetsflöden med mänsklig kontroll.

Leverantörslandskapet är däremot splittrat. Flera avdelningar har redan testat olika verktyg. Vissa vill använda färdiga AI-assistenter i kontorsmiljön. Andra vill använda en hyperscalerbaserad AI-plattform. Data- och analysenheten föredrar open source-modeller och egen modellservering. Säkerhetsfunktionen vill begränsa extern exponering. Juridikfunktionen vill se tydligare avtalsvillkor, datalokalisering och underbiträdeskedjor. Arkitekturgruppen försöker samtidigt undvika att myndigheten bygger ett lapptäcke av lösningar som inte kan styras gemensamt.

Auroras problem är därför inte att det saknas produkter. Problemet är att det finns för många möjliga produkter och för få gemensamma beslutsregler.

## Centrala begrepp

### Plattform

I den här boken betyder plattform en gemensam teknisk förmåga som flera lösningar kan använda. En AI-plattform kan till exempel erbjuda modellåtkomst, utvecklingsmiljö, prompt- och agenthantering, modellutvärdering, deployment, observability, säkerhetskontroller och integrationer.

En plattform är mer än ett verktyg. Den innebär också driftansvar, livscykel, behörighetsmodell, kostnadsmodell, support, kompetenskrav och styrning.

### Produkt

En produkt är en mer avgränsad kommersiell eller intern lösning. Det kan vara en AI-assistent, en RAG-tjänst, ett modell-API, en vektordatabas, ett MLOps-verktyg eller en säkerhetskomponent.

I målarkitekturen bör produkter placeras i förmågor och byggblock. Annars blir produktlistan svår att styra.

### Ramverk

Ett ramverk är ett bibliotek, en utvecklingsmodell eller en teknisk struktur som hjälper team att bygga AI-lösningar. Exempel är ramverk för RAG, agentorkestrering, promptflöden, utvärdering, testning eller modellträning.

Ramverk kan vara kraftfulla men skapar ofta egen komplexitet. De måste därför bedömas lika noggrant som kommersiella produkter, särskilt när de blir kritiska delar av produktionslösningar.

### AI-stack

AI-stack används här som samlingsbegrepp för hela tekniklagret: data, modellåtkomst, orkestrering, applikationslager, säkerhetskontroller, observability, livscykelhantering och drift.

En myndighet behöver sällan en enda AI-stack för allt. Den behöver däremot tydliga tillåtna stackar för olika risk- och användningsfallsklasser.

## Rekommenderat angreppssätt

Ett moget plattformsval börjar inte med leverantörsnamn. Det börjar med en karta över vilka förmågor som ska stödjas.

### Steg 1: Dela upp marknaden i kategorier

Arkitekturgruppen bör först skapa en kategorikarta. För Tullverket Aurora blir följande kategorier relevanta:

- färdiga AI-assistenter,
- generativa AI-plattformar hos molnleverantörer,
- modell-API:er och modellhubbar,
- open source-modeller och egen modellservering,
- RAG-plattformar och dokumentintelligens,
- vektordatabaser och sökinfrastruktur,
- orkestrerings- och agentramverk,
- MLOps- och LLMOps-verktyg,
- säkerhets- och guardrail-komponenter,
- observability- och utvärderingsverktyg,
- dataplattformar och integrationsplattformar,
- utvecklarplattformar och interna plattformstjänster.

Denna uppdelning hindrar att olika typer av lösningar jämförs med varandra på fel nivå. En AI-assistent är inte ett alternativ till en modellplattform. En vektordatabas är inte ett alternativ till en RAG-arkitektur. Ett agentramverk är inte ett alternativ till governance.

### Steg 2: Koppla varje kategori till byggblock i referensarkitekturen

Varje produktkategori ska kopplas till ett byggblock i målarkitekturen. Om en produkt inte passar in i något byggblock finns tre möjliga förklaringar:

- produkten behövs inte,
- målarkitekturen saknar ett byggblock,
- produkten försöker täcka flera byggblock och behöver brytas ned arkitektoniskt.

Tullverket Aurora placerar till exempel färdiga AI-assistenter i byggblocket användarnära AI-stöd, medan RAG-komponenter placeras i byggblocket kunskaps- och retrieval-lager. Vektordatabaser placeras inte som fristående strategi utan som infrastrukturkomponent under retrieval. Modellplattformar placeras under modellåtkomst, deployment och livscykel.

### Steg 3: Matcha kategorier mot arkitekturspår

Kapitel 13 beskrev olika driftspår. Samma logik bör användas för produktkategorier.

För lågklassad produktivitet kan färdiga SaaS-assistenter vara rimliga, om avtal, dataskydd, loggning och användningspolicy är tydliga. För kontrollerad intern RAG kan en moln- eller hybridplattform vara rimlig, beroende på informationsklassning och integrationskrav. För känsliga beslutsnära flöden kan egen modellservering, privat drift eller mer restriktiva plattformar behöva övervägas.

Det viktiga är att varje produktval kopplas till ett tillåtet arkitekturspår. Annars riskerar en till synes liten pilot att etablera ett oönskat driftmönster.

### Steg 4: Bedöm produkten utifrån kontrollpunkter

Varje relevant produkt eller ramverk bör bedömas mot samma kontrollpunkter:

- vilka informationsklasser kan lösningen hantera,
- var behandlas data,
- vilka data används för träning, förbättring eller telemetri,
- vilka avtalsvillkor gäller för promptar, filer, loggar och modellutdata,
- hur hanteras identitet, behörighet och åtkomstkontroll,
- vilka loggar och revisionsspår finns,
- kan lösningen integreras med myndighetens säkerhets- och övervakningsmiljö,
- hur fungerar livscykelhantering, versionering och avveckling,
- kan lösningen köras i önskad driftmodell,
- finns stöd för policy enforcement och guardrails,
- vilka beroenden och inlåsningseffekter uppstår,
- vilken kompetens krävs för att förvalta lösningen.

Kontrollpunkterna bör finnas som en gemensam mall i arkitekturprocessen, inte uppfinnas på nytt för varje initiativ.

Produkt- och ramverksval bör beskrivas som kategorier och krav snarare än som en fast leverantörslista. Marknaden för AI-plattformar, RAG-komponenter, agentramverk, MLOps, LLMOps och säkerhetslager förändras snabbt. Målarkitekturen bör därför uttrycka krav på funktioner, integration, styrbarhet, dataskydd, observability, exit och leverantörsoberoende.

## Produkt- och plattformskategorier

### Färdiga AI-assistenter

Färdiga AI-assistenter är ofta den snabbaste vägen till verksamhetsnytta. De kan ge stöd för sammanfattning, textbearbetning, mötesanteckningar, sökning, kodassistans och enklare analys. De är särskilt relevanta när nyttan ligger nära användarens arbetsyta och informationen är lågklassad eller redan finns i en kontrollerad produktivitetsmiljö.

För en myndighet är huvudfrågan inte om assistenten är imponerande. Huvudfrågan är om den kan användas på ett kontrollerat sätt.

Arkitekten bör särskilt granska:

- vilka datakällor assistenten får åtkomst till,
- om användaren förstår vad som får och inte får matas in,
- hur behörigheter från källsystem respekteras,
- om utdata kan bli allmän handling eller behöva diarieföras,
- hur loggar, prompts och filer behandlas,
- om leverantören använder kunddata för modellförbättring,
- om det finns administrativ styrning, eDiscovery, retention och revision.

Färdiga assistenter passar sämre när användningsfallet kräver djup verksamhetslogik, strikt styrd retrieval, särskild modellutvärdering, specialiserade integrationsmönster eller känsliga informationsklasser som inte får exponeras i den aktuella tjänsten.

För Tullverket Aurora blir färdiga assistenter ett kontrollerat första spår för lågklassade administrativa uppgifter, men inte den primära lösningen för riskanalys eller känsligt handläggarstöd.

### Hyperscalerbaserade AI-plattformar

De stora molnleverantörernas AI-plattformar erbjuder ofta ett brett paket: modellkataloger, API:er, agenttjänster, kunskapsbaser, promptverktyg, utvecklarstöd, säkerhetsintegrationer, skalbar drift och koppling till övriga molntjänster. Sådana plattformar kan vara attraktiva för myndigheter som redan har en etablerad molnstrategi och behöver snabb tillgång till modeller och utvecklingsmiljöer.

Exempel på denna kategori är plattformar som Microsoft Foundry, Google Vertex AI och Amazon Bedrock. De utvecklas snabbt och bör inte beskrivas i målarkitekturen som statiska produkter. I stället bör målarkitekturen ange vilka förmågor som efterfrågas: modellkatalog, styrd modellåtkomst, agenthantering, RAG-stöd, promptversionering, utvärdering, säkerhetsintegration, kostnadsstyrning och spårbarhet.

Styrkan med hyperscalerplattformar är bredd och tempo. Svagheten är att de ofta skapar starka beroenden till leverantörens identitet, nätverk, loggning, policy, dataekosystem och utvecklingsmodell.

Arkitekten bör därför bedöma:

- om plattformen passar myndighetens molnpolicy,
- om datalagring och dataflöden kan styras till godkända regioner,
- om modellåtkomst och modellversioner kan kontrolleras,
- om loggar och telemetri kan integreras med myndighetens övervakning,
- om kostnader kan förutses och följas upp,
- om lösningen kan kompletteras med europeiska, öppna eller interna alternativ,
- om exitstrategi finns för modeller, prompts, embeddings, index och orkestreringslogik.

För Tullverket Aurora är en hyperscalerplattform ett möjligt spår för kontrollerade piloter och vissa produktionslösningar, men bara när juridik, informationsklassning, avtal och säkerhetsarkitektur tillåter det.

### Europeiska och suveräna molnalternativ

För statliga myndigheter kan europeiska driftalternativ, nationellt reglerade molntjänster och så kallade sovereign cloud-erbjudanden vara relevanta. De kan bidra till bättre kontroll över datalokalisering, driftjurisdiktion, åtkomst från leverantörspersonal och vissa avtalsrisker.

Samtidigt är det viktigt att inte behandla ordet suverän som en garanti. Ett sovereign cloud-erbjudande måste analyseras konkret:

- vem äger och driver infrastrukturen,
- i vilken jurisdiktion finns leverantören och underleverantörerna,
- vem kan tekniskt få åtkomst till data,
- hur hanteras support och incidenter,
- vilka AI-modeller och tjänster är faktiskt tillgängliga i miljön,
- vilka begränsningar finns jämfört med publikt moln,
- hur ser revisions- och insynsmöjligheter ut.

I vissa fall kan ett europeiskt eller suveränt alternativ vara rätt för ett helt AI-spår. I andra fall kan det vara rätt för delar av stacken, till exempel data, index, loggning eller modellservering, medan andra delar använder externa modell-API:er med starka kontroller.

### Open source-modeller och egen modellservering

Open source-modeller och egen modellservering kan ge större kontroll över dataflöden, modellåtkomst, deployment, avveckling och anpassning. De kan också minska vissa leverantörsberoenden och göra det möjligt att köra modeller i privat moln eller on-premises.

Men egen modellservering är inte gratis kontroll. Den kräver kapacitet, kompetens, säkerhet, patchning, GPU- eller acceleratorstrategi, övervakning, skalning, modellutvärdering och förvaltningsprocesser. Den innebär också ansvar för att upptäcka brister, hantera modellversioner och skydda infrastrukturen.

Open source-spåret passar särskilt när myndigheten behöver:

- köra modeller i kontrollerad intern miljö,
- undvika extern exponering av känsliga data,
- ha mer kontroll över modellversioner och deployment,
- experimentera med specialiserade modeller,
- minska beroendet till en enskild kommersiell modellleverantör,
- bygga kompetens inom AI-drift.

Spåret passar sämre om myndigheten saknar driftförmåga, saknar GPU-kapacitet, behöver mycket snabbt införande eller inte kan förvalta modell- och säkerhetslivscykeln.

För Tullverket Aurora blir egen modellservering ett möjligt spår för särskilt känsliga användningsfall, men inte standardvägen för all AI. Arkitekturgruppen beslutar därför att egen modellservering bara ska användas där kontrollbehovet motiverar den ökade komplexiteten.

### Modell-API:er och modellhubbar

Många AI-lösningar bygger på åtkomst till externa eller interna modell-API:er. Det kan vara kommersiella API:er, molnleverantörers modellkataloger eller interna modellhubbar.

En modellhub kan ge flexibilitet, men kräver styrning. Annars kan team välja modeller utan gemensam riskbedömning, kostnadsuppföljning eller utvärdering.

En myndighets målarkitektur bör därför definiera ett styrt modellåtkomstlager. Det kan innehålla:

- godkända modeller,
- modellversioner,
- tillåtna användningsfall,
- informationsklasser,
- kostnadsramar,
- loggning,
- spärrlistor,
- utvärderingsresultat,
- kontaktpunkt för modellansvar.

Detta bör inte ligga dolt i varje applikation. Det bör vara en gemensam förmåga, antingen som del av AI-gatewayen, plattformen eller modellregistret.

### RAG-plattformar och dokumentintelligens

RAG är ett centralt mönster för myndigheter eftersom mycket värde finns i dokument, regelverk, handböcker, beslutsunderlag och ärendeinformation. En RAG-plattform kan innehålla dokumentintag, textutvinning, chunking, metadatahantering, embeddings, indexering, retrieval, reranking, promptmallar, källhänvisningar och utvärdering.

För offentlig sektor är dokumentintelligens ofta minst lika viktig som själva språkmodellen. Om dokumenten tolkas fel, metadata saknas eller behörigheter inte följer med in i indexet kan hela lösningen bli opålitlig.

Arkitekten bör därför bedöma RAG-lösningar utifrån:

- stöd för svenska och flerspråkiga dokument,
- hantering av PDF, skannade dokument, tabeller och bilagor,
- metadata och informationsklassning,
- behörighetsfiltrering vid sökning,
- spårbarhet från svar till källa,
- uppdateringsfrekvens och indexlivscykel,
- hantering av gallring och avpublicering,
- utvärdering av retrieval-kvalitet,
- skydd mot prompt injection i källdokument.

För Tullverket Aurora är RAG-plattformen särskilt viktig för kunskapsstödet. Den måste kunna visa källor, respektera behörigheter och hantera att styrdokument ändras över tid.

### Vektordatabaser och sökinfrastruktur

Vektordatabaser används ofta som en central komponent i RAG-lösningar. Men de bör inte väljas isolerat. Ett bra RAG-resultat beror på hela kedjan: dokumenttolkning, chunking, embeddings, metadata, hybrid search, reranking, behörighetsfilter, promptdesign och utvärdering.

En vektordatabas bör därför bedömas tillsammans med sökinfrastrukturen. I vissa fall räcker en befintlig sökplattform med vektorstöd. I andra fall behövs en specialiserad vektordatabas. I ytterligare fall krävs hybridarkitektur där traditionell sökning, semantisk sökning och metadatafilter samverkar.

Viktiga frågor är:

- kan behörigheter tillämpas vid söktillfället,
- kan index segmenteras efter informationsklass,
- stöds hybrid search,
- kan embeddings bytas ut utan orimlig migreringskostnad,
- hur hanteras borttagning och uppdatering av dokument,
- kan driftmodellen matcha datakrav,
- finns tillräcklig observability över retrieval-kvalitet.

### Orkestrerings- och agentramverk

Ramverk för LLM-applikationer, RAG och agenter kan öka utvecklingstakten. De kan hjälpa team att koppla samman modeller, verktyg, dokument, minne, arbetsflöden och utvärdering. Exempel på etablerade ramverkskategorier är kedje- och agentramverk, datakopplingsramverk, RAG-ramverk och grafbaserad agentorkestrering.

Dessa ramverk bör användas med försiktighet i myndighetskritiska miljöer. De kan dölja komplexitet, skapa svårgranskade beroenden och göra det svårt att förstå exakt vilka steg som körs i ett AI-flöde.

För en myndighet är agentfunktioner särskilt känsliga. Ju mer en AI-lösning kan agera, anropa verktyg, skriva till system eller fatta delbeslut, desto större krav på mänsklig kontroll, behörighet, loggning, test och stoppmekanismer.

Arkitekten bör fråga:

- kan varje steg i flödet loggas och förklaras,
- kan verktygsanrop begränsas per roll och användningsfall,
- finns human-in-the-loop där det behövs,
- kan ramverket driftas och patchas långsiktigt,
- kan ramverket ersättas utan att verksamhetslogik går förlorad,
- är agentlogiken testbar,
- kan säkerhetsfunktionen granska vad som faktiskt händer.

För Tullverket Aurora blir rekommendationen att agentramverk först används i avgränsade interna stödflöden, inte i känsliga beslutsnära processer.

### MLOps- och LLMOps-verktyg

Kapitel 12 beskrev livscykelhantering. Produktval inom MLOps och LLMOps bör därför ses som stöd för de processer myndigheten redan definierat.

För prediktiva modeller kan klassiska MLOps-verktyg hantera träningspipelines, modellregister, feature stores, deployment, övervakning och drift. För generativa AI-lösningar behövs ofta kompletterande LLMOps-förmågor: promptversionering, utvärderingsdataset, svarskvalitet, hallucinationsmätning, RAG-utvärdering, kostnad per anrop, modelljämförelser och red-teamingresultat.

Ett vanligt misstag är att välja ett verktyg som fungerar bra för notebook-baserade experiment men inte för produktionssättning, revision och förvaltning. Ett annat misstag är att tro att LLMOps bara är traditionell DevOps med ett modell-API.

För Tullverket Aurora blir kravet att varje produktionssatt AI-lösning ska ha dokumenterad livscykel: godkänd modell, godkänt promptflöde, testresultat, versionshistorik, ägare, loggning, incidentväg och avvecklingsplan.

### Guardrails, säkerhetslager och policy enforcement

AI-säkerhet kan inte lösas med en enskild guardrail-produkt. Däremot kan säkerhetskomponenter vara viktiga delar i en större arkitektur.

Relevanta komponenter kan vara:

- input- och outputfiltrering,
- kontroll av känslig information,
- prompt injection-detektion,
- verktygsbegränsning,
- policybaserad routing,
- modellåtkomstkontroll,
- loggning och revisionsspår,
- säkerhetsklassad testning,
- red teaming-stöd,
- övervakning av missbruksmönster.

Arkitekten bör undvika att skapa en falsk trygghet. En guardrail minskar vissa risker men eliminerar dem inte. Särskilt i myndighetsmiljö måste tekniska kontroller kombineras med behörighet, utbildning, process, juridisk bedömning, informationsklassning och mänsklig kontroll.

### Observability och utvärdering

Observability för AI handlar inte bara om teknisk drift. Det handlar också om svarskvalitet, retrieval-träffar, hallucinationer, policyavvikelser, användarbeteende, kostnad, latency, modellfel och incidenter.

En myndighet bör kunna svara på frågor som:

- vilken modell användes,
- vilken promptmall användes,
- vilka källor hämtades,
- vilka filter tillämpades,
- vilket svar gavs,
- vem använde lösningen,
- vilka avvikelser uppstod,
- hur förändrades kvaliteten efter en modelluppdatering.

Utvärderingsverktyg bör därför ingå i målarkitekturen, särskilt för RAG och generativa AI-flöden. För Tullverket Aurora blir detta viktigt när kunskapsstödet används för regelverksfrågor. Myndigheten behöver veta om svaren bygger på rätt källor och om retrieval-kvaliteten försämras när dokumentmängden växer.

Internationella ramverk kan användas som stöd för struktur och kontrollfrågor. NIST AI Risk Management Framework kan stödja riskhantering, ISO/IEC 42001 kan stödja ledningssystem för AI, och OWASP Top 10 for LLM Applications kan stödja säkerhetsgranskning av generativa AI-lösningar. De ersätter inte svenska rättskällor, men kan ge praktiska kontrollpunkter vid kravställning, designgranskning och intern styrning.

## Exempel från Tullverket Aurora

Auroras arkitekturgrupp tar fram en plattformskarta i fyra nivåer.

### Nivå 1: Användarnära AI-stöd

Den första nivån omfattar färdiga AI-assistenter i kontors- och produktivitetsmiljöer. De tillåts bara för lågklassade arbetsuppgifter och styrs med policy, utbildning, tekniska begränsningar och avtalskontroll.

Exempel på tillåtna användningar är språkgranskning, sammanfattning av öppna interna texter och idéutkast. Exempel på otillåtna användningar är inmatning av sekretessbelagda ärendeuppgifter eller känsliga personuppgifter.

### Nivå 2: Gemensam AI-plattform för kontrollerade lösningar

Den andra nivån är en gemensam AI-plattform för styrda piloter och produktionssatta lösningar med måttlig risk. Plattformen erbjuder modellåtkomst, prompt- och flödeshantering, RAG-stöd, loggning, kostnadsuppföljning och integration med identitetstjänster.

Här placeras kunskapsstödet för interna styrdokument. Plattformen får använda godkända modell-API:er, men dokumentindex, metadata och behörighetsfilter kontrolleras av myndigheten.

### Nivå 3: Kontrollerad intern AI-zon

Den tredje nivån är en mer restriktiv miljö för känsligare användningsfall. Den kan bygga på privat moln, upphandlad reglerad drift eller on-premises-komponenter. Här kan egen modellservering eller särskilt kontrollerade modeller bli aktuella.

Denna nivå används inte för alla AI-lösningar, utan för de där informationsklassning och konsekvensbedömning motiverar högre kontroll.

### Nivå 4: Experiment- och utvärderingsmiljö

Den fjärde nivån är en sandlåda för kontrollerad utforskning. Den får inte hantera känslig information, men den ska vara tillräckligt realistisk för att team ska kunna testa modeller, ramverk, RAG-mönster och agentflöden.

Poängen är att experiment inte ska ske okontrollerat i varje team. Även sandlådan är en styrd del av AI-förmågan.

## Vägvalsfrågor

När en produkt eller ett ramverk föreslås bör arkitekten ställa följande frågor:

1. Vilket byggblock i målarkitekturen fyller lösningen?
2. Vilka användningsfall ska den stödja?
3. Vilka informationsklasser får den hantera?
4. Vilken driftmodell kräver eller möjliggör den?
5. Vilka data lämnar myndighetens kontrollzon?
6. Vilka modellversioner och leverantörer blir myndigheten beroende av?
7. Kan identitet, behörighet och loggning integreras med befintlig miljö?
8. Kan lösningen testas, övervakas och revideras?
9. Hur hanteras promptar, embeddings, index och modellutdata vid exit?
10. Vilken intern kompetens krävs för att använda och förvalta lösningen?
11. Vilka kostnader uppstår vid skala, inte bara vid pilot?
12. Vad händer om leverantören ändrar modell, pris, villkor eller regionstöd?

Dessa frågor bör dokumenteras i arkitekturbeslut, inte bara diskuteras i workshops.

## Vanliga fallgropar

### Att jämföra produkter på fel nivå

En färdig AI-assistent, en modellplattform, en vektordatabas och ett agentramverk löser olika problem. Om de jämförs som om de vore alternativ till varandra blir beslutsunderlaget missvisande.

### Att låta piloter skapa de facto-standard

Ett team kan snabbt skapa en fungerande pilot med ett visst ramverk eller en viss modell. Om piloten sedan skalas utan arkitekturbeslut blir den lokala lösningen en de facto-standard.

### Att underskatta drift- och förvaltningskostnaden

Open source, egen modellservering och avancerade ramverk kan ge kontroll men kräver långsiktig kompetens. Kostnaden ligger ofta inte i licensen utan i drift, säkerhet, utvärdering och livscykelhantering.

### Att tro att en guardrail-produkt löser AI-risk

Guardrails är viktiga men inte tillräckliga. De måste kombineras med informationsklassning, behörighet, loggning, processer, utbildning och mänsklig kontroll.

### Att binda verksamhetslogik till ett ramverk

Om prompts, retrieval-logik, agentflöden och policyregler byggs djupt in i ett ramverk kan det bli svårt att byta senare. Målarkitekturen bör därför skilja verksamhetsregler från teknisk orkestrering.

### Att inte planera för modellbyte

Modeller ändras snabbt. En myndighet bör kunna byta modell eller modellleverantör utan att skriva om hela lösningen. Det kräver abstraktion, testdata, utvärdering och tydliga gränssnitt.

## Checklista

Innan Tullverket Aurora godkänner en plattform, produkt eller ett ramverk för bredare användning bör följande vara besvarat:

- Produkten är placerad i ett namngivet byggblock i målarkitekturen.
- Tillåtna användningsfall och informationsklasser är definierade.
- Driftmodell och datalokalisering är bedömda.
- Avtalsvillkor för data, promptar, loggar och modellutdata är granskade.
- Identitet, behörighet och åtkomstkontroll är beskriven.
- Loggning, revision och incidenthantering är möjliga.
- Modellversioner och modellåtkomst kan styras.
- Kostnadsmodell vid skala är analyserad.
- Exitstrategi är dokumenterad.
- Förvaltningsansvar är utpekat.
- Säkerhetsfunktion, dataskydd och juridik har involverats vid behov.
- Arkitekturbeslut är dokumenterat.

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Målarkitekturen bör inte innehålla en lång lista över rekommenderade produkter som snabbt blir inaktuell. Den bör i stället beskriva:

- vilka produktkategorier som är tillåtna,
- vilka byggblock de får fylla,
- vilka arkitekturspår de får användas i,
- vilka kontrollpunkter som krävs,
- vilka produktval som är beslutade,
- vilka produktval som är öppna,
- vilka val som måste kunna ändras över tid.

För Tullverket Aurora dokumenteras detta som en plattformskarta, kompletterad med arkitekturbeslut för varje större vägval. Målarkitekturen anger till exempel att myndigheten ska ha ett styrt modellåtkomstlager, ett gemensamt RAG-mönster, en kontrollerad experimentmiljö och separata driftspår för låg, medel och hög risk.

Däremot låser den inte alla framtida modeller, ramverk och databaser. Det vore för statiskt. I stället definierar den spelreglerna för hur sådana val får göras.


## Snabb sammanfattning

Plattforms- och produktval för AI bör göras som arkitekturval, inte som isolerade teknikinköp. För en större statlig myndighet är det viktigare att förstå produktkategorier, byggblock, driftspår, kontrollpunkter och livscykel än att snabbt välja en enskild leverantör.

Färdiga AI-assistenter kan ge snabb nytta men kräver tydlig användningspolicy och datakontroll. Hyperscalerplattformar kan ge bredd och tempo men skapar beroenden som måste styras. Europeiska och suveräna alternativ kan vara relevanta men måste bedömas konkret. Open source och egen modellservering ger kontroll men kräver stark förvaltningsförmåga. RAG-plattformar, vektordatabaser, agentramverk, MLOps, LLMOps, guardrails och observability måste alla placeras i en sammanhängande målarkitektur.

Tullverket Aurora väljer därför inte en enda AI-produkt. Myndigheten etablerar en plattformskarta med flera tillåtna arkitekturspår och tydliga beslutsregler. När dessa regler ska omsättas i konkreta beslut används Appendix C som stöd för jämförelser, arkitekturbeslut och omprövningspunkter.

## Nästa steg

Nästa kapitel behandlar när man väljer vad. Där går boken från produktkategorier till konkreta arkitekturbeslut: köpa eller bygga, central eller federerad plattform, en modell eller flera, RAG eller fine-tuning, moln eller on-premises samt gemensam AI-gateway eller separata lösningar.
