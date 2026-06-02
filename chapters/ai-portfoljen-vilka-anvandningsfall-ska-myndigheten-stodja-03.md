# Kapitel 3: AI-portföljen: vilka användningsfall ska myndigheten stödja?

## Varför detta kapitel finns

En målarkitektur för AI kan inte tas fram i ett vakuum. Den måste svara mot de typer av användningsfall myndigheten faktiskt behöver stödja. Om arkitekturarbetet börjar med plattform, modell eller produkt finns en stor risk att myndigheten bygger en generell teknisk förmåga utan tydlig koppling till nytta, risk och styrning.

AI-portföljen är därför ett av de första styrande underlagen. Den visar vilka AI-initiativ myndigheten överväger, vilka som bör prioriteras, vilka som bör stoppas, vilka som kräver särskild juridisk prövning och vilka som kan användas för att bygga gemensam förmåga stegvis.

För en större statlig myndighet är portföljfrågan särskilt viktig eftersom olika AI-användningsfall har mycket olika riskprofil. Ett internt stöd för att sammanfatta öppna styrdokument kräver inte samma arkitektur som ett stöd som påverkar kontrollprioritering, handläggning eller individnära beslut.

Det här kapitlet visar hur en erfaren arkitekt kan strukturera AI-portföljen innan tekniska vägval görs.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva varför AI-portföljen är ett styrande underlag för målarkitekturen
- kategorisera AI-användningsfall utifrån nytta, risk, data och påverkan
- skilja mellan interna produktivitetsstöd, kunskapsstöd, beslutsstöd, automation och verksamhetskritisk AI
- använda use-case triage för att avgöra vilka användningsfall som kan gå vidare
- identifiera vilka användningsfall som kräver fördjupad juridisk, säkerhetsmässig eller etisk bedömning
- koppla portföljens mönster till framtida arkitekturbyggblock

## Arkitekturproblemet

När Tullverket Aurora började experimentera med AI fanns det många idéer. En avdelning ville sammanfatta långa ärendehandlingar. En annan ville använda generativ AI för att söka i interna handböcker. En tredje ville analysera historiska kontrollutfall. Några medarbetare använde redan externa AI-tjänster för att bearbeta texter, ibland utan tydliga riktlinjer.

Varje idé lät rimlig när den beskrevs separat. Men tillsammans skapade de ett arkitekturproblem.

Om alla användningsfall behandlas som tekniskt likvärdiga riskerar myndigheten att välja fel gemensamma lösning. En enkel AI-assistent för intern produktivitet är inte samma sak som ett riskanalysstöd. En RAG-lösning för styrdokument är inte samma sak som en modell som påverkar prioritering av kontroller. En lösning som bara hanterar öppna dokument har inte samma krav som en lösning som behandlar sekretessbelagd information eller personuppgifter.

Portföljfrågan blir därför:

> Vilka typer av AI-användningsfall ska myndighetens målarkitektur stödja, i vilken ordning och under vilka styrvillkor?

Svaret påverkar nästan allt som kommer senare:

- juridisk prövning
- informationsklassning
- säkerhetszoner
- dataplattform
- integrationsmönster
- val av modell och driftmiljö
- loggning och spårbarhet
- mänsklig kontroll
- upphandling
- förvaltning
- organisation och kompetens

AI-portföljen är alltså inte bara en lista över idéer. Den är en arkitekturdrivande analys av vad myndigheten behöver kunna göra.

## Centrala begrepp

### AI-portfölj

En AI-portfölj är den samlade mängden AI-initiativ som myndigheten överväger, testar, utvecklar, driftsätter eller förvaltar. Portföljen bör innehålla både tekniska och icke-tekniska uppgifter: användningsfall, nyttobedömning, risk, data, ägarskap, juridisk status, arkitekturstatus och nästa beslutspunkt.

En mogen AI-portfölj gör det möjligt att se mönster:

- flera initiativ behöver samma dokumentkällor
- flera lösningar behöver samma AI-gateway
- vissa användningsfall kräver samma juridiska prövning
- vissa idéer är egentligen varianter av samma förmåga
- vissa initiativ bör stoppas innan de skapar teknisk skuld
- vissa piloter bör prioriteras eftersom de bygger gemensam plattformsförmåga

För en arkitekt är portföljen ett sätt att identifiera vilka gemensamma byggblock som målarkitekturen måste stödja.

### Användningsfall

