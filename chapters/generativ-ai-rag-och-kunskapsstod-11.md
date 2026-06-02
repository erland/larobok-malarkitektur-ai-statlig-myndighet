# Kapitel 11: Generativ AI, RAG och kunskapsstöd

## Varför detta kapitel finns

Generativ AI är ofta den del av AI-området som först skapar synlig nytta i en större myndighet. Den kan sammanfatta text, stödja handläggare, söka i stora dokumentmängder, formulera utkast, förklara regelverk och hjälpa användare att hitta rätt information. Samtidigt är det också den del som lättast missförstås. En språkmodell kan ge ett svar som låter korrekt utan att svaret är tillräckligt grundat, aktuellt, spårbart eller tillåtet att använda i ett myndighetsbeslut.

För en erfaren IT-arkitekt är den centrala frågan därför inte om generativ AI fungerar i allmänhet. Frågan är hur generativ AI kan placeras i en myndighetsarkitektur där juridik, informationsklassning, ansvar, säkerhet, källor, behörighet och spårbarhet måste hålla ihop.

Detta kapitel fokuserar på generativ AI som kunskapsstöd. Det behandlar när enkel promptning räcker, när RAG är rätt mönster, när finjustering kan vara relevant och när egen modellservering eller mer kontrollerad drift kan behövas. Kapitlet bygger vidare på dataarkitekturen i kapitel 9 och den tekniska referensarkitekturen i kapitel 10.

## Arkitekturproblemet

Tullverket Aurora vill införa ett internt kunskapsstöd för handläggare och analytiker. Användarna vill kunna ställa frågor om interna handböcker, styrdokument, regelverk, kontrollrutiner och verksamhetsstöd. De vill också kunna få sammanfattningar av längre dokument och hjälp att hitta relevanta källor.

Det första experimentet är enkelt. Ett team laddar upp några dokument i ett generativt AI-verktyg och får imponerande svar. Efter några veckor upptäcks flera problem:

- vissa svar bygger på gamla dokumentversioner,
- användaren ser inte alltid vilka källor svaret bygger på,
- modellen blandar säkra uppgifter med antaganden,
- sekretessklassade dokument riskerar att hamna i fel miljö,
- behörigheter från källsystemen följer inte med in i AI-lösningen,
- loggarna visar inte tillräckligt för att utreda felaktiga svar,
- det är oklart vem som ansvarar för kvaliteten i kunskapsstödet.

Auroras arkitekturgrupp behöver därför formulera ett kontrollerat mönster för generativt kunskapsstöd. Mönstret ska inte bara beskriva en språkmodell, utan hela kedjan från källa till svar: dokumentkälla, urval, indexering, chunking, embeddings, vektorsökning, behörighetskontroll, promptkonstruktion, modellkörning, källhänvisning, loggning, uppföljning och förvaltning.

Den avgörande frågan blir:

> Hur bygger vi ett kunskapsstöd där svaret är användbart, men där myndigheten fortfarande kan styra källor, behörigheter, risker och ansvar?

## Centrala begrepp

Generativ AI är AI som kan skapa nytt innehåll, till exempel text, kod, bild, ljud eller sammanfattningar, baserat på mönster i träningsdata och aktuell indata.

Språkmodell är en modell som bearbetar och genererar text. I den här boken används begreppet främst om stora språkmodeller som kan sammanfatta, resonera, klassificera, formulera och svara på frågor.

Prompt är den instruktion eller kontext som skickas till modellen. En prompt kan innehålla användarens fråga, systeminstruktioner, hämtad källtext, formatkrav, säkerhetsregler och begränsningar.

Promptning innebär att styra modellen genom instruktioner och kontext utan att modellen tränas om.

RAG, retrieval-augmented generation, är ett mönster där relevant kontext hämtas från externa källor och skickas med till modellen när den genererar sitt svar. Syftet är att minska beroendet av modellens generella träningsdata och i stället grunda svaret i myndighetens egna auktoritativa källor.

Retrieval är steget där systemet söker fram relevanta dokumentdelar, ofta med en kombination av nyckelordssökning, semantisk sökning och filtrering.

Chunking är uppdelningen av dokument i mindre delar som kan indexeras och hämtas. Chunking påverkar både precision, kontext, spårbarhet och risken att svar bygger på lösryckt information.

Embeddings är numeriska representationer av text eller annat innehåll. De används ofta för semantisk sökning, där systemet försöker hitta innehåll som betyder något liknande som användarens fråga.

Vektordatabas är en databas eller söktjänst som lagrar embeddings och gör det möjligt att hitta semantiskt liknande innehåll.

