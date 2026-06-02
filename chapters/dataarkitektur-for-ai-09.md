# Kapitel 9: Dataarkitektur för AI

## Varför detta kapitel finns

AI-förmåga byggs inte ovanpå modeller i första hand. Den byggs ovanpå data, metadata, behörigheter, informationsägarskap och spårbarhet. För en större statlig myndighet är dataarkitekturen därför inte ett stödspår till AI-arkitekturen. Den är en av de viktigaste delarna av målarkitekturen.

Det gäller särskilt när myndigheten vill använda generativ AI, RAG, analysstöd eller beslutsstöd i verksamhetsnära processer. Samma modell kan ge helt olika risk, kvalitet och nytta beroende på vilka datakällor den får tillgång till, hur informationen är klassad, hur åtkomst kontrolleras, hur svar kan spåras och hur felaktig eller föråldrad information hanteras.

Kapitel 8 beskrev de förmågor myndigheten behöver etablera. Detta kapitel går djupare i en av de mest styrande förmågorna: dataarkitektur för AI.

## Arkitekturproblemet

Tullverket Aurora vill börja med ett till synes enkelt användningsfall: intern kunskapssökning i regelverk, handböcker, styrdokument och vägledningar. Flera verksamhetsområden ser stor nytta. Handläggare lägger mycket tid på att hitta rätt tolkning, jämföra dokument och förstå vilka rutiner som gäller i olika situationer.

Vid första anblick verkar lösningen tekniskt okomplicerad. Dokument kan indexeras, delas upp i mindre textstycken, omvandlas till embeddings och göras sökbara i en vektordatabas. Ett språkmodellbaserat gränssnitt kan sedan hämta relevanta textstycken och generera ett svar.

Men arkitekturgruppen upptäcker snabbt att den svåra frågan inte är hur man skapar ett index. Den svåra frågan är vilken information som får ingå, vem som äger den, hur aktuell den är, vilka användare som får se den, hur källor redovisas, hur felaktiga svar upptäcks och vad som händer när samma dokument finns i flera versioner.

Auroras arkitekturfråga blir därför:

> Hur bygger vi en dataarkitektur som gör AI-lösningar användbara utan att tappa kontroll över information, ansvar, kvalitet, åtkomst och spårbarhet?

Om denna fråga inte besvaras riskerar myndigheten att skapa AI-lösningar som är imponerande i en demo men olämpliga i produktion.

## Centrala begrepp

Dataarkitektur beskriver hur data struktureras, ägs, kvalitetssäkras, görs tillgänglig, skyddas, spåras och används över tid.

Informationsägarskap innebär att det finns en ansvarig verksamhetsfunktion eller roll som kan fatta beslut om informationens användning, kvalitet, klassning, gallring och tillgänglighet.

Metadata är data om data. I AI-sammanhang kan metadata beskriva källa, dokumenttyp, version, giltighetstid, informationsklass, åtkomstregler, språk, ämnesområde, ansvarig informationsägare och datum för senaste granskning.

Data lineage beskriver informationens ursprung, transformationer och användning genom ett flöde. För AI behöver lineage kunna omfatta källdokument, chunking, embeddings, index, promptkontext, modellversion, svar, loggar och feedback.

Embeddings är numeriska representationer av text, bild eller annan information som gör det möjligt att hitta semantiskt liknande innehåll. De är inte neutrala tekniska artefakter; de kan bära information från källmaterialet och måste hanteras utifrån informationsklassning och åtkomstregler.

En vektordatabas lagrar embeddings och gör semantisk sökning möjlig. I en myndighetsarkitektur är vektordatabasen en skyddsvärd komponent eftersom den kan ge indirekt åtkomst till känsligt informationsinnehåll.

Ett sökindex är en strukturerad representation som gör information sökbar. Ett AI-stöd kan behöva både klassiskt textindex, semantiskt vektorindex och metadatafilter.

Chunking innebär att dokument delas upp i mindre textstycken för indexering och hämtning. Chunking påverkar både kvalitet, spårbarhet, svarens precision och risken för att information tas ur sitt sammanhang.

## Rekommenderat angreppssätt

En myndighet bör börja med att beskriva dataarkitekturen utifrån informationsflöden, inte utifrån verktyg. Frågan är inte först vilken vektordatabas som ska väljas. Frågan är hur information rör sig från källa till AI-svar och tillbaka till uppföljning.

Ett praktiskt angreppssätt är att beskriva varje AI-användningsfall genom sju dataarkitekturfrågor.

