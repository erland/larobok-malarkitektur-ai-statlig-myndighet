# Kapitel 16: Säkerhetsarkitektur för AI

## Varför detta kapitel finns

AI förändrar inte grunderna för informationssäkerhet, men den förändrar hur hot, fel och missbruk kan uppstå. En traditionell applikation exekverar instruktioner som utvecklare har skrivit. En AI-baserad lösning tar dessutom emot naturligt språk, hämtar kontext från dokument och system, tolkar osäker information, skapar nytt innehåll och kan ibland anropa verktyg eller API:er. Det gör att säkerhetsarkitekturen måste hantera både klassiska IT-risker och AI-specifika risker.

För en större statlig myndighet är detta särskilt viktigt. Myndigheten hanterar ofta sekretessreglerad information, personuppgifter, skyddsvärda verksamhetsprocesser och beslut som kan påverka enskilda. När AI införs i en sådan miljö räcker det inte att fråga om modellen är bra. Man måste fråga om hela kedjan är säker: data, promptar, åtkomst, retrieval, verktygsanrop, loggar, modellutdata, integrationer, användargränssnitt, driftmiljö och leverantörskedja.

Detta kapitel beskriver hur säkerhetsarkitekturen för AI bör utformas som en del av målarkitekturen. Fokus ligger på hotmodeller, skyddsåtgärder, kontrollpunkter och praktiska vägval. Kapitlet bygger vidare på teknisk referensarkitektur, RAG, plattformsval och beslutsmodeller från tidigare kapitel.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva hur AI-specifika hot skiljer sig från traditionella applikationshot,
- identifiera viktiga risker som prompt injection, data leakage, otillåten verktygsanvändning och bristande spårbarhet,
- utforma en säkerhetsarkitektur med lager av kontroller snarare än en enskild skyddsmekanism,
- placera AI-gateway, policy enforcement, identitet, loggning, guardrails och övervakning i målarkitekturen,
- formulera säkerhetskrav för RAG-baserade kunskapsstöd och agentliknande AI-lösningar,
- avgöra vilka AI-användningsfall som kräver förstärkt granskning, isolering eller on-premises-drift.

## Innan vi börjar

Kapitlet utgår från att myndigheten redan har:

- kategoriserat sina AI-användningsfall,
- gjort grundläggande juridisk triage,
- klassat information och datakällor,
- formulerat arkitekturprinciper,
- beskrivit teknisk referensarkitektur,
- tagit ställning till moln, on-premises och hybrid,
- dokumenterat större vägval i en beslutslogg.

Säkerhetsarkitekturen ska inte skapas som ett sidospår efter att AI-plattformen är vald. Den ska vara en del av plattformsvalet, integrationsmönstret, driftmodellen och produktionssättningen.

## Säkerhetsproblemet i AI-lösningar

En AI-lösning kan se enkel ut från användarens perspektiv. En handläggare skriver en fråga, får ett svar och kan kanske klicka på källhänvisningar. Bakom detta finns ofta en kedja av komponenter:

- användargränssnitt,
- identitet och behörighet,
- AI-gateway eller API-lager,
- promptmallar,
- retrieval och sökindex,
- vektordatabas,
- dokumentlager,
- modell-API eller egen modellservering,
- policy- och säkerhetskontroller,
- loggning och övervakning,
- eventuella verktygs- eller API-anrop.

Varje komponent kan införa risk. Vissa risker är välkända, exempelvis felaktig åtkomstkontroll, sårbara API:er, bristande loggning och otillräcklig nätverkssegmentering. Andra risker är mer specifika för AI. Modellen kan manipuleras via instruktioner i användarens prompt. Retrieval-lagret kan hämta dokument som innehåller dolda instruktioner. En agent kan anropa fel verktyg. Ett svar kan innehålla känslig information som användaren inte borde se. Loggar kan lagra personuppgifter eller sekretessbelagd information i miljöer där de inte hör hemma.

Säkerhetsarkitekturen måste därför behandla AI-lösningen som en besluts- och informationskedja, inte som en isolerad modell.

