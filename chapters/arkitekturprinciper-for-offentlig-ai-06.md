# Kapitel 6: Arkitekturprinciper för offentlig AI

## Varför detta kapitel finns

En målarkitektur utan principer blir lätt en ritning över teknik. En AI-förmåga i en statlig myndighet behöver mer än teknikval, integrationsmönster och plattformskomponenter. Den behöver styrande principer som hjälper arkitekter, verksamhet, juridik, säkerhet och ledning att fatta konsekventa beslut även när detaljerna förändras.

AI-området förändras snabbt. Nya modeller, molntjänster, ramverk, säkerhetsmönster och upphandlingsalternativ dyker upp löpande. Om myndigheten bara styr med produktval blir målarkitekturen snabbt föråldrad. Om den däremot styr med tydliga principer kan arkitekturen vara stabil även när implementationen ändras.

För Tullverket Aurora blir principerna en brygga mellan de föregående kapitlen och de tekniska byggblock som kommer senare. Juridik, informationsklassning och riskstyrning säger vad som måste skyddas och varför. Arkitekturprinciperna säger hur myndigheten ska tänka när den väljer lösningsmönster, driftmodell, plattform, modell, integration och kontrollnivå.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför arkitekturprinciper är nödvändiga i AI-målarkitektur,
- skilja mellan värdeprinciper, styrprinciper och tekniska designprinciper,
- formulera principer som är användbara i verkliga arkitekturbeslut,
- koppla principer till juridik, informationsklassning, säkerhet och verksamhetsnytta,
- använda principer för att styra val mellan moln, on-premises och hybrid,
- identifiera när en princip behöver undantag, kompensatoriska kontroller eller omprövning,
- beskriva hur principer bör förvaltas över tid.

## Arkitekturproblemet

Många organisationer tar fram AI-principer som låter bra men inte styr något. De kan säga att AI ska vara etisk, transparent, säker och människocentrerad. Det är rimliga ambitioner, men de hjälper inte en arkitekt som ska fatta ett konkret beslut:

- Får denna dokumentklass skickas till en extern AI-tjänst?
- Ska användningsfallet använda RAG, finjustering eller vanlig sökning?
- Behöver modellen köras i myndighetens egen miljö?
- Vilken loggning krävs för ett handläggarstöd?
- När är mänsklig kontroll tillräcklig?
- Får en modellutdata återanvändas som träningsdata?
- Hur mycket leverantörsinlåsning är acceptabelt?
- Ska plattformen vara central, federerad eller både och?

Principer behöver därför vara formulerade så att de påverkar beslut. En bra princip är inte bara ett värdeord. Den innehåller en riktning, en konsekvens och ett sätt att avgöra när den gäller.

För Tullverket Aurora blir detta tydligt när flera verksamhetsdelar vill gå olika vägar. En analysenhet vill snabbt testa en molnbaserad AI-tjänst. En handläggningsenhet vill sammanfatta ärendehandlingar. En säkerhetsfunktion vill begränsa all extern behandling. En innovationsgrupp vill använda open source-modeller. Utan gemensamma principer blir varje initiativ ett separat förhandlingsfall.

## Vad en arkitekturprincip ska göra

En arkitekturprincip ska hjälpa organisationen att välja. Den ska inte ersätta analys, juridisk bedömning eller riskklassning, men den ska göra beslutsriktningen tydlig.

En användbar princip bör ha fem delar:

- namn,
- formulering,
- motiv,
- konsekvens,
- exempel på tillämpning.

Exempel:

| Del | Exempel |
|---|---|
| Namn | Klassning före plattformsval |
| Formulering | AI-lösningar ska inte välja modell, molntjänst eller driftmiljö innan användningsfallets information, risk och ansvar är klassade. |
| Motiv | Fel driftmiljö kan skapa sekretessrisk, dataskyddsrisk och svag spårbarhet. |
| Konsekvens | Use-case triage och informationsklassning blir obligatoriska före pilot med verkliga data. |
| Tillämpning | Intern kunskapssökning kan använda kontrollerad molntjänst, men ärendesammanfattning kräver striktare miljö. |