1. Vilka datakällor används?
2. Vem äger och godkänner informationen?
3. Vilken informationsklass och vilka åtkomstregler gäller?
4. Hur skapas metadata, index och embeddings?
5. Hur säkerställs kvalitet, aktualitet och versionshantering?
6. Hur spåras källor, modellinteraktioner och svar?
7. Hur hanteras loggar, feedback, gallring och avveckling?

Dessa frågor bör besvaras innan myndigheten gör ett definitivt plattformsval. Annars riskerar tekniken att låsa dataflöden och ansvar på ett sätt som inte stödjer rättssäkerhet eller förvaltning.

## Datakällor och informationsdomäner

AI-lösningar använder ofta fler datakällor än man först tror. Ett RAG-baserat kunskapsstöd kan till exempel använda styrdokument, processbeskrivningar, rättsliga vägledningar, ärendehandböcker, interna beslut, utbildningsmaterial och vanliga frågor. Ett analysstöd kan dessutom använda transaktionsdata, statistik, historiska ärenden, riskindikatorer och externa datakällor.

Målarkitekturen bör därför beskriva informationsdomäner. En informationsdomän är ett sammanhållet område där information har liknande ägarskap, styrning och skyddsbehov. För Tullverket Aurora kan relevanta domäner vara:

- regelverk och rättsliga vägledningar,
- interna styrdokument och processbeskrivningar,
- ärendeinformation,
- kontroll- och riskinformation,
- samverkansinformation från andra aktörer,
- tekniska loggar och AI-interaktionsdata.

Domänindelningen gör det möjligt att hantera dataarkitekturen med mer precision. Alla dokument ska inte behandlas lika. Alla källor ska inte indexeras på samma sätt. Alla användare ska inte få samma sökresultat.

## Metadata som styrningsmekanism

Metadata är en av de mest underskattade delarna av AI-arkitekturen. Utan metadata vet AI-lösningen inte om ett dokument är aktuellt, internt, publikt, sekretessbelagt, ersatt, granskat, preliminärt eller avgränsat till en viss process.

För AI bör metadata inte bara beskriva dokumentet. Metadata bör också kunna styra beteende. Ett dokument med högre skyddsvärde kan kräva särskild åtkomstkontroll. Ett utgånget dokument bör inte användas som primär källa. Ett preliminärt dokument kan få användas i intern beredning men inte i handläggarstöd. Ett dokument som saknar informationsägare bör inte ingå i produktionssatt AI-stöd.

Aurora beslutar därför att varje kunskapskälla som ska ingå i ett AI-index minst behöver följande metadata:

| Metadatafält | Syfte |
|---|---|
| Informationsägare | Visar vem som ansvarar för innehåll och godkännande. |
| Informationsklass | Styr skyddsnivå, åtkomst och driftmiljö. |
| Källa och dokument-ID | Gör svar spårbara till originalkälla. |
| Version och giltighet | Hindrar att gamla eller ersatta dokument används fel. |
| Åtkomstregel | Avgör vilka användare eller roller som får se innehållet. |
| Ämnesområde | Stödjer sökning, filtrering och ansvarsfördelning. |
| Granskningsdatum | Visar när informationen senast kvalitetssäkrades. |

Metadata ska inte ses som dokumentation vid sidan av lösningen. I en mogen AI-arkitektur är metadata en aktiv del av styrningen.

## Åtkomstkontroll i AI-flöden

Traditionell åtkomstkontroll utgår ofta från att användaren öppnar ett system, en databas eller ett dokument. AI förändrar detta. Användaren kan ställa en fråga i ett gränssnitt och få ett sammanställt svar baserat på flera källor. Då räcker det inte att skydda originaldokumenten. Åtkomstkontrollen måste följa med in i sökning, retrieval, promptkontext och svarsgenerering.

En grundregel är att AI-stödet aldrig ska ge användaren tillgång till information som användaren inte hade haft rätt att se i källsystemet. Det låter enkelt, men är tekniskt och organisatoriskt krävande.

För RAG-lösningar bör målarkitekturen därför kräva behörighetsmedveten retrieval. Det innebär att sökresultat filtreras utifrån användarens roll, behörighet, organisatoriska tillhörighet och informationsklass innan de skickas vidare till modellen. Det bör också finnas skydd mot att modellen sammanställer information från olika källor på ett sätt som kringgår avsedd sekretess.

Aurora väljer därför att dela upp kunskapsstödet i flera index och åtkomstzoner i stället för att skapa ett enda gemensamt index för allt material. Lågkänsliga styrdokument kan ligga i en bredare kunskapszon. Ärendenära material och skyddsvärd verksamhetsinformation kräver striktare zoner, mer loggning och tydligare godkännande.

