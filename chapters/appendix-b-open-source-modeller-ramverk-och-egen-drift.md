# Appendix B: Open source-modeller, ramverk och egen drift

## Varför detta appendix finns

Kapitel 14 beskriver plattforms- och ramverksval som arkitekturfrågor. Appendix A beskriver kommersiella plattformar och molntjänster. Detta appendix kompletterar med öppna modeller, open source-ramverk och byggblock för egen eller mer kontrollerad drift.

Appendixet är avsiktligt placerat utanför huvudkapitlen. Produktnamn, modellfamiljer, licenser och ramverk förändras snabbt. En myndighet bör därför behandla denna del som en uppdateringsbar katalog, inte som en permanent rekommendationslista.

För en större statlig myndighet är open source inte automatiskt bättre, säkrare eller billigare än kommersiella alternativ. Det kan däremot ge större teknisk kontroll, bättre insyn, fler driftalternativ och lägre leverantörsinlåsning om myndigheten samtidigt har kompetens, infrastruktur, livscykelprocesser och säkerhetsstyrning för att ta ansvar för helheten.

## Hur appendixet ska användas

Appendixet ska inte läsas som en ranking. Det är ett arkitekturstöd. Varje område beskriver vad komponenttypen tillför, när den är lämplig, när den kräver särskild analys och vilka frågor en myndighet bör ställa innan alternativet förs in i målarkitekturen.

En praktisk tumregel är:

- Använd open source när myndigheten behöver kontroll, insyn, portabilitet, experimentförmåga eller egen drift.
- Använd inte open source bara för att undvika licenskostnad.
- Räkna alltid in drift, säkerhet, övervakning, patchning, kompetens, juridisk granskning, licensvillkor och långsiktig förvaltning.
- Skilj mellan öppen modell, öppen kod, öppen viktfil, fri användning och kommersiellt tillåten användning.
- Dokumentera varje val som ett arkitekturbeslut, inte som ett utvecklarpreferensval.

## Modellfamiljer med öppna vikter

### Llama-familjen

**Typ:** Modellfamilj med öppna modellvikter och särskilda licensvillkor.

**Vad den tillför:** Llama-modeller kan användas som bas för egen modellservering, prototyper, RAG-lösningar, interna assistenter och specialiserade tillämpningar där myndigheten vill kunna kontrollera driftmiljö, modellversion och åtkomstvägar. De är vanliga i open source-ekosystemet och stöds av många verktyg för inferens, kvantisering, orkestrering och utvärdering.

**När den är lämplig:** Llama-familjen bör övervägas när myndigheten vill bygga ett öppet modellspår för låg- till medelriskanvändning, särskilt där RAG och strikt datakontroll är viktigare än tillgång till den allra senaste kommersiella modellen. Den är också relevant när verksamheten vill kunna jämföra kommersiella modeller med egen driftad modell.

**När den kräver särskild analys:** Licensvillkor, modellversion, träningsdata, säkerhetsegenskaper och tillåten användning måste granskas. En myndighet bör inte anta att en modell med öppna vikter är fri att använda i alla sammanhang. För känsliga användningsfall krävs även test mot svenska myndighetstexter, domänspråk, hallucinationer, säkerhetsbeteende och robusthet mot prompt injection.

**Typiska arkitekturfrågor:**

- Får modellen användas kommersiellt och i myndighetens avsedda användningsfall?
- Vilken modellstorlek ryms i myndighetens driftmiljö?
- Ska modellen användas direkt, via RAG eller efter finjustering?
- Hur dokumenteras modellkort, riskbedömning, testresultat och version?
- Vem ansvarar för uppdatering när en ny modellversion släpps?

### Mistral-familjen

**Typ:** Modellfamilj från europeisk leverantör med både öppna och kommersiella varianter.

**Vad den tillför:** Mistral-modeller kan vara relevanta för myndigheter som vill utvärdera europeiska alternativ och samtidigt kunna välja mellan öppna vikter, API-baserad användning och kommersiella driftmodeller. De kan fylla rollen som generell språkmodell, kodmodell eller komponent i RAG-baserade lösningar.

**När den är lämplig:** Mistral bör övervägas när myndigheten vill ha ett europeiskt alternativ i modellportföljen, när man behöver jämföra språkstöd och när man vill kunna växla mellan egen drift och kommersiell användning beroende på riskklass.

**När den kräver särskild analys:** Precis som för andra modeller måste licensvillkor, driftplats, databehandling, modellversioner och supportmodell granskas. Om modellen används via API blir det en leverantörs- och dataskyddsfråga. Om den används med egen drift blir det en infrastruktur- och förvaltningsfråga.

**Typiska arkitekturfrågor:**

- Vilka varianter är öppna, kommersiella eller API-bundna?
- Hur väl fungerar modellen på svenska myndighetstexter?
- Kan modellen ingå i samma modellgateway som andra modeller?
- Finns det krav på europeisk drift, support eller avtal?
- Hur hanteras byte mellan modellvarianter?

### Gemma-familjen

**Typ:** Öppen modellfamilj från Google med särskilda användningsvillkor.

**Vad den tillför:** Gemma kan vara relevant för mindre eller mer kontrollerade användningsfall där myndigheten vill utvärdera öppna modeller som är nära kopplade till ett större AI-ekosystem men som kan köras i egna miljöer. Den kan vara särskilt intressant för prototyper, jämförelsetester, mindre assistenter och utvärdering av öppna modellspår.

**När den är lämplig:** Gemma bör övervägas när myndigheten vill testa lätta och medelstora modeller, bygga referensimplementationer eller jämföra olika modellfamiljer i samma RAG- och utvärderingsmiljö.

**När den kräver särskild analys:** Licensvillkor, användningsbegränsningar och modellens lämplighet för svenska myndighetsdomäner behöver granskas. Mindre modeller kan vara lättare att drifta men har ofta sämre förmåga i komplexa resonemang, långa dokument och juridiskt känsliga sammanhang.