Principen är användbar eftersom den påverkar faktisk ordning, beslutspunkt och arkitekturkrav.

## Tre nivåer av principer

AI-principer bör delas upp i tre nivåer. Annars blandas övergripande värden med tekniska lösningsregler.

### Värdeprinciper

Värdeprinciper uttrycker vad myndigheten vill skydda och uppnå. De är nära kopplade till uppdrag, rättssäkerhet och förtroende.

Exempel:

- AI ska stärka myndighetens uppdrag utan att försvaga rättssäkerhet.
- AI ska användas så att ansvar kan förstås och utkrävas.
- AI ska stödja människor i myndighetsutövning, inte dölja ansvar bakom teknik.
- AI ska användas med respekt för integritet, sekretess och informationssäkerhet.

Värdeprinciper är viktiga, men de är inte tillräckliga för arkitekturbeslut.

### Styrprinciper

Styrprinciper beskriver hur användning ska kontrolleras. De kopplar värden till processer, beslut och ansvar.

Exempel:

- AI-användningsfall ska genomgå gemensam triage före pilot.
- Driftmodell ska styras av informationsklass, risknivå och rättsliga krav.
- AI-lösningar ska ha namngiven verksamhetsägare, informationsägare och tekniskt ansvarig.
- Avvikelser från målarkitekturen ska dokumenteras som arkitekturbeslut.

Styrprinciper blir särskilt viktiga i större myndigheter eftersom de förhindrar att varje avdelning skapar egna lokala regler.

### Tekniska designprinciper

Tekniska designprinciper beskriver hur lösningar ska utformas.

Exempel:

- AI-komponenter ska integreras via styrda gränssnitt, inte genom punkt-till-punkt-kopplingar.
- Promptar, hämtad kontext, modellutdata och loggar ska hanteras som informationsobjekt.
- Behörighet ska följa användarens faktiska åtkomst till källdata.
- AI-tjänster ska ha observability, spårbarhet och definierad incidenthantering.
- Modell- och leverantörsbyte ska vara möjligt utan att hela verksamhetsprocessen byggs om.

Designprinciper ska vara konkreta nog för att påverka referensarkitektur, upphandling och lösningsgranskning.

## Princip 1: Börja med uppdrag och nytta

AI ska inte införas för att tekniken finns. Den ska införas när den stödjer myndighetens uppdrag, förbättrar kvalitet, frigör kapacitet, stärker analysförmåga eller minskar risk i verksamheten.

För Tullverket Aurora innebär principen att AI-portföljen inte prioriteras utifrån vilka team som är mest tekniskt nyfikna. Den prioriteras utifrån var AI kan skapa mätbar myndighetsnytta utan att skapa oacceptabel rättslig eller säkerhetsmässig risk.

Konsekvensen för målarkitekturen är att varje AI-spår behöver kopplas till en verksamhetsförmåga. Intern kunskapssökning kopplas exempelvis till förmågan att tolka regelverk och stödja handläggare. Riskanalys kopplas till kontrollprioritering och strategisk analys. Administrativ textsammanfattning kopplas till effektivare interna arbetsflöden.

En AI-lösning som inte kan kopplas till en förmåga, en ansvarig verksamhet och en mätbar nytta bör inte drivas vidare som produktionsinitiativ.

## Princip 2: Klassning före plattformsval

Plattform, modell och driftmiljö ska inte väljas innan användningsfallets information och risk är klassade.

Detta är en av de mest praktiskt viktiga principerna i hela målarkitekturen. Den hindrar organisationen från att börja med frågan “vilket AI-verktyg ska vi använda?” och tvingar fram den mer relevanta frågan “vilken information, vilken påverkan och vilken kontrollnivå har användningsfallet?”

För Tullverket Aurora leder principen till tre olika spår:

- lågkänsliga interna texter kan hanteras i en kontrollerad molnbaserad miljö,
- ärendehandlingar med personuppgifter kräver striktare dataskydd, loggning och åtkomstkontroll,
- risk- och prioriteringsstöd kräver mänsklig kontroll, dokumentation, validering och tydlig ansvarskedja.

