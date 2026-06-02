# Kapitel 2: Vad målarkitektur betyder för AI

## Varför detta kapitel finns

När en myndighet börjar arbeta mer systematiskt med AI uppstår snabbt en praktisk fråga: vad är det egentligen som ska tas fram? Ett strategidokument räcker inte. En teknisk plattform räcker inte heller. Ett antal pilotprojekt säger inte hur myndigheten ska kunna skala, styra, säkra och förvalta AI över tid.

Målarkitekturens uppgift är att beskriva det önskade framtida arkitekturläget och göra det möjligt att ta stegvisa beslut i rätt riktning. För AI är detta särskilt viktigt eftersom tekniken påverkar flera arkitekturområden samtidigt: verksamhetsförmågor, data, integration, säkerhet, juridik, drift, leverantörsstyrning och organisation.

En bra AI-målarkitektur ska därför inte vara en teknisk ritning över en enskild lösning. Den ska vara ett styrande underlag för hur myndigheten vill etablera AI som förmåga.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan nuläge, målarkitektur, referensarkitektur, lösningsarkitektur och roadmap
- förklara varför AI-målarkitektur behöver omfatta både teknik, styrning, data, juridik och arbetssätt
- avgränsa vad som bör ingå i en första målarkitektur för AI
- använda arkitekturbeslut som ett sätt att göra vägval spårbara
- bedöma när en myndighet behöver gemensam referensarkitektur respektive lösningsspecifik arkitektur

## Arkitekturproblemet

Många organisationer börjar sitt AI-arbete genom att fråga vilken plattform eller modell de ska använda. Det är förståeligt men riskabelt. Plattformen är bara en del av målbilden.

För en större statlig myndighet är den egentliga frågan bredare:

> Vilket framtida läge behöver myndigheten nå för att kunna använda AI på ett rättssäkert, säkert, kontrollerat, effektivt och återanvändbart sätt?

Det framtida läget måste beskriva mer än teknik. Det måste bland annat svara på följande frågor:

- Vilka typer av AI-användning ska myndigheten stödja?
- Vilka data får användas, i vilka miljöer och med vilka skydd?
- Hur ska juridisk bedömning, informationsklassning och riskprövning kopplas till arkitekturval?
- Vilka gemensamma komponenter behövs?
- När får verksamheten använda färdiga AI-tjänster?
- När krävs kontrollerad intern plattform?
- Hur ska modeller, promptar, kunskapskällor, loggar och beslut hanteras över livscykeln?
- Vilka arkitekturbeslut ska vara gemensamma och vilka får vara lokala?

Utan målarkitektur blir varje AI-initiativ ett separat vägval. Då växer teknisk skuld, juridisk osäkerhet och leverantörsberoende snabbt.

## Centrala begrepp

### Nuläge

Nuläget beskriver hur myndigheten arbetar i dag. För AI handlar nuläget inte bara om vilka verktyg som används. Det omfattar även dataförutsättningar, kompetens, juridiska processer, säkerhetsförmåga, befintlig infrastruktur, styrmodeller och pågående experiment.

Ett användbart nuläge bör svara på frågor som:

- Vilka AI-experiment pågår?
- Vilka verktyg används informellt eller formellt?
- Vilka datakällor används eller efterfrågas?
- Vilka riskbedömningar görs i dag?
- Vilka miljöer finns för utveckling, test och produktion?
- Vilka beslut saknas eller fattas ad hoc?
- Vilka delar av organisationen driver AI-frågan?

Nuläget ska inte bli en katalog över allt som finns. Det ska visa vilka utgångspunkter som påverkar vägen mot målarkitekturen.

### Målarkitektur

Målarkitektur, eller *target architecture*, beskriver ett önskat framtida arkitekturläge. Den ska visa hur verksamhet, information, applikationer, teknik, säkerhet och styrning ska hänga ihop när myndigheten har etablerat en mer mogen AI-förmåga.

För AI bör målarkitekturen minst beskriva:

- styrande principer för AI
- förmågor som behöver etableras
- informations- och datamönster
- tekniska byggblock
- integrationsmönster
- säkerhets- och kontrollmekanismer
- drift- och plattformsmodeller
- ansvar, roller och beslutsforum
- vägval och arkitekturbeslut
- stegvis införande