**Typiska arkitekturfrågor:**

- Är modellen tillräcklig för uppgiften eller bör den bara användas i prototyp?
- Hur jämförs kvaliteten mot större kommersiella och öppna modeller?
- Kan modellen köras i myndighetens standardmiljö?
- Behövs kompletterande guardrails, reranking eller mänsklig kontroll?

### Qwen, DeepSeek och andra öppna modellfamiljer

**Typ:** Modellfamiljer med öppna eller delvis öppna vikter, ofta med snabbt föränderliga licens- och versionsförutsättningar.

**Vad de tillför:** Dessa modellfamiljer kan ge stark prestanda i vissa uppgifter, till exempel kod, resonemang, flerspråkighet, matematik eller kostnadseffektiv inferens. De kan vara viktiga jämförelsemodeller i en modellutvärdering.

**När de är lämpliga:** De bör övervägas i experiment- och benchmarkmiljöer där myndigheten vill förstå hur olika öppna modellfamiljer presterar på egna testfall. De kan också vara relevanta om de har tydliga fördelar i ett visst användningsfall och licensvillkoren tillåter användningen.

**När de kräver särskild analys:** För en statlig myndighet kräver dessa modeller ofta extra granskning av licens, ursprung, leverantörsberoende, träningsdata, säkerhetsegenskaper, uppdateringsmönster och geopolitisk risk. Det är särskilt viktigt när modeller används i verksamhetsnära processer.

**Typiska arkitekturfrågor:**

- Är modellen godkänd enligt myndighetens policy för modellursprung?
- Finns tillräcklig dokumentation om modell, licens och risker?
- Är modellen bara jämförelsemodell eller kandidat för produktion?
- Hur hanteras säkerhetsuppdateringar och modellbyte?
- Behövs särskild riskbedömning kopplad till leverantörsland eller ekosystem?

## Modellhubbar och ekosystem

### Hugging Face

**Typ:** Plattform och ekosystem för modeller, dataset, bibliotek och applikationer.

**Vad den tillför:** Hugging Face fungerar ofta som central ingång till öppna modeller, tokenizer-filer, embeddingsmodeller, dataset och exempel. Ekosystemet omfattar bland annat Transformers, Datasets, Tokenizers, Evaluate och hostingfunktioner.

**När den är lämplig:** Hugging Face är lämpligt för omvärldsbevakning, experiment, modelljämförelser och snabb prototypframtagning. Det kan också vara en källa för modeller som sedan laddas ned, granskas, versionslåses och driftsätts i myndighetens egen miljö.

**När den kräver särskild analys:** En myndighet bör inte okontrollerat låta produktionssystem hämta modeller direkt från en extern modellhub. Modeller bör speglas eller godkännas internt, signeras eller checksummekontrolleras där det är möjligt, versionslåsas och granskas avseende licens och säkerhet.

**Typiska arkitekturfrågor:**

- Ska modellhubben användas direkt, via proxy eller enbart som källkatalog?
- Hur godkänns en modell innan den får användas?
- Var lagras godkända modeller internt?
- Hur spärras ej godkända modeller i produktionsmiljö?
- Hur dokumenteras modellkort, licens och versionshistorik?

### Transformers och Sentence Transformers

**Typ:** Bibliotek för modellinläsning, inferens, finjustering och embeddings.

**Vad de tillför:** Transformers är ett centralt bibliotek för att använda många öppna språk-, bild- och multimodala modeller. Sentence Transformers används ofta för embeddings och semantisk sökning i RAG-lösningar.

**När de är lämpliga:** De är lämpliga i prototyp- och utvecklingsmiljöer, i forskningsnära team och som byggblock i egen modellutvärdering. Sentence Transformers är särskilt relevant när myndigheten vill jämföra embeddingsmodeller för svenska dokument, regeltexter och ärendehandböcker.

**När de kräver särskild analys:** I produktionsmiljö behöver myndigheten standardisera hur modeller paketeras, uppdateras, skannas, testas och driftsätts. Bibliotekens flexibilitet är en styrka, men utan styrning kan varje team skapa egna varianter som blir svåra att förvalta.

**Typiska arkitekturfrågor:**

- Ska biblioteken användas i experimentmiljö, produktion eller båda?
- Hur versionslåses modell, tokenizer och bibliotek?
- Vilka embeddingsmodeller är godkända för svenska myndighetstexter?
- Hur mäts retrieval-kvalitet och hallucinationsrisk?
- Hur undviks att varje team bygger egen osäker modellpipeline?

## Lokal modellkörning och utvecklarnära verktyg

### Ollama

**Typ:** Verktyg för lokal körning av språkmodeller.

**Vad den tillför:** Ollama gör det enkelt för utvecklare och arkitekter att köra modeller lokalt för experiment, demonstrationer och tidiga jämförelser. Det sänker tröskeln för att förstå modellbeteende, promptning och RAG-mönster utan att direkt etablera full produktionsplattform.

**När den är lämplig:** Ollama är lämpligt för labb, utbildning, prototyper och tidig teknisk utvärdering. Det kan användas för att bygga förståelse för modellstorlek, latens, minneskrav, kvantisering och lokal inferens.

**När den kräver särskild analys:** Ollama bör normalt inte vara myndighetens produktionsplattform. Den lokala enkelheten kan skapa skugg-IT om den inte styrs. Det behöver finnas policy för vilka modeller som får laddas ned, vilka data som får användas och hur lokala experiment dokumenteras.

**Typiska arkitekturfrågor:**

- Är verktyget begränsat till labbmiljö?
- Får riktiga myndighetsdata användas lokalt?
- Hur hindras okontrollerad modellnedladdning?
- Hur förs lärdomar från lokala experiment över till styrd plattform?
- När ska prototypen flyttas till godkänd inferensmiljö?

### llama.cpp

