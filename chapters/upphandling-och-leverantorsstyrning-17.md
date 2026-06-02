# Kapitel 17: Upphandling och leverantörsstyrning

## Varför detta kapitel finns

AI-förmåga i en statlig myndighet etableras sällan enbart med interna resurser. Även när myndigheten bygger egna lösningar används normalt externa komponenter: molnplattformar, modell-API:er, open source-modeller, vektordatabaser, RAG-ramverk, säkerhetsverktyg, observability-tjänster, konsultstöd, driftstöd och färdiga AI-assistenter. Därför är upphandling och leverantörsstyrning inte en administrativ eftertanke. De är en del av målarkitekturen.

För en erfaren IT-arkitekt innebär detta att tekniska vägval måste kunna översättas till anskaffningsstrategi, avtalskrav, kontrollpunkter och exitmöjligheter. En arkitektur som bara fungerar med en leverantör, en hemlig modell, oklara datavillkor och svaga revisionsrättigheter är inte en robust målarkitektur för offentlig sektor. Den kan skapa snabb initial nytta, men också långvarig inlåsning, otydligt ansvar och risker som blir svåra att korrigera när lösningen väl är införd.

Kapitlet beskriver hur upphandling och leverantörsstyrning bör integreras i AI-målarkitekturen. Fokus ligger på vad arkitekten behöver säkra innan myndigheten köper, avropar, inför eller förvaltar AI-relaterade produkter och tjänster.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför upphandling är ett arkitekturdrivande område för AI,
- skilja mellan anskaffningsstrategi, kravställning, avtal och löpande leverantörsstyrning,
- formulera arkitekturrelevanta krav på AI-leverantörer,
- bedöma risker kopplade till datalagring, modellvillkor, underleverantörer, transparens och inlåsning,
- koppla informationsklassning och driftmodell till upphandlingskrav,
- utforma en exitstrategi för AI-plattformar och AI-tjänster,
- använda Tullverket Auroras scenario för att resonera om när färdiga tjänster, ramavtal, egen upphandling eller intern utveckling är lämpligt.

## Innan vi börjar

Detta kapitel bygger på tidigare kapitel om juridik, informationsklassning, arkitekturprinciper, governance, teknisk referensarkitektur, plattformsval, vägval och säkerhetsarkitektur. Upphandling ska inte ersätta dessa delar. Den ska operationalisera dem.

Om myndigheten inte vet vilka data som ska behandlas, vilken risknivå användningsfallet har, vilken driftmodell som krävs eller vilka kontroller som behövs, går det inte att kravställa en AI-tjänst på ett hållbart sätt. Då blir upphandlingen lätt en produktjämförelse i stället för ett styrt arkitekturval.

## Upphandling som arkitekturfråga

I traditionella IT-projekt kan upphandling ibland behandlas som ett senare steg: verksamheten beskriver behovet, arkitekten beskriver lösningen och inköpsfunktionen hanterar anskaffningen. För AI är denna sekvens ofta för enkel.

AI-tjänster påverkar flera arkitekturdomäner samtidigt:

- dataarkitektur,
- integrationsarkitektur,
- säkerhetsarkitektur,
- informationsförvaltning,
- identitet och åtkomst,
- drift och observability,
- juridik och regelefterlevnad,
- leverantörsekosystem,
- kostnadsmodell,
- kompetensförsörjning,
- förvaltningsmodell.

Därför behöver upphandling komma in tidigt. Redan när Tullverket Aurora prioriterar sina AI-användningsfall bör myndigheten fråga:

- Kräver användningsfallet en extern AI-tjänst?
- Finns relevant ramavtal eller befintligt avtal?
- Kan behovet lösas med en redan godkänd plattform?
- Måste myndigheten göra en ny upphandling?
- Behöver upphandlingen omfatta både produkt, införande och förvaltning?
- Behöver avtalet reglera modellträning, loggar, underleverantörer och datalokalisering?
- Behöver lösningen kunna flyttas till annan driftmiljö senare?