Finjustering, fine-tuning, innebär att en modell tränas vidare på särskilda data för att ändra modellens beteende, stil eller förmåga inom ett avgränsat område.

Grounding innebär att modellens svar binds till specifika källor, data eller regler. I ett myndighetsstöd bör viktiga svar kunna visa vilka källor de bygger på.

Hallucination är när en modell producerar ett svar som verkar trovärdigt men inte är korrekt, inte följer källorna eller hittar på information.

## Rekommenderat angreppssätt

En myndighet bör inte börja med att fråga vilken språkmodell som är bäst. Den bör börja med att avgöra vilken typ av kunskapsstöd som ska byggas och vilken risknivå stödet har.

Ett praktiskt angreppssätt är att gå i sex steg.

### Steg 1: Avgränsa användningsfallet

Arkitekten bör först skilja mellan olika typer av generativt stöd. Ett internt skrivstöd för lågklassad information har andra krav än ett kunskapsstöd för sekretessbelagda ärenden. Ett stöd som hjälper användaren att hitta rätt dokument har andra risker än ett stöd som föreslår bedömningar i ett enskilt ärende.

Aurora delar in sina första generativa användningsfall i fyra nivåer:

| Nivå | Typ av stöd | Exempel | Arkitekturkonsekvens |
|---|---|---|---|
| 1 | Allmänt skriv- och produktivitetsstöd | Formulera utkast, förenkla text | Kan ofta hanteras med starka policyer och lågklassade data |
| 2 | Internt kunskapsstöd | Fråga i styrdokument och handböcker | Kräver källstyrning, RAG och behörighetskontroll |
| 3 | Ärendenära stöd | Sammanfatta handlingar i ett ärende | Kräver högre kontroll, loggning och tydlig mänsklig granskning |
| 4 | Beslutsnära stöd | Föreslå bedömning eller prioritering | Kräver särskild riskprövning, dokumentation och stark governance |

Denna indelning gör att samma tekniska mönster inte används okritiskt för alla behov.

### Steg 2: Bestäm källorna innan modellen väljs

För kunskapsstöd är källorna viktigare än modellen i den första arkitekturfrågan. Ett RAG-system med fel källor ger fel svar även om modellen är kraftfull. Ett enklare modellval med välstyrda, aktuella och behörighetskontrollerade källor kan vara bättre än en avancerad modell med svag informationsförvaltning.

Aurora beslutar att produktionssatt kunskapsstöd bara får bygga på källor som har:

- utsedd informationsägare,
- tydlig informationsklass,
- dokumenterad giltighet,
- versionshantering,
- definierade åtkomstregler,
- känd uppdateringsprocess,
- möjlighet till spårbarhet från svar till källa.

Det innebär att en stor del av arbetet ligger utanför själva AI-tekniken. Dokumentförvaltning, metadata, informationsägarskap och åtkomstkontroll blir förutsättningar för en säker AI-lösning.

### Steg 3: Välj mönster: promptning, RAG, finjustering eller egen modell

Generativ AI kan användas på flera sätt. Arkitekten behöver kunna välja rätt mönster för rätt problem.

Enkel promptning passar när användaren behöver hjälp med formulering, sammanfattning eller bearbetning av information som användaren själv tillhandahåller, och där kraven på källhänvisning, aktualitet och verksamhetsspecifik kunskap är begränsade.

RAG passar när modellen behöver svara med stöd i myndighetens dokument, regler, handböcker eller ärendematerial. RAG är ofta förstahandsvalet för myndighetsnära kunskapsstöd eftersom källorna kan styras utan att modellen tränas om.

Finjustering kan vara relevant när problemet inte främst handlar om att tillföra kunskap, utan om att modellen behöver lära ett format, en klassificeringsuppgift, en särskild stil eller ett återkommande mönster. Finjustering är däremot inte en ersättning för god informationsförvaltning.

Egen modellservering kan vara relevant när informationsklassning, säkerhetskrav, kostnadskontroll, latens, beroenderisk eller krav på lokal drift gör att extern modell-API eller SaaS inte är lämpligt. Det kräver dock betydligt mer driftkompetens, övervakning och livscykelhantering.

### Steg 4: Gör retrieval behörighetsmedveten

I en myndighet räcker det inte att RAG-systemet hittar semantiskt relevanta dokument. Det måste hitta dokument som användaren faktiskt får se.

Behörighetsmedveten retrieval innebär att åtkomstregler tillämpas innan kontext skickas till modellen. Det bör inte vara modellens ansvar att ignorera otillåten information. Otillåten information ska aldrig skickas till modellen i första läget.