Generativa AI-lösningar bör behandlas som en särskild riskklass, inte bara som vanliga webb- eller API-applikationer. Utöver klassiska hot behöver arkitekturen hantera AI-specifika risker som prompt injection, osäker hantering av modellutdata, manipulerad kontext, förgiftade tränings- eller kunskapsdata, överbelastningsangrepp mot modeller och sårbarheter i modell- och komponentkedjan.

## Centrala hotbilder

### Prompt injection

Prompt injection innebär att en användare eller en informationskälla försöker påverka modellens beteende genom instruktioner som inte borde styra systemet. Det kan vara direkt, till exempel när användaren skriver “ignorera alla tidigare instruktioner”. Det kan också vara indirekt, till exempel när ett dokument som hämtas via RAG innehåller en dold eller öppen instruktion till modellen.

För en myndighet är indirekt prompt injection särskilt relevant. Ett RAG-baserat kunskapsstöd kan hämta dokument från interna dokumentlager, ärendeunderlag, e-post, externa webbplatser eller bilagor. Om modellen behandlar allt hämtat innehåll som lika betrott kan en angripare placera instruktioner i ett dokument och få modellen att ändra beteende.

Ett grundläggande arkitekturbeslut är därför att skilja mellan:

- systeminstruktioner,
- användarinstruktioner,
- hämtad kontext,
- modellens svar,
- verktygsanrop,
- policybeslut.

Hämtad kontext ska normalt behandlas som data, inte som instruktion. Det är lätt att skriva i en princip, men svårt att garantera i praktiken. Därför krävs flera kontroller samtidigt.

### Data leakage

Data leakage uppstår när känslig information exponeras till fel mottagare, fel komponent, fel leverantör eller fel logg. I AI-lösningar kan läckage ske på flera sätt:

- användaren klistrar in sekretessbelagd information i en otillåten AI-tjänst,
- retrieval hämtar dokument som användaren saknar behörighet till,
- modellen sammanfattar information från flera källor och råkar kombinera fram något användaren inte borde få se,
- promptar och svar lagras i loggar med för bred åtkomst,
- leverantören använder data för modellträning i strid med myndighetens krav,
- en agent skickar data till ett externt verktyg,
- testdata innehåller verkliga personuppgifter eller sekretessreglerad information.

Säkerhetsarkitekturen måste därför styra både indata, mellanlagring, modellanrop, utdata och loggar.

### Otillåten verktygsanvändning

När AI-lösningar får tillgång till verktyg ökar riskbilden kraftigt. Ett verktyg kan vara ett API, ett söksystem, ett ärendesystem, en e-postfunktion, ett skript, ett databasgränssnitt eller en RPA-komponent. Om modellen kan välja verktyg och skapa parametrar måste arkitekturen hantera risken att modellen gör fel sak med rätt behörighet.

Exempel:

- modellen söker i fel register,
- modellen skapar ett ärendeutkast med fel uppgifter,
- modellen skickar information till fel mottagare,
- modellen uppdaterar ett system utan tillräcklig mänsklig kontroll,
- modellen anropar ett verktyg med manipulerade parametrar,
- modellen utför en åtgärd baserad på opålitlig kontext.

Ett viktigt designval är att inte ge modellen direkt åtkomst till verksamhetskritiska verktyg. Den bör i stället gå genom ett kontrollerat verktygslager med policy, behörighetskontroll, validering och spårbarhet.

### Hallucination som säkerhetsrisk

Hallucination behandlas ofta som en kvalitetsfråga, men i myndighetsmiljö kan den också vara en säkerhetsrisk. Ett felaktigt svar kan leda till felaktig handläggning, missvisande riskbedömning eller olämplig utlämning av information. Om användaren litar för mycket på svaret kan modellen bli en osynlig beslutsaktör.

Målarkitekturen bör därför tydligt skilja mellan:

- AI som språkstöd,
- AI som kunskapsstöd,
- AI som analysstöd,
- AI som beslutsstöd,
- AI som automatiserad beslutskomponent.

Ju närmare lösningen kommer beslut, myndighetsutövning eller operativ prioritering, desto högre krav bör ställas på validering, källhänvisning, mänsklig kontroll och dokumentation.

### Modell- och leverantörskedjerisk

AI-lösningar är beroende av leverantörskedjor. Det kan handla om modeller, modellvikter, containrar, SDK:er, promptbibliotek, RAG-ramverk, vektordatabaser, molntjänster, open source-komponenter och säkerhetsprodukter.