## Embeddings och vektordatabaser som skyddsvärda tillgångar

Det är lätt att betrakta embeddings som tekniska mellanprodukter. Det är riskabelt. Embeddings kan representera innehåll från källmaterialet och kan i vissa situationer läcka information indirekt, särskilt om de hanteras fel, exporteras okontrollerat eller kombineras med svag åtkomstkontroll.

Målarkitekturen bör därför behandla embeddings och vektorindex som skyddsvärda tillgångar. De ska omfattas av informationsklassning, åtkomstkontroll, loggning, backup, gallring, incidenthantering och driftkrav.

Vektordatabasen bör inte heller väljas enbart utifrån sökprestanda. För en myndighet är följande frågor minst lika viktiga:

- Stödjer lösningen metadatafilter och behörighetsstyrd retrieval?
- Kan index separeras mellan informationsklasser eller verksamhetsdomäner?
- Går det att spåra vilken källa ett svar bygger på?
- Hur hanteras backup, radering och omskapande av index?
- Var lagras data, index och loggar?
- Vilka driftmodeller stöds: SaaS, moln, privat moln eller on-premises?
- Hur integreras lösningen med myndighetens identitets- och behörighetsmodell?

Ett moget arkitekturbeslut beskriver därför inte bara vilken vektordatabas som används, utan också vilken informationsklass den får hantera och vilka kontroller som krävs runt den.

## Datakvalitet och aktualitet

AI förstärker effekten av dålig datakvalitet. Om ett vanligt söksystem visar ett gammalt dokument kan användaren ofta se datum, filnamn och källa. Om ett AI-stöd sammanfattar samma dokument i en självsäker formulering kan felet bli svårare att upptäcka.

Dataarkitekturen behöver därför innehålla mekanismer för kvalitet och aktualitet. Det handlar inte bara om teknisk datakvalitet, utan också om förvaltningskvalitet.

För Tullverket Aurora blir följande regler styrande:

- AI-index ska byggas från auktoritativa källor, inte från privata kopior.
- Dokument utan informationsägare får inte användas i produktionssatt kunskapsstöd.
- Utgångna dokument ska antingen exkluderas eller tydligt markeras som historiska.
- Källhänvisning ska visas där svaret bygger på dokument.
- Index ska uppdateras enligt en definierad rytm eller händelsestyrt när källan ändras.
- Användarfeedback ska kunna kopplas till källa, version och svarstyp.

Det viktiga är att kvalitetssäkringen sker före och under drift, inte först när fel upptäcks i verksamheten.

## Data lineage från källa till AI-svar

Spårbarhet är särskilt viktig i offentlig sektor. När ett AI-stöd används i handläggning, analys eller beslutsnära processer behöver myndigheten kunna visa vilka källor, modeller, regler och versioner som påverkat ett svar.

För generativ AI bör lineage beskrivas bredare än i traditionella datalager. Ett svar kan bero på användarens prompt, behörighet, retrieval-resultat, chunking-strategi, modellversion, systemprompt, guardrails och efterbearbetning.

En praktisk lineage-modell för AI bör minst kunna visa:

- vilken användare eller process som initierade frågan,
- vilken informationsdomän som söktes,
- vilka källor och dokumentversioner som hämtades,
- vilken modell och modellversion som användes,
- vilka policyregler som tillämpades,
- vilket svar som genererades,
- om svaret användes, ändrades, avvisades eller rapporterades som felaktigt.

Allt detta behöver inte exponeras för slutanvändaren. Men det behöver kunna granskas av rätt roller vid incidenter, revision, kvalitetssäkring och förvaltning.

## Exempel från Tullverket Aurora

Aurora prioriterar ett första produktionsspår för intern kunskapssökning. Arkitekturgruppen avgränsar det till styrdokument, processbeskrivningar och interna handböcker som inte innehåller ärendespecifika personuppgifter.

I stället för att börja med modellval gör gruppen en datakarta. Den visar var dokumenten finns, vem som äger dem, hur de versioneras, vilka som får läsa dem och vilka metadata som saknas.

Kartläggningen visar fyra problem:

1. Flera dokument finns både i dokumenthanteringssystemet, på intranätet och i lokala samarbetsytor.
2. Vissa dokument saknar tydlig informationsägare.
3. Giltighetstid och ersatta versioner är inte konsekvent markerade.
4. Behörigheter följer inte alltid samma struktur mellan källsystem och publiceringsytor.

