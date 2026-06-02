# Kapitel 4: Juridik, ansvar och regelefterlevnad

## Varför detta kapitel finns

AI-målarkitektur i en statlig myndighet kan inte tas fram som ett rent teknikarbete. Juridik, ansvar, informationshantering och regelefterlevnad påverkar vilka användningsfall som får prioriteras, vilken data som får användas, vilka tekniska miljöer som är möjliga och vilka kontroller som måste byggas in från början.

För en erfaren IT-arkitekt är den viktiga poängen inte att själv ersätta jurist, dataskyddsombud, säkerhetsspecialist eller upphandlare. Poängen är att förstå när juridiken blir arkitekturdrivande. En målarkitektur för AI behöver därför innehålla mekanismer som gör det möjligt att identifiera rättsliga krav tidigt, dokumentera vägval, spåra ansvar och stoppa användningsfall som inte kan hanteras säkert.

I Tullverket Aurora blir detta tydligt när tre till synes närliggande AI-idéer visar sig ha helt olika rättsliga och arkitekturella konsekvenser:

- intern kunskapssökning i styrdokument,
- sammanfattning av ärendehandlingar,
- riskanalys som påverkar prioritering av kontroller.

Alla tre kan beskrivas som AI-stöd, men de innebär olika grad av personuppgiftsbehandling, sekretessrisk, påverkan på enskilda, krav på mänsklig kontroll och behov av dokumentation.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför juridik och regelefterlevnad behöver vara en del av målarkitekturen,
- skilja mellan juridisk bedömning av ett enskilt användningsfall och arkitekturkrav som bör gälla för flera AI-lösningar,
- identifiera centrala rättsområden som påverkar AI i statlig myndighet,
- formulera en praktisk ansvarskedja för AI-användningsfall,
- beskriva hur juridisk triage bör byggas in i AI-portfölj och införandeprocess,
- koppla juridiska krav till tekniska byggblock som loggning, åtkomstkontroll, dokumentation, modellstyrning och mänsklig kontroll.

## Viktig avgränsning

Detta kapitel är inte juridisk rådgivning och försöker inte ge uttömmande tolkningar av lagstiftning. Kapitlet beskriver hur en IT-arkitekt bör strukturera juridiska och regulatoriska frågor i målarkitekturarbetet. Varje konkret AI-användningsfall behöver bedömas tillsammans med myndighetens jurister, dataskyddsombud, informationssäkerhetsfunktion, upphandlingsfunktion och ansvarig verksamhet.

## Arkitekturproblemet

Det vanligaste misstaget är att behandla juridik som en kontrollpunkt i slutet av ett AI-initiativ. Då har verksamheten redan formulerat nyttan, utvecklingsteamet har valt verktyg, data har börjat flyttas och leverantören har kanske redan etablerats. Juridiken blir då ett hinder i stället för en styrande del av designen.

För AI är detta särskilt riskabelt eftersom flera frågor behöver avgöras tidigt:

- Vilken data skickas till modellen?
- Innehåller promptar, dokument eller loggar personuppgifter?
- Förekommer sekretessbelagd eller säkerhetsskyddsvärd information?
- Påverkar AI-stödet enskilda, företag eller andra myndigheter?
- Är användningen intern, handläggarstödjande, beslutsstödjande eller automatiserad?
- Vem ansvarar för felaktiga rekommendationer eller missvisande sammanfattningar?
- Vilka krav gäller för transparens, dokumentation och mänsklig kontroll?
- Var behandlas data och under vilken jurisdiktion?
- Vilka underbiträden, modellleverantörer och molntjänster ingår i kedjan?

Målarkitekturen behöver ge svar på hur sådana frågor fångas, bedöms och omsätts i arkitekturkrav. Den ska inte lösa varje juridisk fråga i detalj, men den ska säkerställa att rätt frågor ställs i rätt ordning.

## Centrala rättsområden

En statlig myndighet som etablerar AI-förmåga behöver normalt beakta flera rättsområden samtidigt. De överlappar och kan inte hanteras som separata checklistor.