Säkerhetsarkitekturen bör därför omfatta:

- godkända modellkällor,
- versionshantering av modeller,
- sårbarhetshantering för ramverk och bibliotek,
- kontroll av containerbilder och beroenden,
- krav på leverantörens databehandling,
- granskning av modellvillkor,
- exitstrategi,
- möjlighet att byta modell utan att bygga om hela lösningen.

## Säkerhetsarkitektur som lager

Ett vanligt misstag är att försöka lösa AI-säkerhet med en enda mekanism. Ett filter räcker inte. En policytext räcker inte. En bra modell räcker inte. En AI-gateway räcker inte. Säkerhetsarkitekturen behöver flera lager som kompletterar varandra.

En praktisk lagerindelning är:

1. styrning och policy,
2. identitet och åtkomst,
3. dataskydd och informationsklassning,
4. prompt- och kontextkontroll,
5. modell- och plattformsisolering,
6. verktygs- och integrationskontroll,
7. output-validering,
8. loggning och övervakning,
9. incidenthantering och kontinuerlig förbättring.

### Lager 1: styrning och policy

Styrning anger vilka AI-lösningar som får användas, för vilka informationsklasser, av vilka användare och under vilka villkor. Policyn ska inte vara enbart ett dokument i intranätet. Den behöver realiseras i tekniska kontroller.

Exempel på styrande regler:

- vilka dataklasser som får skickas till vilka AI-tjänster,
- vilka användningsfall som får använda extern modell-API,
- vilka användningsfall som kräver on-premises eller avskild drift,
- vilka lösningar som kräver mänsklig granskning,
- vilka användare som får använda agentfunktioner,
- vilka loggar som måste sparas,
- vilka AI-anrop som måste kunna revideras.

Målet är att policy ska bli arkitektur, inte bara text.

### Lager 2: identitet och åtkomst

AI-lösningar ska inte bli genvägar runt befintliga behörighetsmodeller. Användarens behörighet måste följa med genom kedjan från användargränssnitt till retrieval, modellanrop och verktygsanrop.

I ett RAG-baserat kunskapsstöd innebär det att sökresultat ska filtreras utifrån användarens behörighet innan de skickas till modellen. Modellen ska inte få se dokument som användaren inte har rätt att se. Det räcker inte att dölja källhänvisningen i svaret, eftersom modellen redan kan ha använt informationen för att formulera svaret.

Identitet och åtkomst bör därför omfatta:

- stark autentisering,
- roll- och attributbaserad åtkomst,
- åtkomstkontroll i retrieval-lagret,
- separata behörigheter för läsning, generering och verktygsanrop,
- servicekonton med minsta möjliga behörighet,
- tydlig koppling mellan användare, session, prompt, datakällor och AI-anrop.

### Lager 3: dataskydd och informationsklassning

Dataskydd börjar före modellen. Arkitekturen bör styra vilka data som får användas, hur de transformeras, var de lagras och hur länge de sparas.

Viktiga kontroller är:

- dataminimering i promptar,
- maskning eller pseudonymisering där det är möjligt,
- separata index för olika informationsklasser,
- tydliga regler för vilka dokument som får indexeras,
- kontroll av metadata och behörigheter vid indexering,
- gallring av prompt- och svarshistorik,
- skydd av loggar,
- testdata utan verkliga personuppgifter när det är möjligt.

För Tullverket Aurora innebär detta att ett kunskapsstöd för publika regelverk kan ha en annan arkitektur än ett stöd som arbetar med ärendeinformation, riskindikatorer eller uppgifter om enskilda importörer.

### Lager 4: prompt- och kontextkontroll

Prompt- och kontextkontroll handlar om att minska risken att modellen styrs av fel instruktioner eller får fel underlag.

Kontroller kan vara:

- separata systeminstruktioner som inte blandas med användartext,
- tydlig märkning av hämtad kontext som opålitlig data,
- begränsning av kontextfönster,
- filtrering av dokument med misstänkta instruktioner,
- promptmallar som styr hur modellen ska använda källor,
- krav på källhänvisning,
- spärr mot att följa instruktioner i hämtade dokument,
- testfall för prompt injection och indirekt prompt injection.