Principen innebär inte att moln är förbjudet. Den innebär att moln, hybrid och on-premises måste väljas efter klassning, inte efter vana eller leverantörspreferens.

## Princip 3: Mänskligt ansvar ska vara designat, inte antaget

Många AI-lösningar beskrivs som “bara stöd”. Det är ofta för otydligt. Om AI påverkar handläggning, riskbedömning, prioritering eller underlag för beslut måste mänsklig kontroll vara designad i processen.

Mänsklig kontroll betyder inte att en människa råkar finnas i närheten. Det betyder att processen är utformad så att människan kan förstå AI-stödets roll, granska underlaget, ifrågasätta resultatet, fatta beslut och dokumentera avvikelse.

För Tullverket Aurora innebär detta att ett sammanfattningsstöd för ärendehandlingar inte får presentera AI-svaret som en färdig sanning. Det behöver visa källhänvisning, osäkerhet, begränsning och eventuell ofullständighet. En handläggare måste kunna gå tillbaka till originalhandlingarna.

För risk- och prioriteringsstöd blir kravet ännu starkare. AI får inte bli ett dolt beslutsmaskineri där användaren bara följer en rekommendation. Målarkitekturen behöver därför innehålla roller, granskning, dokumentation, behörighet, loggning och mätning av hur AI-stödet faktiskt används.

## Princip 4: Transparens ska anpassas till risk och mottagare

Transparens betyder olika saker beroende på vem som behöver förstå vad.

En arkitekt behöver förstå komponenter, dataflöden, modellval och integrationer. En handläggare behöver förstå vad AI-stödet bygger sitt svar på och när det inte bör användas. En chef behöver förstå risk, ansvar och mätning. En jurist behöver förstå rättslig grund, personuppgiftsbehandling och dokumentation. En extern part kan behöva förstå när AI har använts i ett relevant led.

Därför bör målarkitekturen skilja mellan flera former av transparens:

- teknisk transparens,
- processuell transparens,
- användartransparens,
- juridisk transparens,
- revisionsbarhet.

För Tullverket Aurora innebär detta att ett RAG-baserat kunskapsstöd behöver visa vilka källor svaret bygger på. Ett internt produktivitetsverktyg kan kräva enklare användarinformation. Ett beslutsstöd med påverkan på prioritering behöver mer omfattande dokumentation, validering och möjlighet till granskning.

Transparens ska alltså inte vara maximal i alla lägen. Den ska vara tillräcklig, begriplig och anpassad till risken.

## Princip 5: Spårbarhet ska omfatta hela AI-kedjan

Traditionell systemloggning räcker inte alltid för AI. AI-kedjan kan omfatta användare, prompt, åtkomstkontroll, hämtad kontext, modellversion, verktygsanrop, modellutdata, efterbearbetning och användarens slutliga åtgärd.

Om bara API-anrop loggas blir spårbarheten otillräcklig. Myndigheten behöver kunna förstå vad som hände, varför det hände och vilken information som användes.

För Tullverket Aurora är detta särskilt viktigt när ett AI-stöd sammanfattar ärendehandlingar eller ger underlag för analys. Vid en incident, klagomål, intern granskning eller rättslig prövning kan myndigheten behöva visa:

- vilken modell eller tjänst som användes,
- vilken version eller konfiguration som gällde,
- vilken data som skickades,
- vilka dokumentutdrag som hämtades,
- vilket svar som gavs,
- vem som tog del av svaret,
- vilken mänsklig åtgärd som följde.

Spårbarhet behöver samtidigt balanseras mot dataminimering. Det är inte självklart att alla promptar och svar ska lagras länge. Principen bör därför kompletteras med gallringsregler, loggklassning och tydlig åtkomst till loggar.

## Princip 6: Dataminimering ska gälla även för AI-flöden

AI-lösningar tenderar att vilja ha mer data. Myndigheter behöver ofta göra motsatsen: begränsa data till det som behövs för ändamålet.

Dataminimering i AI handlar inte bara om träningsdata. Den gäller även promptar, hämtad kontext, embeddings, loggar, feedback, utvärderingsdata och modellutdata.