| Område | Arkitekturell betydelse |
|---|---|
| AI-reglering | Påverkar riskklassning, dokumentation, mänsklig kontroll och krav på styrning. |
| Dataskydd | Styr hur personuppgifter får behandlas, minimeras, loggas, delas och raderas. |
| Offentlighet och sekretess | Påverkar vilka uppgifter som får exponeras, indexeras, skickas till modeller eller lämnas ut. |
| Informationssäkerhet | Styr skyddsnivå, åtkomst, loggning, incidenthantering och driftsmiljö. |
| Arkiv och dokumenthantering | Påverkar hur promptar, utdata, beslut, loggar och dokumentation ska bevaras eller gallras. |
| Förvaltningsrätt | Påverkar rättssäkerhet, motivering, insyn och myndighetens ansvar vid handläggning. |
| Upphandling och avtal | Styr leverantörsvillkor, datalokalisering, underbiträden, revision, exit och inlåsning. |
| Säkerhetsskydd | Kan påverka om vissa data, system eller driftmodeller över huvud taget är tillåtna. |

För målarkitekturen innebär detta att AI-förmågan behöver en gemensam juridisk och regulatorisk kontrollmodell. Det räcker inte att varje projekt gör sin egen bedömning i efterhand.

## AI Act som arkitekturdrivande regelverk

EU:s AI Act är riskbaserad. Det innebär att kraven beror på vilken typ av AI-system som används och vilken risk användningen innebär. För en myndighet är den arkitektoniska konsekvensen att AI-användningsfall inte kan behandlas som en enhetlig teknikkategori. De behöver klassas, dokumenteras och styras utifrån risk.

AI Act trädde i kraft den 1 augusti 2024. Huvudregeln är att den blir fullt tillämplig två år senare, den 2 augusti 2026, med vissa bestämmelser som gäller tidigare eller senare. En målarkitektur som tas fram under denna period bör därför utformas för kommande tillämpning, inte bara för dagens lägsta krav.

För arkitekturen innebär AI Act framför allt att myndigheten behöver kunna visa:

- vilken typ av AI-system ett användningsfall avser,
- vilken roll myndigheten har i relation till systemet,
- vilken riskkategori som är relevant,
- vilka kontroller som används för mänsklig översyn,
- hur data, modell, instruktioner och resultat dokumenteras,
- hur fel, incidenter och förändringar hanteras,
- hur användare informeras och utbildas,
- hur leverantörer och tredjepartskomponenter styrs.

AI Act bör därför inte bara hanteras som juridisk text. Den bör översättas till styrbara arkitekturkrav.

AI Act bör hanteras som ett levande kravområde i målarkitekturen. Regelverket har trätt i kraft och tillämpas stegvis, samtidigt som vägledning, standardisering och nationell tillämpning fortsätter att utvecklas. Arkitekturen bör därför inte bygga på ett enda statiskt datum, utan innehålla en regulatorisk bevakningspunkt inför större beslut, särskilt för användningsfall som kan bli högrisk eller där ansvarsfördelningen är komplex.

## GDPR och personuppgifter

När AI-lösningar behandlar personuppgifter gäller dataskyddsreglerna parallellt med AI-reglering. För en statlig myndighet är detta ofta centralt, eftersom många verksamhetsprocesser innehåller uppgifter om fysiska personer, företagare, kontaktpersoner, resande, anställda eller andra berörda.

Ur arkitekturperspektiv behöver varje AI-användningsfall kunna svara på följande frågor:

- Vilka personuppgifter behandlas?
- Varför behövs de för användningsfallet?
- Vilken rättslig grund åberopas?
- Kan uppgifterna minimeras, pseudonymiseras eller uteslutas?
- Skickas uppgifter till extern tjänst, modellleverantör eller underbiträde?
- Sparas promptar, svar, embeddings eller loggar på ett sätt som innehåller personuppgifter?
- Hur hanteras rättigheter, gallring och åtkomst?
- Behövs konsekvensbedömning avseende dataskydd?

En särskild risk i generativ AI är att personuppgifter kan förekomma i flera lager samtidigt. De kan finnas i användarens prompt, i dokument som hämtas via RAG, i modellens svar, i säkerhetsloggar, i applikationsloggar och i leverantörens övervakningsdata. Därför behöver målarkitekturen definiera var personuppgifter får förekomma, var de inte får förekomma och hur de detekteras eller begränsas.

## Offentlighet, sekretess och handlingar

Statliga myndigheter behöver även tänka på hur AI interagerar med offentlighetsprincipen, sekretessregler och dokumenthantering. En AI-lösning kan skapa nya informationsobjekt: promptar, sammanfattningar, rekommendationer, förklaringar, loggar, utvärderingar, modellutdata och beslutstöd.

Arkitekturfrågan blir då inte bara om informationen är korrekt. Frågan är också vilken status informationen har i myndighetens informationshantering.