**Typ:** Lättviktig inferensmotor för lokala och resursbegränsade miljöer.

**Vad den tillför:** llama.cpp gör det möjligt att köra kvantiserade modeller på en bred uppsättning hårdvaror. Det kan vara användbart för lokala tester, edge-liknande scenarier, offline-demonstrationer eller miljöer där enkelhet och låg overhead är viktigare än maximal throughput.

**När den är lämplig:** llama.cpp bör övervägas när myndigheten vill förstå hur små och kvantiserade modeller fungerar, när man vill köra experiment utan tung GPU-infrastruktur eller när man behöver lokala demonstratorer.

**När den kräver särskild analys:** För produktion måste myndigheten bedöma prestanda, driftbarhet, övervakning, säkerhetsuppdatering, API-styrning och support. Verktyget löser inferens, men inte hela plattformsbehovet runt identitet, loggning, behörighet, observability och incidenthantering.

**Typiska arkitekturfrågor:**

- Är användningen lokal, edge, test eller produktion?
- Hur hanteras modellfiler och kvantiseringar?
- Hur mäts kvalitetstapp vid kvantisering?
- Hur integreras verktyget med säkerhets- och loggningskrav?
- Behövs en mer robust serveringsplattform i produktion?

## Produktionsnära modellservering

### vLLM

**Typ:** Open source-bibliotek och serveringsmotor för LLM-inferens.

**Vad den tillför:** vLLM är relevant när myndigheten vill köra öppna modeller med högre throughput, effektiv minneshantering, batching och OpenAI-kompatibla API-mönster. Det kan vara ett centralt byggblock i ett eget modellserveringsspår.

**När den är lämplig:** vLLM bör övervägas när myndigheten behöver produktionsnära servering av öppna modeller i GPU-miljö, särskilt där flera applikationer ska anropa modellen via gemensam gateway eller API.

**När den kräver särskild analys:** vLLM ställer krav på GPU-infrastruktur, Kubernetes- eller servermiljö, kapacitetsstyrning, observability och säker drift. Det löser inte i sig modellgovernance, åtkomstpolicy, innehållsfiltrering eller livscykelhantering.

**Typiska arkitekturfrågor:**

- Vilka modeller ska serveras och med vilken kapacitet?
- Ska vLLM exponeras direkt eller bakom AI-gateway?
- Hur dimensioneras GPU, minne, batchning och samtidighet?
- Hur kopplas serveringen till loggning, metrics och kostnadsstyrning?
- Hur hanteras modellbyte utan att bryta applikationer?

### Text Generation Inference

**Typ:** Serveringslösning för textgenerering, ofta kopplad till Hugging Face-ekosystemet.

**Vad den tillför:** Text Generation Inference kan vara relevant när myndigheten vill servera öppna modeller i ett mer standardiserat containerbaserat mönster och dra nytta av stöd i Hugging Face-ekosystemet.

**När den är lämplig:** Den är lämplig när teamet redan använder Hugging Face-modeller, vill ha containerbaserad servering och behöver en mer produktionsnära väg än lokal modellkörning.

**När den kräver särskild analys:** Som för annan egen modellservering krävs ansvar för drift, säkerhet, uppdatering, API-styrning och övervakning. Myndigheten måste också bedöma hur nära man vill koppla sitt driftspår till Hugging Face-ekosystemet.

**Typiska arkitekturfrågor:**

- Är Hugging Face-ekosystemet en godkänd del av målarkitekturen?
- Hur hanteras modellartefakter och licenser?
- Ska inferensen köras i Kubernetes, VM eller annan containerplattform?
- Vilka API-kontrakt ska applikationer använda?
- Hur jämförs lösningen mot vLLM eller kommersiell modellservering?

### SGLang och liknande serveringsramverk

**Typ:** Open source-ramverk för LLM-servering och strukturerade agent-/promptflöden.

**Vad de tillför:** Dessa ramverk kan ge hög prestanda och mer specialiserade mönster för komplex inferens, agentliknande arbetsflöden och optimerad servering.

**När de är lämpliga:** De kan övervägas av mer mogna AI-plattformsteam som har tydliga prestandakrav, stark teknisk kompetens och behov av att optimera egna modellflöden.

**När de kräver särskild analys:** För en myndighet kan mer specialiserade serveringsramverk bli svårare att förvalta än bredare etablerade alternativ. De bör införas först när behovet är tydligt och kompetensen finns.

**Typiska arkitekturfrågor:**

- Vilket problem löser ramverket bättre än enklare alternativ?
- Finns tillräcklig community, dokumentation och förvaltningsbarhet?
- Hur ser säkerhets- och uppgraderingsmodellen ut?
- Vilka interna team kan äga driften?
- Är ramverket strategiskt eller bara ett experimentverktyg?

## RAG- och orkestreringsramverk

### LangChain och LangGraph

**Typ:** Ramverk för LLM-applikationer, verktygsanrop, agenter och grafbaserade arbetsflöden.

**Vad de tillför:** LangChain ger byggblock för att koppla modeller, verktyg, dokument, prompts och externa system. LangGraph är relevant när agent- eller arbetsflöden behöver tillstånd, grenar, återförsök, mänsklig kontroll eller mer explicit kontroll än enkla kedjor.

**När de är lämpliga:** De bör övervägas när myndigheten bygger mer än en enkel RAG-pipeline och behöver orkestrera verktyg, beslutssteg, minne eller arbetsflöden. LangGraph är särskilt relevant där agentflöden behöver vara kontrollerbara och granskningsbara.

**När de kräver särskild analys:** Flexibiliteten kan skapa komplexitet. Agentflöden får inte införas utan tydliga begränsningar, loggning, testfall och säkerhetsregler. För myndigheter är det ofta bättre att börja med explicita, begränsade flöden än med autonoma agenter.

**Typiska arkitekturfrågor:**

