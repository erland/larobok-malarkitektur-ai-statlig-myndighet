# Kapitel 5: Informationsklassning, dataskydd och riskstyrning

## Varför detta kapitel finns

AI-målarkitektur behöver börja i verksamhetens information, inte i modellen. En myndighet som väljer AI-plattform innan den vet vilken information som ska hanteras riskerar att bygga en tekniskt imponerande men styrningsmässigt oanvändbar förmåga.

Informationsklassning, dataskydd och riskstyrning avgör vilka AI-användningsfall som kan använda färdiga molntjänster, vilka som kräver särskilda skyddsåtgärder, vilka som bör isoleras i egna miljöer och vilka som tills vidare inte bör genomföras alls. För en statlig myndighet är detta inte bara en säkerhetsfråga. Det påverkar rättssäkerhet, sekretess, dataskydd, arkiv, upphandling, kontinuitet och allmänhetens förtroende.

I Tullverket Aurora blir frågan konkret. Samma tekniska AI-funktion, till exempel textsammanfattning, kan ha helt olika arkitekturkrav beroende på vilken information som matas in:

- en publik instruktion på intranätet,
- en intern arbetsrutin,
- ett ärendedokument med personuppgifter,
- en sekretessbelagd underrättelse,
- en riskprofil som påverkar prioritering av kontroller.

AI-förmågan måste därför kunna styra användning efter informationsklass, ändamål, risknivå och driftmodell.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför informationsklassning behöver göras före plattforms- och modellval,
- skilja mellan informationsklassning, dataskyddsbedömning och AI-riskbedömning,
- beskriva hur promptar, svar, embeddings, loggar och modellutdata blir en del av informationshanteringen,
- formulera en praktisk klassningsmodell för AI-användningsfall,
- koppla risknivå till tekniska skyddsåtgärder och tillåten driftmodell,
- identifiera när moln, hybrid eller on-premises bör vara möjliga respektive olämpliga,
- beskriva hur riskstyrning bör integreras i AI-portfölj, arkitekturbeslut och livscykelhantering.

## Arkitekturproblemet

Det vanligaste felet är att informationsklassning görs på ursprungliga dokument och databaser, men inte på det AI-systemet faktiskt skapar och lagrar. I traditionell systemarkitektur är detta redan ett problem. I AI-arkitektur blir det större.

En generativ AI-lösning kan skapa flera nya informationsobjekt:

- användarens prompt,
- hämtade dokumentutdrag,
- modellens svar,
- mellanliggande resonemang eller verktygsanrop,
- embeddings,
- sökindex,
- konversationshistorik,
- loggar,
- felrapporter,
- utvärderingsdata,
- tränings- eller finjusteringsdata,
- metadata om användning och åtkomst.

Om målarkitekturen bara klassar ursprungskällan missar den hur informationen rör sig genom AI-kedjan. Ett dokument som är korrekt skyddat i ett ärendehanteringssystem kan bli fel hanterat när det skickas till en extern modell, bäddas in i ett vektorindex eller lagras i en felsökningslogg.

För Tullverket Aurora innebär det att arkitekturgruppen inte kan fråga: “Är dokumentkällan tillåten?” Den måste fråga: “Vilka informationsobjekt uppstår i hela AI-flödet, vem får se dem, var lagras de, hur länge finns de kvar och kan de användas för andra ändamål?”

## Tre bedömningar som måste hållas isär

Informationsklassning, dataskydd och AI-riskbedömning överlappar, men de är inte samma sak. Målarkitekturen behöver behandla dem som tre sammanhängande men separata bedömningar.

### Informationsklassning

Informationsklassning beskriver informationens skyddsbehov. Den bör minst omfatta konfidentialitet, riktighet och tillgänglighet. För en myndighet behöver den också relateras till sekretess, verksamhetskritikalitet, nationella eller samhällsviktiga intressen och möjlig påverkan på enskilda eller företag.

En AI-lösning som använder offentliga styrdokument har låg konfidentialitetsrisk men kan fortfarande kräva hög riktighet om svaret används i handläggning. En AI-lösning som sammanfattar sekretessbelagda ärenden har hög konfidentialitetsrisk även om den bara används internt.