Ett användningsfall beskriver en avgränsad situation där AI skapar nytta. Det bör beskrivas från verksamhetens perspektiv, inte som en teknisk lösning.

Ett svagt formulerat användningsfall är:

- Vi vill ha en språkmodell.

Ett bättre formulerat användningsfall är:

- Handläggare ska kunna få ett sammanfattande stöd när de läser långa interna styrdokument, med källhänvisningar till godkända dokument och utan att sekretessbelagd information skickas till otillåten miljö.

Det andra exemplet säger mer om målgrupp, uppgift, data, kontroll och risk. Det ger arkitekten något att arbeta med.

### Use-case triage

Use-case triage är en första strukturerad bedömning av AI-användningsfall. Syftet är inte att göra fullständig juridisk analys, informationsklassning eller lösningsdesign. Syftet är att snabbt avgöra vad som kan gå vidare, vad som behöver fördjupad prövning och vad som bör stoppas eller omformuleras.

En enkel triage bör minst svara på:

- Vilken verksamhetsnytta ska skapas?
- Vilka användare berörs?
- Vilka data behövs?
- Finns personuppgifter eller sekretess?
- Påverkar lösningen enskilda personer eller rättsliga beslut?
- Är AI-resultatet rådgivande, beslutsstödjande eller automatiserande?
- Hur felkänsligt är användningsfallet?
- Vilken mänsklig kontroll krävs?
- Finns en tydlig ansvarig verksamhetsägare?
- Vilken gemensam förmåga bygger initiativet upp?

Triage ska vara lätt nog att användas tidigt, men skarp nog att sortera bort olämpliga idéer.

### Nyttoklassning

Nyttoklassning beskriver vilken typ av nytta ett användningsfall förväntas skapa. För AI i myndighet räcker det sällan att bara ange effektivisering. Nytta kan vara bredare än tidsbesparing.

Exempel på nyttotyper är:

- kortare handläggningstid
- bättre kunskapsstöd
- högre kvalitet i beslutsunderlag
- minskad manuell administration
- bättre prioritering av resurser
- bättre spårbarhet i informationsflöden
- snabbare introduktion av nya medarbetare
- förbättrad service till allmänhet eller företag
- ökad förmåga att upptäcka avvikelser
- bättre analys av stora informationsmängder

Nyttoklassningen hjälper arkitekten att se vilka förmågor som ger återkommande värde.

### Risknivå

Risknivå beskriver hur känsligt och potentiellt konsekvensrikt ett AI-användningsfall är. Risknivån påverkas av data, användare, kontext, grad av automation, felkonsekvens och påverkan på individ eller verksamhet.

Ett användningsfall kan ha låg teknisk komplexitet men hög risk. Ett exempel är en enkel textgenerator som används i ett sammanhang där formuleringen kan påverka myndighetsutövning. Ett annat användningsfall kan ha hög teknisk komplexitet men lägre juridisk risk, till exempel intern analys av anonymiserade driftmönster.

Risknivå ska därför inte sättas enbart utifrån teknisk svårighet.

## Rekommenderat angreppssätt

### Börja med användningsfall, inte teknik

Det första steget är att samla in och normalisera användningsfall. Normalisering betyder att idéerna skrivs om till ett jämförbart format.

Varje användningsfall bör minst beskriva:

- namn
- verksamhetsproblem
- tänkt användare
- vilken uppgift AI ska stödja
- vilka data som behövs
- om personuppgifter kan förekomma
- om sekretessbelagd information kan förekomma
- om resultatet påverkar beslut eller prioritering
- förväntad nytta
- preliminär risknivå
- ansvarig verksamhetsägare
- föreslagen nästa beslutspunkt

Det är viktigt att inte låta verksamheten beskriva användningsfallet som en beställd produkt. Om beställningen är “vi behöver Copilot”, “vi behöver en chatbot” eller “vi behöver en vektordatabas” bör arkitekten backa ett steg och fråga vilken uppgift som ska lösas.

### Dela in portföljen i användningsfallstyper

När idéerna är normaliserade bör de delas in i typer. En praktisk indelning för större myndigheter är:

| Typ | Beskrivning | Typisk risk | Arkitekturfråga |
|---|---|---|---|
| Intern produktivitet | Stöd för text, sammanfattning, mötesanteckningar och enklare informationsbearbetning | Låg till medel | Vilka data får användas i generella assistenter? |
| Kunskapsstöd | Sökning och svar baserat på godkända dokument och kunskapskällor | Medel | Hur säkras källor, behörighet och spårbarhet? |
| Handläggarstöd | Stöd i ärendeprocesser, dokumentgranskning och bedömning | Medel till hög | Hur säkerställs mänsklig kontroll och ansvar? |
| Analysstöd | Analys av större datamängder, mönster och avvikelser | Medel till hög | Vilken dataplattform och modellstyrning krävs? |
| Prioriterings- och riskstöd | Stöd för att prioritera kontroller, resurser eller insatser | Hög | Hur hanteras rättssäkerhet, bias och förklarbarhet? |
| Automation | AI används för att automatisera steg i processer | Hög | Vilka beslut får automatiseras och med vilken kontroll? |
| Medborgar- eller företagsnära tjänst | AI interagerar direkt eller indirekt med externa parter | Medel till hög | Hur hanteras ansvar, transparens och felaktiga svar? |

Tabellen är inte en juridisk klassificering. Den är ett arkitekturstöd för att se vilka användningsfall som bör hanteras tillsammans och vilka som kräver särskild prövning.

### Skilj på AI som assistent, stöd och styrande komponent

Ett av de viktigaste portföljbesluten är att avgöra vilken roll AI-resultatet har i arbetsflödet. Samma tekniska modell kan få helt olika riskprofil beroende på hur den används.

AI kan användas som:

- **Assistent:** AI hjälper användaren att formulera, sammanfatta eller hitta information, men resultatet används inte direkt i myndighetsutövning.
- **Kunskapsstöd:** AI hjälper användaren att hitta relevant information i godkända källor.
- **Beslutsstöd:** AI föreslår bedömningar, prioriteringar eller slutsatser som påverkar ett ärende eller en verksamhetsåtgärd.
- **Styrande komponent:** AI-resultatet påverkar automatiskt flöden, prioriteringar, beslut eller åtkomst.
- **Automatiserad aktör:** AI utför hela eller delar av en process utan individuell mänsklig bedömning i varje steg.

Målarkitekturen bör behandla dessa nivåer olika. En generell AI-assistent kan kanske införas med tydliga användarregler och tekniska begränsningar. Ett beslutsstöd kräver däremot mycket mer av datakvalitet, spårbarhet, dokumentation, validering och ansvar. En styrande eller automatiserande komponent kräver ytterligare prövning.

### Bedöm användningsfallens datakrav

AI-användningsfall ska inte bara klassas efter funktion. De ska också klassas efter data.

En praktisk första indelning är:

| Datatyp | Exempel | Arkitekturkonsekvens |
|---|---|---|
| Öppen information | Publicerade föreskrifter, öppna vägledningar, publika dokument | Kan ofta användas i mindre känsliga miljöer, men kräver ändå källkontroll |
| Intern men okänslig information | Interna rutiner, utbildningsmaterial, mötesmallar | Kräver behörighetsstyrning och riktlinjer för delning |
| Intern skyddsvärd information | Operativa rutiner, interna riskmodeller, säkerhetsrelaterade dokument | Kräver starkare kontroll, loggning och miljöval |
| Personuppgifter | Ärendedata, kontaktuppgifter, handläggningsinformation | Kräver dataskyddsbedömning och tydligt ändamål |
| Sekretessbelagd information | Uppgifter som omfattas av sekretessregler | Kräver särskild juridisk och säkerhetsmässig prövning |
| Verksamhetskritisk analysdata | Data som används för prioritering, kontroll eller styrning | Kräver kvalitetssäkring, spårbarhet och modellstyrning |

Den här indelningen ersätter inte informationsklassning. Den hjälper bara portföljen att sortera användningsfall så att rätt spår startas tidigt.

### Bedöm felkonsekvens

AI-fel är inte likvärdiga. Ett felaktigt förslag på rubrik i en intern text är inte samma sak som en felaktig riskindikator i kontrollverksamhet.

Arkitekten bör därför fråga:

- Vad händer om AI ger ett felaktigt svar?
- Vem kan påverkas?
- Kan felet upptäckas av användaren?
- Finns källor eller förklaringar som stödjer granskning?
- Kan felet skapa rättsliga, ekonomiska eller säkerhetsmässiga konsekvenser?
- Finns risk att användaren övertolkar AI-resultatet?
- Kan felet förstärkas om resultatet återanvänds i flera processer?

Ett användningsfall med hög felkonsekvens bör inte automatiskt stoppas. Men det ska inte hanteras som ett enkelt produktivitetsstöd.

