# Kapitel 18: Roadmap från nuläge till etablerad AI-förmåga på 24 månader

## Varför detta kapitel finns

En målarkitektur får verklig betydelse först när den kan omsättas i en genomförbar införandeplan. För AI i en större statlig myndighet räcker det inte att beskriva ett önskat framtida läge med principer, byggblock, plattformar och styrmodeller. Myndigheten behöver också veta i vilken ordning förmågan ska etableras, vilka beslut som behöver fattas tidigt, vilka beroenden som måste hanteras och vilka delar som inte bör skalas innan kontrollen är tillräckligt mogen.

Detta kapitel beskriver en praktisk roadmap för de första 24 månaderna. Den är inte tänkt som en detaljerad projektplan med alla aktiviteter, datum och resursnamn. Den är en arkitekturell införandeplan som visar hur styrning, juridik, data, säkerhet, plattform, arbetssätt och användningsfall bör utvecklas tillsammans.

För en erfaren IT-arkitekt är huvudpoängen att AI-förmågan inte bör byggas i en linjär kedja där allt styrande arbete blir klart först och all teknik kommer sist. Samtidigt bör tekniken inte rusa före juridik, informationsklassning och säkerhetsarkitektur. En hållbar roadmap kombinerar kontrollerad parallellitet med tydliga beslutspunkter.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva varför en AI-roadmap behöver omfatta både styrning, teknik, organisation och användningsfall,
- dela upp etableringen av AI-förmåga i rimliga faser,
- skilja mellan experiment, sandlåda, pilot, produktionssättning och skalad förvaltning,
- identifiera vilka arkitekturbeslut som bör fattas tidigt och vilka som kan skjutas upp,
- planera hur juridik, informationsklassning, plattformsval och leverantörsstyrning samverkar över tid,
- använda en 24-månaders roadmap för att strukturera införandet hos Tullverket Aurora,
- formulera mätpunkter och kontrollpunkter som visar om AI-förmågan mognar på rätt sätt.

## Innan vi börjar

Roadmapen i detta kapitel bygger på de tidigare kapitlens grundlogik. AI-förmågan ska utgå från användningsfall, risk, juridik, informationsklassning, principer och governance innan myndigheten skalar teknik och användning. Den ska också återanvända målarkitekturens byggblock: dataarkitektur, teknisk referensarkitektur, AI-gateway, modellplattform, RAG-lager, säkerhetszoner, MLOps, LLMOps, upphandling och leverantörsstyrning.

Roadmapen ska därför inte förstås som ett fristående projektspår. Den är en sammanhållen plan för att göra målarkitekturen verklig.

## Roadmap som arkitekturprodukt

En roadmap är inte bara en tidslinje. I arkitektursammanhang är den en styrande produkt som binder samman nuläge, målbild, beslut, beroenden och införandesteg. Den visar hur myndigheten rör sig från där den är i dag till ett önskat läge utan att hoppa över nödvändiga kontroller.

För AI är detta särskilt viktigt eftersom förmågan har flera samtidiga utvecklingsspår:

- verksamhetens användningsfall behöver prioriteras,
- juridiska och etiska ramar behöver operationaliseras,
- informationsklassning behöver kopplas till tillåtna driftmodeller,
- tekniska byggblock behöver etableras stegvis,
- leverantörer och produkter behöver kravställas,
- säkerhetskontroller behöver testas,
- produktteam behöver lära sig nya arbetssätt,
- förvaltning och incidenthantering behöver fungera innan lösningar blir verksamhetskritiska.

Om roadmapen bara beskriver teknik riskerar myndigheten att införa en plattform utan styrbar användning. Om den bara beskriver policy riskerar myndigheten att skapa styrdokument utan praktisk förmåga. Om den bara beskriver piloter riskerar myndigheten att fastna i experimentläge.

En AI-roadmap behöver därför ha minst sex parallella spår:

1. styrning och ansvar,
2. juridik, risk och regelefterlevnad,
3. data och informationshantering,
4. teknisk plattform och integration,
5. användningsfall och produktteam,
6. drift, säkerhet och förvaltning.

## Faser i en 24-månaders etablering

En praktisk 24-månaders roadmap kan delas in i sex faser. Faserna överlappar, men de har olika huvudfokus.

