# Kapitel 1: Från AI-experiment till myndighetsgemensam AI-förmåga

## Syfte med kapitlet

Det första arkitekturproblemet är sällan att välja modell, molnplattform eller vektordatabas. Det första problemet är att förstå vad myndigheten egentligen försöker etablera. En större statlig myndighet som har experimenterat med AI har ofta redan bevisat att tekniken kan vara användbar i enskilda situationer. Det betyder inte att myndigheten har en AI-förmåga.

Det här kapitlet beskriver skillnaden mellan lokala AI-experiment och en myndighetsgemensam AI-förmåga. Kapitlet visar också varför målarkitekturen behöver börja med förmåga, styrbarhet och risk innan den går in i tekniska plattformsval.

Efter kapitlet ska läsaren kunna:

- skilja mellan AI-experiment, AI-lösning och AI-förmåga
- beskriva varför lokala experiment inte automatiskt kan skalas till produktion
- identifiera de första arkitekturfrågorna som bör ställas innan plattformsval
- formulera en första struktur för hur en myndighet går från test till styrd förmåga
- använda Tullverket Aurora som ett återkommande exempel för att resonera om införandet

## Arkitekturproblemet

Många organisationer börjar sin AI-resa på samma sätt. Några teknikintresserade medarbetare testar en generativ AI-tjänst. En verksamhetsenhet bygger en prototyp för att sammanfatta dokument. Ett datateam testar en prediktiv modell på historiska data. En innovationsfunktion skapar en sandlåda. En leverantör visar en lovande demo.

Det är inte fel. Experiment behövs. Problemet uppstår när organisationen tolkar experimenten som bevis för att förmågan redan finns.

En prototyp kan visa att något är möjligt. Den visar däremot inte automatiskt att lösningen är rättssäker, spårbar, informationssäker, förvaltningsbar, kostnadskontrollerad, upphandlingsbar eller möjlig att integrera i myndighetens ordinarie arkitektur. Den visar inte heller att det finns en tydlig ansvarskedja när AI-stöd används i handläggning, analys eller verksamhetskritiska beslut.

För en statlig myndighet är detta särskilt viktigt. Myndigheten kan inte enbart optimera för innovationstakt. Den måste samtidigt kunna visa att AI-användningen följer rättsliga krav, informationssäkerhetskrav, interna styrmodeller, arkitekturprinciper och förvaltningsansvar. AI-förmågan måste därför vara både möjliggörande och kontrollerande.

Den centrala arkitekturfrågan blir därför:

> Hur etablerar myndigheten en AI-förmåga som gör det möjligt att använda AI i relevant omfattning, utan att varje initiativ behöver uppfinna sin egen juridik, säkerhet, datamodell, tekniska plattform och förvaltningsmodell?

Detta är en annan fråga än “vilken AI-produkt ska vi använda?”. Produktvalet kommer senare. Först behöver myndigheten förstå vilken förmåga den behöver bygga.

## Från experiment till förmåga

Ett AI-experiment är en avgränsad prövning. Det kan vara en teknisk proof of concept, en verksamhetsnära pilot, en testmiljö för generativ AI eller en begränsad analysmodell. Experimentet har ofta låg formell komplexitet, få användare, begränsad datamängd och otydlig koppling till ordinarie förvaltning.

En AI-lösning är mer konkret. Den har ett specifikt användningsfall, en målgrupp, en teknisk implementation och någon form av drift- eller användningsmodell. En lösning kan till exempel vara ett internt frågeverktyg baserat på RAG, en modell för dokumentklassificering eller ett assistentstöd för sammanfattning av ärenden.

En AI-förmåga är bredare. Den omfattar de strukturer som gör att myndigheten kan identifiera, bedöma, utveckla, införa, använda, övervaka, förbättra och avveckla AI-lösningar över tid. Förmågan består av teknik, men också av juridik, styrning, roller, data, säkerhet, metoder, finansiering, kompetens och arkitektur.

Skillnaden kan sammanfattas så här:

| Nivå | Fråga | Typiskt resultat | Risk om nivån blandas ihop |
|---|---|---|---|
| AI-experiment | Kan detta fungera? | Prototyp, demo eller pilot | Organisationen tror att tekniken är produktionsklar |
| AI-lösning | Hur stödjer vi ett visst användningsfall? | Applikation, modell eller tjänst | Lösningen blir isolerad och svår att förvalta |
| AI-förmåga | Hur kan myndigheten använda AI säkert och återkommande? | Styrning, plattform, processer och arkitektur | Varje initiativ bygger egna mönster och egna risker |

Målarkitekturen ska i första hand beskriva den tredje nivån. Den ska inte bara beskriva en teknisk lösning för ett enskilt användningsfall. Den ska visa hur myndigheten vill kunna arbeta med AI som återkommande förmåga.

## Varför experiment inte räcker

Experiment har ofta andra villkor än produktion. Under ett experiment kan organisationen acceptera manuella kontroller, begränsat användarantal och osäker dokumentation. I produktion förändras kraven.

En produktionssatt AI-lösning behöver kunna hantera åtminstone följande frågor:

- Vem är ansvarig för användningsfallet?
- Vilken information behandlas?
- Finns personuppgifter, sekretessbelagd information eller annan skyddsvärd data?
- Vilken rättslig grund eller vilket rättsligt stöd finns för behandlingen?
- Vilka användare får använda lösningen?
- Hur styrs åtkomst till data, promptar, modeller och loggar?
- Hur dokumenteras modellval, datakällor, begränsningar och risker?
- Hur upptäcks fel, driftstörningar, hallucinationer eller otillåten användning?
- Hur hanteras ändringar i modell, promptar, datakällor och integrationspunkter?
- Hur avvecklas lösningen om risk, kostnad eller rättsläge förändras?

Enskilda experiment besvarar sällan allt detta. Det är därför myndigheten behöver en strukturerad övergång från experiment till förmåga.

Det är också vanligt att experiment skapar en skev bild av kostnad och komplexitet. En liten pilot kan vara billig eftersom den använder manuellt arbete, fria testnivåer, en begränsad datamängd eller ett isolerat team. När lösningen ska införas brett tillkommer kostnader för säkerhet, integration, drift, support, övervakning, incidenthantering, upphandling, dokumentation och förvaltning.

Det är inte ett argument mot AI. Det är ett argument för att behandla AI som arkitekturfråga, inte som isolerad tekniktest.

## Tullverket Aurora: nuläget

Tullverket Aurora är en fiktiv större statlig tullmyndighet. Myndigheten har ett samhällskritiskt uppdrag och hanterar stora mängder information: ärenden, tulldeklarationer, regelverk, styrdokument, kontrollinformation, analysunderlag, samverkansdata och interna rutiner.

Aurora har under det senaste året genomfört flera mindre AI-experiment:

- ett team har testat generativ AI för att sammanfatta långa interna styrdokument
- en verksamhetsenhet har prövat ett frågegränssnitt mot interna handböcker
- ett analysområde har experimenterat med maskininlärning för att hitta mönster i historiska data
- IT har testat en molnbaserad AI-tjänst i en avskild miljö
- några handläggare har använt publika AI-verktyg för att formulera utkast till texter, utan att det funnits en tydlig myndighetsgemensam rutin

De flesta testerna har gett positiva signaler. Medarbetare ser möjligheter till snabbare informationssökning, bättre sammanfattningar och effektivare analys. Samtidigt finns tydliga problem:

- juridik och dataskydd har involverats olika mycket i olika tester
- informationsklassning har inte gjorts på samma sätt
- vissa team vill använda molnbaserade lösningar medan andra kräver on-premises
- det saknas en gemensam syn på loggning och spårbarhet
- det saknas gemensamma kriterier för när AI får användas i handläggarstöd
- det finns ingen beslutad målarkitektur
- det finns ingen gemensam livscykel för modeller, promptar, datakällor eller AI-tjänster

Aurora står alltså inte inför frågan om AI är intressant. Den frågan är redan besvarad. Den nya frågan är hur myndigheten etablerar en kontrollerad AI-förmåga.

## Vad myndigheten behöver etablera

En myndighetsgemensam AI-förmåga kan beskrivas som ett antal samverkande delområden. Målarkitekturen behöver inte lösa alla detaljer i första versionen, men den behöver visa hur delområdena hänger ihop.

