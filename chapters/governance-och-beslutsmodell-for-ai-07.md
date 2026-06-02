# Kapitel 7: Governance och beslutsmodell för AI

## Varför detta kapitel finns

AI-förmåga blir inte styrbar enbart genom principer, plattformar och policyer. Den blir styrbar först när det finns tydliga beslutspunkter, roller, mandat och arbetssätt som gör att rätt frågor ställs vid rätt tidpunkt. Governance är därför inte ett administrativt tillägg till målarkitekturen. Det är en del av målarkitekturen.

För en större statlig myndighet är detta särskilt viktigt. AI kan påverka informationssäkerhet, dataskydd, rättssäkerhet, verksamhetsprocesser, arbetsmiljö, upphandling, integration, arkitektur och medborgarnas förtroende. Om besluten fattas lokalt utan gemensam modell blir resultatet ofta fragmentering: olika avdelningar väljer olika verktyg, olika risknivåer bedöms på olika sätt och ingen har en samlad bild av vilka AI-lösningar som faktiskt används.

Tullverket Aurora har redan sett detta mönster. Några team har testat generativa AI-verktyg för sammanfattning. Ett annat team vill bygga ett RAG-baserat kunskapsstöd för interna rutiner. En analysenhet undersöker prediktiva modeller för prioriteringsstöd. Juridik, säkerhet, dataskydd, arkitektur och upphandling kopplas in ojämnt. Problemet är inte att initiativen finns. Problemet är att myndigheten saknar en beslutsmodell som gör dem jämförbara, prioriterbara och möjliga att styra.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför AI-governance behöver vara en integrerad del av målarkitekturen,
- skilja mellan strategiska, taktiska och operativa AI-beslut,
- beskriva vilka forum och roller som behövs i en större myndighet,
- utforma en beslutsmodell som kopplar samman användningsfall, risk, juridik, säkerhet, data och teknik,
- avgöra vilka beslut som bör vara centrala och vilka som kan delegeras,
- använda Tullverket Aurora som exempel för att organisera AI-styrning utan att stoppa innovation,
- formulera miniminivåer för dokumentation, ansvar och uppföljning.

## Arkitekturproblemet

Det vanliga misstaget är att se governance som en fråga om kommittéer. Då blir lösningen snabbt att skapa ett AI-råd, ett styrforum eller en policygrupp. Sådana forum kan vara nödvändiga, men de löser inte problemet om de saknar tydliga beslutstyper och ingångar.

Arkitekturproblemet är i stället detta: varje AI-initiativ behöver passera ett antal beslutspunkter där myndigheten avgör om initiativet är tillåtet, prioriterat, arkitektoniskt rimligt, säkert, juridiskt hanterbart och förvaltningsbart. Beslutspunkterna behöver vara tillräckligt tydliga för att skapa kontroll, men inte så tunga att varje idé fastnar i en långsam granskningsprocess.

För Tullverket Aurora innebär det att ett enkelt internt användningsfall, till exempel sammanfattning av offentliga styrdokument, inte ska behöva samma beslutsprocess som ett användningsfall där AI ger prioriteringsstöd i kontrollverksamhet. Samtidigt får det enkla användningsfallet inte gå helt utanför styrning, eftersom även intern användning kan innebära personuppgifter, sekretess, loggar, molnöverföring eller otillåten användning av leverantörens modellträning.

## Grundprincip: styr flödet, inte bara forumen

En användbar AI-governance börjar med flödet från idé till avveckling. Forum och roller placeras sedan där de behövs i flödet.

Ett praktiskt flöde kan se ut så här:

1. Idé eller behov fångas.
2. Användningsfallet beskrivs på en gemensam mall.
3. Use-case triage genomförs.
4. Juridisk, säkerhetsmässig och datamässig klassning görs.
5. Arkitekturvägval föreslås.
6. Beslut fattas om avslag, sandlåda, pilot, produktionsförberedelse eller direkt återanvändning av befintlig lösning.
7. Lösningen utvecklas eller konfigureras enligt godkända mönster.
8. Godkännande inför produktion görs.
9. Drift, uppföljning och incidenthantering etableras.
10. Lösningen omprövas, förändras eller avvecklas.

Detta flöde gör governance konkret. Det visar när juridik ska kopplas in, när arkitektur ska göra vägval, när säkerhet ska granska, när dataskyddsfrågor behöver utredas och när ett verksamhetsbeslut krävs.