- Behövs agentflöde eller räcker en deterministisk pipeline?
- Vilka verktyg får modellen anropa?
- Var finns mänsklig kontroll?
- Hur loggas varje steg i flödet?
- Hur testas och godkänns agentbeteende före produktion?

### LlamaIndex

**Typ:** Ramverk för data- och kontextorkestrering i LLM-applikationer.

**Vad den tillför:** LlamaIndex är särskilt relevant för RAG, indexering, dokumentkoppling, datakonnektorer och byggande av kunskapsapplikationer. Det hjälper team att strukturera hur data görs tillgänglig för språkmodeller.

**När den är lämplig:** LlamaIndex bör övervägas när myndigheten vill bygga kunskapsstöd ovanpå dokument, databaser, ärendesystem eller andra informationskällor och behöver hantera ingestion, chunking, metadata och retrieval.

**När den kräver särskild analys:** Ramverket löser inte informationsägarskap, sekretessgränser eller datakvalitet. Det måste integreras med myndighetens datastyrning, behörighetsmodell och loggning.

**Typiska arkitekturfrågor:**

- Vilka datakällor får indexeras?
- Hur bevaras behörighet och sekretess i retrieval?
- Hur versioneras index, chunkingstrategi och embeddings?
- Hur mäts kvaliteten i söksvar och källhänvisningar?
- Hur undviks att RAG-lagret blir en okontrollerad kopia av myndighetens informationsmängder?

### Haystack

**Typ:** Open source-ramverk för RAG, sök, pipelines och agentapplikationer.

**Vad den tillför:** Haystack erbjuder ett pipelineorienterat sätt att bygga RAG-applikationer, sökflöden och agentliknande lösningar. Det kan passa organisationer som vill ha tydliga komponenter och explicit dataflöde.

**När den är lämplig:** Haystack bör övervägas när myndigheten vill bygga produktionsnära RAG-pipelines med kontrollerbara steg, till exempel dokumentkonvertering, retrieval, reranking, promptbyggande och svarsgenerering.

**När den kräver särskild analys:** Även här krävs integration med säkerhet, behörighet, datastyrning och observability. Pipelinekontroll är en fördel, men den måste kompletteras med myndighetens governance.

**Typiska arkitekturfrågor:**

- Är pipelineflödet tydligt nog för granskning?
- Vilka komponenter är godkända?
- Hur loggas källor, retrieval och svar?
- Hur hanteras fallback till webbsökning eller externa källor?
- Hur testas pipelineändringar mot regressionsdata?

### Semantic Kernel

**Typ:** Open source-ramverk för AI-orkestrering, plugins och agent-/processmönster.

**Vad den tillför:** Semantic Kernel kan vara relevant när myndigheten vill bygga applikationer som kombinerar språkmodeller, funktioner, plugins, planering och befintliga system på ett mer applikationsnära sätt.

**När den är lämplig:** Det bör övervägas när myndigheten har Microsoft-nära utvecklingsmiljöer men vill bygga mer kontrollerade egna AI-applikationer med tydliga funktioner och integrationspunkter.

**När den kräver särskild analys:** Ramverket kan föra med sig arkitekturmönster som kräver stark styrning: vilka plugins får användas, hur behörighet fungerar, hur verktygsanrop loggas och hur promptar versioneras.

**Typiska arkitekturfrågor:**

- Vilka plugins är tillåtna?
- Hur separeras användarens behörighet från systemets behörighet?
- Hur granskas funktionsanrop?
- Hur samspelar ramverket med myndighetens AI-gateway?
- Är detta strategiskt ramverk eller ett teamval?

### DSPy och prompt-/pipelineoptimering

**Typ:** Ramverk för programmerbar optimering av prompts och LLM-pipelines.

**Vad den tillför:** DSPy och liknande ramverk kan hjälpa team att systematiskt förbättra promptar och pipelinebeteenden mot testdata i stället för att manuellt justera instruktioner.

**När den är lämplig:** Det är relevant i mer mogna team som har utvärderingsdata, kvalitetsmått och tydliga mål för RAG- eller LLM-applikationer.

**När den kräver särskild analys:** Optimering utan tydliga kontrollmål kan förbättra ett mått men försämra rättssäkerhet, spårbarhet eller förklarbarhet. Myndigheten behöver besluta vilka mått som faktiskt är styrande.

**Typiska arkitekturfrågor:**

- Finns tillräckliga testfall och kvalitetsmått?
- Vilka mål får optimeras?
- Hur undviks överanpassning till testdata?
- Hur dokumenteras optimerade promptar och pipelineversioner?
- Vem godkänner ändringar i produktion?

## Vektordatabaser och sökplattformar

### PostgreSQL med pgvector

**Typ:** Relationsdatabas med vektorsökningsutökning.

**Vad den tillför:** pgvector gör det möjligt att lägga embeddings nära befintliga relationsdata och använda PostgreSQL-kompetens, backup, åtkomstkontroll och driftmönster som många myndigheter redan har.

**När den är lämplig:** Det är ofta ett bra förstaval för mindre och medelstora RAG-lösningar, särskilt när datamängden är hanterbar och myndigheten vill minimera antalet nya driftkomponenter.

**När den kräver särskild analys:** För mycket stora vektormängder, höga latenskrav eller avancerad hybrid search kan en dedikerad vektordatabas eller sökplattform vara mer lämplig. Myndigheten behöver också säkra att behörighet och metadata följer med.

**Typiska arkitekturfrågor:**

- Räcker befintlig PostgreSQL-kompetens och driftmodell?
- Hur stora blir index och embeddingvolymer?
- Behövs hybrid sökning, metadatafilter eller reranking?
- Hur isoleras olika informationsklasser?
- Hur återställs och versioneras index?

### OpenSearch

**Typ:** Open source-sökplattform med stöd för bland annat text-, logg- och vektorsökning.

**Vad den tillför:** OpenSearch kan vara relevant när myndigheten redan behöver en sök- och analysplattform och vill kombinera klassisk textsearch, filtrering, logganalys och vektorsökning.