### Styrning och ansvar

AI-förmågan behöver tydliga beslutspunkter. Någon måste kunna avgöra vilka användningsfall som får gå vidare, vilka risker som kräver särskild prövning och vilka arkitekturprinciper som är obligatoriska. Det behövs också ansvar för modeller, data, plattform, informationssäkerhet, juridik och verksamhetsnytta.

För Aurora innebär detta att AI inte kan vara ett rent IT-initiativ. Juridik, säkerhet, dataskydd, verksamhet, arkitektur och IT behöver ingå i samma styrmodell, även om de inte alltid behöver fatta alla beslut tillsammans.

### Use-case triage

Alla AI-användningsfall är inte lika riskfyllda. En intern assistent som hjälper en medarbetare att sammanfatta öppen utbildningstext är något annat än ett stöd som påverkar prioritering av tullkontroller eller handläggningsbeslut. Myndigheten behöver därför en gemensam triage där användningsfall klassas utifrån nytta, data, rättslig påverkan, säkerhet, automatiseringsgrad och konsekvens för enskilda.

Triage är en arkitekturfråga eftersom den styr vilka tekniska och organisatoriska mönster som får användas.

### Informations- och datagrund

AI behöver data, men myndigheten kan inte låta AI-lösningar få godtycklig åtkomst till information. Det behövs ordning på informationsägarskap, datakvalitet, metadata, behörighet, sökindex, loggning och dataminimering. För generativ AI behöver myndigheten dessutom hantera promptar, kontext, embeddings och modellutdata som informationsobjekt.

För Aurora betyder detta att intern kunskapssökning i regelverk och rutiner inte bara handlar om att lägga dokument i ett index. Myndigheten behöver veta vilka dokument som är gällande, vem som ansvarar för dem, vilka som får läsa dem och hur svar ska kunna spåras tillbaka till källor.

### Teknisk plattform

Den tekniska plattformen behöver stödja flera typer av AI-lösningar. Den kan omfatta modellåtkomst, AI-gateway, RAG-lager, orkestrering, vektordatabas, MLOps, LLMOps, övervakning, behörighet, loggning, säkerhetskontroller och integrationer.

Plattformen behöver inte vara en enda produkt. Den bör snarare förstås som en sammanhängande arkitektur av komponenter och kontroller. För vissa användningsfall kan en SaaS-tjänst vara rimlig. För andra krävs mer kontrollerad drift, egen modellservering eller on-premises-miljö.

### Livscykelhantering

AI-förmågan behöver processer för hela livscykeln. Det räcker inte att utveckla eller köpa en modell. Myndigheten behöver kunna testa, validera, produktionssätta, övervaka, ändra, pausa och avveckla AI-lösningar.

För generativ AI gäller detta inte bara modellen. Även promptar, systeminstruktioner, RAG-index, datakällor, säkerhetsfilter och utvärderingsdataset behöver versionshanteras och förvaltas.

### Kompetens och arbetssätt

AI-förmåga kräver nya samarbeten. Arkitekter behöver förstå juridiska och verksamhetsmässiga begränsningar. Jurister behöver förstå hur tekniska val påverkar risk. Säkerhetsfunktioner behöver kunna bedöma nya hotbilder. Verksamheten behöver förstå att AI inte är magi, utan ett stöd med begränsningar.

För Aurora blir ett viktigt mål att skapa tvärfunktionella arbetssätt där AI-initiativ inte fastnar i separata stuprör.

## Den första ordningen

En vanlig fälla är att börja med plattformsjämförelse. Det kan kännas konkret, men det leder ofta fel. Plattformen ska väljas utifrån behov, risk och styrning, inte tvärtom.

En mer robust första ordning är:

1. Beskriv varför myndigheten behöver AI-förmåga.
2. Inventera befintliga experiment och användningsfall.
3. Kategorisera användningsfallen efter nytta, risk och datakänslighet.
4. Etablera preliminära principer för AI-användning.
5. Definiera vilka beslut som måste fattas centralt och vilka som kan fattas lokalt.
6. Identifiera de minsta gemensamma arkitekturbyggblocken.
7. Skapa en kontrollerad sandlåda för lärande och jämförelse.
8. Välj ett litet antal representativa piloter.
9. Ta fram referensarkitektur och målarkitektur iterativt.
10. Förbered för produktion, förvaltning och uppföljning.