För Tullverket Aurora innebär detta att ett kunskapsstöd inte automatiskt ska indexera alla dokument som finns i myndigheten. Det ska bara indexera de dokumentkällor som är relevanta, kvalitetssäkrade, åtkomststyrda och rättsligt lämpliga för ändamålet. En RAG-lösning för interna styrdokument ska inte utan särskilt beslut blandas med ärendedata eller underrättelseinformation.

Dataminimering påverkar också arkitekturen. Den driver behov av:

- separata datadomäner,
- åtkomststyrda index,
- filtrering före modellanrop,
- begränsad loggning,
- tydliga ändamål,
- gallring och retention,
- separering mellan testdata och produktionsdata.

Principen skyddar inte bara integritet och sekretess. Den minskar också fel, kostnader, komplexitet och risken för att modellen svarar på irrelevanta eller inaktuella källor.

## Princip 7: Säkerhet ska byggas in i plattformen

AI-säkerhet får inte vara något varje projekt löser lokalt. Om varje team själv ska bygga promptfilter, loggning, åtkomstkontroll, dataskydd, incidenthantering och leverantörskontroll blir resultatet ojämnt och svårt att granska.

Målarkitekturen bör därför styra mot gemensamma säkerhetsbyggblock. Exempel:

- identitet och behörighet,
- nätverks- och zonindelning,
- secrets management,
- AI-gateway,
- policy enforcement,
- logging och monitoring,
- innehållsfilter och guardrails,
- test- och valideringsmiljöer,
- incidentflöden,
- godkända modell- och tjänstekataloger.

För Tullverket Aurora innebär principen att nya AI-användningsfall inte ska integrera direkt mot valfri modellleverantör. De ska gå via godkända mönster och kontrollerade gränssnitt. Det gör det möjligt att införa gemensam loggning, kostnadskontroll, behörighet, datafilter och spärrar mot otillåten användning.

Denna princip är central för att skala AI-förmågan. Den gör säkerhet till en del av produktionsplattformen, inte ett projektberoende tillägg.

## Princip 8: Återanvändning före lokala speciallösningar

Större myndigheter har ofta många verksamhetsgrenar, system och projekt. Utan styrning kommer varje område att bygga egen AI-stack. Det kan vara snabbt i början men dyrt och riskfyllt över tid.

Återanvändning betyder inte att alla användningsfall ska använda exakt samma lösning. Det betyder att myndigheten bör återanvända gemensamma byggblock där det är rimligt:

- triagemodell,
- principer,
- AI-gateway,
- identitetsintegration,
- loggning,
- RAG-mönster,
- modellregister,
- utvärderingsmetodik,
- leverantörskrav,
- arkitekturbeslutsmallar.

För Tullverket Aurora innebär detta att intern kunskapssökning, ärendesammanfattning och analysstöd kan använda olika driftmiljöer men ändå följa samma principer, ansvarskedjor och dokumentationsmönster.

Återanvändning minskar inte bara kostnad. Den gör också regelefterlevnad, säkerhet och förvaltning mer konsekvent.

## Princip 9: Modularitet och utbytbarhet ska prioriteras

AI-marknaden förändras snabbt. Dagens mest attraktiva modell, ramverk eller tjänst kan vara olämplig om ett år. Målarkitekturen bör därför inte låsa verksamhetsprocesser hårt till en enskild modell eller leverantör.

Modularitet innebär att viktiga delar kan bytas ut med kontrollerade konsekvenser. Det gäller exempelvis:

- språkmodell,
- embeddingmodell,
- vektordatabas,
- orkestreringsramverk,
- modellservering,
- säkerhetslager,
- observability-komponent,
- molnleverantör eller driftmiljö.

För Tullverket Aurora betyder detta att RAG-lösningen för intern kunskapssökning inte bör byggas så att alla promptar, index, behörighetsregler och källhänvisningar är hårdkodade mot en enda leverantörs egen struktur. Arkitekturen bör ha tydliga gränssnitt mellan dokumentinhämtning, indexering, behörighetsfiltrering, promptorkestrering, modellanrop och svarspresentation.