**När den är lämplig:** Den bör övervägas när hybrid search är viktigt, när befintlig sökinfrastruktur kan återanvändas eller när RAG-lösningen behöver kombinera semantisk sökning med metadata, behörighet och traditionella sökfunktioner.

**När den kräver särskild analys:** OpenSearch är en plattform som kräver driftkompetens, klusterstyrning, indexdesign och kapacitetsplanering. Felaktigt använd kan den bli en tung komponent för små RAG-fall.

**Typiska arkitekturfrågor:**

- Behövs både textsearch och vektorsökning?
- Finns befintlig OpenSearch-kompetens?
- Hur hanteras index per informationsklass?
- Hur kopplas sökträffar till ursprungskällor och behörighet?
- Är klustret dimensionerat för AI-belastning?

### Elasticsearch

**Typ:** Sök- och analysplattform med vektorsökningsförmågor, licens- och distributionsmodell som behöver granskas.

**Vad den tillför:** Elasticsearch kan vara relevant där organisationen redan använder Elastic Stack för sök, loggning eller observability och vill återanvända kompetens och infrastruktur för AI-sökning.

**När den är lämplig:** Den är lämplig när myndigheten redan har en etablerad Elastic-miljö, avtal, driftkompetens och tydlig licenshantering.

**När den kräver särskild analys:** Elasticsearch är inte alltid ett rent open source-val i praktiken. Licensvillkor, kommersiella funktioner och driftmodell måste granskas. För en appendixdel om open source bör myndigheten dokumentera om det rör sig om open source, source-available eller kommersiell licens.

**Typiska arkitekturfrågor:**

- Vilken licens och distribution används?
- Är vektorfunktionerna tillgängliga i vald licensmodell?
- Finns redan etablerad Elastic-drift?
- Hur undviks otydlighet mellan sökplattform och AI-plattform?
- Hur säkerställs export och exit?

### Milvus

**Typ:** Open source-vektordatabas för skalbar vektorsökning.

**Vad den tillför:** Milvus är relevant när myndigheten har stora vektormängder, höga prestandakrav och behov av en dedikerad vektordatabas snarare än att lägga vektorer i en generell databas.

**När den är lämplig:** Den bör övervägas när pgvector eller generell sökplattform inte räcker och när teamet har kapacitet att drifta en mer specialiserad komponent.

**När den kräver särskild analys:** Dedikerade vektordatabaser ökar plattformsytan. De kräver driftkompetens, backupstrategi, indexförvaltning, uppgraderingsplan och tydlig integration med metadata och behörighet.

**Typiska arkitekturfrågor:**

- Vilken volym och latens kräver en dedikerad vektordatabas?
- Hur hanteras metadata, access control och segmentering?
- Hur ser backup och restore ut för index?
- Hur benchmarkas lösningen mot myndighetens egna data?
- Är komplexiteten motiverad?

### Qdrant

**Typ:** Open source-vektordatabas med fokus på vektorsökning och metadatafiltrering.

**Vad den tillför:** Qdrant kan vara relevant för RAG-lösningar där metadatafilter, enkel utvecklarupplevelse och egen drift är viktiga. Den kan också vara lättare att komma igång med än mer komplexa alternativ.

**När den är lämplig:** Den bör övervägas för RAG-applikationer med tydliga metadatafilter, avgränsade datamängder och behov av containeriserad eller egen drift.

**När den kräver särskild analys:** Myndigheten måste bedöma mognad, supportmodell, klusterdrift, säkerhet, backup och hur väl den passar organisationens standardplattform.

**Typiska arkitekturfrågor:**

- Hur används metadata för behörighet och informationsklass?
- Räcker Qdrants driftmodell för myndighetens SLA?
- Hur sker backup och återindexering?
- Vilka team ansvarar för uppgraderingar?
- Hur benchmarkas den mot pgvector och OpenSearch?

### Weaviate

**Typ:** Vektordatabas med open source- och kommersiella distributionsmodeller.

**Vad den tillför:** Weaviate kan ge en tydlig vektordatabasplattform med hybrid search, schemahantering och integrationer. Den är relevant när myndigheten vill ha mer än enkel vektorsökning men inte bygga allt själv.

**När den är lämplig:** Den bör övervägas när RAG-lösningen kräver en mer specialiserad vektordatabas, hybrid search och strukturerade objektmodeller.

**När den kräver särskild analys:** Licens, driftmodell, kommersiella tillägg, support och datalokalisering måste bedömas. För en myndighet är det viktigt att skilja mellan självdrift och managed service.

**Typiska arkitekturfrågor:**

- Används open source-distribution eller managed service?
- Hur hanteras schema och metadata över tid?
- Hur kontrolleras åtkomst per dokument och informationsklass?
- Vilka funktioner kräver kommersiella tillägg?
- Hur ser exit ut om plattformen byts?

### Chroma och FAISS

**Typ:** Lättviktiga vektorverktyg och bibliotek för experiment, prototyper och vissa avgränsade användningsfall.

**Vad de tillför:** Chroma och FAISS kan vara användbara i prototyper, lokala tester och forskningsnära experiment där enkelhet eller låg overhead är viktigare än komplett driftplattform.

**När de är lämpliga:** De bör övervägas i labbmiljö, utbildning och tidiga proof of concept-arbeten. FAISS är särskilt relevant som bibliotek för vektorindexering där teamet bygger mer själv.

**När de kräver särskild analys:** De är normalt inte tillräckliga som ensam myndighetsgemensam produktionsplattform för RAG. Drift, backup, åtkomstkontroll, multi-tenancy och governance måste lösas runt dem.

**Typiska arkitekturfrågor:**

- Är användningen begränsad till prototyp?
- Hur flyttas resultat till produktionsplattform?
- Hur hanteras metadata och behörighet?
- Finns risk att prototypverktyget blir permanent?
- Vilket produktionsalternativ ersätter labbkomponenten?