Om dessa frågor kommer för sent kan målarkitekturen bli beroende av villkor som aldrig förankrats i avtal.

Anskaffning av generativ AI bör utgå från verksamhetens behov, befintliga avtal där de räcker och reglerna för offentlig upphandling. Licens- och avtalsvillkor behöver bedömas före användning, inte först när piloten redan är igång.

## Anskaffningsstrategi före produktval

Ett vanligt misstag är att börja med produktlistan: vilka AI-plattformar finns, vilken vektordatabas är bäst, vilken molnleverantör har bäst modellutbud och vilket RAG-ramverk är mest populärt? För en statlig myndighet bör ordningen vara en annan.

Först behöver myndigheten välja anskaffningsstrategi. Den kan omfatta flera spår samtidigt:

| Anskaffningsspår | När det passar | Arkitekturrisk |
|---|---|---|
| Befintligt avtal eller ramavtal | När behovet ryms inom redan godkända villkor och risknivån är låg till medel | Avtalet kan sakna AI-specifika villkor |
| Färdig SaaS-tjänst | När användningsfallet är standardiserat och data inte är för känslig | Begränsad kontroll över data, modell och loggar |
| Hyperscalerbaserad plattform | När myndigheten behöver brett tjänsteutbud, skalning och integrationsmöjligheter | Leverantörsberoende och komplex kostnadsstyrning |
| Europeisk eller suverän molntjänst | När datalokalisering, jurisdiktion och kontroll väger tungt | Begränsat tjänsteutbud eller mognad kan påverka tempo |
| Egen plattform med open source-komponenter | När kontroll, isolering eller särskilda säkerhetskrav väger tungt | Högre krav på intern kompetens och livscykelhantering |
| Konsultstöd för införande | När myndigheten behöver kapacitet och specialistkunskap | Risk för kunskapsberoende och svag intern förmåga |
| Intern utveckling ovanpå gemensam plattform | När myndigheten vill äga verksamhetslogiken och undvika produktinlåsning | Kräver produktteam, plattformsförmåga och förvaltning |

Poängen är inte att välja ett spår för hela myndigheten. Målarkitekturen bör definiera vilka spår som är tillåtna för olika risknivåer och användningsfall.

## Tullverket Aurora: tre anskaffningssituationer

Tullverket Aurora har tre aktuella AI-behov.

Det första är ett internt skriv- och sammanfattningsstöd för administrativ personal. Användningen gäller icke sekretessbelagda dokument och generellt kontorsarbete. Här kan ett befintligt avtal eller en färdig SaaS-lösning vara rimlig, förutsatt att användningspolicy, dataskydd, loggning och villkor är kontrollerade.

Det andra är ett RAG-baserat kunskapsstöd för handläggare som ska söka i interna regelverk, styrdokument och handböcker. Här behöver myndigheten kontrollera datakällor, åtkomst, källhänvisningar, loggar och driftmiljö. En färdig assistent kan vara för begränsad om den inte kan följa myndighetens behörighetsmodell och informationsklassning.

Det tredje är ett analysstöd för riskbedömning i kontrollverksamheten. Det kan påverka prioriteringar, resursfördelning och i förlängningen enskilda aktörer. Här krävs starkare styrning, tydlig ansvarskedja, validering, spårbarhet, modellstyrning och ofta mer kontrollerad drift. Anskaffningen behöver då omfatta inte bara teknik, utan även krav på dokumentation, testbarhet, revision, incidenthantering och modellförvaltning.

Samma myndighet kan alltså behöva tre olika anskaffningsmönster. Det är därför målarkitekturen måste vara flerspårig.

## Kravställning som arkitekturartefakt

Krav på AI-leverantörer bör inte bara skrivas i upphandlingsdokument. De bör härledas från målarkitekturen och kunna spåras tillbaka till principer, riskklassning och arkitekturbeslut.