## Tre beslutsnivåer

En större myndighet behöver normalt tre nivåer av AI-beslut: strategisk, taktisk och operativ. Målet är inte att alla beslut ska lyftas till högsta nivå. Målet är att varje beslut hamnar på rätt nivå.

## Strategiska beslut

Strategiska beslut handlar om inriktning, riskaptit, mandat och investeringar. De bör ägas av myndighetsledning eller ett etablerat ledningsnära forum.

Exempel på strategiska beslut:

- Vilken roll ska AI ha i myndighetens verksamhetsutveckling?
- Vilka användningsfallstyper är prioriterade de kommande två åren?
- Vilken riskaptit gäller för generativ AI, prediktiv AI och beslutsstöd?
- Vilka informationsklasser får hanteras i molnbaserade AI-tjänster?
- Ska myndigheten etablera en gemensam AI-plattform?
- Vilken balans ska finnas mellan centralt ägd plattform och lokala initiativ?
- Vilka principer gäller för moln, on-premises och hybrid?
- Hur mycket ska myndigheten investera i intern kompetens jämfört med leverantörsstöd?

Strategiska beslut ska inte vara tekniska detaljbeslut, men de måste ge tillräcklig riktning för tekniska vägval. Om ledningen exempelvis säger att myndigheten ska använda AI men inte tar ställning till riskaptit, datahantering eller driftmodeller kommer arkitekturen att fyllas av lokala tolkningar.

## Taktiska beslut

Taktiska beslut översätter strategin till portfölj, arkitektur och styrning. De bör normalt hanteras av ett AI-governanceforum, ett arkitekturforum eller ett kombinerat forum där verksamhet, IT, juridik, säkerhet och dataskydd är representerade.

Exempel på taktiska beslut:

- Vilka användningsfall går vidare till pilot?
- Vilka lösningsmönster är godkända för olika risknivåer?
- Vilka referensarkitekturer ska återanvändas?
- Vilka modeller, plattformar och ramverk får användas i sandlåda respektive produktion?
- Vilka minimikrav gäller för loggning, test, dokumentation och uppföljning?
- Vilka undantag från principer godkänns och vilka kompensatoriska kontroller krävs?
- När ska ett användningsfall lyftas till ledningen?

Taktiska beslut är särskilt viktiga eftersom de hindrar två ytterligheter. Den ena är att alla initiativ stoppas i väntan på perfekta regler. Den andra är att alla initiativ får fortsätta utan gemensam styrning. Ett bra taktiskt forum skapar kontrollerad rörelse framåt.

## Operativa beslut

Operativa beslut fattas nära teamen, produkterna och projekten. De handlar om hur en godkänd riktning omsätts i lösning, konfiguration, test och drift.

Exempel på operativa beslut:

- Vilka datakällor får kopplas till ett specifikt RAG-index?
- Vilken promptmall ska användas för ett visst handläggarstöd?
- Hur ska behörigheter sättas för en användargrupp?
- Vilka testfall krävs inför driftsättning?
- Hur ska avvikande svar, hallucinationer eller felaktiga rekommendationer rapporteras?
- När behöver en modellversion spärras eller rullas tillbaka?

Operativa beslut ska vara styrda av godkända mönster. Teamen bör ha handlingsfrihet inom ramarna, men inte frihet att uppfinna egna säkerhetsregler, egna leverantörsvillkor eller egna riskklassningsmodeller.

## Roller i AI-governance

En beslutsmodell blir bara användbar om det är tydligt vem som gör vad. För Tullverket Aurora behövs inte nödvändigtvis en helt ny organisation, men befintliga roller behöver kompletteras med AI-specifikt ansvar.

## Verksamhetsägare

Verksamhetsägaren äger behovet och nyttan. Det är verksamhetsägaren som ska kunna förklara varför användningsfallet behövs, vilken process det stödjer, vilka användare som berörs och vilka konsekvenser det får om AI-lösningen ger felaktigt, ofullständigt eller olämpligt stöd.

Verksamhetsägaren ska inte ensam avgöra om lösningen är juridiskt eller tekniskt lämplig, men utan tydligt verksamhetsägarskap blir AI-initiativet ofta teknikdrivet.

## Informationsägare