Denna ordning gör att myndigheten kan lära sig utan att låsa in sig för tidigt. Den gör också att arkitekturen utvecklas tillsammans med juridik, informationsklassning och verksamhetsbehov.

## Ett första förmågemönster

För att konkretisera kan Aurora beskriva sin första AI-förmåga med fem nivåer.

### Nivå 1: Kontrollerad användning

Myndigheten beslutar vilka externa eller interna AI-verktyg som får användas, för vilka ändamål och med vilken information. Fokus ligger på policy, användarstöd, riskmedvetenhet och grundläggande kontroller.

För Aurora innebär detta att medarbetare får tydliga regler för vad som aldrig får matas in i publika AI-tjänster, vilka godkända verktyg som finns och hur AI-genererat material ska granskas.

### Nivå 2: Gemensam sandlåda

Myndigheten etablerar en teknisk och juridiskt granskad miljö där team kan testa AI med kontrollerade data. Sandlådan används för lärande, metodutveckling och jämförelse av lösningsmönster.

För Aurora kan sandlådan innehålla avidentifierade eller syntetiska dokument, testade modellanslutningar och ett enkelt RAG-mönster för interna styrdokument.

### Nivå 3: Styrda piloter

Utvalda användningsfall får gå vidare som piloter med tydlig ansvarig verksamhet, riskbedömning, dokumentation och teknisk lösningsskiss. Piloterna ska inte bara visa nytta, utan också testa målarkitekturens antaganden.

Aurora väljer exempelvis intern kunskapssökning och sammanfattning av icke-sekretessbelagda ärendehandlingar som tidiga piloter, medan mer känsligt prioriteringsstöd får vänta tills riskmodell och dataarkitektur är tydligare.

### Nivå 4: Produktionsförmåga

Myndigheten har gemensamma byggblock för identitet, behörighet, loggning, modellåtkomst, övervakning, incidenthantering och livscykelhantering. AI-lösningar kan tas i produktion utan att varje team uppfinner allt från början.

För Aurora innebär detta att en verksamhetslösning kan använda en godkänd AI-gateway, etablerade loggkrav, standardiserad källspårning och gemensamma rutiner för förändring av promptar och datakällor.

### Nivå 5: Skalad och förvaltad AI-portfölj

AI är en del av myndighetens ordinarie portföljstyrning. Det finns återkommande uppföljning av nytta, risk, kostnad, kvalitet och efterlevnad. Arkitekturen utvecklas med nya krav, modeller och leverantörsförutsättningar.

Aurora kan då hantera flera AI-lösningar parallellt utan att förlora kontrollen över ansvar, data, modellval och drift.

## Exempel från Tullverket Aurora

I Tullverket Aurora blir den första arkitekturfrågan inte vilken modell som är bäst, utan vilken förmåga myndigheten vill kunna bära över tid. Ett experiment med textsammanfattning i en enskild enhet kan vara värdefullt, men målarkitekturen behöver visa hur samma mönster kan klassas, säkras, följas upp och återanvändas i andra delar av myndigheten.

I scenariot används därför Aurora som en röd tråd: varje nytt AI-initiativ ska kunna kopplas till en ansvarig verksamhetsägare, ett informationsflöde, en riskklass, en teknisk driftmodell och en förvaltningsbar lösningskomponent.

## Vägvalsfrågor

Innan myndigheten tar fram sin första detaljerade målarkitektur bör arkitekten samla beslutsfattare kring ett antal vägvalsfrågor.

- Vilka AI-användningsfall är strategiskt viktigast de kommande två åren?
- Vilka användningsfall är lämpliga för tidig pilot och vilka bör vänta?
- Vilka dataklasser får användas i vilka typer av AI-miljöer?
- Ska myndigheten börja med intern produktivitets-AI, verksamhetsnära handläggarstöd eller analysstöd?
- Vilka beslut måste ägas centralt?
- Vilka delar av AI-förmågan ska vara gemensamma för hela myndigheten?
- Vilka lösningsmönster får användas innan målarkitekturen är fullt beslutad?
- Vilken risknivå kräver särskild juridisk, säkerhetsmässig eller arkitektonisk prövning?
- Hur ska myndigheten undvika att varje avdelning etablerar sin egen AI-stack?
- Hur ska lärdomar från experiment återföras till målarkitektur och principer?