Detta får flera arkitekturkonsekvenser:

- metadata om informationsklass och åtkomst måste följa med in i index,
- användarens identitet och roll måste vara känd i retrieval-steget,
- sökresultat måste filtreras före promptkonstruktion,
- loggar måste visa vilka källor som hämtades och vilka som filtrerades bort,
- index måste kunna separeras eller segmenteras vid behov,
- källsystemens behörigheter måste synkroniseras eller mappas till AI-plattformens åtkomstmodell.

För Aurora blir detta en grundprincip: RAG får inte vara ett sätt att kringgå källsystemens behörighetsmodell.

### Steg 5: Kräv källor, osäkerhetsmarkering och mänsklig kontroll

Ett kunskapsstöd ska inte bara ge ett svar. Det ska hjälpa användaren att bedöma svarets tillförlitlighet. Därför bör svaret normalt innehålla källhänvisningar, dokumentversioner eller andra spår till underlaget.

Aurora inför tre designregler:

1. Svar som bygger på myndighetens dokument ska visa källor.
2. När relevanta källor saknas ska systemet säga det i stället för att gissa.
3. Ärendenära eller beslutsnära användning ska kräva mänsklig kontroll och tydlig ansvarsfördelning.

Detta påverkar både användargränssnitt och backend-arkitektur. Källhänvisningar måste följa med från retrieval till svarspresentation. Modellens svar måste kunna jämföras med hämtad kontext. Loggar måste kunna visa vilken modell, prompt, källkontext och policy som användes.

### Steg 6: Förvalta kunskapsstödet som en produkt

Ett RAG-baserat kunskapsstöd är inte färdigt när den första versionen fungerar. Det kräver löpande förvaltning.

Aurora definierar därför ett produktansvar för kunskapsstödet. Produktteamet ansvarar inte bara för användargränssnittet utan även för kvalitet i sökresultat, indexuppdatering, feedbackloopar, mätetal, incidenter, användarstöd och förändringshantering.

Minsta förvaltningsförmåga omfattar:

- ägarskap för källsamlingar,
- uppdateringsrutiner för index,
- testfrågor och regressionskontroller,
- uppföljning av felaktiga svar,
- hantering av användarfeedback,
- modell- och promptversionering,
- kostnads- och kapacitetsuppföljning,
- incidentprocess vid felaktig exponering eller missvisande svar.

## Exempel från Tullverket Aurora

Aurora väljer att börja med ett internt kunskapsstöd för handläggare inom varuflödeskontroll. Syftet är inte att automatisera beslut, utan att hjälpa användare att hitta relevanta rutiner, styrdokument och tolkningar snabbare.

Arkitekturgruppen formulerar användningsfallet så här:

> Handläggaren ska kunna ställa frågor på naturligt språk och få ett svar som sammanfattar relevanta interna dokument, visar källor och markerar när underlaget är otillräckligt.

Use caset klassas som internt kunskapsstöd. Det får inte fatta beslut, inte föreslå sanktioner och inte ersätta handläggarens ansvar. Det får däremot sammanfatta källor, visa skillnader mellan dokumentversioner och föreslå vilka dokument användaren bör läsa vidare i.

Aurora väljer ett RAG-mönster med följande byggblock:

1. Dokumentkällor från dokumenthanteringssystem och intern regelverksportal.
2. Metadataextraktion för informationsklass, dokumentägare, giltighet och version.
3. Chunking som tar hänsyn till rubriker, avsnitt och dokumentstruktur.
4. Embedding och indexering i en kontrollerad vektordatabas.
5. Behörighetsmedveten retrieval kopplad till identitet och roll.
6. Promptkonstruktion med systeminstruktioner, källkontext och svarskrav.
7. Modellkörning via AI-gateway.
8. Svarspresentation med källor och osäkerhetsmarkering.
9. Loggning av fråga, retrieval, modellversion, svar och källhänvisningar enligt fastställd loggpolicy.

Arkitekturgruppen dokumenterar också vad lösningen inte får göra:

- den får inte besvara frågor utifrån dokument som användaren saknar behörighet till,
- den får inte använda öppna webbkällor utan separat godkännande,
- den får inte spara användarens promptar i en extern modellleverantörs träningsdata,
- den får inte dölja när underlaget är otillräckligt,
- den får inte presentera modellens svar som myndighetens formella beslut.