Målarkitekturen ska vara tillräckligt konkret för att styra beslut, men inte så detaljerad att den blir en lösningsdesign för ett enskilt system.

### Referensarkitektur

Referensarkitektur beskriver ett återanvändbart mönster för en typ av lösning eller förmåga. Där målarkitekturen beskriver det önskade framtida läget för myndigheten kan referensarkitekturen beskriva hur återkommande AI-lösningar bör byggas.

Exempel på referensarkitekturer för AI kan vara:

- referensarkitektur för intern generativ AI-assistent
- referensarkitektur för RAG-baserat kunskapsstöd
- referensarkitektur för modellservering i kontrollerad miljö
- referensarkitektur för AI-stödd ärendesammanfattning
- referensarkitektur för prediktiv analys med MLOps

Referensarkitekturen gör det möjligt att återanvända godkända mönster i flera lösningar. Den minskar behovet av att varje projekt uppfinner sin egen säkerhetsmodell, integrationsmodell och driftmodell.

### Lösningsarkitektur

Lösningsarkitektur beskriver hur ett specifikt användningsfall ska realiseras. Den är mer detaljerad än både målarkitektur och referensarkitektur.

Om Tullverket Aurora till exempel vill skapa ett AI-stöd för intern sökning i styrdokument kan lösningsarkitekturen beskriva:

- vilka dokumentkällor som ingår
- hur dokument indexeras
- vilken vektordatabas som används
- vilken språkmodell som används
- hur behörighet kontrolleras
- hur promptar konstrueras
- hur svar loggas
- hur felaktiga svar rapporteras
- hur lösningen driftsätts

Lösningsarkitekturen ska följa målarkitekturen och återanvända relevanta referensarkitekturer. Om den avviker behöver avvikelsen vara medveten och dokumenterad.

### Roadmap

En roadmap beskriver hur myndigheten rör sig från nuläge till målarkitektur. Den ska inte bara vara en projektplan. För AI bör den beskriva den ordning som minskar risk och bygger förmåga stegvis.

En enkel roadmap kan innehålla steg som:

1. Etablera styrning, principer och juridisk triage.
2. Kartlägga nuläge och användningsfall.
3. Införa kontrollerad sandlåda.
4. Ta fram referensarkitektur för prioriterade mönster.
5. Välja första gemensamma plattformskomponenter.
6. Produktionssätta lågrisklösningar.
7. Etablera MLOps eller LLMOps där det behövs.
8. Skala till mer verksamhetskritiska användningsfall.
9. Förvalta portfölj, modeller, risker och leverantörer.

Roadmapen är därmed målarkitekturens genomförandespår.

### Arkitekturbeslut

Ett arkitekturbeslut är ett dokumenterat vägval. Det kan beskrivas som en *Architecture Decision Record*, ofta förkortat ADR.

AI-området kräver tydliga arkitekturbeslut eftersom många val får konsekvenser för juridik, säkerhet, drift och ekonomi. Exempel på beslut är:

- Myndigheten ska använda en gemensam AI-gateway för åtkomst till externa och interna modeller.
- Sekretessklassad information får inte skickas till publika AI-tjänster utan särskilt beslut.
- RAG ska vara förstahandsmönster för kunskapsstöd innan finjustering övervägs.
- Produktionssatta AI-lösningar ska ha ägare, loggning, incidentprocess och livscykelplan.
- Vissa användningsfall ska endast köras on-premises eller i särskilt kontrollerad miljö.

Ett bra arkitekturbeslut beskriver beslutet, sammanhanget, övervägda alternativ, konsekvenser, giltighet och omprövningspunkt.

## Rekommenderat angreppssätt

### Börja med arkitekturens syfte

Det första steget är att tydliggöra varför målarkitekturen tas fram. Syftet bör inte uttryckas som “välja AI-plattform”. Ett bättre syfte är att beskriva vilken organisatorisk förmåga myndigheten behöver etablera.

Ett exempel:

> Målarkitekturen ska ange hur myndigheten stegvis etablerar en gemensam AI-förmåga som gör det möjligt att pröva, utveckla, driftsätta och förvalta AI-lösningar på ett rättssäkert, säkert, spårbart och kostnadseffektivt sätt.