Det är viktigt att inte översälja dessa kontroller. De minskar risk, men de eliminerar den inte. Därför behöver de kombineras med åtkomstkontroll, output-kontroll och begränsad verktygsbehörighet.

### Lager 5: modell- och plattformsisolering

Alla AI-användningsfall bör inte dela samma runtime, samma modell, samma nätverksväg eller samma loggflöde. Målarkitekturen bör definiera säkerhetszoner för AI.

En möjlig zonindelning är:

- öppen experimentzon för icke-känsliga data,
- intern produktivitetszon för godkända interna data,
- skyddad verksamhetszon för känsligare dokument och handläggarstöd,
- avskild analyszon för högt skyddsvärda data,
- on-premises-zon för användningsfall där extern drift inte är acceptabel.

Zonerna bör kopplas till informationsklassning, risknivå, tillåtna modeller, loggningskrav, nätverksåtkomst, leverantörskrav och incidentrutiner.

### Lager 6: verktygs- och integrationskontroll

Om AI-lösningen kan använda verktyg måste varje verktyg behandlas som en privilegierad funktion. Modellen ska inte själv vara behörighetsbärare. Den ska begära en åtgärd, men ett kontrollerat lager ska avgöra om åtgärden får utföras.

Kontroller kan vara:

- explicit allowlist för verktyg,
- separata behörigheter per verktyg,
- parameter-validering,
- transaktionsgränser,
- mänsklig bekräftelse före skrivande åtgärder,
- sandbox för kod och filhantering,
- spärr mot externa nätverksanrop,
- spårbarhet från prompt till verktygsanrop,
- möjlighet att stänga av verktyg snabbt vid incident.

För en myndighet bör skrivande åtgärder i verksamhetssystem normalt börja som förslag eller utkast, inte som automatisk exekvering.

### Lager 7: output-validering

Modellens svar är inte automatiskt säkert bara för att indata kontrollerats. Output-validering behövs för att upptäcka eller minska risker i det genererade svaret.

Exempel på output-kontroller:

- kontroll mot känsliga datamönster,
- klassning av svarets innehåll,
- spärr mot otillåtna instruktioner,
- krav på källhänvisning,
- kontroll att svar inte påstår mer än källorna stödjer,
- formatvalidering när svaret ska användas maskinellt,
- markering av osäkerhet,
- tvingande mänsklig granskning för vissa användningsfall.

Output-validering är särskilt viktig när AI-svaret går vidare till ett annat system, till ett beslutsunderlag eller till en extern mottagare.

### Lager 8: loggning och övervakning

AI-lösningar behöver loggas, men loggning är också en risk. Promptar, svar, retrieval-resultat och verktygsanrop kan innehålla personuppgifter eller sekretessreglerad information. Därför måste loggningen utformas med både spårbarhet och dataminimering.

Loggningen bör kunna svara på frågor som:

- vem använde lösningen,
- vilket användningsfall gällde det,
- vilken modell och version användes,
- vilken promptmall användes,
- vilka dokument hämtades,
- vilka policybeslut fattades,
- vilka verktyg anropades,
- vilket svar gavs,
- flaggades något som risk,
- avbröts eller blockerades något.

Samtidigt behöver arkitekturen styra:

- vilka loggar som får innehålla promptar,
- vilka loggar som ska maskas,
- vem som får läsa loggar,
- hur länge loggar sparas,
- hur loggar kopplas till incidenthantering och revision.

### Lager 9: incidenthantering och förbättring

AI-incidenter kan se annorlunda ut än vanliga IT-incidenter. Det kan handla om felaktiga svar, otillåten informationsspridning, prompt injection, modellbeteende, leverantörsförändringar, felaktigt indexerade dokument eller oväntade verktygsanrop.

Myndigheten bör därför ha en AI-specifik incidentmodell som kopplar till befintlig incidenthantering. Den bör omfatta:

- hur en misstänkt AI-incident rapporteras,
- hur promptar, svar och loggar säkras,
- vem som bedömer juridiska konsekvenser,
- vem som bedömer informationssäkerhet,
- vem som kan pausa en modell eller funktion,
- hur användare informeras,
- hur lärdomar förs tillbaka till arkitekturprinciper, testfall och policy.