Modularitet kostar något i början. Den kräver design, testbarhet och tydliga kontrakt. Men för en myndighet med lång livslängd, upphandlingskrav och föränderliga regelverk är den ofta nödvändig.

## Princip 10: Leverantörsoberoende ska vara riskbaserat

Leverantörsoberoende betyder inte att myndigheten aldrig får använda proprietära tjänster. Det betyder att beroenden ska vara synliga, bedömda och hanterbara.

En färdig AI-tjänst kan vara rätt val för lågkänsliga interna användningsfall där nyttan är hög, risken låg och exitkostnaden acceptabel. Egen modellservering kan vara rätt val för känsliga eller strategiskt viktiga användningsfall. Hybrid kan vara rätt när vissa dataflöden måste stanna internt medan andra kan använda molnbaserade komponenter.

För Tullverket Aurora bör leverantörsberoenden bedömas utifrån:

- data som behandlas,
- avtalsvillkor,
- jurisdiktion,
- möjlighet till revision,
- modellens förändring över tid,
- export av loggar och konfiguration,
- möjlighet att byta modell,
- kompetenskrav,
- kostnadsutveckling,
- påverkan på kritiska verksamhetsprocesser.

Principen leder till en mer nyanserad hållning än “bygg allt själv” eller “köp allt som tjänst”. Den styr mot medvetna beroenden.

## Princip 11: Moln, on-premises och hybrid ska vara arkitekturspår

En myndighet bör inte formulera en enda generell regel som säger att AI alltid ska köras i moln eller alltid on-premises. AI-förmågan behöver flera arkitekturspår, styrda av information, risk, nytta och operativt behov.

En förenklad princip kan vara:

- använd kontrollerade molntjänster när informationsklass, juridik, avtal och risk tillåter det,
- använd hybrid när vissa komponenter kan dra nytta av moln men känslig data eller integration behöver skyddas närmare myndigheten,
- använd on-premises eller privat miljö när data, beroenden, säkerhet, kontinuitet eller lagkrav kräver det.

För Tullverket Aurora kan intern produktivitet och lågkänsligt kunskapsstöd börja i en kontrollerad molnmiljö. Ärendehandlingar kan kräva striktare miljö. Riskanalys med känsliga datakällor kan behöva hybrid eller on-premises beroende på data och kontrollkrav.

Det viktiga är att driftmodellen inte blir en ideologisk fråga. Den ska vara en dokumenterad arkitekturbedömning.

## Princip 12: AI ska vara mätbar i produktion

Ett AI-stöd är inte färdigt när det fungerar i en demo. Det behöver följas upp i produktion. Mätning bör omfatta både teknisk drift och verksamhetseffekt.

Exempel på mätområden:

- användning,
- svarskvalitet,
- fel och avvikelser,
- användarfeedback,
- källträffsäkerhet i RAG,
- latens och tillgänglighet,
- kostnad per användning,
- säkerhetshändelser,
- dataskyddsincidenter,
- påverkan på handläggningstid eller kvalitet,
- behov av omträning, omindexering eller modellbyte.

För Tullverket Aurora innebär detta att intern kunskapssökning inte bara mäts i antal frågor. Den bör också mätas i om svaren använder rätt källor, om användare litar för mycket på svaret, om gamla styrdokument förekommer och om felaktiga svar rapporteras.

Mätbarhet kräver att målarkitekturen innehåller observability, feedbackflöden, ägarskap och beslutspunkter för förbättring eller avveckling.

## Princip 13: Arkitekturbeslut ska vara spårbara och omprövningsbara

AI-vägval kommer att behöva ändras. Därför bör viktiga beslut dokumenteras som arkitekturbeslut med tydlig omprövningspunkt.

Ett AI-relaterat arkitekturbeslut bör minst beskriva:

- beslutet,
- bakgrunden,
- vilka alternativ som övervägdes,
- vilka risker som accepterades,
- vilka skyddsåtgärder som krävs,
- vilka antaganden beslutet bygger på,
- när beslutet ska omprövas,
- vem som äger beslutet.