En praktisk modell är att dela in krav i sju grupper.

### Funktionella krav

Funktionella krav beskriver vad tjänsten ska kunna göra. För AI räcker det inte att skriva att systemet ska “använda generativ AI” eller “ha stöd för chatbot”. Kraven behöver vara kopplade till användningsfall.

Exempel:

- Tjänsten ska kunna besvara frågor med källhänvisningar till godkända dokumentkällor.
- Tjänsten ska kunna sammanfatta dokument utan att lagra innehållet för modellträning.
- Tjänsten ska kunna hantera separata kunskapsbaser för olika verksamhetsområden.
- Tjänsten ska kunna visa vilka dokument eller datakällor som använts som kontext.
- Tjänsten ska kunna begränsa användning utifrån roll, behörighet och informationsklass.

### Datakrav

Datakraven är ofta de viktigaste AI-kraven. De bör reglera vilken data leverantören får behandla, var den får lagras, hur den får användas och hur länge den får sparas.

Frågor att kravställa:

- Får kunddata användas för träning eller förbättring av leverantörens modeller?
- Var lagras promptar, filer, embeddings, loggar och modellutdata?
- Vilka underleverantörer behandlar data?
- Kan myndigheten styra retention för loggar och konversationer?
- Kan data raderas på begäran och vid avtalets slut?
- Kan data exporteras i öppna eller dokumenterade format?
- Kan leverantören separera myndighetens data från andra kunders data?
- Stödjer tjänsten dataminimering och separata miljöer för olika informationsklasser?

### Säkerhetskrav

Säkerhetskrav ska koppla till säkerhetsarkitekturen från kapitel 16.

Exempel:

- stöd för federerad identitet och stark autentisering,
- roll- och attributbaserad åtkomstkontroll,
- separering mellan test, pilot och produktion,
- kryptering i vila och under överföring,
- sekretesshantering för loggar och promptar,
- skydd mot prompt injection och otillåten verktygsanvändning,
- stöd för säkerhetsloggning och integration med SIEM,
- incidentrapportering med tydliga tidskrav,
- möjlighet till penetrationstest eller oberoende säkerhetsgranskning,
- dokumenterad hantering av sårbarheter och patchning.

### Transparens- och dokumentationskrav

AI kräver mer transparens än många traditionella IT-tjänster. Myndigheten behöver förstå vad tjänsten gör, vilka begränsningar den har och hur den kan granskas.

Krav kan omfatta:

- beskrivning av modelltyp och modellversion,
- dokumentation av kända begränsningar,
- information om träningsdata på den nivå leverantören kan lämna,
- dokumentation av dataflöden och underleverantörer,
- redovisning av logik för retrieval, ranking och filtrering,
- stöd för källhänvisning och spårbarhet,
- dokumenterad förändringshantering när modeller, funktioner eller villkor ändras,
- rapportering av större modelluppdateringar som kan påverka resultat.

### Livscykel- och förvaltningskrav

AI-lösningar förändras över tid. Modeller uppdateras, tjänster får nya funktioner, leverantörer byter underleverantörer och användningsmönster förändras. Därför måste avtalet reglera livscykeln.

Exempel:

- versionering av modeller och API:er,
- möjlighet att låsa eller välja modellversion där det behövs,
- testmiljö före produktionsändringar,
- förändringsmeddelanden i god tid,
- bakåtkompatibilitet eller migreringsstöd,
- mätvärden för kvalitet, tillgänglighet, svarstid och fel,
- process för incidenter, avvikelser och avstängning av funktioner,
- krav på avveckling och dataradering.

### Rättsliga och avtalsmässiga krav

Rättsliga krav behöver anpassas till användningsfall, data och leverantörsroll. Det kan gälla personuppgiftsbiträdesavtal, sekretess, AI Act-relaterade roller, upphovsrätt, informationssäkerhet, revision och ansvar.