| Fas | Period | Huvudfokus | Resultat |
|---|---|---|---|
| 1 | Månad 0–3 | Nuläge, mandat och första styrning | Beslutsmandat, nulägesbild, preliminära principer |
| 2 | Månad 3–6 | Kontrollerad sandlåda och use-case triage | Prioriterad AI-portfölj, risktriage, första säkra miljö |
| 3 | Månad 6–9 | Referensarkitektur och styrda piloter | Arkitekturspår, pilotkriterier, första RAG- eller assistentpiloter |
| 4 | Månad 9–12 | Produktionsförmåga för låg till måttlig risk | Produktionsmönster, AI-gateway, loggning, förvaltning |
| 5 | Månad 12–18 | Skalning och differentierade driftmodeller | Flera produktteam, hybridmodell, leverantörsstyrning |
| 6 | Månad 18–24 | Mognad, optimering och portföljstyrning | Stabil AI-förmåga, mätning, revision, kontinuerlig förbättring |

Tabellen är inte ett schema som alla myndigheter måste följa exakt. Den är ett sätt att undvika två vanliga ytterligheter: att försöka lösa allt innan någon nytta skapas, eller att skala användning innan styrning, data och säkerhet är redo.

## Fas 1: Månad 0–3, skapa mandat och nulägesbild

Den första fasen handlar om att skapa kontroll över läget. Många myndigheter börjar inte från noll. Det finns ofta redan informella tester, upphandlade verktyg, lokala scripts, manuella AI-arbetssätt, experiment med generativa tjänster och idéer från verksamheten. Problemet är att ingen har en samlad bild.

Arkitektens första uppgift är därför att synliggöra nuläget och etablera ett tydligt mandat.

### Arkitekturproblemet

Tullverket Aurora upptäcker att flera enheter redan använder AI på olika sätt. Kommunikationsavdelningen testar sammanfattning av remisser. En analysenhet har provat en molnbaserad modell för textklassificering. Ett utvecklingsteam har byggt ett enkelt RAG-experiment mot interna handböcker. Några medarbetare använder publika AI-verktyg för allmän språkgranskning, men styrningen är oklar.

Det finns alltså både nytta, risk och lärande. Men det finns inte en gemensam målbild.

### Rekommenderat angreppssätt

Under de första tre månaderna bör myndigheten fokusera på sex aktiviteter.

1. Skapa ett tydligt uppdrag för AI-målarkitekturen.
2. Inventera pågående AI-användning och planerade initiativ.
3. Etablera ett tillfälligt men beslutsfähigt AI-forum.
4. Ta fram preliminära arkitekturprinciper.
5. Definiera en enkel triagemodell för användningsfall.
6. Stoppa eller styra om uppenbart riskfylld användning.

Målet är inte att skapa fullständig perfektion. Målet är att minska okontrollerad variation och skapa en grund för nästa fas.

### Leverabler

Fas 1 bör resultera i följande artefakter:

- uppdragsbeskrivning för AI-målarkitekturen,
- nulägesinventering av AI-initiativ,
- preliminär AI-portfölj,
- första version av principer för AI-användning,
- enkel use-case triage,
- lista över omedelbara risker och stoppregler,
- förslag till governance och beslutsforum,
- första kommunikation till verksamheten om tillåten och otillåten användning.

### Vägvalsfrågor

- Vem har mandat att prioritera AI-användningsfall?
- Vilka typer av AI-användning måste stoppas tills riskbedömning finns?
- Vilka användningsfall kan fortsätta som kontrollerade experiment?
- Vilka centrala funktioner måste delta från början?
- Ska myndigheten skapa ett tillfälligt AI-program eller integrera arbetet i befintlig arkitekturstyrning?

### Vanliga fallgropar

- Att börja med plattformsval innan nuläget är känt.
- Att försöka skriva kompletta riktlinjer innan någon användningsfallsanalys är gjord.
- Att förbjuda all användning utan att erbjuda ett kontrollerat alternativ.
- Att låta varje enhet själv definiera risknivå och tillåtna verktyg.
- Att göra AI-frågan till ett rent IT-initiativ utan verksamhetsägarskap.

### Kontrollpunkt efter fas 1

Efter tre månader bör myndigheten kunna svara på följande frågor:

- Vilka AI-initiativ finns redan?
- Vilka användningsfall är mest angelägna?
- Vilka risker är omedelbara?
- Vilket forum fattar beslut?
- Vilka principer gäller tills vidare?
- Vilka initiativ får fortsätta, pausas eller avvecklas?

Om dessa frågor inte kan besvaras är det för tidigt att skala tekniken.

## Fas 2: Månad 3–6, etablera kontrollerad sandlåda och portföljtriage

Den andra fasen handlar om att skapa en kontrollerad plats för lärande. En myndighet som bara säger nej till AI skapar ofta skugg-IT. En myndighet som säger ja utan kontroll skapar risk. Sandlådan är kompromissen: den gör det möjligt att pröva användningsfall under definierade regler.

### Arkitekturproblemet

Aurora har identifierat flera användningsfall med möjlig nytta. Vissa är lågkänsliga, till exempel sammanfattning av offentliga dokument och språkstöd för interna texter. Andra är mer känsliga, till exempel handläggarstöd mot interna rutiner, analys av ärendeinformation och stöd för kontrollprioritering.

Alla dessa kan inte testas i samma miljö och med samma regler.

### Rekommenderat angreppssätt

Under månad 3–6 bör myndigheten skapa en kontrollerad AI-sandlåda med tydliga gränser. Sandlådan ska inte vara produktionsmiljö. Den ska vara en miljö där godkända team kan testa godkända användningsfall med godkända datatyper.

Sandlådan bör ha:

- tydliga regler för vilka data som får användas,
- godkända modell- och verktygsalternativ,
- loggning av användning,
- instruktioner för promptar och testfall,
- grundläggande säkerhetskontroller,
- möjlighet att jämföra olika lösningsmönster,
- process för att lyfta ett användningsfall till pilot eller avveckla det.

Samtidigt behöver AI-portföljen struktureras. Alla idéer bör inte bli piloter. De bör först bedömas utifrån nytta, risk, datatillgång, rättslig grund, teknisk komplexitet och organisatorisk beredskap.

### Leverabler

Fas 2 bör resultera i:

- kontrollerad sandlådemiljö,
- portföljmodell för AI-användningsfall,
- triagekriterier för nytta, risk och genomförbarhet,
- godkända dataklasser för sandlådan,
- mall för juridisk och informationssäkerhetsmässig förstagranskning,
- första uppsättning mätpunkter för piloter,
- prioriterad lista över 3–5 möjliga piloter.

### Exempel från Tullverket Aurora

Aurora väljer tre första spår:

1. Intern sammanfattning av lågkänsliga dokument.
2. RAG-baserad sökning i godkända handböcker och styrdokument.
3. Analysstöd med syntetiska eller avidentifierade data för att förstå tekniska möjligheter.

Däremot pausas användningsfall som kräver direkt påverkan på kontrollprioritering eller automatiserat beslutsstöd. De får vänta tills juridik, dataskydd, säkerhetsarkitektur och modellvalidering är mer mogna.

### Vägvalsfrågor

- Vilka datatyper får användas i sandlådan?
- Vilka modeller och tjänster får testas?
- Vem godkänner att ett användningsfall går från idé till sandlåda?
- Hur dokumenteras testresultat?
- När ska ett experiment avbrytas?

### Kontrollpunkt efter fas 2

Efter sex månader bör myndigheten ha en fungerande portföljtriage och en kontrollerad testmiljö. Den bör också ha stoppat eller omformat användningsfall som kräver högre kontroll än sandlådan kan erbjuda.

## Fas 3: Månad 6–9, skapa referensarkitektur och styrda piloter

Den tredje fasen handlar om att gå från experiment till styrda piloter. Skillnaden är viktig. Ett experiment svarar på frågan om något kan fungera. En pilot prövar om lösningen kan fungera under realistiska villkor med rätt kontroller, ansvar och mätning.

### Arkitekturproblemet

Aurora har fått positiv respons på intern kunskapssökning. Handläggare ser nytta i att snabbt hitta relevanta styrdokument, men arkitekturgruppen ser också risker: felaktiga svar, bristande källhänvisning, åtkomstproblem, otydlig loggning och risk för att användare tror att AI-svaret är en auktoritativ tolkning.