Informationsägaren ansvarar för att data och information hanteras enligt myndighetens krav. I AI-sammanhang är detta centralt eftersom promptar, dokument, träningsdata, embeddings, loggar och utdata kan innehålla information som behöver klassas och skyddas.

Informationsägaren bör medverka tidigt, särskilt när användningsfallet bygger på dokument, ärendedata, analysdata eller känslig verksamhetsinformation.

## Systemägare och produktägare

Systemägare och produktägare ansvarar för de system eller produkter som AI-lösningen kopplas till. De behöver ta ställning till integration, förvaltning, livscykel, användarstöd, incidenter och förändringar.

För AI-lösningar räcker det inte att säga att någon äger applikationen. Någon behöver också äga modellberoenden, kunskapsbaser, promptmallar, kvalitetsmätning och regler för uppdatering.

## Chefsarkitekt och arkitekturforum

Chefsarkitekturen eller arkitekturforumet ansvarar för att AI-lösningar passar in i målarkitekturen. Det handlar om byggblock, integrationsmönster, teknisk skuld, återanvändning, leverantörsberoenden, säkerhetszoner och livscykel.

Arkitekturforumet bör inte granska varje prompt eller varje liten konfiguration, men det ska besluta om godkända arkitekturmönster och hantera avvikelser från dem.

## Informationssäkerhetsfunktion

Informationssäkerhetsfunktionen bedömer skyddsbehov, hotbild, säkerhetskrav och kontroller. I AI-sammanhang behöver funktionen även förstå nya riskmönster som prompt injection, data leakage, modellmissbruk, otillräcklig loggning och bristande separation mellan miljöer.

Säkerhetsfunktionen bör inte komma in först vid produktionssättning. Då är många vägval redan låsta. Den bör vara del av triage och arkitekturvägval.

## Dataskyddsombud och dataskyddsfunktion

Dataskyddsfunktionen bedömer frågor kopplade till personuppgifter, rättslig grund, ändamålsbegränsning, dataminimering, transparens, konsekvensbedömning och registrerades rättigheter.

För generativ AI är det viktigt att dataskyddsfrågor inte bara ställs om träningsdata. Även promptar, dokumentunderlag, loggar och modellutdata kan innehålla personuppgifter.

## Juridik

Juridikfunktionen hanterar frågor om AI Act, offentlighet och sekretess, upphandling, avtal, ansvar, arkiv och rättsliga konsekvenser av AI-stöd i verksamhetsprocesser.

Juridik ska inte användas som ett sent godkännandesteg. Rollen bör vara att tidigt identifiera rättsliga ramar och hjälpa arkitekturen att hitta möjliga lösningsmönster.

## Inköp och leverantörsstyrning

Inköp och leverantörsstyrning behöver förstå AI-specifika krav: datalokalisering, underbiträden, modellträning på kunddata, loggåtkomst, transparens, revision, exit, SLA, modelluppdateringar och ändrade leverantörsvillkor.

AI-governance utan koppling till upphandling riskerar att skapa fina principer som sedan inte syns i avtalen.

## AI-plattformsägare

När myndigheten etablerar en gemensam AI-plattform behövs en tydlig plattformsägare. Plattformsägaren ansvarar för tillhandahållande, driftmodell, teknisk roadmap, standardtjänster, onboarding av team, kostnadsmodell, säkerhetskontroller och förvaltningsprocess.

Plattformsägaren ska inte äga alla användningsfall, men ska äga den gemensamma förmåga som användningsfallen bygger på.

## Rekommenderad forumstruktur

En praktisk modell för Tullverket Aurora är att använda fyra kompletterande forum. De bör vara lätta nog att fungera i vardagen, men tydliga nog att ge kontroll.

## AI-styrgrupp

AI-styrgruppen är ledningsnära och fattar strategiska beslut. Den beslutar om inriktning, prioriteringar, riskaptit, större investeringar och övergripande policy.

Typiska deltagare:

- verksamhetsledning,
- IT-ledning,
- chefsarkitekt,
- säkerhetsansvarig,
- juridiskt ansvarig,
- dataskyddsansvarig,
- portfölj- eller utvecklingsansvarig.

AI-styrgruppen ska inte vara ett tekniskt designforum. Den ska skapa mandat och prioriteringar.

## AI-governanceforum