Den första versionen begränsas till dokument med låg till måttlig skyddsnivå. Mer känsliga dokument och ärendenära sammanfattning skjuts till senare steg, efter att loggning, åtkomstkontroll, testmetodik och incidenthantering har verifierats.

## Vägvalsfrågor

### Räcker promptning?

Promptning kan räcka när användaren själv förser modellen med allt relevant underlag, när informationen är lågklassad och när svaret inte behöver vara spårbart till myndighetens auktoritativa källor. Det kan vara användbart för språkgranskning, strukturering av text, mötesanteckningar eller idéutkast.

Promptning räcker normalt inte när svaret behöver bygga på myndighetens aktuella styrdokument, när behörigheter spelar roll eller när användaren behöver kunna granska källorna.

### Är RAG rätt mönster?

RAG är ofta rätt när problemet är kunskapsåtkomst. Det gäller särskilt när myndigheten redan har dokument, handböcker, regler, rutiner eller tidigare ärenden som ska användas som kontext.

RAG är däremot inte en garanti för korrekta svar. Ett RAG-system kan fortfarande hämta fel dokument, missa relevant kontext, tolka källor fel eller formulera ett svar som går längre än underlaget. Därför behöver RAG kombineras med källstyrning, testning, loggning och användargränssnitt som visar underlaget.

### Behövs finjustering?

Finjustering bör inte vara första svaret på att modellen saknar kunskap om myndighetens dokument. I många fall är RAG bättre eftersom källorna kan uppdateras utan att modellen tränas om.

Finjustering kan övervägas när myndigheten har ett stabilt, återkommande mönster som modellen behöver lära sig. Det kan exempelvis vara klassificering av dokumenttyper, strukturering av text enligt en särskild mall eller hantering av återkommande språkbruk. Beslutet kräver dock tydlig datahantering, testning och modellförvaltning.

### Ska modellen köras i moln eller on-premises?

Detta avgörs inte av generativ AI i sig, utan av informationsklassning, krav på datalokalisering, beroenderisk, kostnad, prestanda och intern förmåga. För lågklassade produktivitetsstöd kan en kontrollerad molntjänst vara rimlig. För känsliga ärendenära flöden kan on-premises, privat moln eller särskilt kontrollerad molnmiljö vara nödvändig.

Det viktiga är att driftmodellen följer riskklassningen. Samma myndighet kan behöva flera driftmodeller samtidigt.

### Ska myndigheten ha en gemensam AI-gateway?

För Aurora är svaret ja. En gemensam AI-gateway ger en plats för modellval, policy, loggning, kvoter, kostnadsstyrning och kontroll av vilka tjänster som får användas. Det betyder inte att alla användningsfall måste använda samma modell, men det betyder att åtkomsten till modeller bör vara styrd och observerbar.

Utan en gemensam gateway riskerar varje team att bygga egna kopplingar till olika modellleverantörer, med olika loggning, olika villkor och olika säkerhetsnivå.

## Arkitekturmönster för RAG i myndighetsmiljö

Ett robust RAG-mönster i myndighetsmiljö bör innehålla flera lager.

### Källager

Källagret består av dokumenthanteringssystem, regelverksportaler, ärendesystem, kunskapsdatabaser och andra auktoritativa informationskällor. Varje källa bör ha ägare, informationsklass och uppdateringsrutin.

### Indexeringslager

Indexeringslagret hämtar, normaliserar och delar upp innehåll. Det skapar embeddings, lagrar metadata och bygger sökbara index. Detta lager måste hantera versioner, borttag, uppdateringar och fel i källdata.

### Retrieval-lager

Retrieval-lagret tar emot användarens fråga och hämtar relevant kontext. Det bör kombinera semantisk sökning med metadatafilter, behörighetskontroll och ibland traditionell sökning. I känsliga miljöer är detta lager ett säkerhetskritiskt kontrollsteg.

### Prompt- och orkestreringslager

Detta lager konstruerar prompten som skickas till modellen. Det avgör vilka instruktioner, källtexter, begränsningar och formatkrav som ska ingå. Här kan även kontrollfrågor, omformulering av fråga och val av modell ske.

### Modell- och inferenslager

Modellagret genererar svaret. Det kan bestå av en extern modell-API-tjänst, en molnbaserad modellplattform eller en intern inferensmiljö. Modellens beteende måste betraktas som en del av helhetsarkitekturen, inte som en svart låda utan ansvar.

### Svarskontroll och presentation

Efter modellkörning kan svaret kontrolleras mot policy, formatkrav, källhänvisningar och tillåtna svarstyper. Användargränssnittet bör visa källor, begränsningar och när svaret inte är tillräckligt underbyggt.