### Dataskyddsbedömning

Dataskyddsbedömningen handlar om personuppgifter. Den behöver svara på frågor om ändamål, rättslig grund, personuppgiftsansvar, personuppgiftsbiträden, uppgiftsminimering, lagringstid, registrerades rättigheter, överföring till tredjeland och behov av konsekvensbedömning.

För AI är det viktigt att inte bara fråga om källdatan innehåller personuppgifter. Promptar, svar, embeddings, loggar och utvärderingsdata kan också innehålla personuppgifter eller göra personer indirekt identifierbara.

### AI-riskbedömning

AI-riskbedömningen handlar om hur AI-systemet används, vilken roll AI har i processen och vilken påverkan resultatet kan få. En AI-assistent som hjälper en anställd att skriva en intern text är något annat än ett system som påverkar vilka försändelser, företag eller personer som väljs ut för kontroll.

I målarkitekturen bör AI-risk inte reduceras till modelltyp. Risk uppstår i kombinationen av användningsfall, data, process, användare, automatiseringsgrad och konsekvens.

## En praktisk klassningsmodell för AI

Tullverket Aurora inför en klassningsmodell med fyra nivåer. Syftet är inte att ersätta myndighetens ordinarie informationsklassningsmodell, utan att skapa ett arkitekturlager som gör AI-vägval möjliga.

### Nivå A: Öppen eller lågkänslig information

Denna nivå omfattar information som är publik eller intern med lågt skyddsbehov. Exempel är publicerade föreskrifter, publika vägledningar och generella utbildningstexter.

Möjliga AI-mönster:

- generativ AI för sammanfattning och språkstöd,
- intern kunskapssökning mot publik dokumentation,
- enklare RAG-lösningar,
- färdiga SaaS-tjänster efter normal leverantörsbedömning.

Viktiga kontroller:

- tydlig märkning av att AI-svar behöver verifieras,
- loggning av användning,
- grundläggande leverantörsgranskning,
- instruktioner om vad användare inte får mata in.

### Nivå B: Intern verksamhetsinformation

Denna nivå omfattar information som inte är publik men normalt inte är sekretessbelagd eller särskilt känslig. Exempel är interna rutiner, handböcker, arkitekturdokument och processbeskrivningar.

Möjliga AI-mönster:

- intern AI-assistent,
- RAG mot interna dokument,
- sammanfattning av interna mötesanteckningar,
- stöd för handläggare vid tolkning av rutiner.

Viktiga kontroller:

- autentisering och behörighetsstyrning,
- åtkomstfiltrering mot källsystem,
- loggning och spårbarhet,
- granskning av hur leverantören hanterar promptar och svar,
- beslut om datalagring och retention.

### Nivå C: Skyddsvärd information och personuppgifter

Denna nivå omfattar information med tydligt skyddsbehov, till exempel personuppgifter, ärendeinformation, känsliga verksamhetsuppgifter eller data som kan påverka enskilda och företag.

Möjliga AI-mönster:

- kontrollerad sammanfattning i skyddad miljö,
- RAG med strikt behörighetsfiltrering,
- beslutsstöd med mänsklig kontroll,
- modellåtkomst via AI-gateway med policy enforcement,
- begränsade pilotmiljöer med särskilt godkännande.

Viktiga kontroller:

- dataskyddsbedömning,
- bedömning av rättslig grund och ändamål,
- åtkomstkontroll på dokumentnivå,
- kryptering, loggning och säkerhetsövervakning,
- begränsad retention,
- testdatahantering,
- tydlig ansvarskedja,
- bedömning av leverantör, driftlandskap och underbiträden.

### Nivå D: Särskilt känslig, sekretessbelagd eller verksamhetskritisk information

Denna nivå omfattar information där fel hantering kan orsaka allvarlig skada för enskilda, myndigheten, samhället eller statens intressen. För Tullverket Aurora kan det röra underrättelser, kontrollstrategier, känslig samverkansinformation eller information som avslöjar kontrollförmåga.

Möjliga AI-mönster:

- isolerad miljö,
- on-premises eller särskilt kontrollerad drift,
- strikt begränsad modellåtkomst,
- ingen extern modellträning,
- separata logg- och övervakningskrav,
- manuell granskning före produktion.

Viktiga kontroller:

- fördjupad riskanalys,
- säkerhetsskydds- och sekretessbedömning där relevant,
- strikt nätverkssegmentering,
- begränsade användargrupper,
- detaljerad spårbarhet,
- incidentberedskap,
- explicit beslut på högre nivå innan pilot eller produktion.

## Informationsobjekt i AI-flödet

En praktisk AI-målarkitektur behöver beskriva vilka informationsobjekt som uppstår i ett AI-flöde. Det räcker inte att dokumentera källsystem och målgrupp.

För varje AI-användningsfall bör arkitekten kartlägga följande objekt:

| Informationsobjekt | Fråga att besvara | Arkitekturkonsekvens |
|---|---|---|
| Källdata | Varifrån kommer informationen? | Styr integration, behörighet och klassning. |
| Prompt | Vad skriver användaren eller systemet till modellen? | Kan innehålla personuppgifter, sekretess och verksamhetsdata. |
| Kontext | Vilka dokumentutdrag skickas med? | Kräver åtkomstfiltrering och dataminimering. |
| Embeddings | Vilken information representeras i vektorform? | Måste klassas och skyddas som härledd information. |
| Modellutdata | Vad skapar modellen? | Kan bli ny handling, beslutsunderlag eller arbetsmaterial. |
| Loggar | Vad sparas för felsökning och spårbarhet? | Behöver retention, åtkomstkontroll och sekretessbedömning. |
| Feedback | Hur används användarens bedömning av svaret? | Kan bli träningsdata eller kvalitetsdata. |
| Utvärderingsdata | Vilka testfall och facit används? | Kan innehålla skyddsvärd verksamhetskunskap. |

Särskilt embeddings kräver arkitekturell uppmärksamhet. De är inte läsbara dokument i vanlig mening, men de kan bära informationsinnehåll, möjliggöra återidentifiering i vissa sammanhang och användas för att hitta känsliga textutdrag. Därför bör de normalt klassas utifrån den information de representerar, inte som ofarlig teknisk metadata.

I en AI-lösning räcker det inte att klassificera de ursprungliga källdokumenten. Även promptar, kontextdokument, embeddings, loggar, modellutdata, feedbackdata och eventuell åtkomst från leverantör eller supportpersonal kan innehålla personuppgifter, sekretessreglerad information eller andra skyddsvärda uppgifter. Klassningsmodellen behöver därför följa informationen genom hela AI-flödet, inte bara i källsystemet.

## Dataminimering som arkitekturprincip

Dataminimering är inte bara en juridisk princip. Det är en konkret arkitekturprincip.

För AI betyder dataminimering att lösningen bara ska exponera den information som behövs för uppgiften, vid rätt tidpunkt, för rätt användare och med rätt teknisk begränsning. I en RAG-lösning innebär det till exempel att modellen inte ska få tillgång till hela dokumentlager om användaren bara har rätt att se vissa dokument eller vissa avsnitt.

Tullverket Aurora formulerar därför följande arkitekturregler:

- AI-komponenter ska inte få bredare dataåtkomst än den användare eller process de stödjer.
- Kontextfönster ska fyllas med minsta relevanta informationsmängd.
- Sökning och retrieval ska respektera källsystemens behörigheter.
- Promptar och svar ska inte sparas längre än nödvändigt.
- Produktionsdata ska inte användas för test, demo eller utvärdering utan särskilt beslut.
- AI-leverantörer ska inte få använda myndighetens data för modellträning utan uttryckligt och godkänt ändamål.

Detta påverkar den tekniska referensarkitekturen. Den behöver innehålla behörighetsmedveten retrieval, policykontroll, loggstyrning, masking eller pseudonymisering där det passar, samt tydliga gränser mellan utveckling, test och produktion.

## Riskstyrning i portföljen

Riskstyrning ska inte vara ett dokument som skrivs efteråt. Den ska vara en styrande mekanism i AI-portföljen.