En sådan formulering visar att teknik är nödvändig men inte tillräcklig.

### Definiera arkitekturens omfattning

AI är ett brett område. Därför behöver den första målarkitekturen avgränsas. Det är ofta bättre att skapa en första version som styr rätt beslut än att försöka täcka alla möjliga AI-frågor.

En första målarkitektur kan till exempel omfatta:

- generativ AI för interna användare
- RAG-baserat kunskapsstöd
- hantering av AI-användningsfall från idé till produktion
- gemensamma principer för moln, on-premises och hybrid
- övergripande krav på säkerhet, loggning och livscykel
- beslutsmodell för plattformsval och riskklassning

Den kan samtidigt uttryckligen avgränsa bort:

- detaljerad modellträning för specialiserade ML-modeller
- fullständig dataplattformsmodernisering
- automatiserat beslutsfattande med rättsverkan
- medborgarnära AI-tjänster med hög risk
- detaljerad produktjämförelse mellan leverantörer

Avgränsning är inte ett sätt att undvika ansvar. Det är ett sätt att göra arbetet styrbart.

### Skilj på gemensamma och lokala beslut

En central uppgift för målarkitekturen är att avgöra vilka beslut som ska vara gemensamma för myndigheten och vilka beslut som kan fattas lokalt.

Gemensamma beslut bör normalt omfatta:

- principer för AI-användning
- miniminivå för juridisk och säkerhetsmässig bedömning
- krav på loggning, spårbarhet och incidenthantering
- godkända driftmodeller för olika informationsklasser
- gemensamma integrations- och åtkomstmönster
- krav på modell- och tjänsteleverantörer
- ansvar för förvaltning och livscykel

Lokala beslut kan ofta omfatta:

- exakt användargränssnitt
- verksamhetsspecifika arbetsflöden
- prioritering inom godkänd portfölj
- lokala promptmallar inom gemensamma regler
- lösningsdetaljer som inte påverkar gemensamma risker

Om allt blir gemensamt blir myndigheten långsam. Om allt blir lokalt blir myndigheten osäker och fragmenterad. Målarkitekturen behöver hitta balansen.

### Beskriv förmågor före produkter

Ett återkommande misstag är att beskriva målarkitekturen som en lista över produkter. Det gör arkitekturen bräcklig. Produkter förändras, avtal löper ut och tekniken utvecklas snabbt.

Börja i stället med förmågor. Exempel på AI-förmågor är:

- ta emot och bedöma AI-idéer
- klassificera data och risk
- välja godkänt AI-mönster
- ge åtkomst till modeller
- bygga RAG-lösningar
- testa kvalitet och säkerhet
- driftsätta AI-lösningar
- övervaka användning och kostnad
- hantera incidenter
- ompröva eller avveckla lösningar

När förmågorna är tydliga blir det enklare att välja produkter och plattformar. Då kan varje produkt bedömas utifrån vilken förmåga den stödjer och vilka risker den introducerar.

### Använd lager i målarkitekturen

En praktisk AI-målarkitektur bör kunna visas i lager. Lagren gör det lättare att diskutera olika typer av vägval utan att blanda ihop dem.

Ett användbart lagerperspektiv är:

1. Verksamhets- och användningsfallslager.
2. Styrnings- och risklager.
3. Informations- och datalager.
4. AI- och modellager.
5. Integrations- och orkestreringslager.
6. Säkerhets- och identitetslager.
7. Drift-, plattforms- och infrastrukturlager.
8. Observability-, logg- och livscykellager.

Poängen är inte att varje lager måste bli ett eget dokument. Poängen är att målarkitekturen ska synliggöra beroenden mellan verksamhet, regler, data och teknik.

### Dokumentera beslut tidigt

AI-målarkitektur blir snabbt föremål för många diskussioner. Vissa handlar om teknik. Andra handlar om juridik, riskaptit, ekonomi eller organisation. Om besluten inte dokumenteras kommer samma frågor tillbaka i varje pilot.

Därför bör arkitekturarbetet tidigt införa en enkel beslutslogg. Varje större vägval bör dokumenteras med:

- beslut
- datum
- beslutsägare
- bakgrund
- alternativ
- konsekvenser
- vilka användningsfall beslutet gäller
- när beslutet ska omprövas

Det viktigaste är inte formatet. Det viktigaste är spårbarheten.

## Exempel från Tullverket Aurora

Tullverket Aurora har under två år testat AI i begränsad skala. Flera delar av organisationen har experimenterat:

- HR har prövat textsammanfattning av interna dokument.
- En analysenhet har testat språkmodeller för att sammanfatta rapporter.
- IT har byggt en enkel prototyp för intern kunskapssökning.
- En verksamhetsavdelning vill använda AI för att prioritera dokumentgranskning.
- Några team använder publika AI-verktyg informellt för textbearbetning.

När myndighetsledningen ber om en AI-målarkitektur uppstår först en missuppfattning. Flera aktörer förväntar sig att arkitekterna ska rekommendera en produkt eller välja mellan moln och on-premises.

Arkitekturgruppen väljer i stället att rama in arbetet som en målarkitektur för AI-förmåga. De delar upp uppdraget i sex frågor:

1. Vilka AI-användningsfall ska myndigheten kunna stödja de kommande två åren?
2. Vilka risk- och informationsklasser ska hanteras?
3. Vilka gemensamma principer ska gälla?
4. Vilka byggblock behöver vara gemensamma?
5. Vilka driftmodeller är tillåtna för olika typer av data?
6. Vilka beslut måste fattas nu och vilka kan skjutas upp?

Resultatet blir inte en färdig lösningsdesign. Resultatet blir en styrande målbild.

Auroras första version av målarkitekturen innehåller:

- en nulägesbild över experiment och brister
- principer för AI-användning
- en klassning av prioriterade användningsfall
- beslut om att börja med intern generativ AI och RAG-baserat kunskapsstöd
- krav på gemensam AI-gateway
- krav på att känsliga data endast får användas i godkända miljöer
- en preliminär referensarkitektur för intern kunskapssökning
- en roadmap för 0–24 månader
- en beslutslogg för större vägval

Det gör att Tullverket Aurora kan fortsätta experimentera, men inom tydligare ramar.

## Vad målarkitekturen bör innehålla

En första AI-målarkitektur för en större myndighet bör vara tillräckligt komplett för att styra kommande beslut. Den behöver inte vara perfekt. Den behöver vara användbar.

### Arkitekturens sammanhang

Beskriv varför målarkitekturen behövs och vilka problem den ska lösa. Detta bör inkludera nuläge, drivkrafter, risker och koppling till myndighetens uppdrag.

Exempel på drivkrafter:

- behov av effektivare handläggarstöd
- ökande informationsvolymer
- behov av bättre kunskapssökning
- tryck från verksamheten att använda generativ AI
- behov av kontrollerad innovation
- krav på rättssäkerhet och dataskydd
- risk för okontrollerad skugg-AI

### Omfattning och avgränsningar

Ange vad målarkitekturen omfattar och vad den inte omfattar. Det gör dokumentet lättare att använda och minskar risken för felaktiga förväntningar.

En tydlig avgränsning kan vara:

> Denna version omfattar intern AI-användning och verksamhetsstödjande AI-lösningar. Den omfattar inte automatiserat beslutsfattande med rättsverkan eller publika medborgartjänster.

Avgränsningen kan senare ändras, men då ska den ändras medvetet.

### Principer

Principerna ska styra beslut när detaljer saknas. För AI bör principerna vara både arkitektoniska och verksamhetsmässiga.

Exempel:

- AI-lösningar ska ha tydlig ägare och livscykel.
- Informationsklassning ska styra teknik- och driftval.
- Mänsklig kontroll ska finnas där AI påverkar bedömningar eller beslut.
- Gemensamma byggblock ska återanvändas innan nya lokala lösningar införs.
- Modellutdata ska inte behandlas som fakta utan verifiering i relevanta processer.
- Spårbarhet ska byggas in från början.
- Leverantörsinlåsning ska minimeras där det är praktiskt och ekonomiskt rimligt.

Principer ska inte vara slogans. De ska kunna användas för att fatta beslut.

### Förmågor

Målarkitekturen bör beskriva vilka förmågor myndigheten behöver etablera. Detta gör målbilden mindre produktberoende.