### Skapa en första portföljvy

När användningsfallen har normaliserats kan portföljen visualiseras enkelt. En första vy kan kombinera nytta och risk.

| Användningsfall | Nytta | Risk | Rekommenderat nästa steg |
|---|---|---|---|
| Sammanfattning av öppna styrdokument | Medel | Låg | Kan testas i kontrollerad sandlåda |
| Intern sökning i handböcker och rutiner | Hög | Medel | Kräver RAG-mönster, behörighet och källhänvisning |
| Sammanfattning av ärendehandlingar | Hög | Medel till hög | Kräver dataskydds- och sekretessbedömning |
| Riskanalys för kontrollprioritering | Hög | Hög | Kräver fördjupad juridisk, etisk och modellriskbedömning |
| Automatisk kommunikation med företag | Medel | Medel till hög | Kräver transparens, kvalitetssäkring och ansvarsfördelning |
| Generell extern AI-tjänst för alla medarbetare | Medel | Varierar | Kräver policy, databegränsning och tekniska skydd |

Syftet är inte att besluta allt i tabellen. Syftet är att se vilka initiativ som kan gå snabbt, vilka som kräver fördjupning och vilka gemensamma byggblock som återkommer.

## Exempel från Tullverket Aurora

### Auroras första portföljinventering

Auroras arkitekturgrupp samlar in 37 AI-idéer från verksamheten. Efter normalisering visar det sig att många idéer är variationer av samma behov. Gruppen reducerar listan till sex portföljkategorier.

| Kategori | Exempel | Preliminär bedömning |
|---|---|---|
| Intern produktivitet | Sammanfatta möten, skriva utkast, förenkla texter | Lämpligt för kontrollerad användning med tydliga regler |
| Kunskapsstöd | Söka i styrdokument, handböcker och regelverk | Bra kandidat för gemensam RAG-förmåga |
| Ärendestöd | Sammanfatta ärendehandlingar och föreslå relevanta interna rutiner | Kräver stark datakontroll och tydlig mänsklig granskning |
| Analysstöd | Hitta mönster i stora informationsmängder | Kräver dataplattform, kvalitetssäkring och modellstyrning |
| Risk- och prioriteringsstöd | Stödja urval för kontrollverksamhet | Hög risk, kräver särskild styrning och dokumentation |
| Externa tjänster | Svara på frågor från företag och allmänhet | Kräver avgränsat innehåll, ansvar och kvalitetskontroll |

Det viktigaste resultatet är inte listan i sig. Det viktigaste är att Aurora slutar behandla AI som en enda teknisk kategori. De ser att olika användningsfall kräver olika arkitekturspår.

### Tre användningsfall som jämförs

Arkitekturgruppen väljer tre representativa användningsfall för fördjupad analys.

| Användningsfall | Datakrav | AI-roll | Risknivå | Trolig arkitekturinriktning |
|---|---|---|---|---|
| Intern kunskapssökning i styrdokument | Godkända interna dokument | Kunskapsstöd | Medel | RAG med behörighetsstyrning och källhänvisning |
| Sammanfattning av ärendehandlingar | Ärendedata, möjliga personuppgifter och sekretess | Handläggarstöd | Medel till hög | Kontrollerad miljö, loggning, mänsklig granskning |
| Riskanalys för kontrollprioritering | Historiska kontroll- och flödesdata | Beslutsstöd | Hög | Fördjupad modellrisk, validering och governance |

Denna jämförelse visar varför ett enda plattformsbeslut inte räcker. Alla tre kan använda AI, men de kräver olika kontrollnivåer, olika databehandling och olika grad av juridisk prövning.

### Vad Aurora lär sig

Efter portföljanalysen drar Aurora fem slutsatser.

För det första behöver myndigheten en gemensam process för use-case triage. Utan triage går för många initiativ direkt till tekniska diskussioner.

För det andra är kunskapsstöd ett bra första område för gemensam förmåga. Det är verksamhetsnära, ger tydlig nytta och bygger flera viktiga komponenter: dokumenthantering, åtkomstkontroll, källhänvisning, RAG-mönster och användarstöd.

För det tredje kan ärendenära AI inte behandlas som en enkel fortsättning på intern produktivitet. Så snart ärendedata, personuppgifter eller sekretess förekommer krävs mer kontrollerad arkitektur.

För det fjärde kräver risk- och prioriteringsstöd särskild styrning. Det handlar inte bara om modellprestanda utan om rättssäkerhet, förklarbarhet, bias, spårbarhet och ansvar.