Arkitekten ska inte ensam formulera dessa krav, men behöver säkerställa att de tekniska och arkitekturella konsekvenserna blir synliga.

Exempel:

- tydlig rollfördelning mellan myndighet och leverantör,
- reglering av personuppgiftsbehandling,
- sekretesskrav och åtkomstbegränsning,
- rätt till revision eller motsvarande kontrollmekanismer,
- krav på underleverantörslista och förändringsprocess,
- ansvar vid felaktig behandling, säkerhetsincidenter eller otillåtna förändringar,
- regler för immateriella rättigheter till konfigurationer, promptmallar, kod och anpassningar,
- regler för användning av myndighetens material i leverantörens produktutveckling.

### Exit- och portabilitetskrav

Exit är särskilt viktigt för AI eftersom inlåsning kan uppstå på många nivåer:

- modell-API:er,
- embeddings,
- vektordatabaser,
- promptmallar,
- agenter,
- integrationer,
- loggformat,
- träningsdata,
- utvärderingsdata,
- användarhistorik,
- metadata,
- policykonfigurationer.

Exitkrav bör därför inte begränsas till “data ska kunna exporteras”. Myndigheten behöver veta vad som krävs för att flytta eller ersätta lösningen.

Exempel:

- export av dokument, metadata, indexkonfiguration och promptmallar,
- dokumenterade API:er,
- möjlighet att återskapa embeddings eller byta embeddingmodell,
- separering mellan verksamhetslogik och leverantörsspecifik runtime,
- rätt att behålla egenutvecklade konfigurationer och kod,
- stöd för stegvis migrering,
- avvecklingsplan vid avtalets slut.

Krav på datalokalisering, underbiträden, loggning, revision, informationssäkerhet, modellvillkor, transparens, exit och förändringshantering ska spåras från användningsfall och informationsklassning till avtal och förvaltning. De är arkitekturkrav, inte enbart juridiska bilagor.

## AI Act, GDPR och offentlig upphandling

AI Act och GDPR påverkar inte bara användningen av AI. De påverkar också vad myndigheten behöver kräva av leverantörer. Om myndigheten använder ett AI-system i en roll där den blir deployer, måste den kunna uppfylla sina skyldigheter i praktiken. Det kräver tillgång till information, dokumentation, loggar, instruktioner och stöd från leverantören. Om leverantören däremot är provider av ett AI-system behöver myndigheten förstå vilka skyldigheter leverantören har och vilka bevis eller dokument som bör efterfrågas.

GDPR innebär att personuppgifter inte får bli en otydlig restpost i AI-avtalet. Personuppgiftsbehandling kan förekomma i promptar, uppladdade dokument, loggar, embeddings, testdata, supportärenden och modellutdata. Myndigheten behöver därför veta var personuppgifter förekommer, varför de behandlas, vem som behandlar dem och hur länge de sparas.

För offentlig upphandling innebär detta att AI-krav måste vara tydliga, proportionerliga och kopplade till behovet. Myndigheten bör inte kravställa specifika tekniska produkter utan skäl, men den måste kunna ställa krav på säkerhet, dataskydd, spårbarhet, dokumentation, kontroll och interoperabilitet.

I praktiken bör arkitekten, upphandlingsfunktionen, jurist, dataskyddsombud och informationssäkerhetsfunktion arbeta tillsammans redan före kravspecifikationen.

## Leverantörens AI-villkor måste granskas

AI-tjänster har ofta särskilda villkor som skiljer sig från traditionella IT-tjänster. Dessa villkor kan finnas i huvudavtalet, databehandlingsavtalet, produktvillkor, tjänstebeskrivningar, onlinevillkor, API-villkor eller dokumentation.

Tullverket Aurora inför därför en regel: ingen AI-tjänst får användas i pilot eller produktion innan AI-specifika villkor har granskats.

Granskningen omfattar minst:

- om kunddata används för träning,
- om promptar och svar lagras,
- om leverantören har rätt att analysera användning,
- vilka modeller som används,
- om modeller eller regioner kan ändras ensidigt,
- vilka underleverantörer som används,
- var data behandlas,
- vilka supportfunktioner som kan få åtkomst,
- hur incidenter rapporteras,
- hur loggar kan exporteras eller raderas,
- om myndigheten kan begränsa funktioner,
- vad som händer när avtalet upphör.

Det är inte ovanligt att en tjänst som verkar acceptabel i användargränssnittet har villkor som är olämpliga för myndighetsdata. Arkitektens roll är att se till att sådana villkor upptäcks innan tjänsten blir en del av målarkitekturen.

## Underleverantörer och leverantörskedja

AI-leverantörer använder ofta egna underleverantörer. En SaaS-assistent kan bygga på en molnplattform, en extern modellleverantör, ett separat analyslager, supportverktyg och loggningstjänster. En konsultleverans kan använda open source-komponenter, modell-API:er och färdiga ramverk.

Målarkitekturen bör därför innehålla krav på leverantörskedjans synlighet.

Minimikrav:

- aktuell lista över relevanta underleverantörer,
- beskrivning av vilken data varje underleverantör behandlar,
- geografisk placering för behandling och lagring,
- process för att informera om nya underleverantörer,
- möjlighet att invända mot väsentliga förändringar,
- krav på att säkerhets- och dataskyddskrav följer med i kedjan,
- ansvarsfördelning vid incidenter.

För Tullverket Aurora är detta särskilt viktigt i känsliga användningsfall. Om ett RAG-baserat handläggarstöd behandlar interna regelverk och ärenderelaterad information kan myndigheten inte nöja sig med att huvudleverantören säger att “tjänsten är säker”. Den måste förstå leverantörskedjan tillräckligt väl för att bedöma risk.

## Inlåsning på flera nivåer

Leverantörsinlåsning i AI är bredare än traditionell applikationsinlåsning. En myndighet kan bli beroende av:

- en specifik modell,
- ett specifikt promptformat,
- en specifik embeddingmodell,
- en specifik vektordatabas,
- ett proprietärt agentramverk,
- leverantörens säkerhetslager,
- leverantörens loggformat,
- leverantörens observability-lösning,
- leverantörens sätt att hantera källhänvisningar,
- konsultens odokumenterade kod och konfiguration.

Det går inte alltid att undvika inlåsning. Ibland är beroende acceptabelt om nyttan är stor och risken låg. Men beroendet måste vara medvetet, dokumenterat och styrt.

En praktisk regel är att målarkitekturen ska skilja mellan tre typer av inlåsning:

| Typ av inlåsning | Exempel | Rekommenderad hantering |
|---|---|---|
| Acceptabel inlåsning | Standardiserad kontorsnära AI-tjänst med låg informationsrisk | Dokumentera beroende och följ upp villkor |
| Hanterbar inlåsning | RAG-plattform där data och konfiguration kan exporteras | Kräv portabilitet, API:er och exitplan |
| Kritisk inlåsning | Verksamhetskritisk AI-lösning utan export, insyn eller alternativ drift | Undvik eller kräva omarkitektur före produktion |

## Konsultberoende och kunskapsöverföring

Många myndigheter kommer att behöva konsultstöd för att etablera AI-förmåga. Det kan vara rimligt, särskilt i tidiga faser. Men konsultstöd får inte bli en ersättning för intern arkitektur- och förvaltningsförmåga.

Krav på konsultleveranser bör därför omfatta:

- dokumenterad arkitektur,
- dokumenterade arkitekturbeslut,
- överlämning av kod och konfiguration,
- testfall och utvärderingsdata,
- drift- och förvaltningsinstruktioner,
- utbildning av interna roller,
- gemensamt arbete med myndighetens arkitekturfunktion,
- krav på att lösningar följer myndighetens referensarkitektur.