## MLOps, LLMOps och arbetsflöden

### MLflow

**Typ:** Open source-plattform för MLOps och LLMOps.

**Vad den tillför:** MLflow kan användas för experiment tracking, modellregister, utvärdering, spårning av LLM-applikationer, prompt- och versionshantering samt observability för agent- och LLM-flöden.

**När den är lämplig:** MLflow bör övervägas när myndigheten vill ha ett leverantörsneutralt sätt att spåra experiment, modeller, promptar, utvärderingar och produktionsbeteende. Den är särskilt relevant när både klassisk ML och generativ AI ska hanteras i samma livscykel.

**När den kräver särskild analys:** MLflow behöver driftas, säkras och integreras med identitet, lagring, nätverk, CI/CD och modellservering. En lokal filbaserad utvecklingsinstallation är inte samma sak som myndighetsgemensam LLMOps-plattform.

**Typiska arkitekturfrågor:**

- Ska MLflow vara central plattform eller teamverktyg?
- Vilka metadata måste registreras för varje modell och prompt?
- Hur kopplas MLflow till godkännandeprocesser?
- Hur skyddas loggar, prompts och utdata?
- Hur integreras MLflow med observability och incidenthantering?

### Kubeflow

**Typ:** Open source-plattform för ML-arbetsflöden på Kubernetes.

**Vad den tillför:** Kubeflow kan ge stöd för pipelines, träningsjobb, experiment och produktionsnära ML-arbetsflöden i Kubernetes-miljö.

**När den är lämplig:** Kubeflow bör övervägas när myndigheten redan har stark Kubernetes-kompetens och vill bygga en mer komplett ML-plattform för flera team.

**När den kräver särskild analys:** Kubeflow kan vara komplext. För en myndighet som främst behöver RAG och modellkonsumtion kan det vara överdimensionerat. Det passar bäst där det finns flera ML-team, återkommande modellträning och behov av standardiserade pipelines.

**Typiska arkitekturfrågor:**

- Finns tillräcklig Kubernetes- och ML-plattformskompetens?
- Är behovet modellträning, inferens eller båda?
- Hur integreras Kubeflow med säkerhet och identitet?
- Hur förvaltas pipelines över tid?
- Är komplexiteten rimlig jämfört med enklare MLOps-verktyg?

### Argo Workflows och Apache Airflow

**Typ:** Open source-verktyg för arbetsflöden och orkestrering.

**Vad de tillför:** Argo Workflows passar container- och Kubernetesnära arbetsflöden. Apache Airflow passar schemalagd data- och pipelineorkestrering. Båda kan användas för AI-relaterade flöden som ingestion, indexering, utvärdering, batchinferens och återkommande datakvalitetskontroller.

**När de är lämpliga:** De bör övervägas när myndigheten behöver robust orkestrering runt AI-plattformen snarare än bara modellkörning. Airflow kan passa dataflöden. Argo kan passa containeriserade ML- och AI-pipelines.

**När de kräver särskild analys:** Arbetsflödesverktyg löser inte modellkvalitet, riskbedömning eller säkerhet. De ska ses som teknisk orkestrering som behöver styras av arkitekturprinciper och processer.

**Typiska arkitekturfrågor:**

- Är arbetsflödet datadrivet, containerdrivet eller båda?
- Vilka steg kräver godkännande?
- Hur loggas och återstartas misslyckade körningar?
- Hur separeras miljöer och informationsklasser?
- Hur kopplas workflow till modellregister och utvärdering?

### KServe, Ray Serve och BentoML

**Typ:** Serverings- och deploymentverktyg för modeller och AI-tjänster.

**Vad de tillför:** Dessa verktyg kan hjälpa myndigheten att paketera och exponera modeller som tjänster, ofta med stöd för skalning, versionering och integration med Kubernetes eller Pythonbaserade driftmönster.

**När de är lämpliga:** De bör övervägas när myndigheten vill standardisera hur modeller publiceras och körs i egen drift, särskilt om det finns flera modelltyper och team.

**När de kräver särskild analys:** De tillför ett serveringslager men inte automatiskt full AI-governance. Myndigheten måste fortfarande styra modellgodkännande, åtkomst, loggning, säkerhet, utvärdering och livscykel.

**Typiska arkitekturfrågor:**

- Vilken serveringsstandard ska myndigheten välja?
- Ska modeller köras som individuella tjänster eller bakom gateway?
- Hur hanteras canary, rollback och versionsbyte?
- Vilka krav finns på autoskalning och GPU-planering?
- Hur integreras servering med MLflow eller annat register?

## Utvärdering, kvalitet och observability

### Ragas, DeepEval och liknande evalueringsramverk

**Typ:** Open source-ramverk för utvärdering av RAG- och LLM-applikationer.

**Vad de tillför:** Evalueringsramverk kan hjälpa team att mäta retrieval-kvalitet, svarskvalitet, relevans, hallucinationer, kontextanvändning och regressionsrisk. De gör AI-utveckling mer systematisk.

**När de är lämpliga:** De bör övervägas när myndigheten går från demo till pilot eller produktion och behöver visa att ändringar förbättrar kvalitet utan att försämra säkerhet eller korrekthet.

**När de kräver särskild analys:** LLM-baserad utvärdering är inte neutral. Domänspecifika testfall, mänsklig granskning och tydliga kvalitetskriterier behövs. För juridiskt eller operativt känsliga användningsfall räcker inte automatiska mått.

**Typiska arkitekturfrågor:**

- Vilka kvalitetsmått är styrande?
- Finns testfall från verkliga myndighetsscenarier?
- Hur hanteras svenska termer och myndighetsspråk?
- Vilka resultat kräver mänsklig granskning?
- Hur kopplas utvärdering till releasebeslut?

### OpenTelemetry, Prometheus och Grafana

**Typ:** Observability-byggblock för spårning, metrics, loggning och visualisering.