AI-governanceforumet hanterar den taktiska styrningen. Det bedömer användningsfall, följer portföljen, beslutar om pilotkandidater, hanterar undantag och ser till att juridik, säkerhet, arkitektur och verksamhet vägs samman.

Forumet bör ha mandat att säga något av följande:

- avslå användningsfallet,
- be om komplettering,
- godkänna för sandlåda,
- godkänna för pilot,
- kräva särskild riskutredning,
- skicka ärendet till arkitekturforum,
- eskalera till AI-styrgruppen.

## Arkitekturforum för AI

Arkitekturforumet ansvarar för referensarkitektur, målarkitektur, byggblock, tekniska mönster och arkitekturbeslut. Det kan vara ett befintligt arkitekturforum som får ett tydligt AI-spår.

Forumet bör hantera frågor som:

- godkända integrationsmönster,
- modellservering,
- RAG-arkitektur,
- AI-gateway,
- säkerhetszoner,
- loggning och observability,
- återanvändbara komponenter,
- undantag från arkitekturprinciper.

## Operativt AI-community

Ett operativt AI-community samlar arkitekter, utvecklare, data scientists, säkerhetsspecialister, jurister, verksamhetsutvecklare och produktägare som arbetar praktiskt med AI. Det är inte främst ett beslutsforum utan ett lärande forum.

Syftet är att sprida mönster, erfarenheter, incidenter, återanvändbara komponenter och praktiska lösningar. För en myndighet som vill etablera förmåga är detta viktigt. Utan community blir varje team isolerat och lärandet stannar i projekten.

## Beslutsmodell från idé till produktion

En fungerande beslutsmodell bör vara enkel att använda och svår att kringgå. Följande modell är ett praktiskt utgångsläge.

## Steg 1: Registrera användningsfallet

Alla AI-initiativ registreras i en gemensam portfölj, även om de bara är idéer. Registreringen bör vara enkel men obligatorisk.

Minsta information:

- namn på användningsfallet,
- verksamhetsägare,
- tänkt användargrupp,
- typ av AI-roll,
- berörda datakällor,
- preliminär nyttobedömning,
- preliminär riskbedömning,
- tänkt lösningsmönster om det är känt,
- om externa AI-tjänster berörs.

Poängen är inte att skapa tung administration. Poängen är att myndigheten ska veta vilka AI-initiativ som finns.

## Steg 2: Genomför use-case triage

Use-case triage avgör hur mycket styrning användningsfallet behöver. Triage ska inte vara en fullständig utredning, utan en första sortering.

Frågor i triage:

- Hanteras personuppgifter?
- Hanteras sekretessbelagd eller skyddsvärd information?
- Påverkar AI-stödet beslut om enskilda?
- Används AI i operativ kontrollverksamhet?
- Finns risk för automatiseringsbias?
- Är modellen extern, intern, öppen eller leverantörsstyrd?
- Kommer promptar, dokument eller utdata att loggas av leverantör?
- Behöver användaren kunna förstå, ifrågasätta eller dokumentera AI-stödet?
- Finns ett befintligt godkänt mönster som kan återanvändas?

Resultatet blir en styrklass, inte ett slutligt godkännande.

## Steg 3: Välj styrklass

Tullverket Aurora kan använda fyra styrklasser.

| Styrklass | Typisk användning | Beslutsnivå |
|---|---|---|
| Klass A | Låg risk, interna stöd, godkända datatyper, befintligt mönster | Operativt beslut inom godkända ramar |
| Klass B | Måttlig risk, intern pilot, begränsade data, tydligt verksamhetsägarskap | AI-governanceforum |
| Klass C | Högre risk, känslig information, påverkan på ärendeprocess eller verksamhetskritiska flöden | AI-governanceforum och arkitekturforum |
| Klass D | Mycket hög risk, möjlig påverkan på enskildas rättigheter, omfattande sekretess eller strategisk betydelse | AI-styrgrupp och särskild utredning |

Styrklassen avgör inte om användningsfallet är bra eller dåligt. Den avgör hur mycket styrning, dokumentation och granskning som behövs.

## Steg 4: Besluta om väg framåt

Efter triage ska beslutet vara tydligt. Oklara mellanlägen skapar skuggprojekt.

Möjliga beslut:

- Avslå eftersom användningsfallet inte är lämpligt.
- Parkera eftersom nytta, ansvar eller datagrund är otydlig.
- Gå till sandlåda med begränsade data.
- Gå till pilot med tydliga villkor.
- Återanvänd befintlig godkänd lösning.
- Starta arkitekturutredning.
- Starta juridisk eller dataskyddsrättslig fördjupning.
- Förbereda produktionssättning enligt godkänd referensarkitektur.

Varje beslut bör dokumenteras kort, gärna som ett architecture decision record när det har arkitekturkonsekvenser.

## Steg 5: Produktionsgodkännande

Innan en AI-lösning går i produktion behöver myndigheten kontrollera mer än att tekniken fungerar.

Minimikrav för produktionsgodkännande:

- verksamhetsägare är utsedd,
- system- eller produktägarskap är tydligt,
- informationsklassning är genomförd,
- personuppgiftsfrågor är hanterade,
- säkerhetskrav och loggning är implementerade,
- användare vet hur AI-stödet får användas,
- begränsningar och felkällor är dokumenterade,
- incidentprocess finns,
- uppföljningsmått är definierade,
- avvecklings- eller omprövningspunkt finns.

Det sista är viktigt. AI-lösningar ska inte bara godkännas en gång. Modeller, data, lagkrav, leverantörsvillkor och verksamhetsprocesser förändras.

## Exempel från Tullverket Aurora

Tullverket Aurora får in tre AI-initiativ samma månad.

Det första är ett internt stöd för att sammanfatta offentliga styrdokument och interna mötesanteckningar utan personuppgifter. Det använder en redan godkänd AI-assistent och ett begränsat dokumenturval. Triage placerar initiativet i styrklass A eller B beroende på om interna anteckningar kan innehålla skyddsvärd information. Beslutet blir att använda befintlig plattform med tydlig användarinstruktion och begränsad loggning.

Det andra är ett RAG-baserat kunskapsstöd för handläggare som söker i interna rutiner, rättsliga ställningstaganden och ärendehandböcker. Här finns risk för föråldrade svar, felaktig tolkning och oavsiktlig exponering av dokument. Initiativet placeras i styrklass C. AI-governanceforumet godkänner en pilot, men kräver informationsägare, dokumentklassning, behörighetsstyrt index, svar med källhänvisning, loggning och tydlig begränsning: AI-stödet får inte fatta beslut.

Det tredje är ett prediktivt prioriteringsstöd för kontrollverksamhet. Det kan påverka vilka ärenden som granskas först och kan därmed få rättsliga, etiska och förtroendemässiga konsekvenser. Initiativet placeras i styrklass D. AI-styrgruppen beslutar att en särskild förstudie krävs innan tekniskt arbete får börja. Förstudien ska omfatta rättslig bedömning, modellrisk, datakvalitet, transparens, mänsklig kontroll, uppföljning och alternativa icke-AI-lösningar.

Poängen med modellen är att alla tre initiativ kan hanteras, men inte på samma sätt.

## Dokumentation som governance-verktyg

Dokumentation ska inte bara skapas för revision. Den ska hjälpa myndigheten att fatta bättre beslut och återanvända kunskap.

För varje AI-initiativ bör följande dokumentation finnas på rätt nivå:

- use-case canvas,
- triagebedömning,
- informationsklassning,
- juridiska ställningstaganden,
- arkitekturbeslut,
- riskbedömning,
- modell- eller leverantörsbeskrivning,
- test- och valideringsresultat,
- användarinstruktion,
- produktionsgodkännande,
- uppföljnings- och omprövningsplan.

För enklare styrklass A-initiativ kan dokumentationen vara kort. För styrklass D behöver den vara omfattande. Governance ska vara proportionerlig.

## Centralt och federerat ansvar

En vanlig fråga är om AI-förmågan ska styras centralt eller federerat. Det bästa svaret är ofta båda, men för olika saker.

Centralt bör myndigheten styra:

- principer,
- policy,
- riskklassning,
- godkända arkitekturmönster,
- gemensam plattform,
- informationssäkerhetskrav,
- leverantörsvillkor,
- dokumentationsmallar,
- portföljöversikt,
- produktionsgodkännande för högre risknivåer.

Federerat kan verksamhetsnära team äga:

- behovsformulering,
- användningsfall,
- lokal processanpassning,
- användarstöd,
- domänkunskap,
- mätning av nytta,
- förbättringsförslag,
- operativ förvaltning inom givna ramar.