Tullverket Aurora inför en princip: konsulten får accelerera införandet, men inte äga förmågan. Det betyder att myndigheten måste kunna förstå, förvalta, vidareutveckla och avveckla lösningen även efter konsultuppdragets slut.

## Kontroll före pilot och produktion

Upphandling och leverantörsstyrning behöver kopplas till kontrollpunkterna i AI-livscykeln. En AI-tjänst bör inte gå från inköp till fri användning utan arkitekturgranskning.

Före pilot bör myndigheten kontrollera:

- att användningsfallet är beskrivet,
- att informationsklassning är gjord,
- att personuppgiftsfrågor är bedömda,
- att avtalsvillkor tillåter avsedd användning,
- att data inte används för otillåten träning,
- att loggning och retention är förstådda,
- att användarna får tydliga instruktioner,
- att pilotens gränser är dokumenterade,
- att resultat inte används som automatiskt beslut utan särskilt beslut.

Före produktion bör myndigheten dessutom kontrollera:

- att leverantörskrav är uppfyllda,
- att säkerhetskrav är verifierade,
- att incidentprocess är etablerad,
- att ansvar och förvaltning är beslutade,
- att exitplan finns,
- att övervakning och mätning är på plats,
- att ändringshantering är reglerad,
- att användarstöd och utbildning finns,
- att arkitekturbeslut är dokumenterade.

## Leverantörsstyrning efter införande

AI-leverantörsstyrning är inte färdig när avtalet är undertecknat. Tjänsten förändras över tid. Leverantören kan byta modell, införa nya funktioner, justera villkor, ändra regioner, byta underleverantör eller ändra hur loggar behandlas.

Därför behöver myndigheten etablera återkommande uppföljning.

Exempel på uppföljningspunkter:

- ändringar i tjänstevillkor,
- nya eller ändrade underleverantörer,
- modelluppdateringar,
- säkerhetsincidenter,
- avvikelser från SLA,
- användningsvolymer och kostnader,
- kvalitet och felmönster,
- klagomål eller incidenter från verksamheten,
- förändringar i dataskyddsbedömning,
- nya regulatoriska krav,
- behov av omklassning eller omarkitektur.

För Tullverket Aurora rapporterar större AI-leverantörer regelbundet till ett kombinerat forum för leverantörsstyrning, arkitektur och informationssäkerhet. Syftet är att undvika att avtalsuppföljning blir en ren inköpsfråga. AI-tjänsten är en del av myndighetens operativa arkitektur.

## Kostnadsstyrning och konsumtionsmodeller

AI-tjänster har ofta andra kostnadsmodeller än traditionella system. Kostnaden kan bero på antal användare, antal tokens, modelltyp, API-anrop, vektorindex, lagring, dokumentvolym, inferenstid, GPU-resurser, loggning, säkerhetsfunktioner och supportnivå.

Det kan skapa oväntade kostnadsrisker. En lyckad AI-tjänst kan bli dyr just för att den används mycket. En ineffektiv promptkedja kan skapa höga tokenkostnader. Ett RAG-flöde kan bli dyrt om det hämtar för mycket kontext. En agentlösning kan skapa många API-anrop bakom varje användarfråga.

Arkitekturen bör därför omfatta kostnadskontroller:

- budget per miljö och användningsfall,
- mätning per team, tjänst och modell,
- begränsning av dyra modeller till relevanta användningsfall,
- caching där det är lämpligt,
- maxgränser för promptstorlek och kontext,
- uppföljning av tokenförbrukning,
- larm vid avvikande konsumtion,
- regelbunden kostnadsoptimering.

Kostnadsstyrning är inte bara ekonomi. Den påverkar arkitekturval. Ett användningsfall som verkar tekniskt rimligt kan vara olämpligt om kostnaden per ärende blir för hög.

## Krav på öppna gränssnitt och dokumenterade integrationer