Tullverket Aurora behöver till exempel avgöra:

- om promptar och AI-svar ska betraktas som arbetsmaterial, ärendeinformation eller logginformation,
- när en AI-genererad sammanfattning blir en del av ett ärende,
- hur länge olika AI-relaterade loggar ska sparas,
- om sökindex eller embeddings kan innehålla sekretessbelagd information,
- vem som får söka i vilka kunskapskällor,
- hur utlämnandefrågor ska hanteras när AI-relaterad information efterfrågas.

Detta får direkta konsekvenser för tekniska lösningar. RAG-index, vektordatabaser, auditloggar och promptarkiv måste designas med samma noggrannhet som andra informationsbärande komponenter.

## Ansvarskedjan

AI får inte göra ansvar otydligt. En myndighet kan använda AI som stöd, men ansvar för myndighetsutövning, informationshantering, säkerhet, dataskydd och beslut måste fortfarande vara placerat hos människor och organisatoriska funktioner.

En praktisk ansvarskedja för AI bör minst omfatta följande roller.

| Roll | Ansvar i målarkitekturen |
|---|---|
| Verksamhetsägare | Äger behov, nytta, processpåverkan och verksamhetsrisk. |
| Informationsägare | Ansvarar för informationsklassning, tillåten användning och åtkomstprinciper. |
| Systemägare eller produktägare | Ansvarar för lösningens funktion, förvaltning och prioriteringar. |
| Modellägare | Ansvarar för modellval, modellversion, validering och uppföljning där myndigheten själv styr modellen. |
| Arkitekturfunktion | Säkerställer att lösningen följer målarkitektur, principer och referensarkitektur. |
| Informationssäkerhetsfunktion | Bedömer säkerhetskrav, skyddsåtgärder och incidentförmåga. |
| Dataskyddsombud eller dataskyddsfunktion | Ger råd och kontrollerar dataskyddsfrågor där personuppgifter behandlas. |
| Juridisk funktion | Bedömer rättsliga frågor, ansvar, förvaltningsrätt, sekretess och avtal. |
| Upphandlingsfunktion | Säkerställer att krav, avtal, leverantörsstyrning och exit hanteras. |
| Användaransvarig chef | Säkerställer utbildning, instruktioner och kontrollerad användning i vardagen. |

Målarkitekturen bör göra det tydligt att en AI-lösning inte får gå från pilot till produktion utan utsedd ansvarskedja.

## Juridisk triage i AI-portföljen

Kapitel 3 etablerade behovet av use-case triage. I detta kapitel fördjupas den juridiska delen. Triage ska inte vara ett tungt juridiskt projekt för varje idé, men det ska snabbt sortera användningsfall i rätt spår.

En enkel modell är att varje AI-idé först bedöms genom sex frågor:

1. Behandlas personuppgifter?
2. Förekommer sekretessbelagd eller särskilt skyddsvärd information?
3. Kan användningen påverka enskilda, företag eller andra externa parter?
4. Används AI som assistent, kunskapsstöd, beslutsstöd eller automatiserad komponent?
5. Ska data skickas till extern leverantör, molntjänst eller modell som myndigheten inte själv kontrollerar?
6. Finns behov av särskild dokumentation, transparens, mänsklig kontroll eller konsekvensbedömning?

Svar på dessa frågor avgör vilket arkitekturspår användningsfallet får gå vidare i.

| Triageutfall | Typisk innebörd | Arkitekturkonsekvens |
|---|---|---|
| Låg juridisk risk | Intern användning med okänslig information och mänsklig kontroll. | Kan hanteras i kontrollerad sandlåda med standardvillkor. |
| Medelhög risk | Personuppgifter, verksamhetsdata eller påverkan på intern process. | Kräver tydlig informationsklassning, loggning, behörighet och juridisk granskning. |
| Hög risk | Sekretess, känslig data, betydande påverkan eller beslutsnära användning. | Kräver formell riskbedömning, ansvarskedja, starka kontroller och ofta särskild driftmodell. |
| Ej tillåten eller pausad | Användningen saknar laglig grund, rimlig kontroll eller acceptabel risknivå. | Ska stoppas, omformas eller vänta tills styrning och teknik kan hantera kraven. |

Denna triage bör finnas som ett gemensamt steg i myndighetens AI-portfölj, inte som ett valfritt dokument per projekt.

## Exempel från Tullverket Aurora