Varje användningsfall i Tullverket Auroras AI-portfölj får därför en preliminär riskprofil redan vid idéstadiet. Riskprofilen används för att avgöra:

- om idén får gå vidare till utforskning,
- vilken miljö den får använda,
- vilka roller som måste granska den,
- vilka tekniska skydd som krävs,
- om en pilot får göras med verklig data,
- om produktionssättning kräver särskilt beslut,
- hur ofta lösningen ska omprövas.

Riskprofilen bör innehålla minst följande dimensioner:

| Dimension | Exempel på fråga |
|---|---|
| Information | Vilka informationsklasser förekommer i hela AI-flödet? |
| Personuppgifter | Behandlas personuppgifter, känsliga uppgifter eller uppgifter om lagöverträdelser? |
| Sekretess | Kan information omfattas av sekretess eller annat särskilt skydd? |
| Påverkan | Kan AI-resultatet påverka enskilda, företag eller kontrollprioritering? |
| Automatiseringsgrad | Är AI assistent, beslutsstöd eller styrande komponent? |
| Felkonsekvens | Vad händer om AI-svaret är fel, ofullständigt eller missvisande? |
| Leverantör | Vilka parter får teknisk eller juridisk tillgång till information? |
| Drift | Var behandlas och lagras data? |
| Återanvändning | Kan data användas för träning, utvärdering eller förbättring? |
| Spårbarhet | Går det att i efterhand förstå vad som användes och varför? |

## Driftmodell som konsekvens av klassning

Klassning och risk ska leda till arkitekturval. Annars blir de bara administration.

För Tullverket Aurora innebär det att driftmodellen inte väljs generellt för “AI”, utan per riskkategori och användningsmönster.

### När molnlösningar ofta är rimliga

Molnlösningar kan vara rimliga när informationen är öppen eller lågkänslig, när användningsfallet är internt produktivitetsstöd, när leverantörens villkor är tydliga och när myndigheten kan säkerställa att data inte används på otillåtna sätt.

Moln kan också vara lämpligt när behovet av skalbarhet, snabb innovation, färdiga säkerhetsfunktioner och tillgång till moderna modeller väger tungt. För lägre risknivåer kan detta ge snabbare nytta än att bygga allt själv.

### När hybrid ofta är realistiskt

Hybrid blir ofta realistiskt när myndigheten vill använda molnbaserade modeller eller plattformstjänster men behöver behålla källdata, index, loggar eller vissa bearbetningar i en mer kontrollerad miljö.

Ett vanligt mönster är att behörighetsstyrning, dokumentlager, vektorindex och policykontroll ligger i myndighetens kontrollerade miljö, medan modellinferens sker i en godkänd molntjänst. Ett annat mönster är att lågkänsliga användningsfall får använda moln medan känsligare användningsfall körs i separata miljöer.

### När on-premises eller isolerad drift bör övervägas

On-premises eller isolerad drift bör övervägas när informationen är särskilt känslig, när lagring och behandling hos extern part inte kan accepteras, när sekretess- eller säkerhetsskyddsskäl väger tungt, eller när myndigheten behöver mycket stark kontroll över modell, loggar, nätverk och åtkomst.

On-premises är dock inte automatiskt säkrare. Det kräver egen kompetens, patchning, övervakning, kapacitetsplanering, incidenthantering, modellhantering och livscykelförvaltning. Arkitekturbeslutet måste därför väga kontroll mot faktisk förmåga att drifta säkert.

När personuppgifter behandlas behöver GDPR-frågorna hanteras oavsett om lösningen utvecklas internt, används som SaaS, körs i moln eller driftas on-premises. Bedömningen bör omfatta personuppgiftsansvar, personuppgiftsbiträden, tredjelandsöverföring, åtkomst för support, loggning och hur data används för eventuell träning eller förbättring av modeller.

## Tullverket Aurora: tre användningsfall

Aurora testar klassningsmodellen på tre återkommande användningsfall.

### Intern kunskapssökning i publika och interna styrdokument

Det första användningsfallet är en AI-assistent som hjälper anställda att hitta och sammanfatta styrdokument, rutiner och utbildningsmaterial.