**Vad de tillför:** Dessa verktyg kan användas för att mäta latens, fel, köer, kostnadsindikatorer, tokenvolymer, API-anrop, pipelineflöden och teknisk hälsa i AI-lösningar.

**När de är lämpliga:** De bör övervägas när myndigheten vill integrera AI-plattformen i befintlig övervakning och incidenthantering. OpenTelemetry är särskilt relevant för spårning över flera komponenter.

**När de kräver särskild analys:** AI-loggar kan innehålla personuppgifter, sekretessuppgifter, prompts och modellutdata. Observability får inte bli en okontrollerad kopia av känsligt innehåll. Maskning, retention och åtkomstkontroll är centrala.

**Typiska arkitekturfrågor:**

- Vilka AI-specifika telemetrydata behövs?
- Vilka data får inte loggas?
- Hur maskas prompts, dokumentutdrag och utdata?
- Hur länge sparas spår och loggar?
- Hur kopplas incidenter till AI-governance?

### Langfuse och öppna LLM-observabilityverktyg

**Typ:** Verktyg för tracing, promptversionering, utvärdering och analys av LLM-applikationer.

**Vad de tillför:** Langfuse och liknande verktyg kan ge detaljerad insyn i promptar, modellanrop, kostnader, svar, kedjor och användarbeteende. De kan vara värdefulla vid felsökning och kvalitetssäkring av RAG- och agentlösningar.

**När de är lämpliga:** De bör övervägas när myndigheten bygger flera LLM-applikationer och behöver ett gemensamt sätt att felsöka och jämföra kvalitet.

**När de kräver särskild analys:** Denna typ av verktyg samlar ofta mycket känslig kontext. Driftplats, databas, åtkomstkontroll, retention och maskning måste bedömas innan de används med riktiga myndighetsdata.

**Typiska arkitekturfrågor:**

- Var lagras traces och promptdata?
- Kan verktyget köras i myndighetens miljö?
- Vilka roller får läsa LLM-traces?
- Hur maskas personuppgifter och sekretess?
- Hur kopplas observability till release- och incidentprocesser?

## Säkerhet, policy och guardrails

### NeMo Guardrails

**Typ:** Open source-ramverk för att styra samtalsflöden och skyddsregler runt LLM-applikationer.

**Vad den tillför:** NeMo Guardrails kan användas för att definiera regler för vad en assistent får säga, vilka dialogflöden som är tillåtna och hur vissa riskbeteenden ska hanteras.

**När den är lämplig:** Den bör övervägas när myndigheten bygger kontrollerade assistenter där svarsbeteende och begränsningar behöver vara explicit definierade.

**När den kräver särskild analys:** Guardrails ersätter inte testning, informationsklassning eller juridisk bedömning. Reglerna måste versioneras, testas och anpassas till användningsfallet. För hårt skrivna regler kan ge falsk trygghet eller dålig användbarhet.

**Typiska arkitekturfrågor:**

- Vilka risker ska guardrails faktiskt minska?
- Hur testas reglerna mot realistiska attacker?
- Vem äger regelverket?
- Hur versioneras och godkänns ändringar?
- Hur kombineras guardrails med policy enforcement och loggning?

### Open Policy Agent

**Typ:** Policy motor för kodifierade åtkomst- och beslutsregler.

**Vad den tillför:** Open Policy Agent kan vara relevant för att uttrycka policy som kod i AI-plattformen, till exempel vilka användare, system eller informationsklasser som får använda vissa modeller eller dataflöden.

**När den är lämplig:** Den bör övervägas när myndigheten vill göra policybeslut mer konsekventa och maskinellt kontrollerbara i API-gateways, Kubernetes, CI/CD eller interna plattformstjänster.

**När den kräver särskild analys:** Policy som kod kräver tydliga ägarskap. Felaktiga regler kan blockera legitima flöden eller tillåta otillåtna. Den juridiska och informationssäkerhetsmässiga innebörden måste översättas korrekt till teknisk policy.

**Typiska arkitekturfrågor:**

- Vilka AI-beslut ska kodifieras som policy?
- Vem äger policyreglerna?
- Hur testas policyändringar?
- Hur loggas policybeslut?
- Hur hanteras undantag?

### LLM Guard, Guardrails AI och liknande skyddsverktyg

**Typ:** Verktyg för input-/outputkontroll, promptskydd, validering och filtrering.

**Vad de tillför:** Dessa verktyg kan hjälpa till att upptäcka riskabla inputs, otillåten output, personuppgifter, känsligt innehåll, osäkra verktygsanrop eller svar som inte följer formatkrav.

**När de är lämpliga:** De bör övervägas som kompletterande skydd i RAG- och assistentlösningar, särskilt där användare kan skriva fri text eller där modellen kan anropa verktyg.

**När de kräver särskild analys:** Skyddsverktyg är inte perfekta. De måste testas mot svenska data, myndighetsspråk, falska positiva och falska negativa. De får inte bli enda kontrollen i en lösning som hanterar känslig information.

**Typiska arkitekturfrågor:**

- Vilka kontroller sker före modellanrop?
- Vilka kontroller sker efter modellutdata?
- Hur hanteras blockeringar och eskalering?
- Hur mäts false positives och false negatives?
- Hur integreras verktygen med AI-gateway och observability?

## Infrastruktur för egen drift

### Kubernetes

**Typ:** Containerorkestrering och standardplattform för många AI- och ML-komponenter.

**Vad den tillför:** Kubernetes kan ge en gemensam körmiljö för modellservering, pipelines, RAG-komponenter, vektordatabaser, observability och interna AI-tjänster. Den kan bidra till portabilitet mellan on-premises, privat moln och publikt moln.

**När den är lämplig:** Kubernetes är lämpligt när myndigheten redan har plattformskompetens, behöver flera tjänster och vill standardisera driftmönster. Den är ofta relevant i hybridarkitektur.