Det räcker därför inte att RAG-lösningen tekniskt fungerar. Den måste pilottestas med rätt kontroller.

### Rekommenderat angreppssätt

Under månad 6–9 bör myndigheten formulera en första teknisk referensarkitektur och välja 1–3 styrda piloter.

Referensarkitekturen bör beskriva:

- godkända arkitekturspår,
- dataklasser och driftmodeller,
- identitet och åtkomst,
- modellåtkomst,
- retrieval och indexering,
- loggning och spårbarhet,
- mänsklig kontroll,
- test och validering,
- incidenthantering,
- krav på leverantörer och komponenter.

Piloterna bör väljas så att de testar olika delar av förmågan, men inte så många delar att organisationen tappar kontrollen.

### Leverabler

Fas 3 bör resultera i:

- första version av teknisk referensarkitektur,
- pilotkriterier och beslutspunkter,
- arkitekturbeslut för valda piloter,
- dokumenterad riskbedömning per pilot,
- testplan och acceptanskriterier,
- modell för användarfeedback,
- drift- och supportmodell för pilot,
- beslut om vilka piloter som kan gå vidare mot produktion.

### Pilotkriterier

En AI-pilot bör inte godkännas enbart för att den är tekniskt intressant. Den bör uppfylla följande kriterier:

- tydligt verksamhetsägarskap,
- avgränsad användargrupp,
- kända datakällor,
- genomförd informationsklassning,
- preliminär juridisk bedömning,
- definierade risker och kontroller,
- mätbar nytta,
- tydlig pilotperiod,
- dokumenterad väg till produktion eller avveckling.

### Exempel från Tullverket Aurora

Aurora väljer att göra kunskapsstödet till sin första styrda pilot. Lösningen får bara använda godkända styrdokument och handböcker. Den ska visa källhänvisningar, logga frågor och svar enligt fastställda regler, använda behörighetsstyrd åtkomst och ha en tydlig instruktion om att svaret är ett stöd, inte ett beslut.

Aurora väljer också att inte pilottesta analysstöd för kontrollprioritering i detta skede. Det användningsfallet kräver högre modellvalidering, starkare governance och mer avancerad riskhantering.

### Kontrollpunkt efter fas 3

Efter nio månader bör myndigheten ha minst en styrd pilot som testar både teknik och arbetssätt. Den bör också ha dokumenterade arkitekturspår som kan återanvändas i kommande initiativ.

## Fas 4: Månad 9–12, etablera produktionsförmåga för låg till måttlig risk

Den fjärde fasen handlar om att skapa den första verkliga produktionsförmågan. Det betyder inte att myndigheten ska produktionssätta alla typer av AI. Det betyder att den ska kunna produktionssätta vissa användningsfall på ett kontrollerat sätt.

### Arkitekturproblemet

Auroras kunskapsstöd fungerar i pilot, men produktionssättning kräver mer än ett lyckat test. Lösningen behöver förvaltningsansvar, övervakning, incidentprocess, ändringshantering, användarstöd, kostnadsuppföljning, åtkomstkontroll, livscykel för index och promptmallar samt tydliga regler för modelluppdateringar.

### Rekommenderat angreppssätt

Under månad 9–12 bör myndigheten etablera en minsta produktionsförmåga för AI. Den bör vara smal men robust.

Den minsta produktionsförmågan bör omfatta:

- godkänd driftmodell för låg till måttlig risk,
- standardmönster för AI-gateway eller motsvarande kontrollpunkt,
- loggning och övervakning,
- hantering av promptmallar och konfiguration,
- versionshantering av index, modeller och integrationskomponenter,
- support- och incidentprocess,
- roller för produktägare, systemägare, modellansvar och teknisk förvaltning,
- process för att godkänna förändringar.

### Leverabler

Fas 4 bör resultera i:

- första produktionssatta AI-lösningen eller produktionsredo release,
- operativ förvaltningsmodell,
- AI-specifik incidentklassning,
- mätning av nytta, kvalitet, risk och användning,
- beslutad modell för kostnadsuppföljning,
- dokumenterad användarvägledning,
- uppdaterad referensarkitektur baserad på pilotlärdomar.

### Produktionskriterier

Ett AI-användningsfall bör inte gå i produktion om följande saknas:

- verksamhetsägare,
- informationsägare,
- teknisk förvaltare,
- godkänd riskbedömning,
- tydligt tillåtet användningsområde,
- loggning och uppföljning,
- process för felrapportering,
- process för förändringar av modell, prompt, index och datakällor,
- avvecklingsplan eller exitmöjlighet.

### Exempel från Tullverket Aurora

Aurora produktionssätter kunskapsstödet för en avgränsad grupp handläggare. Lösningen används för att hitta relevanta interna rutiner, inte för att fatta beslut. Arkitekturbeslutet anger att nya dokumentkällor inte får kopplas på utan informationsklassning, behörighetskontroll och test mot felaktiga svar.

Aurora inför också en regel: varje AI-lösning i produktion måste ha en ansvarig produktägare och en teknisk systemförvaltning. AI får inte vara ett löst experiment som ingen äger efter projektets slut.

### Kontrollpunkt efter fas 4

Efter tolv månader bör myndigheten kunna visa att den kan gå från idé till kontrollerad produktion för minst en riskmässigt lämplig kategori av AI-användningsfall. Detta är en viktig mognadsgräns.

## Fas 5: Månad 12–18, skala med differentierade driftmodeller

Den femte fasen handlar om skalning. Men skalning betyder inte att alla användningsfall ska använda samma lösning. Tvärtom bör myndigheten nu skapa flera godkända arkitekturspår för olika risknivåer och dataklasser.

### Arkitekturproblemet

Aurora får fler förfrågningar. Enheter vill använda AI för e-postsammanfattningar, dokumentgranskning, intern sökning, strategisk analys, ärendeberedning och kontrollstöd. Vissa användningsfall kan ligga i kontrollerad molnmiljö. Andra kräver starkare avskiljning. Några bör kanske inte genomföras alls.

Utan differentierade driftmodeller riskerar Aurora antingen att överkontrollera enkla användningsfall eller underkontrollera känsliga.

### Rekommenderat angreppssätt

Under månad 12–18 bör myndigheten etablera flera arkitekturspår. Ett arkitekturspår är ett godkänt mönster för en viss typ av AI-användning, med tillhörande krav på data, drift, säkerhet, modellval, loggning, ansvar och förvaltning.

Exempel på arkitekturspår:

- spår A: lågkänsligt produktivitetsstöd,
- spår B: RAG-baserat kunskapsstöd med godkända interna dokument,
- spår C: analysstöd med skyddsvärda data i särskild miljö,
- spår D: verksamhetsnära beslutsstöd med förhöjd kontroll,
- spår E: experimentmiljö för teknisk utvärdering med syntetiska eller avidentifierade data.

Varje spår bör ha egna regler. Ett lågkänsligt skrivstöd ska inte bära samma börda som ett beslutsstöd i kontrollverksamhet. Men ett känsligt beslutsstöd får heller inte ärva frihetsgrader från ett lågkänsligt produktivitetsverktyg.

### Leverabler

Fas 5 bör resultera i:

- beslutade arkitekturspår,
- uppdaterad modellkatalog,
- tydligare leverantörsstyrning,
- etablerad process för nya AI-användningsfall,
- flera produktteam som kan använda gemensamma byggblock,
- förbättrad AI-gateway eller motsvarande kontrollplan,
- standardiserade mallar för ADR, riskbedömning och produktionsgodkännande,
- plan för kompetensutveckling och kunskapsöverföring.

### Skalningsprinciper

Skalning bör följa fem principer.

1. Skala mönster före lösningar.
2. Skala kontroller före känsliga användningsfall.
3. Skala produktteam före centrala flaskhalsar.
4. Skala mätning före verksamhetskritisk användning.
5. Skala bara det som har tydlig ägare.

Den första principen är särskilt viktig. Om varje team bygger sin egen RAG-lösning, sin egen modellåtkomst och sin egen loggning skalar inte myndigheten AI-förmågan. Den skalar variation.

### Exempel från Tullverket Aurora

Aurora inför tre första produktionsspår:

- kontrollerat produktivitetsstöd för lågkänsliga arbetsuppgifter,
- RAG-baserat kunskapsstöd för godkända interna dokument,
- skyddad analysmiljö för mer känsliga data med striktare åtkomst och isolering.