Tullverket Aurora gör juridisk triage av tre användningsfall.

| Användningsfall | Första juridiska bedömning | Arkitekturspår |
|---|---|---|
| Intern kunskapssökning i styrdokument | Låg till medelhög risk om källorna är interna men inte sekretessbelagda. | RAG i kontrollerad miljö med behörighetsstyrda källor och loggning. |
| Sammanfattning av ärendehandlingar | Medelhög till hög risk eftersom handlingar kan innehålla personuppgifter och sekretess. | Begränsad miljö, stark åtkomstkontroll, dataminimering, loggpolicy och mänsklig kontroll. |
| Riskanalys för kontrollprioritering | Hög risk eftersom resultat kan påverka operativ prioritering och indirekt enskilda eller företag. | Formell riskklassning, juridisk granskning, modellvalidering, förklarbarhet, governance och beslutsdokumentation. |

Aurora upptäcker att de tre användningsfallen inte bör lösas med samma generella AI-assistent. Det första kan möjligen stödjas av en gemensam intern RAG-tjänst. Det andra kräver en striktare zon och tydligare logik för vad som får skickas till modellen. Det tredje kräver en mer kontrollerad beslutsstödsarkitektur, där modellens roll, mänsklig kontroll och uppföljning är centrala.

Slutsatsen är att juridisk triage inte bara sorterar risk. Den driver arkitekturspår.

## Regelefterlevnad som byggblock i målarkitekturen

En mogen AI-målarkitektur behöver göra regelefterlevnad praktiskt genomförbar. Det räcker inte att skriva principer. Det måste finnas byggblock, processer och kontroller som gör principerna användbara i utveckling och drift.

Följande byggblock bör övervägas i målarkitekturen:

- AI-use-case register där varje användningsfall dokumenteras.
- Beslutslogg för arkitekturbeslut och juridiska vägval.
- Gemensam triagemodell för juridik, risk, data och säkerhet.
- Mallar för konsekvensbedömning, informationsklassning och modellbeskrivning.
- Behörighetsmodell som kopplar användare till tillåtna datakällor och AI-funktioner.
- AI-gateway som kan styra åtkomst, loggning, policy och leverantörsanrop.
- Loggstrategi som skiljer mellan säkerhetslogg, användningslogg, promptlogg och ärendedokumentation.
- Modellregister eller komponentregister för modeller, versioner, leverantörer och användningsområden.
- Kontrollpunkter inför pilot, produktionssättning och större förändring.
- Incidentprocess för AI-relaterade fel, dataläckage, felaktiga svar och otillåten användning.

Dessa byggblock behöver inte alla vara avancerade från dag ett, men de behöver finnas som målbild. Annars blir regelefterlevnad beroende av manuella undantag.

För Tullverket Aurora innebär detta att varje betydande AI-användningsfall behöver kunna klassas, tilldelas ansvarig roll, dokumenteras, granskas och följas upp. Mänsklig kontroll, transparens, loggning och ändrade tillämpningsdatum ska kunna hanteras utan att hela målarkitekturen behöver göras om.

## Dokumentation som arkitekturkrav

AI-lösningar behöver dokumenteras på ett sätt som går att följa över tid. Dokumentationen ska inte enbart finnas för revision. Den ska hjälpa arkitekter, jurister, säkerhetsspecialister och verksamhetsägare att förstå varför lösningen ser ut som den gör.

För varje AI-användningsfall bör minst följande dokumenteras:

- syfte och verksamhetsnytta,
- användargrupp och process,
- AI-roll,
- datakällor och informationsklasser,
- personuppgiftsbehandling,
- modell eller modelltyp,
- leverantörer och underbiträden,
- riskklassning,
- mänsklig kontroll,
- loggning och bevarande,
- kända begränsningar,
- arkitekturbeslut,
- godkännanden och omprövningsdatum.

Dokumentationen bör vara kopplad till portföljstyrning och arkitekturbeslut. Om den bara finns som bilagor i projektmappar kommer den snabbt att bli inaktuell.

## Mänsklig kontroll och rättssäkerhet

Mänsklig kontroll är inte en formulering som kan läggas till i efterhand. Den behöver designas.

För ett AI-baserat handläggarstöd behöver arkitekten till exempel veta:

- var i processen AI används,
- vad användaren ser,
- vad användaren förväntas kontrollera,
- om AI-svaret kan kopieras in i ett ärende,
- om systemet markerar osäkerhet,
- om källor och underlag visas,
- om avvikelser kan rapporteras,
- om det går att följa hur AI-svaret uppstod,
- om användaren har utbildning och instruktioner.