AI-målarkitekturen bör undvika att verksamhetslogik byggs in i oåtkomliga produktlager. Om en AI-tjänst hanterar promptmallar, retrieval-logik, källfiltrering, agentregler och policyer i proprietära konfigurationer som inte går att exportera, blir det svårt att styra och byta lösning.

Därför bör myndigheten efterfråga:

- dokumenterade API:er,
- export av konfiguration,
- tydliga format för promptmallar,
- dokumenterade integrationsmönster,
- stöd för standardiserad identitet,
- separering mellan data, modell och applikationslogik,
- möjlighet att integrera med myndighetens loggning och övervakning,
- möjlighet att använda externa utvärderings- och testverktyg.

Det betyder inte att varje komponent måste vara open source. Men myndigheten bör undvika svart låda där både data, logik och kontrollmekanismer sitter fast i samma produkt utan insyn.

## Upphandlingsunderlagets arkitekturbilagor

Ett upphandlingsunderlag för AI bör ofta kompletteras med arkitekturbilagor. Dessa gör kraven mer begripliga och minskar risken för att leverantörer svarar på fel nivå.

Exempel på bilagor:

- målarkitekturöversikt,
- klassning av användningsfall,
- informations- och datakrav,
- säkerhetskrav,
- integrationsprinciper,
- krav på identitet och åtkomst,
- logg- och observabilitykrav,
- krav på modell- och tjänstedokumentation,
- miljö- och driftmodell,
- exit- och portabilitetskrav,
- krav på förvaltningssamverkan.

Dessa bilagor bör inte beskriva en färdig produktlösning i onödan. De ska beskriva myndighetens styrande arkitekturkrav och de egenskaper lösningen måste uppfylla.

## Exempel från Tullverket Aurora

När Tullverket Aurora upphandlar stöd för generativ AI behöver kravställningen spegla målarkitekturen. Det räcker inte att fråga efter en chattfunktion. Myndigheten behöver krav på datalagring, logghantering, åtkomstkontroll, modellvillkor, underleverantörer, incidentrapportering, revision, portabilitet och möjlighet att avveckla eller byta leverantör.

I scenariot används upphandlingen som ett sätt att operationalisera arkitekturprinciperna: det som är viktigt i målarkitekturen måste synas i krav, avtal, uppföljning och exitplan.

## Vägvalsfrågor

När en myndighet ska anskaffa AI bör arkitekten kunna svara på följande frågor:

- Är detta ett standardiserat behov eller ett myndighetsspecifikt förmågebehov?
- Vilken informationsklass ska lösningen kunna hantera?
- Kommer personuppgifter, sekretess eller skyddsvärda verksamhetsdata att behandlas?
- Är leverantören provider, personuppgiftsbiträde, underleverantör eller endast teknisk tjänsteleverantör?
- Kan myndigheten uppfylla sina skyldigheter om leverantören inte lämnar mer information än i standardvillkoren?
- Behöver lösningen stödja flera modeller eller leverantörer?
- Kan data, konfiguration och loggar exporteras?
- Vad händer om leverantören ändrar modell, villkor eller region?
- Finns det ett realistiskt exitspår?
- Vilka delar måste myndigheten själv äga för att inte tappa AI-förmågan?

## Vanliga fallgropar

- **Fallgrop: Att köpa AI innan användningsfallet är klassat.**
  - Varför det händer: Produkten är lätt att testa och verksamheten vill snabbt komma igång.
  - Hur du undviker det: Kräv use-case triage, informationsklassning och avtalsgranskning före pilot.

- **Fallgrop: Att lita på generella säkerhetsintyg.**
  - Varför det händer: Leverantören presenterar certifieringar och standardtexter.
  - Hur du undviker det: Koppla kraven till myndighetens dataflöden, loggar, promptar, underleverantörer och driftmodell.

- **Fallgrop: Att missa att AI-villkor kan ändras.**
  - Varför det händer: Onlinevillkor och produktvillkor behandlas som statiska.
  - Hur du undviker det: Kräv förändringsmeddelanden, uppföljning och rätt att ompröva användningen.