Riskanalys för kontrollprioritering får fortfarande inte fullt produktionsspår. Det placeras i ett särskilt utredningsspår med krav på juridisk fördjupning, modellvalidering, dokumentation, bias-analys och tydlig mänsklig kontroll.

### Kontrollpunkt efter fas 5

Efter arton månader bör myndigheten ha gått från enstaka lösningar till en återanvändbar AI-förmåga. Den bör kunna starta nya initiativ snabbare än tidigare, men med bättre kontroll.

## Fas 6: Månad 18–24, skapa mognad och kontinuerlig förbättring

Den sista fasen i den första 24-månadersperioden handlar om mognad. Nu ska AI-förmågan inte längre bero på enstaka eldsjälar, tillfälliga projekt eller informella undantag. Den ska vara en del av myndighetens ordinarie arkitektur, styrning och förvaltning.

### Arkitekturproblemet

Aurora har flera AI-lösningar i drift och fler på väg. Det finns återanvändbara byggblock, men också växande komplexitet. Kostnaderna ökar. Modellversioner ändras. Nya leverantörsvillkor kommer. Fler team vill använda agentliknande flöden och verktygsanrop. Juridiken utvecklas. Användarna blir mer beroende av lösningarna.

Det som tidigare var innovation blir nu operativ förmåga.

### Rekommenderat angreppssätt

Under månad 18–24 bör myndigheten fokusera på styrbarhet över tid. Det innebär att AI-förmågan integreras i ordinarie processer för arkitektur, säkerhet, dataskydd, upphandling, portföljstyrning, budget, kompetens och revision.

Myndigheten bör också börja mäta mognad, inte bara antal lösningar.

### Leverabler

Fas 6 bör resultera i:

- etablerad AI-portföljstyrning,
- återkommande revision av AI-lösningar,
- mognadsmodell för AI-förmågan,
- kostnads- och nyttouppföljning,
- process för omprövning av arkitekturbeslut,
- process för modell- och leverantörsförändringar,
- förbättrad incident- och avvikelsehantering,
- kompetensplan för arkitekter, produktteam, jurister, säkerhet och verksamhet,
- uppdaterad målarkitektur för nästa planeringscykel.

### Mognadsmått

Antalet AI-lösningar är ett svagt mognadsmått. En myndighet kan ha många AI-lösningar och ändå låg kontroll. Bättre mognadsmått är till exempel:

- andel AI-lösningar med dokumenterad riskbedömning,
- andel AI-lösningar med tydlig ägare och förvaltning,
- andel AI-användningsfall placerade i godkänt arkitekturspår,
- tid från idé till godkänd pilot,
- tid från pilot till produktionsbeslut,
- antal avvikelser från målarkitekturen,
- antal incidenter eller felrapporter per lösning,
- kvalitet i källhänvisningar och svar,
- användarnytta över tid,
- kostnad per användningsfall eller användargrupp,
- andel leverantörsvillkor som är granskade och uppdaterade.

### Exempel från Tullverket Aurora

Aurora inför en årlig AI-arkitekturgenomgång. Där granskas portföljen, driftmodeller, leverantörer, incidenter, kostnader, nyttor och kommande rättsliga förändringar. AI-målarkitekturen behandlas inte som ett engångsdokument utan som en levande styrprodukt.

Aurora inför också en princip om att varje produktionssatt AI-lösning ska ha ett omprövningsdatum. Vid omprövningen kontrolleras om användningsfallet fortfarande är relevant, om modellen fortfarande är lämplig, om datakällorna är korrekta, om loggningen fungerar, om kostnaden är rimlig och om lösningen följer gällande arkitekturspår.

### Kontrollpunkt efter fas 6

Efter tjugofyra månader bör myndigheten ha en etablerad AI-förmåga som kan beskrivas, styras, granskas och vidareutvecklas. Alla svåra frågor är inte lösta, men organisationen har ett sätt att hantera dem.

## Beroenden mellan spåren

En roadmap blir ofta missvisande om den bara visar tidsperioder. Det viktiga är beroendena. Vissa aktiviteter kan ske parallellt, medan andra inte bör påbörjas innan grundläggande beslut finns.

### Beroenden som bör vara tydliga