För Tullverket Aurora innebär detta att säkerhetsarkitekturen behöver kombinera klassiska kontroller med AI-specifika kontroller: isolering av verktygsanrop, validering av modellutdata, skydd mot manipulerad kontext, styrning av retrieval, begränsning av agentbeteenden, övervakning av kostnads- och kapacitetsangrepp samt en tydlig incidentprocess för AI-relaterade händelser.

## Exempel från Tullverket Aurora

Tullverket Aurora vill produktionssätta ett RAG-baserat kunskapsstöd för handläggare. Systemet ska kunna svara på frågor om interna handböcker, styrdokument, publika regelverk och vissa processbeskrivningar. I en senare fas vill verksamheten även kunna använda ärenderelaterade dokument.

Arkitekturteamet delar upp lösningen i två etapper.

### Etapp 1: kunskapsstöd för lågkänsligt material

I första etappen får lösningen använda:

- publika regelverk,
- interna men ej sekretessklassade handböcker,
- godkända processbeskrivningar,
- styrdokument som informationsägare har godkänt för indexering.

Säkerhetsarkitekturen innehåller:

- inloggning med myndighetens identitetslösning,
- rollbaserad åtkomst till användargränssnittet,
- dokumentindex med metadata om ägare och informationsklass,
- AI-gateway med godkända modeller,
- promptmall som kräver källhänvisningar,
- loggning av modellversion, promptmall, dokumentreferenser och policybeslut,
- spärr mot att användaren laddar upp egna dokument i produktionsmiljön,
- användargränssnitt som tydligt markerar att svaret är stöd, inte beslut.

Denna etapp får köras i en kontrollerad molnmiljö eftersom informationsklassen är låg och avtalsvillkoren förbjuder träning på myndighetens data.

### Etapp 2: handläggarstöd med ärendenära information

I andra etappen vill verksamheten inkludera ärendenära dokument. Arkitekturteamet bedömer att detta kräver en annan säkerhetsnivå.

Nya krav införs:

- separata index per informationsklass,
- behörighetsfiltrering innan retrieval,
- strängare loggskydd,
- avskild driftmiljö,
- begränsning av vilka användare som får använda funktionen,
- obligatorisk källhänvisning,
- mänsklig granskning innan information används i formella beslut,
- testsvit för indirekt prompt injection,
- tydligt stopp för verktygsanrop mot ärendesystem i denna etapp.

Beslutet blir att inte bara “utöka” den första lösningen. I stället etablerar Aurora en skyddad AI-zon med striktare krav. Det gör att myndigheten kan återanvända vissa byggblock, men ändå hålla risknivåerna isär.

## Säkerhetskrav för RAG-baserat kunskapsstöd

Ett RAG-baserat kunskapsstöd är ofta ett bra första produktionsspår, men det kräver tydliga säkerhetskrav.

### Krav på dokumentintag

Dokumentintag bör styras av informationsägare och tekniska kontroller.

Krav:

- endast godkända dokumentkällor får indexeras,
- varje dokument ska ha ägare, informationsklass och livscykelstatus,
- dokument med oklar klassning ska inte indexeras,
- behörigheter ska följa med från källsystem eller sättas explicit,
- indexering ska loggas,
- gamla dokument ska kunna tas bort eller ersättas,
- dokument som innehåller instruktioner till modellen ska flaggas eller hanteras särskilt.

### Krav på retrieval

Retrieval-lagret ska inte bara hitta relevanta dokument. Det ska också skydda åtkomst.

Krav:

- sökresultat filtreras efter användarens behörighet,
- informationsklass styr vilka index som får användas,
- retrieval-resultat loggas på referensnivå,
- kontextmängden begränsas,
- källor visas för användaren,
- systemet ska kunna förklara vilka dokument svaret bygger på.

### Krav på modellanrop

Modellanrop ska gå genom kontrollerade gränssnitt.

Krav:

- endast godkända modeller får användas,
- modellversion ska loggas,
- data får inte användas för leverantörens modellträning om inte särskilt beslutat,
- prompt och kontext ska hanteras enligt informationsklass,
- externa modell-API:er ska bara användas för tillåtna dataklasser,
- fallback till annan modell får inte ske utan arkitekturbeslut.