I Tullverket Aurora beslutar arkitekturgruppen att AI-stöd i ärenden alltid ska visa källor när det bygger på interna dokument. För beslutsnära användning ska systemet dessutom markera att AI-svaret är ett stöd och inte ett myndighetsbeslut. Dessa krav blir inte bara användargränssnittsfrågor. De påverkar RAG-design, loggning, behörighet, testning och dokumentation.

## Leverantörer och avtalsvillkor

Många AI-tjänster består av flera lager: applikation, AI-plattform, modellleverantör, molninfrastruktur, observability-tjänster, säkerhetskomponenter och underbiträden. Myndigheten behöver förstå hela kedjan.

Innan en AI-tjänst används bör arkitekten och upphandlingsfunktionen kunna besvara följande:

- Var behandlas data geografiskt och juridiskt?
- Används kunddata för modellträning, förbättring eller felsökning?
- Vilka underbiträden ingår?
- Hur hanteras loggar, promptar och utdata?
- Finns möjlighet att stänga av datalagring eller modellträning?
- Vilka revisioner, intyg och säkerhetsåtaganden finns?
- Hur fungerar exit, dataexport och radering?
- Kan myndigheten byta modell eller leverantör utan att bygga om hela lösningen?
- Vilka villkor ändras om tjänsten används via SaaS, API, privat instans eller on-premises?

Dessa frågor påverkar målarkitekturens leverantörsstrategi. En myndighet kan mycket väl använda molnbaserade AI-tjänster för vissa användningsfall, men samma lösning är inte automatiskt lämplig för sekretessbelagda ärendedata eller beslutsnära riskanalys.

## När juridiken påverkar moln eller on-premises

Driftmodell ska inte väljas enbart utifrån teknikpreferens. Juridik och regelefterlevnad kan göra vissa val mer eller mindre lämpliga.

| Situation | Möjlig arkitekturell slutsats |
|---|---|
| Intern produktivitet med okänslig information | SaaS eller molntjänst kan vara rimlig om avtal, dataskydd och loggning är hanterade. |
| Personuppgifter i större skala | Kräver tydlig rättslig grund, dataskyddsbedömning, biträdeskedja och kontroll över lagring. |
| Sekretessbelagd information | Kräver strikt informationsklassning, särskild åtkomstkontroll och ofta begränsad driftmodell. |
| Säkerhetsskyddsvärd information | Kan kräva särskild prövning och kan utesluta vissa moln- eller leverantörsalternativ. |
| Beslutsnära användning | Kräver dokumentation, mänsklig kontroll, validering och ofta starkare styrning än enkel assistentfunktion. |
| Egen modellutveckling | Kräver livscykelkontroll, datastyrning, modellregister och tydligt modellansvar. |

Det viktiga är inte att påstå att moln alltid är rätt eller att on-premises alltid är säkrast. Det viktiga är att målarkitekturen ger en spårbar beslutsmodell.

## Vägvalsfrågor

När myndigheten tar fram målarkitektur för AI bör arkitekten ställa följande vägvalsfrågor:

1. Ska juridisk triage vara obligatorisk för alla AI-användningsfall?
2. Vilka användningsfall får hanteras i en gemensam AI-sandlåda?
3. Vilka informationsklasser får aldrig skickas till externa AI-tjänster?
4. När krävs särskild dataskyddsbedömning?
5. När krävs formellt arkitekturbeslut innan pilot?
6. Hur dokumenteras AI-systemets roll i verksamhetsprocessen?
7. Vem ansvarar för modellval, modellbyte och modelluppföljning?
8. Hur säkerställs mänsklig kontroll i beslutsnära processer?
9. Vilka loggar ska sparas, var och hur länge?
10. Hur hanteras leverantörsvillkor som tillåter modellträning på kunddata?
11. Vilka krav ska alltid finnas i upphandling av AI-tjänster?
12. När måste användningsfallet stoppas eller omformas?

Dessa frågor bör integreras i målarkitekturens beslutsmodell och inte behandlas som informella diskussionspunkter.

## Vanliga fallgropar

- **Fallgrop: Juridiken kommer in för sent.**
  - Varför det händer: AI-initiativ startar ofta som snabba experiment.
  - Konsekvens: Lösningen kan behöva byggas om eller stoppas när data, ansvar eller leverantörsvillkor granskas.
  - Motåtgärd: Inför juridisk triage redan i idé- och portföljsteget.