Dessa frågor är avsiktligt breda. De hjälper myndigheten att undvika att teknikval blir substitut för styrning.

## Vanliga fallgropar

### Att börja med verktyg i stället för förmåga

Det vanligaste misstaget är att inleda med en jämförelse mellan plattformar eller modeller. Det kan vara relevant senare, men först behöver myndigheten veta vilka användningsfall, dataklasser, risknivåer och styrkrav som plattformen ska stödja.

### Att behandla AI som ett innovationsspår vid sidan av ordinarie arkitektur

AI kan börja i innovation, men kan inte stanna där. När användningsfallen påverkar verklig verksamhet måste de in i ordinarie arkitektur, säkerhet, juridik, förvaltning och portföljstyrning.

### Att tro att en policy räcker

En policy kan säga vad som är tillåtet, men den skapar inte automatiskt tekniska kontroller, behörighetsmodeller, loggning, uppföljning eller livscykelhantering. Policy behöver omsättas i arkitektur.

### Att underskatta datafrågan

AI-diskussioner börjar ofta med modeller, men misslyckas ofta på grund av data. Saknad informationsklassning, låg datakvalitet, otydligt informationsägarskap och bristande metadata gör AI-lösningar svåra att skala.

### Att skapa för många lokala lösningar

Lokala initiativ kan skapa tempo, men de kan också skapa fragmentering. Om varje enhet väljer egen AI-tjänst, egen vektordatabas, egna promptmönster och egen loggning blir den samlade risken snabbt större än nyttan.

### Att vänta på den perfekta målarkitekturen

Motsatt misstag är att försöka rita hela målarkitekturen färdig innan någon lär sig något praktiskt. AI-området förändras snabbt, och myndigheten behöver arbeta iterativt. En första målarkitektur bör vara styrande men inte orimligt detaljerad.

## Checklista

Använd denna checklista när myndigheten ska bedöma om den fortfarande befinner sig i experimentfas eller har börjat etablera verklig AI-förmåga.

- Finns en gemensam definition av vad AI-förmåga betyder för myndigheten?
- Finns en aktuell inventering av AI-experiment och AI-idéer?
- Finns en gemensam modell för att triagera användningsfall?
- Är juridik, dataskydd och informationssäkerhet involverade enligt en beslutad process?
- Finns preliminära arkitekturprinciper för AI?
- Finns regler för vilka data som får användas i olika AI-miljöer?
- Finns en kontrollerad sandlåda eller annan godkänd testmiljö?
- Finns beslut om vilka AI-byggblock som ska vara gemensamma?
- Finns en plan för hur piloter kan bli produktionssatta lösningar?
- Finns någon som äger den samlade målarkitekturen för AI?
- Finns en mekanism för att föra lärdomar från piloter tillbaka till arkitektur, principer och styrning?
- Finns en tydlig gräns mellan tillåten individuell användning av AI-verktyg och myndighetsgodkända AI-lösningar?

Om svaret är nej på flera av dessa frågor är myndigheten troligen fortfarande i experimentfas, även om det finns flera lovande prototyper.

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Det här kapitlet etablerar bokens grundtes: AI i en större statlig myndighet bör behandlas som en förmåga, inte som en samling verktyg. Målarkitekturen ska därför beskriva hur myndigheten vill kunna använda AI över tid, med rätt styrning, rätt datahantering, rätt teknik och rätt ansvar.

I nästa kapitel fördjupas vad målarkitektur betyder i AI-sammanhang. Där skiljer vi mellan nuläge, målbild, referensarkitektur, lösningsarkitektur och roadmap. Det är den distinktionen som gör det möjligt att senare diskutera juridik, informationsklassning, tekniska byggblock, plattformar och driftmodeller utan att blanda ihop nivåerna.