Exempel på förmågeområden:

- AI-portföljstyrning
- juridisk och säkerhetsmässig triage
- dataåtkomst och datakvalitet
- modellåtkomst och modellval
- prompt- och kunskapsbasförvaltning
- test och validering
- driftsättning
- observability och kostnadsuppföljning
- incidenthantering
- leverantörsstyrning
- avveckling

Förmågorna kan senare mappas till roller, processer, system och plattformar.

### Byggblock

Byggblock är de komponenter och mönster som återkommer i flera lösningar.

Vanliga byggblock i AI-målarkitektur är:

- AI-gateway
- modellkatalog eller modellregister
- RAG-lager
- vektordatabas eller sökindex
- API-lager
- identitets- och behörighetsintegration
- logg- och observability-plattform
- policy enforcement
- test- och utvärderingsmiljö
- sandlådemiljö
- modellservering
- promptförvaltning
- kunskapskällor och dokumentpipeline

Byggblock ska beskrivas på rätt nivå. En målarkitektur behöver inte alltid ange produkt, men den bör ange funktion, ansvar och viktiga krav.

### Driftmodeller

AI-målarkitekturen bör beskriva vilka driftmodeller som är tillåtna och när de kan användas.

Exempel:

- SaaS för lågkänsliga interna produktivitetsfall
- publikt moln för kontrollerade lösningar med godkända dataklasser
- sovereign cloud där jurisdiktion och operationell kontroll kräver särskild hantering
- privat moln eller on-premises för särskilt skyddsvärda data
- hybrid där data, orkestrering och modellåtkomst placeras i olika miljöer

Poängen är inte att välja en modell för allt. Poängen är att skapa en beslutsmodell som kopplar driftval till risk och nytta.

### Roadmap

Målarkitekturen ska innehålla en realistisk väg framåt. Annars blir den en framtidsbild utan genomförandekraft.

Roadmapen bör visa:

- vilka beslut som krävs först
- vilka förmågor som ska etableras i vilken ordning
- vilka pilotfall som kan användas för att validera arkitekturen
- vilka komponenter som måste vara gemensamma från början
- vilka delar som kan växa fram stegvis
- vilka beroenden som finns till dataplattform, IAM, säkerhetsarkitektur och upphandling

För AI är ordningen central. En myndighet bör normalt inte skala till känsliga, verksamhetskritiska användningsfall innan styrning, riskklassning, loggning, ansvar och incidenthantering finns på plats.

## Förhållandet mellan målarkitektur och styrning

AI-målarkitektur är inte bara en IT-artefakt. Den är också ett styrinstrument.

Det innebär att målarkitekturen behöver kopplas till:

- portföljstyrning
- informationssäkerhetsarbete
- dataskyddsprocesser
- juridisk prövning
- arkitekturstyrning
- upphandling
- verksamhetsutveckling
- förvaltningsmodell
- intern kontroll

Om målarkitekturen saknar koppling till styrning kommer den inte påverka verkliga beslut. Om styrningen saknar arkitekturstöd riskerar den att bli principer utan teknisk genomförbarhet.

En praktisk lösning är att låta målarkitekturen innehålla beslutsgrindar. Exempel:

1. Idé registreras.
2. Use-case triage genomförs.
3. Informationsklassning och juridisk förbedömning görs.
4. Godkänt referensmönster väljs.
5. Lösningsarkitektur tas fram.
6. Risk- och säkerhetsgranskning genomförs.
7. Produktion godkänns.
8. Lösningen följs upp och omprövas.

Detta gör arkitekturen operativ.

## Vägvalsfrågor

När myndigheten tar fram sin AI-målarkitektur bör arkitektgruppen åtminstone besvara följande frågor:

- Ska målarkitekturen omfatta all AI eller börja med generativ AI?
- Ska målarkitekturen omfatta både interna och externa användningsfall?
- Vilka användningsfall är förbjudna, pausade eller särskilt reglerade?
- Vilka dataklasser får användas i vilka AI-miljöer?
- Vilka beslut måste vara myndighetsgemensamma?
- Vilka delar får verksamhetsområden själva välja?
- Ska myndigheten ha en gemensam AI-gateway?
- Ska RAG vara standardmönster för kunskapsstöd?
- När är externa molntjänster tillåtna?
- När krävs on-premises eller privat drift?
- Hur ska arkitekturbeslut dokumenteras och omprövas?
- Vilka delar av målarkitekturen ska realiseras första året?