Följande beroenden bör dokumenteras i roadmapen:

- användningsfall kräver portföljtriage innan pilot,
- pilot kräver informationsklassning och riskbedömning,
- produktionssättning kräver ägare, förvaltning och incidentprocess,
- känsliga data kräver godkänd driftmodell,
- RAG kräver datakällor med ägarskap och åtkomstkontroll,
- verktygsanrop kräver särskild säkerhetsbedömning,
- leverantörsavtal kräver granskade AI-villkor,
- modelluppdateringar kräver förändringshantering,
- skalning kräver återanvändbara arkitekturspår,
- verksamhetskritisk användning kräver mätning, loggning och omprövning.

### Beslut som bör fattas tidigt

Vissa beslut bör inte skjutas upp för länge:

- vem som äger AI-portföljen,
- vilka dataklasser som får användas i vilka miljöer,
- vilka typer av AI-användning som är otillåtna tills vidare,
- vilken funktion som godkänner piloter,
- hur arkitekturbeslut dokumenteras,
- vilken miniminivå av loggning som krävs,
- hur leverantörsvillkor granskas,
- vilken roll AI-gateway eller motsvarande kontrollpunkt ska ha.

### Beslut som kan skjutas upp

Andra beslut kan ofta skjutas upp, eftersom för tidig låsning kan skapa onödig inlåsning:

- exakt modellval för alla framtida användningsfall,
- fullständig standardisering av hela AI-plattformen,
- beslut om egen modellträning,
- avancerade agentramverk,
- omfattande on-premises-infrastruktur för alla scenarier,
- specialiserade MLOps-flöden för användningsfall som ännu inte finns.

Konsten är att låsa rätt saker tidigt och lämna rätt saker öppna.

## Roadmapens styrningsnivåer

En AI-roadmap behöver kunna läsas på flera nivåer. Ledningen behöver förstå beslut, risk och investeringar. Arkitekter behöver förstå byggblock och beroenden. Produktteam behöver förstå vad som krävs för att få bygga, testa och gå i produktion.

### Ledningsnivå

På ledningsnivå bör roadmapen visa:

- varför AI-förmågan behövs,
- vilka nyttor som prioriteras,
- vilka risker som styr införandet,
- vilka beslut som kräver ledningsmandat,
- vilka investeringar som behövs,
- hur framdrift mäts.

### Arkitekturnivå

På arkitekturnivå bör roadmapen visa:

- målarkitekturens byggblock,
- arkitekturspår,
- integrationsmönster,
- driftmodeller,
- beroenden mellan data, plattform och säkerhet,
- beslutspunkter och ADR:er,
- vilka delar som är temporära och vilka som är målbild.

### Produktteamsnivå

På produktteamsnivå bör roadmapen visa:

- hur ett användningsfall går från idé till produktion,
- vilka mallar och kontroller som ska användas,
- vilka komponenter som är återanvändbara,
- hur support och incidenter hanteras,
- hur lösningen mäts och förbättras.

En vanlig fallgrop är att roadmapen skrivs för bara en av dessa nivåer. Då blir den antingen för strategisk för att styra tekniken, eller för teknisk för att ge ledningen rätt beslutsunderlag.

## Arkitektens arbetsordning

När en erfaren IT-arkitekt får uppdraget att ta fram en AI-roadmap kan arbetet angripas i följande ordning.

1. Beskriv nuläget och pågående experiment.
2. Gruppera användningsfall i portföljkategorier.
3. Identifiera risk- och dataklasser.
4. Beskriv tillåtna och otillåtna användningsmönster.
5. Formulera preliminära arkitekturprinciper.
6. Etablera beslutsforum och ansvar.
7. Definiera första sandlådan.
8. Välj styrda piloter.
9. Ta fram referensarkitektur.
10. Etablera produktionskriterier.
11. Skapa arkitekturspår.
12. Skala genom portföljstyrning och förvaltning.

Ordningen är viktig eftersom varje steg skapar underlag för nästa. Det går att iterera, men inte att hoppa över grunden utan konsekvens.

## Roadmap för Tullverket Aurora

Auroras 24-månaders roadmap kan sammanfattas så här.