Riskprofilen är relativt låg om dokumentmängden begränsas till publik och lågkänslig intern information. Molnbaserad RAG kan vara möjlig efter leverantörsbedömning, tydliga användarinstruktioner, åtkomstkontroll och loggstyrning.

Viktigaste arkitekturfrågan är att assistenten inte får bli en bakväg till dokument som användaren inte har rätt att se.

### Sammanfattning av ärendehandlingar

Det andra användningsfallet är att sammanfatta långa ärendehandlingar för handläggare.

Här ökar risknivån. Ärendehandlingar kan innehålla personuppgifter, sekretessbelagd information och uppgifter som påverkar enskilda eller företag. Lösningen behöver därför starkare åtkomstkontroll, dataskyddsbedömning, begränsad loggning, tydlig retention och mänsklig kontroll.

Moln kan bara övervägas om drift, avtalsvillkor, personuppgiftsbiträden, dataflöden och skyddsåtgärder är godtagbara. Hybrid eller kontrollerad miljö kan vara mer realistiskt.

### Riskanalys och prioriteringsstöd för kontrollverksamhet

Det tredje användningsfallet är AI-stöd för riskanalys och prioritering.

Här är risknivån hög. Även om AI inte fattar formella beslut kan systemet påverka vilka objekt, företag eller personer som granskas. Fel, bias, bristande transparens eller otillräcklig dokumentation kan få stora konsekvenser.

För detta användningsfall bör Aurora kräva fördjupad juridisk bedömning, dataskyddsbedömning, modellvalidering, dokumenterad mänsklig kontroll, tydlig ansvarskedja, hög spårbarhet och regelbunden omprövning. Driftmodellen bör vara starkt kontrollerad och plattformsvalet får inte göras innan riskbilden är förstådd.

## Exempel från Tullverket Aurora

När Tullverket Aurora prövar AI-stöd för dokumentgranskning upptäcker arkitekterna att samma användargränssnitt kan beröra flera informationsklasser. En handläggare kan ställa en enkel fråga om ett publikt regelverk, men nästa fråga kan innehålla ärendedata, personuppgifter eller uppgifter om kontrollurval.

I målarkitekturen leder detta till en viktig konsekvens: klassningen måste göras på hela informationsflödet, inte bara på datakällan. Promptar, kontext, sökindex, embeddings, modellutdata, loggar och återkoppling från användaren behandlas som delar av samma skyddsvärda kedja.

## Vägvalsfrågor

Innan ett AI-användningsfall får gå från idé till pilot bör arkitekten kunna svara på följande frågor:

- Vilken information används, skapas, lagras och loggas?
- Vilka informationsklasser förekommer i hela AI-flödet?
- Behandlas personuppgifter, och i så fall för vilket ändamål?
- Finns sekretess, säkerhetsskydd eller annan särskild reglering?
- Är AI-svaret arbetsmaterial, beslutsunderlag eller del av en handling?
- Vilka användare får använda lösningen?
- Får användaren se all information som lösningen kan hämta?
- Var körs modellen?
- Var lagras promptar, svar, embeddings och loggar?
- Kan leverantören använda data för träning, felsökning eller produktförbättring?
- Hur länge sparas informationen?
- Hur upptäcks felaktiga eller olämpliga svar?
- Vem äger risken när AI används i processen?
- Vilken driftmodell är tillåten för denna risknivå?
- Vilket beslut krävs för att gå vidare till pilot respektive produktion?

## Vanliga fallgropar

- **Fallgrop: Att bara klassa källdokument.**
  - Varför det händer: Arkitekturen är van vid system och databaser, men inte AI-flödets nya informationsobjekt.
  - Hur det undviks: Klassa promptar, svar, embeddings, loggar och utvärderingsdata tillsammans med källdatan.

- **Fallgrop: Att betrakta embeddings som ofarlig metadata.**
  - Varför det händer: Embeddings är svåra att läsa direkt och uppfattas därför som tekniska.
  - Hur det undviks: Klassa dem efter informationsinnehållet de representerar och skydda vektorindex därefter.