- **Fallgrop: Alla AI-användningsfall behandlas lika.**
  - Varför det händer: Organisationen ser AI som en teknik i stället för flera riskprofiler.
  - Konsekvens: Antingen överstyr man enkla användningsfall eller underskyddar känsliga.
  - Motåtgärd: Klassificera användningsfall efter AI-roll, data, påverkan och driftmodell.

- **Fallgrop: Promptar och loggar glöms bort.**
  - Varför det händer: Fokus ligger på dokument och databaser, inte på interaktionen med modellen.
  - Konsekvens: Personuppgifter eller sekretess kan hamna i loggar, supportdata eller leverantörsmiljöer.
  - Motåtgärd: Definiera loggstrategi, dataminimering och retention tidigt.

- **Fallgrop: Ansvar blir otydligt när AI ger rekommendationer.**
  - Varför det händer: Organisationen antar att mänsklig kontroll räcker utan att beskriva den.
  - Konsekvens: Handläggare, chefer och systemägare vet inte vem som ansvarar för fel.
  - Motåtgärd: Dokumentera ansvarskedja och mänsklig kontroll för varje användningsfall.

- **Fallgrop: Leverantörens standardvillkor styr arkitekturen.**
  - Varför det händer: Tjänsten är enkel att börja använda.
  - Konsekvens: Data, loggar, modellträning och underbiträden hanteras på ett sätt som inte passar myndigheten.
  - Motåtgärd: Kravställ AI-tjänster utifrån myndighetens informationsklasser och exitstrategi.

## Checklista för kapitel 4

Använd checklistan när ett AI-användningsfall ska bedömas juridiskt och arkitekturellt.

- Är användningsfallet tydligt beskrivet med syfte, användare och process?
- Är AI-roll angiven: assistent, kunskapsstöd, beslutsstöd eller automatiserad komponent?
- Är datakällor och informationsklasser identifierade?
- Är personuppgiftsbehandling identifierad och bedömd?
- Är sekretess och skyddsvärde bedömda?
- Är möjlig påverkan på enskilda, företag eller externa parter beskriven?
- Är preliminär AI Act-riskklassning dokumenterad?
- Är ansvarskedjan utsedd?
- Är mänsklig kontroll beskriven som praktisk process, inte bara princip?
- Är leverantörer, underbiträden och driftlandskap kartlagda?
- Är promptar, svar, embeddings och loggar inkluderade i informationshanteringen?
- Är dokumentation, bevarande och gallring bedömda?
- Finns beslut om vilket arkitekturspår användningsfallet tillhör?
- Finns omprövningspunkt när lagtolkning, leverantörsvillkor eller modellversion förändras?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Kapitlets viktigaste arkitekturbudskap är att juridik och regelefterlevnad måste översättas till förmågor, byggblock och beslutspunkter. En AI-målarkitektur för en statlig myndighet bör därför innehålla:

- gemensam juridisk triage,
- register över AI-användningsfall,
- ansvarskedja per användningsfall,
- klassning av AI-roll och risknivå,
- dokumenterade arkitekturbeslut,
- styrning av personuppgifter, sekretess och loggar,
- krav på mänsklig kontroll,
- leverantörs- och avtalskrav,
- beslutsmodell för moln, on-premises och hybrid,
- kontrollpunkter före pilot och produktion.

När Tullverket Aurora går vidare till informationsklassning i nästa kapitel är juridiken därför inte ett separat spår. Den är redan en del av arkitekturens grundstruktur.


## Snabb sammanfattning

AI i statlig myndighet kräver att juridik, ansvar och regelefterlevnad byggs in i målarkitekturen från början. AI Act, GDPR, offentlighet och sekretess, arkivregler, förvaltningsrätt, informationssäkerhet och upphandling påverkar både vilka användningsfall som kan genomföras och hur tekniska lösningar måste utformas.

Den praktiska lösningen är inte att varje AI-projekt gör sin egen sena juridiska granskning. Myndigheten behöver en gemensam triagemodell, tydlig ansvarskedja, dokumenterade arkitekturbeslut och tekniska byggblock som gör efterlevnad möjlig i vardagen.

Nästa kapitel går djupare in i informationsklassning, dataskydd och riskstyrning. Där blir frågan mer konkret: vilken information får användas i vilken AI-miljö, med vilka skydd och med vilken driftmodell?