Aurora beslutar därför att det första AI-stödet bara får indexera auktoritativa källor. Man inför en metadata-miniminivå, separerar index efter informationsklass och kräver källhänvisning i varje svar. Man väljer också att logga retrieval-resultat och modellversion för att kunna granska felaktiga svar.

Detta gör den första lösningen smalare än många önskat, men betydligt mer produktionsbar.

## Vägvalsfrågor

När dataarkitekturen för AI tas fram bör arkitekten ställa följande frågor:

- Är datakällan auktoritativ eller bara en kopia?
- Vem ansvarar för informationens kvalitet och aktualitet?
- Vilken informationsklass gäller för källan, indexet, embeddings, promptar, svar och loggar?
- Ska index delas per domän, informationsklass, system eller användargrupp?
- Behöver retrieval filtreras utifrån användarens behörighet?
- Vilken metadata krävs för att AI-stödet ska kunna ge säkra och spårbara svar?
- Hur snabbt behöver ändringar i källsystem slå igenom i AI-stödet?
- Vilka delar av AI-flödet behöver lineage?
- Hur ska feedback, felrapportering och rättning hanteras?
- När ska data gallras, index raderas eller embeddings återskapas?

Dessa frågor bör dokumenteras som arkitekturbeslut eller som del av referensarkitekturen för AI.

## Vanliga fallgropar

- **Att indexera allt som finns.**
  - Varför det händer: Det verkar ge bättre svar och snabbare nytta.
  - Konsekvens: AI-stödet kan blanda aktuellt, gammalt, känsligt och felaktigt material.
  - Motåtgärd: Börja med auktoritativa källor och tydliga informationsdomäner.

- **Att glömma att embeddings också behöver skyddas.**
  - Varför det händer: Embeddings uppfattas som teknisk metadata.
  - Konsekvens: Skyddsvärd information kan hanteras i fel miljö.
  - Motåtgärd: Klassificera embeddings och vektorindex utifrån källmaterial och användningsfall.

- **Att bygga AI-sökning utan behörighetsmedveten retrieval.**
  - Varför det händer: Det är enklare att skapa ett gemensamt index.
  - Konsekvens: Användare kan få svar som bygger på information de inte borde nå.
  - Motåtgärd: Inför metadatafilter, zonindelning och integration med identitets- och behörighetsmodell.

- **Att sakna källhänvisning.**
  - Varför det händer: Det genererade svaret upplevs som tillräckligt.
  - Konsekvens: Användaren kan inte granska kvalitet, aktualitet eller ansvarig källa.
  - Motåtgärd: Kräv källor, dokumentversion och tydlig markering av osäkerhet.

- **Att behandla datakvalitet som ett AI-teams problem.**
  - Varför det händer: AI-lösningen synliggör felen först när den tas i bruk.
  - Konsekvens: Produktteamet får ansvar för informationsproblem som egentligen hör hemma i verksamhetsförvaltningen.
  - Motåtgärd: Koppla AI-flödet till informationsägarskap och datastyrning.

## Checklista

En målarkitektur för AI bör innehålla en tydlig dataarkitektur som minst beskriver:

- informationsdomäner och auktoritativa datakällor,
- informationsägare och ansvar för kvalitet,
- informationsklassning för källor, index, embeddings, promptar, svar och loggar,
- metadata som krävs för styrning, åtkomst och spårbarhet,
- åtkomstmodell och behörighetsmedveten retrieval,
- strategi för chunking, indexering och uppdatering,
- hantering av vektordatabaser och sökindex som skyddsvärda komponenter,
- lineage från källa till AI-svar,
- regler för feedback, felrapportering och kvalitetssäkring,
- gallring, radering, omskapande av index och avveckling.

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Dataarkitekturen är en av de delar som tydligast avgör om AI-förmågan blir produktionsbar. Den påverkar plattformsval, driftmodell, säkerhetszoner, integrationsmönster, governance, livscykelhantering och upphandling.

I målarkitekturen bör dataarkitekturen därför inte beskrivas som en bilaga. Den bör vara ett eget arkitekturperspektiv med tydliga principer, byggblock, beslut och krav.

För Tullverket Aurora leder kapitlets arbete till tre centrala målarkitekturbeslut:

1. AI-lösningar ska utgå från auktoritativa källor och dokumenterat informationsägarskap.
2. Index, embeddings, promptar, svar och loggar ska klassas och skyddas som delar av samma informationsflöde.
3. Retrieval ska vara behörighetsmedveten och kunna spåras från användarfråga till källor och modellversion.

Nästa kapitel bygger vidare på detta och beskriver den tekniska referensarkitektur som behövs för att omsätta förmågor, dataflöden och styrkrav i konkreta byggblock.