För Tullverket Aurora kan ett exempel vara beslutet att tillåta en kontrollerad molnbaserad språkmodell för lågkänslig intern kunskapssökning men inte för ärendehandlingar. Beslutet bör dokumentera varför gränsen dras där, vilka datakällor som ingår, vilka loggar som sparas och när beslutet ska omprövas.

Spårbara beslut gör målarkitekturen levande. De gör också att framtida arkitekter kan förstå varför vägen valdes.

## Princip 14: Avvikelser ska vara möjliga men styrda

En målarkitektur som aldrig tillåter undantag blir ofta kringgången. En målarkitektur som tillåter alla undantag styr inget. Därför behöver undantag vara möjliga men kontrollerade.

En avvikelse bör kräva:

- motivering,
- riskbedömning,
- tidsbegränsning,
- kompensatoriska kontroller,
- ansvarig beslutsfattare,
- plan för återgång eller permanent beslut,
- dokumentation i arkitekturbeslutslogg.

För Tullverket Aurora kan en analysenhet behöva testa ett nytt verktyg i en mycket avgränsad sandlåda. Det kan vara acceptabelt om datan är syntetisk eller lågkänslig, testet är tidsbegränsat, loggning finns och resultatet inte används i operativ verksamhet. Samma verktyg skulle däremot inte vara acceptabelt för känsliga ärendehandlingar utan ny bedömning.

Undantagsprocessen är en del av innovationsförmågan. Den gör det möjligt att lära utan att tappa styrning.

## Princip 15: AI-förmågan ska kunna avveckla lösningar

Många arkitekturer fokuserar på införande men glömmer avveckling. AI-lösningar kan behöva stängas av när modellkvalitet försämras, avtal ändras, lagkrav skärps, kostnader ökar, dataunderlag blir inaktuellt eller riskprofilen förändras.

Målarkitekturen bör därför kräva att AI-lösningar har en avvecklingsbar design:

- data och loggar kan exporteras eller gallras,
- modellberoenden är dokumenterade,
- användare kan flyttas till alternativt arbetssätt,
- integrationer är identifierade,
- avtal har exitmöjlighet,
- dokumentation finns,
- beslut om avveckling kan fattas av rätt forum.

För Tullverket Aurora betyder detta att ett pilotverktyg inte får bli verksamhetskritiskt utan att först få produktionsklassad förvaltning. Om ett verktyg används i handläggning behöver det finnas en plan för vad som händer om leverantören ändrar villkor eller om modellen inte längre får användas med viss data.

Avvecklingsbarhet är en del av myndighetens kontroll över sin AI-förmåga.

## Principkatalog för Tullverket Aurora

Auroras arkitekturgrupp formulerar en första principkatalog. Den är inte en fullständig policy, men den räcker för att styra målarkitekturen och de första pilotspåren.

| Nr | Princip | Praktisk innebörd |
|---|---|---|
| 1 | Uppdrag före teknik | AI-initiativ ska kopplas till myndighetsnytta och ansvarig verksamhetsförmåga. |
| 2 | Klassning före plattformsval | Information, risk och rättsliga krav avgör driftmodell och modellval. |
| 3 | Mänskligt ansvar designas | Mänsklig kontroll ska beskrivas i processen, inte antas i efterhand. |
| 4 | Transparens efter risk | Användare, granskare och beslutsfattare ska få rätt nivå av insyn. |
| 5 | Spårbar AI-kedja | Prompt, kontext, modell, svar och åtgärd ska kunna följas där risk kräver det. |
| 6 | Dataminimering i hela flödet | AI-lösningar ska bara använda och lagra den information som behövs. |
| 7 | Säkerhet som plattformsförmåga | Gemensamma skydd ska byggas in i AI-plattform och integrationsmönster. |
| 8 | Återanvändbara byggblock | Lokala lösningar ska återanvända gemensamma mönster där det är möjligt. |
| 9 | Modulär arkitektur | Modeller, index, orkestrering och driftkomponenter ska kunna bytas kontrollerat. |
| 10 | Riskbaserat leverantörsoberoende | Beroenden ska vara synliga, dokumenterade och hanterbara. |
| 11 | Flera driftspår | Moln, hybrid och on-premises ska användas efter risk och informationsklass. |
| 12 | Mätbar produktion | AI-lösningar ska följas upp tekniskt, säkerhetsmässigt och verksamhetsmässigt. |
| 13 | Spårbara beslut | Viktiga vägval ska dokumenteras och kunna omprövas. |
| 14 | Styrda avvikelser | Undantag ska vara tidsbegränsade, riskbedömda och dokumenterade. |
| 15 | Avvecklingsbarhet | AI-lösningar ska kunna stängas, bytas eller flyttas utan okontrollerad verksamhetspåverkan. |