### Krav på svar

Svar från modellen ska utformas för att minska risken för övertillit och felanvändning.

Krav:

- svar ska visa källor när det är möjligt,
- svar ska markera osäkerhet,
- systemet ska undvika kategoriska formuleringar när underlaget är svagt,
- svaret ska inte presenteras som myndighetsbeslut,
- känsliga uppgifter ska inte återges i onödan,
- användaren ska få vägledning om när man måste kontrollera originalkälla.

## Säkerhetsarkitektur för agentliknande lösningar

Agentliknande AI-lösningar innebär att modellen inte bara svarar, utan också planerar steg, väljer verktyg och utför åtgärder. För myndigheter bör sådana lösningar införas med stor försiktighet.

En säkerhetsarkitektur för agenter bör innehålla:

- tydlig avgränsning av agentens uppdrag,
- minsta möjliga verktygsuppsättning,
- separata behörigheter per verktyg,
- tvingande mänsklig bekräftelse för skrivande eller externa åtgärder,
- transaktionslogg,
- policybeslut före varje verktygsanrop,
- sandbox för fil- och kodoperationer,
- spärr mot obehörig kedjning av verktyg,
- tids- och kostnadsgränser,
- incidentfunktion som snabbt kan pausa agenten.

För Tullverket Aurora innebär detta att en agent som sammanställer ett internt beslutsunderlag kan vara acceptabel om den bara läser godkända källor och skapar ett utkast. En agent som själv uppdaterar ärendesystem, skickar meddelanden eller påverkar kontrollprioritering kräver betydligt starkare styrning och bör inte vara ett första steg.

## AI-gateway som säkerhetskomponent

En AI-gateway kan vara ett centralt byggblock i målarkitekturen. Den kan fungera som kontrollerad passage mellan applikationer och modeller.

Typiska ansvar för en AI-gateway:

- dirigera anrop till godkända modeller,
- tillämpa policy per användningsfall,
- logga modell, version och anropsmetadata,
- begränsa dataklasser per modell,
- tillämpa rate limits,
- filtrera eller flagga riskabla promptar,
- tillämpa output-kontroller,
- hantera kostnadskontroll,
- stödja byte av modell utan att applikationen byggs om.

AI-gatewayen ska inte ses som en magisk säkerhetsprodukt. Den är ett kontrollplan. Den måste kompletteras med behörighetsstyrning, dataarkitektur, säkerhetszoner, testning och incidenthantering.

## Guardrails och content filtering

Guardrails är regler, kontroller eller mekanismer som begränsar vad AI-lösningen får göra eller svara. Content filtering är en typ av guardrail, men begreppet är bredare.

Exempel på guardrails:

- ämnesbegränsning,
- spärr mot vissa dataklasser,
- krav på källhänvisning,
- formatkrav för svar,
- blockering av otillåtna verktygsanrop,
- mänsklig granskning,
- svarsmallar,
- policybeslut baserat på användarroll,
- detektion av prompt injection,
- stopp vid låg tillförlitlighet.

Guardrails bör dokumenteras som arkitekturbeslut. Det ska framgå vilken risk de adresserar, var de ligger i kedjan, hur de testas och vad som händer om de misslyckas.

## Red teaming och säkerhetstestning

AI-säkerhet kräver testning som liknar traditionell penetrationstestning, men med AI-specifika scenarier.

Testningen bör omfatta:

- direkt prompt injection,
- indirekt prompt injection via dokument,
- försök att få modellen att avslöja systeminstruktioner,
- försök att komma åt dokument utan behörighet,
- manipulation av retrieval-resultat,
- försök att få modellen att anropa fel verktyg,
- försök att kringgå content filters,
- test av hallucination i kritiska frågor,
- test av loggning och spårbarhet,
- test av incidentrutiner.

För myndigheten bör dessa tester inte vara engångsaktiviteter. De bör kopplas till releaseprocessen, modelluppdateringar, nya dokumentkällor, nya verktyg och större ändringar i promptmallar.

## Observability för AI-säkerhet

Observability i AI-miljö handlar inte bara om CPU, minne, svarstid och felkoder. Arkitekturen behöver även observera modell- och beteendenivå.