För det femte behöver målarkitekturen stödja flera driftmodeller. Vissa användningsfall kan vara lämpliga för kontrollerade molnlösningar, andra kan kräva mer begränsade miljöer och vissa kan behöva hybridmönster.

## Vägvalsfrågor

### Vilka användningsfall ska gå först?

En vanlig frestelse är att börja med det mest verksamhetskritiska användningsfallet. Det kan vara rätt om myndigheten har hög mognad, stark datagrund och tydlig styrning. För en myndighet som bara har experimenterat lite med AI är det ofta bättre att börja med användningsfall som både ger nytta och bygger gemensam förmåga utan maximal risk.

Bra första kandidater har ofta dessa egenskaper:

- tydlig verksamhetsnytta
- avgränsad användargrupp
- kontrollerade datakällor
- begränsad påverkan på enskilda
- möjlighet till mänsklig granskning
- återanvändbara arkitekturbyggblock
- rimlig teknisk komplexitet
- tydlig verksamhetsägare

Intern kunskapssökning är ofta ett sådant område, särskilt om källorna kan avgränsas och svaren måste innehålla källhänvisningar. Det betyder inte att risken är obetydlig, men att den kan göras hanterbar och pedagogiskt användbar för organisationen.

### Ska portföljen styras centralt eller federerat?

En större myndighet behöver ofta både central styrning och lokal innovation. Ett helt centraliserat arbetssätt kan bli långsamt och kväva verksamhetsnära initiativ. Ett helt federerat arbetssätt kan skapa oöverskådlig risk, dubbelarbete och leverantörsinlåsning.

En praktisk modell är att styra gemensamma saker centralt och låta verksamhetsnära användningsfall utvecklas inom tydliga ramar.

Centralt bör myndigheten styra:

- principer
- risknivåer
- triageprocess
- tillåtna driftmodeller
- gemensamma säkerhetskrav
- godkända arkitekturmönster
- gemensamma plattformskomponenter
- dokumentation och spårbarhet
- uppföljning av portföljen

Lokalt kan verksamheten ofta driva:

- behovsformulering
- prioritering inom verksamhetsområde
- pilotdesign inom godkända ramar
- användartest
- nyttomätning
- förvaltningsnära förbättringar

Målarkitekturen bör därför inte bara beskriva teknik. Den bör beskriva vilka delar av AI-förmågan som är gemensamma och vilka som kan vara lokala.

### När ska ett användningsfall stoppas?

En AI-portfölj måste kunna säga nej. Annars blir den bara en önskelista.

Ett användningsfall bör stoppas eller omformuleras när:

- det saknar tydlig verksamhetsägare
- nyttan är oklar eller spekulativ
- datakällorna inte får användas för ändamålet
- lösningen kräver sekretess- eller personuppgiftsbehandling utan tydlig rättslig grund
- AI-resultatet riskerar att påverka beslut utan tillräcklig kontroll
- tekniken föreslås innan problemet är förstått
- det finns enklare icke-AI-lösningar som löser behovet bättre
- lösningen skulle skapa oacceptabel leverantörsinlåsning
- organisationen saknar förmåga att förvalta lösningen

Att stoppa ett användningsfall är inte ett misslyckande. Det är en del av styrningen.

## Vanliga fallgropar

### Fallgrop 1: Portföljen blir en idélista

Många organisationer samlar AI-idéer i en lista men saknar bedömningsmodell. Då går det inte att jämföra initiativ eller se vilka som bör prioriteras.

Undvik detta genom att kräva minsta gemensamma information för varje användningsfall: nytta, data, användare, AI-roll, risk, ansvarig ägare och nästa beslutspunkt.

### Fallgrop 2: All AI behandlas som samma sak

En generell AI-assistent, ett RAG-baserat kunskapsstöd och ett riskanalysstöd har olika riskprofil. Om de hanteras som samma kategori blir arkitekturen antingen för svag för känsliga användningsfall eller för tung för enkla användningsfall.

Undvik detta genom att dela in portföljen i användningsfallstyper och risknivåer.

### Fallgrop 3: Teknikval görs innan användningsfallet är förstått

Om användningsfallet formuleras som “vi behöver en chatbot” eller “vi behöver en modell” är lösningen redan inbyggd i problembeskrivningen. Det gör det svårt att bedöma alternativa lösningar.