| Period | Aurora gör | Arkitekturresultat |
|---|---|---|
| Månad 0–3 | Inventerar AI-användning, skapar AI-forum och första principer | Mandat, nulägesbild, preliminär portfölj |
| Månad 3–6 | Inför sandlåda och triagerar användningsfall | Kontrollerad testmiljö, prioriterade piloter |
| Månad 6–9 | Tar fram referensarkitektur och startar RAG-pilot | Arkitekturspår, pilotbeslut, testkriterier |
| Månad 9–12 | Produktionssätter avgränsat kunskapsstöd | Förvaltningsmodell, AI-gateway, incidentprocess |
| Månad 12–18 | Skalar till flera produktteam och driftspår | Modellkatalog, differentierad drift, leverantörsstyrning |
| Månad 18–24 | Integrerar AI i ordinarie portfölj- och arkitekturstyrning | Mognadsmodell, revision, förbättringscykel |

Aurora väljer att inte göra alla avancerade användningsfall under första året. Det är ett medvetet arkitekturbeslut. Myndigheten etablerar först de kontroller som krävs för enklare och medelrisknära användningsfall. Därefter kan den ta sig an mer verksamhetskritiska scenarier med bättre styrning.

## Vanliga fallgropar

### Att göra roadmapen till en teknikplan

En teknikplan kan beskriva plattform, integrationer, modeller och miljöer. Men en AI-roadmap måste också beskriva juridik, styrning, data, ansvar, leverantörer, produktteam och förvaltning. Annars blir planen för smal.

### Att skala innan ansvar finns

Om användningsfall sprids utan tydligt ägarskap skapas operativ risk. Varje AI-lösning behöver en ägare, en förvaltning och en tydlig användningsgräns.

### Att behandla piloter som produktion

En pilot kan vara kontrollerad utan att vara produktionssatt. Om pilotlösningar blir permanenta utan produktionsbeslut uppstår ofta brister i loggning, support, ansvar, säkerhet och kostnadsstyrning.

### Att låsa plattformen för tidigt

För tidig standardisering kan skapa inlåsning innan myndigheten förstår sina användningsfall. Standardisera därför principer, kontroller och arkitekturspår innan alla tekniska detaljer låses.

### Att skjuta upp styrningen för länge

Motsatt problem är att låta experimenten fortsätta utan gemensam styrning. Då växer variationen snabbare än förmågan.

### Att sakna avvecklingslogik

AI-lösningar bör kunna avvecklas. Modeller, datakällor, promptmallar, index, integrationer och avtal förändras. Roadmapen behöver därför beskriva inte bara införande utan också omprövning och avslut.

## Checklista för en 24-månaders AI-roadmap

En användbar AI-roadmap bör kunna svara på följande frågor:

- Vilket nuläge utgår vi från?
- Vilket mandat finns för AI-målarkitekturen?
- Vilka användningsfall prioriteras först?
- Vilka användningsfall ska pausas eller avgränsas?
- Vilka dataklasser får användas i vilka miljöer?
- Vilka arkitekturprinciper styr införandet?
- Vilken sandlåda behövs?
- Vilka piloter ska genomföras?
- Vilka kriterier krävs för produktionssättning?
- Vilka byggblock ska vara gemensamma?
- Vilka driftmodeller ska stödjas?
- Vilka leverantörs- och avtalsfrågor måste lösas?
- Hur mäts nytta, kvalitet, risk och kostnad?
- Hur hanteras incidenter och avvikelser?
- Hur omprövas modellval, datakällor och arkitekturbeslut?
- När uppdateras målarkitekturen?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Roadmapen är målarkitekturens genomförandelogik. Den visar i vilken ordning målbildens delar ska realiseras och vilka kontroller som måste vara på plats innan myndigheten skalar.

För Tullverket Aurora innebär detta att målarkitekturen inte blir ett statiskt dokument. Den utvecklas genom kontrollerade steg: från nulägesbild och principer, via sandlåda och styrda piloter, till produktionsförmåga, arkitekturspår och portföljstyrning.

Nästa kapitel använder denna roadmap som grund för att beskriva en samlad målarkitektur för Tullverket Aurora. Där knyts bokens delar ihop i ett konkret helhetsexempel med målbild, byggblock, principer, driftmodell, säkerhetszoner, roadmap och arkitekturbeslut.