## Hur principerna påverkar målarkitekturen

Principer blir värdefulla först när de syns i arkitekturen. För Aurora leder principerna till flera konkreta krav.

### Krav på process

Use-case triage blir obligatoriskt före pilot. Juridik, informationssäkerhet, dataskydd, arkitektur och ansvarig verksamhet behöver kunna delta på rätt nivå. Det betyder inte att alla initiativ ska gå genom långsam kommittéhantering, men det betyder att risknivå avgör beslutsgång.

### Krav på informationshantering

Promptar, kontext, embeddings, modellutdata och loggar betraktas som informationsobjekt. De behöver klassas, skyddas, gallras och åtkomststyras. Det gör att AI-målarkitekturen får ett starkt beroende till dataarkitektur och informationsförvaltning.

### Krav på plattform

AI-plattformen behöver gemensamma kontroller: identitet, behörighet, loggning, policy enforcement, modellkatalog, kostnadsuppföljning, observability och integrationsmönster. En plattform som bara erbjuder modellanrop räcker inte.

### Krav på driftmodell

Driftmodellen behöver delas i spår. Lågkänsliga användningsfall kan ha ett snabbare molnbaserat spår. Skyddsvärda användningsfall kan kräva hybrid eller on-premises. Högre risk kräver mer kontroll, dokumentation och validering.

### Krav på upphandling

Principerna behöver översättas till krav på leverantörer: datalokalisering, loggåtkomst, underbiträden, modellförändringar, revisionsmöjlighet, exit, säkerhetskontroller, incidentrapportering och möjlighet att separera myndighetens data från leverantörens modellutveckling.

## Exempel från Tullverket Aurora

Tullverket Aurora använder arkitekturprinciperna för att stoppa otydliga vägval tidigt. När ett verksamhetsteam vill införa en extern AI-tjänst för snabb textanalys frågar arkitekturforumet först vilka informationsklasser som berörs, vilket mänskligt ansvar som ska finnas kvar och hur beslutet kan återanvändas i kommande lösningar.

Principerna blir därmed inte en bilaga till målarkitekturen. De blir ett praktiskt filter för portföljstyrning, upphandling, plattformsval och lösningsdesign.

## Vägvalsfrågor

När principerna används i ett konkret AI-initiativ bör arkitekten ställa frågor som dessa:

- Vilken myndighetsförmåga stödjer användningsfallet?
- Vilken information behandlas i hela AI-flödet?
- Vilken mänsklig kontroll krävs och var sker den?
- Vilken transparens behövs för användare, granskare och ansvariga?
- Vad behöver loggas, hur länge och med vilken åtkomst?
- Vilken driftmodell är tillåten utifrån klassning och risk?
- Vilka gemensamma byggblock ska återanvändas?
- Vilka leverantörsberoenden uppstår?
- Hur kan modellen, tjänsten eller plattformen bytas?
- Hur mäts kvalitet, säkerhet, kostnad och nytta?
- Vilka beslut behöver dokumenteras som arkitekturbeslut?
- Vilka antaganden behöver omprövas senare?

Frågorna gör principerna operativa. De förvandlar dem från policytext till arkitekturarbete.

## Vanliga fallgropar

- **Principerna blir för allmänna.**
  - Varför det händer: Organisationen vill skapa enighet och undviker därför skarpa formuleringar.
  - Hur du undviker det: Skriv principer som påverkar ordning, ansvar, teknikval eller beslutspunkt.