Undvik detta genom att beskriva uppgiften, användaren, datan och beslutssituationen innan teknik diskuteras.

### Fallgrop 4: Nytta överskattas och förvaltning underskattas

Många AI-idéer ser lovande ut i pilotform men kräver omfattande förvaltning: datakvalitet, promptunderhåll, modelluppdateringar, behörigheter, loggning, support, incidenthantering och användarutbildning.

Undvik detta genom att bedöma förvaltningsbarhet redan i triage.

### Fallgrop 5: Riskanalys skjuts upp till slutet

Om juridik, dataskydd och informationssäkerhet kommer in först efter en teknisk pilot kan myndigheten ha byggt en lösning som inte kan produktionssättas.

Undvik detta genom att låta triage avgöra vilka initiativ som måste ha fördjupad prövning innan tekniskt arbete startar.

## Checklista

Använd checklistan när ett nytt AI-användningsfall föreslås.

- Är verksamhetsproblemet tydligt beskrivet?
- Är målgruppen för lösningen angiven?
- Är det tydligt vilken uppgift AI ska stödja?
- Är det tydligt om AI ska vara assistent, kunskapsstöd, beslutsstöd eller automatiserande komponent?
- Är förväntad nytta konkret nog för att kunna följas upp?
- Är datakällorna identifierade?
- Finns personuppgifter, sekretess eller annan skyddsvärd information?
- Är felkonsekvensen bedömd?
- Finns krav på mänsklig kontroll?
- Finns en ansvarig verksamhetsägare?
- Finns en preliminär risknivå?
- Finns en rekommenderad nästa beslutspunkt?
- Bygger användningsfallet någon gemensam AI-förmåga?
- Finns enklare alternativ som bör prövas före AI?
- Är användningsfallet lämpligt för pilot, sandlåda, fördjupad analys eller stopp?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

AI-portföljen visar vilka förmågor målarkitekturen behöver stödja. Om portföljen domineras av intern produktivitet behövs tydliga användarregler, databegränsningar och kontrollerade assistenttjänster. Om portföljen domineras av kunskapsstöd behövs dokumenthantering, sökindex, RAG-mönster, källhänvisning och behörighetsstyrning. Om portföljen innehåller beslutsstöd och prioriteringsstöd behövs starkare modellstyrning, validering, spårbarhet, mänsklig kontroll och governance.

Portföljanalysen påverkar därmed målarkitekturen på flera sätt:

- Den visar vilka arkitekturbyggblock som bör prioriteras.
- Den visar vilka risknivåer arkitekturen måste kunna hantera.
- Den visar vilka driftmodeller som behöver utredas.
- Den visar vilka juridiska och säkerhetsmässiga processer som behöver integreras.
- Den visar vilka referensarkitekturer som bör tas fram först.
- Den visar vilka kompetenser och roller som behövs.
- Den visar vilka användningsfall som bör ingå i roadmapen.

För Tullverket Aurora leder portföljanalysen till ett viktigt arkitekturbeslut: myndigheten ska inte välja en enda AI-lösning för alla behov. Den ska etablera en gemensam AI-förmåga med flera kontrollerade spår:

1. ett spår för kontrollerad intern produktivitet
2. ett spår för RAG-baserat kunskapsstöd
3. ett spår för ärendenära handläggarstöd
4. ett spår för analys- och riskstöd med fördjupad modellstyrning
5. ett spår för framtida externa tjänster efter särskild prövning

Detta blir en central utgångspunkt för nästa kapitel, där juridik, ansvar och regelefterlevnad behandlas mer systematiskt.

## Snabb sammanfattning

- AI-portföljen är ett styrande underlag för målarkitekturen, inte bara en lista över idéer.
- Användningsfall bör beskrivas utifrån verksamhetsproblem, användare, data, AI-roll, nytta, risk och ansvar.
- Use-case triage hjälper myndigheten att avgöra vilka idéer som kan gå vidare, vilka som kräver fördjupad prövning och vilka som bör stoppas.
- Olika AI-användningsfall kräver olika arkitekturspår.
- Intern produktivitet, kunskapsstöd, handläggarstöd, analysstöd, prioriteringsstöd, automation och externa tjänster ska inte behandlas som samma sak.
- Portföljanalysen visar vilka gemensamma byggblock som målarkitekturen bör prioritera.
- För en myndighet som Tullverket Aurora är det klokt att börja med användningsfall som skapar nytta och samtidigt bygger kontrollerad gemensam förmåga.