### Observability och förvaltning

Alla steg behöver kunna följas upp. Det handlar inte nödvändigtvis om att spara allt innehåll i klartext, men om att ha tillräcklig spårbarhet för felsökning, revision, kvalitet och incidenthantering. Loggningen måste balansera spårbarhet mot dataskydd och sekretess.

## Vanliga fallgropar

- **Fallgrop: Att tro att RAG löser hallucinationer automatiskt.**
  - Varför det händer: RAG ger modellen källor, men modellen kan fortfarande tolka fel, missa nyanser eller formulera sig för säkert.
  - Hur det undviks: Kräv källhänvisningar, testa med kända frågor, visa osäkerhet och begränsa användningsfall med hög risk.

- **Fallgrop: Att indexera allt som går att hitta.**
  - Varför det händer: Fler dokument känns som bättre täckning.
  - Hur det undviks: Indexera bara källor med ägare, klassning, giltighet och uppdateringsrutin.

- **Fallgrop: Att låta modellen hantera behörigheter.**
  - Varför det händer: Man hoppas att prompten ska instruera modellen att inte visa känslig information.
  - Hur det undviks: Filtrera otillåten kontext före modellkörning.

- **Fallgrop: Att behandla embeddings som ofarliga tekniska artefakter.**
  - Varför det händer: Embeddings ser inte ut som läsbar text.
  - Hur det undviks: Klassa embeddings och index utifrån källmaterial, användningsfall och återidentifieringsrisk.

- **Fallgrop: Att bygga ett kunskapsstöd utan förvaltning.**
  - Varför det händer: Den första demonstrationen fungerar bra.
  - Hur det undviks: Etablera produktägarskap, testfrågor, indexrutiner, feedbackloopar och incidentprocess från start.

- **Fallgrop: Att använda finjustering för fel problem.**
  - Varför det händer: Finjustering låter mer avancerat än RAG.
  - Hur det undviks: Använd finjustering för beteende, format eller klassificeringsmönster, inte som ersättning för aktuella källor.

## Checklista

- Är användningsfallet klassat som produktivitetsstöd, kunskapsstöd, ärendenära stöd eller beslutsnära stöd?
- Är informationsklassning gjord för promptar, källor, embeddings, index, svar och loggar?
- Finns utsedd informationsägare för varje källa?
- Är källorna aktuella, versionerade och giltiga?
- Är retrieval behörighetsmedveten?
- Filtreras otillåten kontext innan den skickas till modellen?
- Visar svaret källor när det bygger på myndighetens dokument?
- Finns hantering för när underlaget är otillräckligt?
- Är promptar, modellval och policyregler versionerade?
- Finns loggning som stödjer felsökning, revision och incidenthantering?
- Är användargränssnittet tydligt med att stödet inte ersätter mänskligt ansvar?
- Finns testfrågor och regressionskontroller?
- Finns process för att uppdatera index när källor ändras?
- Är leverantörens villkor för dataanvändning, loggning och träning granskade?
- Är driftmodell vald utifrån risk, inte utifrån bekvämlighet?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Generativ AI och RAG ska inte beskrivas som en isolerad lösning i målarkitekturen. De bör beskrivas som ett återanvändbart mönster inom myndighetens AI-förmåga.

I målarkitekturen bör följande delar synas:

- vilka typer av generativa användningsfall myndigheten stödjer,
- vilka källor som får användas för produktionssatt kunskapsstöd,
- hur RAG-index skapas, uppdateras och avvecklas,
- hur behörighetsmedveten retrieval fungerar,
- hur AI-gateway används för modellåtkomst och policy,
- hur promptar, modeller och svar versioneras,
- hur källhänvisning och grounding ska fungera,
- hur loggning och observability utformas,
- vilka driftmodeller som är tillåtna för olika informationsklasser,
- vilka roller som ansvarar för källor, produkt, modell, säkerhet och juridik.

För Tullverket Aurora blir resultatet ett styrande RAG-mönster som kan återanvändas i flera produkter. Det första kunskapsstödet för handläggare blir därmed inte en engångslösning, utan ett sätt att etablera gemensamma byggblock för framtida AI-förmåga.

Kapitlets viktigaste arkitekturpoäng är enkel: generativ AI blir användbar i myndighetsmiljö först när den binds till styrda källor, rätt behörighet, tydlig riskklassning, spårbarhet och mänskligt ansvar. RAG är ett kraftfullt mönster, men bara när det behandlas som en del av myndighetens informations- och säkerhetsarkitektur.