- **Principerna blandas ihop med lösningsdesign.**
  - Varför det händer: Arkitekter vill göra principerna konkreta och går direkt till produktval.
  - Hur du undviker det: Skilj mellan princip, referensarkitektur och lösningsarkitektur.

- **Principerna saknar konsekvens.**
  - Varför det händer: Formuleringen säger vad man vill uppnå men inte vad det innebär.
  - Hur du undviker det: Lägg alltid till motiv, konsekvens och exempel.

- **Principerna används inte i upphandling.**
  - Varför det händer: Upphandling drivs som separat spår från arkitekturarbetet.
  - Hur du undviker det: Översätt principer till krav, utvärderingsfrågor och avtalsvillkor.

- **Moln eller on-premises blir ideologi.**
  - Varför det händer: Organisationen förenklar en komplex riskfråga till en positionsfråga.
  - Hur du undviker det: Använd klassning, risk, juridik och kontinuitet som beslutsgrund.

- **Mänsklig kontroll antas räcka utan design.**
  - Varför det händer: Lösningen kallas beslutsstöd och betraktas därför som ofarlig.
  - Hur du undviker det: Beskriv exakt vem som granskar, vad personen ser, hur avvikelse hanteras och vad som dokumenteras.

- **Spårbarhet skapar nya dataskyddsproblem.**
  - Varför det händer: Allt loggas för säkerhets skull.
  - Hur du undviker det: Klassificera loggar, minimera innehåll, styr åtkomst och definiera retention.

## Checklista

Använd denna checklista när principerna ska fastställas eller användas i målarkitekturen.

- Finns principer på både värde-, styr- och designnivå?
- Har varje princip ett motiv och en praktisk konsekvens?
- Är principerna tillräckligt konkreta för att påverka arkitekturbeslut?
- Går principerna att använda i use-case triage?
- Styr principerna val av moln, hybrid och on-premises?
- Styr principerna krav på loggning, åtkomst, transparens och mänsklig kontroll?
- Är undantag och avvikelser hanterade?
- Finns koppling till upphandling och leverantörsstyrning?
- Finns ansvar för att förvalta och ompröva principerna?
- Är principerna förankrade hos verksamhet, juridik, säkerhet, dataskydd och arkitektur?
- Är principerna dokumenterade på ett sätt som kan återanvändas i referensarkitektur och lösningsgranskning?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Arkitekturprinciperna är det lager som gör målarkitekturen styrbar innan alla tekniska detaljer är beslutade. De ska användas när myndigheten:

- prioriterar AI-portföljen,
- väljer driftmodell,
- definierar referensarkitektur,
- kravställer plattform,
- granskar lösningsarkitektur,
- beslutar om undantag,
- upphandlar tjänster,
- följer upp produktion,
- omprövar vägval.

För Tullverket Aurora innebär kapitlets principer att nästa steg inte är att rita en teknisk plattform direkt. Nästa steg är att skapa en governance- och beslutsmodell som gör principerna verkliga i vardagen. Vem får godkänna ett AI-användningsfall? Vilka beslut ligger hos arkitekturforumet? När ska juridik, säkerhet och dataskydd involveras? Hur dokumenteras avvikelser?

Det är ämnet för nästa kapitel.

## Snabb sammanfattning

Arkitekturprinciper för offentlig AI behöver vara mer än värdeord. De ska hjälpa myndigheten att fatta konsekventa beslut om användningsfall, data, ansvar, teknik, driftmodell, säkerhet och leverantörer.

För en statlig myndighet bör principerna särskilt styra uppdrag och nytta, klassning före plattformsval, mänsklig kontroll, transparens, spårbarhet, dataminimering, gemensamma säkerhetsbyggblock, återanvändning, modularitet, leverantörsoberoende, driftspår, mätbarhet, arkitekturbeslut, undantag och avvecklingsbarhet.

Tullverket Aurora använder principerna för att gå från juridik och riskbedömning till praktiska vägval. Därmed blir principerna en direkt länk mellan styrning och teknisk målarkitektur.