Frågorna är viktigare än att snabbt producera en snygg målbild. Fel frågor leder till fel arkitektur.

## Vanliga fallgropar

### Fallgrop: Målarkitekturen blir en produktlista

Det är vanligt att målarkitekturen reduceras till en jämförelse mellan plattformar. Då försvinner kopplingen till förmåga, ansvar, data och risk.

Undvik detta genom att beskriva förmågor och byggblock före produkter. Produkter ska komma in som möjliga realiseringar, inte som arkitekturens utgångspunkt.

### Fallgrop: Målarkitekturen blir för abstrakt

En annan risk är att målarkitekturen blir så principiell att den inte styr någonting. Ord som säker, etisk, robust och innovativ är viktiga men otillräckliga om de inte leder till beslut.

Undvik detta genom att koppla varje princip till konsekvenser. Om principen är att informationsklassning styr driftmodell ska målarkitekturen också visa hur olika klasser påverkar val mellan SaaS, moln, hybrid och on-premises.

### Fallgrop: Lösningsarkitektur blandas ihop med målarkitektur

När ett konkret pilotprojekt dominerar arbetet kan målarkitekturen bli en detaljerad design för just den lösningen. Då blir den svår att återanvända.

Undvik detta genom att skilja på tre nivåer:

- målarkitektur för myndighetens AI-förmåga
- referensarkitektur för återkommande AI-mönster
- lösningsarkitektur för ett specifikt användningsfall

### Fallgrop: Roadmapen saknar riskordning

En roadmap som bara följer teknisk leveransordning kan skapa risk. AI bör införas i en ordning som bygger styrning och kontroll innan de mest känsliga användningsfallen skalar.

Undvik detta genom att låta juridik, informationsklassning, säkerhet och driftförmåga påverka ordningen.

### Fallgrop: Arkitekturbeslut dokumenteras inte

När AI-området rör sig snabbt kan organisationen fatta många tillfälliga beslut. Om de inte dokumenteras blir det svårt att förstå varför en viss väg valdes.

Undvik detta genom att använda en enkel ADR-modell från början.

## Checklista

Använd checklistan för att bedöma om en första AI-målarkitektur är tillräckligt användbar.

- Är syftet med målarkitekturen tydligt?
- Är nuläget beskrivet på ett sätt som påverkar målbilden?
- Är omfattning och avgränsningar tydliga?
- Finns styrande principer som kan användas i beslut?
- Är skillnaden mellan målarkitektur, referensarkitektur och lösningsarkitektur tydlig?
- Beskrivs de viktigaste AI-förmågorna?
- Beskrivs gemensamma byggblock utan att arkitekturen blir produktberoende?
- Finns en beslutsmodell för moln, on-premises och hybrid?
- Finns koppling till juridik, informationsklassning och säkerhet?
- Finns krav på loggning, spårbarhet och livscykelhantering?
- Finns en roadmap från nuläge till målbild?
- Finns arkitekturbeslut dokumenterade eller planerade?
- Är det tydligt vilka beslut som är gemensamma och vilka som kan vara lokala?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Detta kapitel etablerar den begreppsram som resten av boken bygger på. Kapitel 3 använder ramen för att strukturera myndighetens AI-portfölj. Därefter går boken in i juridik, informationsklassning, principer och governance innan tekniska byggblock och plattformsval behandlas.

Den viktigaste slutsatsen är att målarkitektur för AI inte är samma sak som en teknisk plattform. Plattformen är ett realiseringsval. Målarkitekturen beskriver det framtida läge där myndigheten kan använda AI kontrollerat, säkert och ändamålsenligt över tid.

För Tullverket Aurora innebär detta att arkitekturgruppen inte börjar med att fråga vilken språkmodell som är bäst. De börjar med att definiera vilka förmågor, principer, byggblock, driftmodeller och beslut som krävs för att AI ska kunna bli en del av myndighetens ordinarie verksamhetsutveckling.