- **Fallgrop: Att välja moln eller on-premises ideologiskt.**
  - Varför det händer: Organisationer tenderar att förenkla vägval till “moln är snabbt” eller “on-premises är säkert”.
  - Hur det undviks: Låt informationsklass, risk, driftförmåga, juridik och verksamhetsnytta styra beslutet.

- **Fallgrop: Att använda verklig ärendedata för tidiga experiment.**
  - Varför det händer: Verklig data ger bättre testkänsla och snabbare demonstrationer.
  - Hur det undviks: Använd syntetisk, maskerad eller särskilt godkänd testdata tills riskbedömning och skyddsåtgärder är klara.

- **Fallgrop: Att logga för mycket.**
  - Varför det händer: Utvecklingsteam vill kunna felsöka och utvärdera modellen.
  - Hur det undviks: Definiera loggsyfte, logginnehåll, åtkomst, retention och maskning innan produktion.

- **Fallgrop: Att riskbedömningen görs en gång.**
  - Varför det händer: Risk ses som ett projektsteg.
  - Hur det undviks: Koppla riskbedömning till modellversioner, datakällor, leverantörsvillkor, driftförändringar och nya användargrupper.

## Checklista

Ett AI-användningsfall bör inte gå vidare till pilot innan följande är hanterat:

- Användningsfallet är beskrivet med syfte, användare och process.
- AI-roll är angiven: assistent, kunskapsstöd, beslutsstöd eller styrande komponent.
- Källdata, promptar, kontext, svar, embeddings, loggar och feedback är kartlagda.
- Informationsklassning är gjord för hela AI-flödet.
- Personuppgifter och dataskyddsfrågor är identifierade.
- Sekretess och skyddsvärd verksamhetsinformation är bedömda.
- Felkonsekvens och påverkan på enskilda eller företag är bedömda.
- Driftmodell är preliminärt vald utifrån risknivå.
- Leverantörens datahantering är granskad.
- Beslut om retention och loggning finns.
- Testdata är godkänd för ändamålet.
- Ansvarig informationsägare, systemägare och verksamhetsägare är identifierade.
- Beslutspunkt för pilot och produktion är dokumenterad.
- Omprövningspunkter finns för nya datakällor, modellversioner och driftförändringar.

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Informationsklassning, dataskydd och riskstyrning ska synas i målarkitekturen som konkreta byggblock och beslutspunkter. En AI-målarkitektur för Tullverket Aurora bör därför innehålla:

- klassningsmodell för AI-användningsfall,
- riskprofil per användningsfall,
- AI-use-case register,
- dataflödeskarta för promptar, svar, embeddings och loggar,
- behörighetsmedveten retrieval,
- policy enforcement före modellanrop,
- logg- och retentionmodell,
- modell för testdata och syntetisk data,
- beslutsträd för moln, hybrid och on-premises,
- krav på dataskyddsbedömning och informationssäkerhetsbedömning,
- arkitekturbeslut som kopplar risknivå till tillåtna plattformsmönster.

Nästa kapitel bygger vidare på detta genom att formulera arkitekturprinciper för offentlig AI. Där blir klassningen och riskstyrningen översatta till styrande principer som kan användas i målarkitektur, upphandling, plattformsval och lösningsgranskning.


## Snabb sammanfattning

AI-målarkitektur måste utgå från informationens skyddsbehov och användningsfallets risk, inte från vilken modell eller plattform som råkar vara mest tillgänglig. Informationsklassning, dataskydd och AI-riskbedömning är tre olika men sammanhängande perspektiv.

För statliga myndigheter behöver klassningen omfatta hela AI-flödet: källdata, promptar, kontext, embeddings, modellutdata, loggar, feedback och utvärderingsdata. Riskprofilen ska styra vilken miljö som får användas, vilka skyddsåtgärder som krävs och vilket beslut som behövs före pilot och produktion.

Tullverket Aurora använder klassningen för att skilja mellan lågkänslig intern kunskapssökning, skyddsvärd ärendesammanfattning och högrisknära prioriteringsstöd. Det gör att målarkitekturen kan stödja innovation utan att tappa kontroll över juridik, säkerhet och förtroende.