För Tullverket Aurora innebär detta att huvudkontoret inte ska detaljstyra varje AI-idé, men inte heller låta varje avdelning välja egen plattform och egna riskregler.

## Beslutsartefakter i målarkitekturen

Governance bör synas i målarkitekturen som konkreta artefakter. Annars blir den osynlig för projekt och leverantörer.

Minst följande bör ingå:

- AI-governancemodell,
- roll- och ansvarskarta,
- beslutsflöde från idé till produktion,
- styrklassmodell,
- RACI för centrala beslut,
- mall för architecture decision records,
- portföljmodell för AI-användningsfall,
- undantagsprocess,
- modell för produktionsgodkännande,
- modell för uppföljning och omprövning.

Detta gör att målarkitekturen inte bara beskriver teknikens framtida läge, utan även hur myndigheten styr vägen dit.

## Vägvalsfrågor

- Vilka AI-beslut ska fattas centralt och vilka kan delegeras till produkt- eller verksamhetsteam?
- Vilka användningsfall kräver formellt godkännande innan pilot?
- Vilka roller får stoppa ett AI-initiativ och på vilka grunder?
- Hur dokumenteras arkitekturbeslut så att de kan följas upp över tid?
- När ska governance-modellen vara rådgivande och när ska den vara styrande?

## Vanliga fallgropar

- **Fallgrop: Ett AI-råd utan beslutskraft.**
  - Varför det händer: Organisationen skapar ett forum men ger det inget mandat.
  - Hur du undviker det: Definiera vilka beslut forumet får fatta och vilka beslut som ska eskaleras.

- **Fallgrop: Alla initiativ granskas lika tungt.**
  - Varför det händer: Rädslan för AI-risk gör att även lågriskfall får tung process.
  - Hur du undviker det: Använd styrklasser och proportionerlig dokumentation.

- **Fallgrop: Juridik och säkerhet kommer in för sent.**
  - Varför det händer: Teamen vill först visa att tekniken fungerar.
  - Hur du undviker det: Gör triage obligatoriskt innan pilot med verkliga data.

- **Fallgrop: Governance blir en broms i stället för ett styrsystem.**
  - Varför det händer: Processen fokuserar på nej, inte på villkorade ja.
  - Hur du undviker det: Ge beslutsalternativ som sandlåda, pilot, komplettering och återanvändning.

- **Fallgrop: Ingen äger modellen efter driftsättning.**
  - Varför det händer: Projektet lämnar över applikationen men inte modellens livscykel.
  - Hur du undviker det: Kräv produktägarskap för modell, data, promptar, kunskapsbas och uppföljning.

## Checklista

Använd checklistan när målarkitekturen ska beskriva AI-governance:

- Finns ett tydligt flöde från idé till produktion och avveckling?
- Är AI-användningsfall registrerade i en gemensam portfölj?
- Finns en triagemodell som fångar nytta, risk, data, juridik och teknik?
- Finns styrklasser eller motsvarande nivåindelning?
- Är det tydligt vilka beslut som är strategiska, taktiska och operativa?
- Har varje forum definierat mandat?
- Är verksamhetsägare och informationsägare obligatoriska roller?
- Är arkitektur, juridik, säkerhet och dataskydd inkopplade vid rätt beslutspunkt?
- Finns en undantagsprocess med kompensatoriska kontroller?
- Finns minimikrav för produktionsgodkännande?
- Finns krav på omprövning, uppföljning och avveckling?
- Är governance-modellen tillräckligt enkel för lågriskfall och tillräckligt robust för högriskfall?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Governance och beslutsmodell är den del av målarkitekturen som gör resten av arkitekturen användbar. Utan governance blir principerna svåra att tillämpa, riskklassningen ojämn och tekniska plattformar svåra att förvalta. Med governance kan myndigheten styra vilka användningsfall som går vidare, vilka byggblock som återanvänds, vilka risker som kräver särskild granskning och vilka lösningar som får gå i produktion.

I nästa kapitel flyttar vi fokus från beslutsmodellen till förmågekartan. Där beskriver vi vilka organisatoriska och tekniska förmågor Tullverket Aurora behöver etablera för att AI inte bara ska vara en serie projekt, utan en långsiktigt styrd myndighetsförmåga.