Exempel på signaler:

- ovanliga promptmönster,
- plötsligt ökad användning,
- hög andel blockerade anrop,
- ovanligt många svar utan källor,
- många retrieval-träffar från oväntade datakällor,
- verktygsanrop som avviker från normalt beteende,
- ökade kostnader,
- återkommande användarrapporter om felaktiga svar,
- förändrat svarsbeteende efter modelluppdatering.

Dessa signaler bör kopplas till säkerhetsövervakning och förvaltning. Vissa signaler hör hemma i SOC-flöden. Andra hör hemma hos produktteamet, modellansvarig eller informationsägare.

## Arkitekturbeslut: säkerhetszoner för AI

Ett av de viktigaste besluten i målarkitekturen är hur AI-lösningar delas in i säkerhetszoner. Utan zoner riskerar myndigheten att antingen överkontrollera enkla användningsfall eller underkontrollera känsliga användningsfall.

En beslutsmatris kan se ut så här:

| Zon | Datatyp | Typiska användningsfall | Tillåten drift | Särskilda krav |
|---|---|---|---|---|
| Experimentzon | Testdata och öppna data | Utvärdering, prototyper | Kontrollerat moln eller lokal sandlåda | Ingen produktion, ingen verklig sekretessdata |
| Intern produktivitetszon | Lågkänsliga interna data | Sammanfattning, språkstöd, intern hjälp | Godkänd SaaS eller moln | Policy, loggning, användarutbildning |
| Kunskapsstödszon | Godkända dokument och regelverk | RAG, handböcker, styrdokument | Moln, hybrid eller privat drift | Källhänvisning, dokumentägare, behörighetsfilter |
| Skyddad verksamhetszon | Känsliga ärendedata | Handläggarstöd, analysstöd | Hybrid, privat moln eller on-premises | Stark åtkomstkontroll, avskild loggning, mänsklig granskning |
| Kritisk zon | Högt skyddsvärda data eller beslutspåverkan | Operativ prioritering, högriskbeslut | Normalt avskild eller on-premises | Förstärkt riskanalys, revision, red teaming, formella beslutspunkter |

Matrisen är inte ett facit. Den är ett sätt att göra risknivåer synliga i målarkitekturen.

## Vägvalsfrågor

När säkerhetsarkitekturen tas fram bör arkitekten ställa följande frågor:

- Vilka dataklasser får AI-lösningen hantera?
- Vilka användare får använda lösningen?
- Vilka dokument får indexeras?
- Följer behörigheter med från källsystem till retrieval?
- Kan modellen se information som användaren inte får se?
- Kan modellen anropa verktyg?
- Är verktygsanrop läsande eller skrivande?
- Krävs mänsklig bekräftelse?
- Var lagras promptar, svar och retrieval-resultat?
- Kan loggarna i sig innehålla sekretessreglerad information?
- Vilka modeller är godkända för detta användningsfall?
- Får leverantören använda data för träning eller förbättring?
- Hur upptäcks prompt injection?
- Hur testas indirekt prompt injection?
- Hur stoppas en AI-funktion vid incident?
- Vem äger risken efter produktionssättning?

## Vanliga fallgropar

- **Misstag: Att behandla AI-lösningen som en vanlig webbapplikation.**
  - Varför det händer: Många byggblock är bekanta, till exempel API:er, identitet, loggning och datalager.
  - Hur det undviks: Lägg till AI-specifik hotmodellering för promptar, retrieval, modellutdata och verktygsanrop.

- **Misstag: Att låta modellen se mer information än användaren.**
  - Varför det händer: Retrieval byggs med tekniskt servicekonto som har bred åtkomst.
  - Hur det undviks: Inför behörighetsfiltrering före kontext skickas till modellen.

- **Misstag: Att lita för mycket på promptinstruktioner.**
  - Varför det händer: Det är enkelt att skriva “du får inte avslöja känslig information” i systemprompten.
  - Hur det undviks: Kombinera promptregler med tekniska kontroller, dataminimering, output-validering och åtkomstkontroll.

- **Misstag: Att logga allt utan att klassificera loggarna.**
  - Varför det händer: Drift och felsökning behöver spårbarhet.
  - Hur det undviks: Bestäm loggpolicy per informationsklass och maska eller begränsa prompt- och svardata.