- **Fallgrop: Att bygga verksamhetskritisk logik i en proprietär AI-studio.**
  - Varför det händer: Verktyget gör det snabbt att bygga prototyper.
  - Hur du undviker det: Dokumentera logik, kräv exportmöjligheter och separera verksamhetsregler från produktens interna format.

- **Fallgrop: Att upphandla konsultkapacitet men inte förmåga.**
  - Varför det händer: Myndigheten saknar initial kompetens och behöver extern hjälp.
  - Hur du undviker det: Kräv kunskapsöverföring, dokumentation, intern medverkan och förvaltningsbar leverans.

- **Fallgrop: Att sakna exitstrategi.**
  - Varför det händer: Fokus ligger på införande och pilotnytta.
  - Hur du undviker det: Kräv exitplan, exportformat, dokumenterade API:er och avvecklingsstöd redan i upphandlingen.

## Checklista för AI-upphandling

Före anskaffning bör myndigheten kontrollera:

- användningsfallet är beskrivet och prioriterat,
- informationsklassning är genomförd,
- personuppgiftsbehandling är bedömd,
- risknivå och driftmodell är dokumenterad,
- befintliga avtal och ramavtal är genomgångna,
- AI-specifika villkor är granskade,
- datalagring och datalokalisering är klarlagda,
- användning för modellträning är reglerad,
- underleverantörer är identifierade,
- loggning och retention är reglerade,
- säkerhetskrav är kopplade till målarkitekturen,
- transparens- och dokumentationskrav finns,
- livscykel- och ändringshantering är reglerad,
- kostnadsmodell och konsumtionsrisk är förstådda,
- exit- och portabilitetskrav finns,
- ansvarig för leverantörsstyrning är utsedd.

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Upphandling och leverantörsstyrning bör synas direkt i målarkitekturen. Det räcker inte att målarkitekturen visar tekniska byggblock. Den bör också visa hur externa beroenden styrs.

Målarkitekturen bör därför innehålla:

- tillåtna anskaffningsspår per risknivå,
- kravprinciper för AI-leverantörer,
- beslutsmodell för befintligt avtal, ramavtal, ny upphandling eller intern utveckling,
- regler för datalagring, träning, loggning och retention,
- krav på underleverantörssynlighet,
- krav på modell- och tjänstedokumentation,
- krav på exit och portabilitet,
- kontrollpunkter före pilot och produktion,
- modell för löpande leverantörsuppföljning.

När Tullverket Aurora går vidare mot en 24-månaders roadmap blir detta avgörande. Införandeplanen kan inte bara säga vilka tekniska komponenter som ska etableras. Den måste också ange när upphandling, avtalsgranskning, leverantörsstyrning och intern förmågeuppbyggnad ska ske.


## Snabb sammanfattning

AI-upphandling är inte bara inköp av teknik. För en större statlig myndighet är den ett sätt att omsätta målarkitekturens principer, riskbedömningar och driftmodeller i bindande krav och styrbar förvaltning.

De viktigaste frågorna är inte vilken produkt som har flest funktioner, utan om myndigheten kan kontrollera data, förstå leverantörskedjan, uppfylla juridiska skyldigheter, granska förändringar, hantera kostnader, undvika kritisk inlåsning och lämna lösningen om förutsättningarna förändras.

Tullverket Aurora använder därför upphandling som en del av AI-governance. Varje större AI-anskaffning kopplas till användningsfall, informationsklassning, arkitekturbeslut, säkerhetskrav, avtalsvillkor, exitstrategi och löpande leverantörsstyrning.

## Nästa steg

Nästa kapitel behandlar roadmapen från nuläge till etablerad AI-förmåga på 24 månader. Där blir upphandling och leverantörsstyrning en del av införandeplanen: vilka beslut, förmågor, avtal, plattformar och styrprocesser som behöver komma på plats i vilken ordning.