**När den kräver särskild analys:** Kubernetes löser inte automatiskt säker drift. GPU-hantering, nätverkspolicy, secrets, image scanning, runtime security, kostnadsstyrning och plattformsförvaltning måste fungera.

**Typiska arkitekturfrågor:**

- Finns etablerad Kubernetes-plattform?
- Hur hanteras GPU-noder?
- Hur separeras informationsklasser?
- Vilka nätverkspolicys gäller för modellanrop?
- Hur paketeras AI-komponenter som standardtjänster?

### Docker och containerbaserad paketering

**Typ:** Paketerings- och körningsmönster för applikationer och AI-komponenter.

**Vad den tillför:** Containers gör det möjligt att paketera modeller, API:er, pipelines och verktyg på ett mer reproducerbart sätt. Det förenklar flytt mellan utveckling, test och produktion.

**När den är lämplig:** Containerisering bör vara standard för många egenutvecklade AI-komponenter, förutsatt att myndigheten har säker containerkedja och godkända basavbildningar.

**När den kräver särskild analys:** AI-containers kan innehålla stora modellfiler, osäkra beroenden och externa nedladdningsmekanismer. Supply chain security är därför särskilt viktig.

**Typiska arkitekturfrågor:**

- Vilka basimages är godkända?
- Hur skannas containerimages?
- Får modeller laddas ned vid runtime?
- Hur hanteras secrets och API-nycklar?
- Hur byggs reproducerbara releases?

## Datakvalitet och informationsförberedelse

### Apache Airflow, Dagster och dbt Core

**Typ:** Dataorkestrering, dataflöden och transformationsverktyg.

**Vad de tillför:** Dessa verktyg kan användas för att förbereda data, köra återkommande ingestion, datakvalitetskontroller och transformationer innan information görs tillgänglig för AI-lösningar.

**När de är lämpliga:** De bör övervägas när AI-förmågan bygger på återkommande dataflöden, dataplattformar och behov av spårbarhet från källa till AI-tjänst.

**När de kräver särskild analys:** AI-problem är ofta dataförvaltningsproblem. Verktygen kan hjälpa, men informationsägarskap, gallring, sekretess, metadata och datakvalitet måste vara styrda.

**Typiska arkitekturfrågor:**

- Vilka datakällor får användas för AI?
- Hur dokumenteras datalinje?
- Hur hanteras gallring och arkivkrav?
- Vilka kontroller sker före indexering?
- Hur upptäcks felaktig eller föråldrad information?

### Great Expectations, Soda Core och liknande verktyg

**Typ:** Datakvalitetsverktyg.

**Vad de tillför:** Datakvalitetsverktyg kan användas för att definiera och testa förväntningar på data innan den används i AI-lösningar, till exempel schema, nullvärden, intervall, uppdateringsfrekvens och anomalier.

**När de är lämpliga:** De är relevanta när myndigheten använder strukturerade data för prediktiva modeller, beslutsstöd eller RAG-metadata. De kan även användas för att upptäcka att indexeringsflöden har börjat ta in fel information.

**När de kräver särskild analys:** Datakvalitetsmått måste kopplas till verksamhetsbetydelse. Att ett dataset är tekniskt korrekt betyder inte att det är lämpligt för AI-användning.

**Typiska arkitekturfrågor:**

- Vilka datakvalitetsregler är kritiska?
- Vem godkänner reglerna?
- Vad händer när ett dataflöde fallerar?
- Hur syns datakvalitet i AI-tjänstens riskbedömning?
- Hur dokumenteras kvalitet i modell- eller systemkort?

## När open source är rätt väg

Open source bör övervägas när minst ett av följande är sant:

- Myndigheten behöver kunna drifta AI-komponenter i egen miljö.
- Informationsklassning eller riskbedömning gör kommersiell SaaS olämplig.
- Myndigheten vill minska beroendet av enskilda leverantörer.
- Det finns stark intern plattformskompetens.
- Användningsfallet kräver djup teknisk anpassning.
- Det finns behov av reproducerbara benchmarkar och transparenta jämförelser.
- Myndigheten vill etablera ett öppet modellspår parallellt med kommersiella modeller.

För en myndighet är open source-spåret särskilt relevant för experimentmiljö, RAG-prototyper, modelljämförelser, egen vektorsökning och vissa interna assistenter där data inte bör skickas till extern SaaS.

## När open source bör undvikas

Open source bör inte väljas när:

- myndigheten saknar förvaltningsförmåga,
- driftteamet inte kan hantera GPU, Kubernetes, säkerhet och observability,
- licensvillkor är oklara,
- modellen saknar dokumentation,
- användningsfallet kräver support, garanti och avtalsstyrning,
- teamet vill använda open source för att kringgå upphandling eller riskbedömning,
- varje utvecklingsteam vill välja eget ramverk utan gemensamma standarder.

I sådana fall kan kommersiell plattform, kontrollerad molntjänst eller ett smalare internt plattformserbjudande vara bättre.

## Rekommenderad position i målarkitekturen

För en större statlig myndighet bör open source inte vara ett sidospår utanför styrningen. Det bör vara ett formellt arkitekturspår med tydliga regler.

myndigheten bör därför överväga att etablera:

- en godkänd intern modellkatalog för öppna modeller,
- ett standardiserat RAG-mönster med godkända ramverk,
- en beslutad strategi för vektorsökning,
- en kontrollerad inferensmiljö för egen modellservering,
- ett LLMOps-spår för test, versionering och observability,
- en policy för nedladdning, spegling och godkännande av externa modeller,
- en process för licens- och säkerhetsgranskning,
- en exitmodell för att kunna byta mellan öppna och kommersiella komponenter.

Det viktiga är inte att myndigheten väljer flest open source-komponenter. Det viktiga är att myndigheten kan välja dem medvetet, drifta dem säkert och byta ut dem när risk, kvalitet eller kostnad förändras.