- **Misstag: Att införa agentfunktioner för tidigt.**
  - Varför det händer: Agentfunktioner ger snabb demonstrationseffekt.
  - Hur det undviks: Börja med läsande och förslagsgenererande funktioner. Kräv särskilt beslut för skrivande eller externa åtgärder.

- **Misstag: Att blanda experiment och produktion.**
  - Varför det händer: En lyckad pilot får snabbt fler användare.
  - Hur det undviks: Ha separata zoner, tydliga produktionskriterier och stopp för verklig känslig data i experimentmiljöer.

## Checklista för säkerhetsarkitektur

### Minimikrav före produktion

- Användningsfallet är juridiskt och säkerhetsmässigt triagerat.
- Informationsklassning är genomförd.
- Tillåtna datakällor är dokumenterade.
- Modell och driftmiljö är godkända för aktuell dataklass.
- Användarens behörighet styr retrieval.
- Promptar, svar och loggar har definierad skyddsnivå.
- AI-gateway eller motsvarande kontrollpunkt används.
- Guardrails är dokumenterade och testade.
- Output-validering finns för riskfyllda svar.
- Verktygsanrop är avstängda eller strikt kontrollerade.
- Incidentrutin finns.
- Ansvarig produktägare, informationsägare och teknisk ägare är utsedda.

### Förstärkta krav för känsliga användningsfall

- Separat säkerhetszon används.
- Red teaming är genomförd.
- Indirekt prompt injection har testats.
- Modell- och promptversioner är spårbara.
- Loggar är åtkomstbegränsade och gallringsstyrda.
- Mänsklig granskning krävs före beslut eller externa åtgärder.
- Leverantörens databehandling är granskad.
- Exit- och avvecklingsplan finns.
- Förändringar i modell, datakälla eller promptmall kräver godkänd ändringsprocess.

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Säkerhetsarkitekturen ska synas i målarkitekturen på flera nivåer.

I förmågekartan bör det finnas förmågor för:

- AI-riskbedömning,
- AI-säkerhetstestning,
- modell- och promptgranskning,
- incidenthantering,
- säkerhetsövervakning,
- leverantörs- och modellkontroll.

I den tekniska referensarkitekturen bör det finnas byggblock för:

- identitet och behörighet,
- AI-gateway,
- policy enforcement,
- retrieval-filter,
- loggning och observability,
- guardrails,
- säkra integrationsmönster,
- säkerhetszoner.

I beslutsloggen bör det finnas beslut om:

- vilka AI-zoner som används,
- vilka dataklasser som får gå till vilka modeller,
- om RAG får användas för ärendenära information,
- om verktygsanrop tillåts,
- om drift sker i moln, hybrid eller on-premises,
- vilken loggningsnivå som gäller,
- vilken incidentmodell som används.


## Snabb sammanfattning

- AI-säkerhet handlar om hela kedjan: användare, data, promptar, retrieval, modell, verktyg, output, loggar och drift.
- Prompt injection och indirekt prompt injection gör att hämtad kontext måste behandlas som opålitlig data, inte som instruktion.
- Data leakage kan ske via promptar, retrieval, modellutdata, loggar, leverantörskedjan och verktygsanrop.
- Agentliknande lösningar kräver särskild försiktighet eftersom modellen kan initiera åtgärder.
- Säkerhetsarkitekturen bör byggas i lager: policy, identitet, dataskydd, kontextkontroll, isolering, verktygskontroll, output-validering, loggning och incidenthantering.
- AI-gateway och guardrails är viktiga kontrollpunkter, men de ersätter inte informationsklassning, behörighetsstyrning och säkerhetszoner.
- För en myndighet bör känsliga AI-användningsfall placeras i särskilda zoner med förstärkt kontroll, spårbarhet och mänsklig granskning.

## Nästa steg

Nästa kapitel behandlar upphandling och leverantörsstyrning. Säkerhetsarkitekturen behöver då översättas till krav: datalokalisering, modellvillkor, revisionsrätt, exitstrategi, loggning, SLA, underbiträden, öppenhet och möjlighet att byta komponenter utan att målarkitekturen låses till en enskild leverantör.
