# Kapitel 20: Vanliga misstag och anti-patterns

## Varför detta kapitel finns

Målarkitektur för AI misslyckas sällan för att organisationen saknar idéer. Den misslyckas oftare för att idéerna angrips i fel ordning, för att teknikval görs innan risk och ansvar är klarlagda, eller för att organisationen underskattar hur mycket styrning, dataarbete, säkerhet och förvaltning som krävs för att AI ska fungera i produktion.

Det här kapitlet samlar återkommande misstag och anti-patterns som en erfaren arkitekt bör kunna känna igen tidigt. Syftet är inte att skapa rädsla för AI. Syftet är att göra riskerna synliga så att myndigheten kan röra sig framåt med bättre kontroll.

Ett anti-pattern är ett återkommande arbetssätt eller arkitekturval som ser rimligt ut på kort sikt men ofta leder till problem över tid. I AI-sammanhang kan ett anti-pattern vara tekniskt, organisatoriskt, juridiskt eller verksamhetsmässigt. Det kan handla om att börja med en produkt i stället för ett behov, att bygga en modellplattform utan dataförmåga, att införa generativ AI utan loggning eller att låta varje avdelning skapa sin egen AI-stack.

För Tullverket Aurora blir kapitlet en kontrollpunkt. Myndigheten har tagit fram en målarkitektur, men den behöver också veta vilka vägval som riskerar att underminera målbilden.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- känna igen vanliga anti-patterns i AI-arkitektur,
- skilja mellan teknisk skuld, styrningsskuld, dataskuld och säkerhetsskuld,
- se varför vissa kortsiktiga lösningar försvårar långsiktig AI-förmåga,
- formulera motåtgärder som arkitekturbeslut, principer, checklistor och införandesteg,
- använda Tullverket Aurora som exempel för att korrigera felaktiga vägval,
- prioritera vilka misstag som måste hanteras tidigt och vilka som kan hanteras stegvis.

## Innan vi börjar

Ett anti-pattern är inte samma sak som ett dåligt beslut i alla sammanhang. Ibland kan ett val vara rimligt i en begränsad pilot men olämpligt som myndighetsgemensam målarkitektur. En publik AI-tjänst kan vara rätt för lågkänslig intern produktivitet men fel för sekretessbelagda ärendehandlingar. En enkel RAG-lösning kan vara rätt för en första kunskapsassistent men otillräcklig för beslutsstöd med hög verksamhetspåverkan.

Det viktiga är därför inte att förbjuda alla riskabla mönster. Det viktiga är att placera dem i rätt kontext, dokumentera beslutet och sätta tydliga gränser.

I det här kapitlet används fyra skuldtyper:

| Skuldtyp | Innebörd | Typisk konsekvens |
|---|---|---|
| Teknisk skuld | Tekniska genvägar som gör lösningen svår att ändra, säkra eller förvalta | Dyrare vidareutveckling och ökande komplexitet |
| Styrningsskuld | Otydliga mandat, roller, beslut och ansvar | Oklara prioriteringar och svag regelefterlevnad |
| Dataskuld | Brister i datakvalitet, metadata, ägarskap, åtkomst och spårbarhet | Sämre AI-resultat och högre risk |
| Säkerhetsskuld | Bristande kontroller, loggning, behörighet, segmentering eller incidentförmåga | Ökad risk för läckage, manipulation och otillåten användning |

En målarkitektur ska inte bara beskriva önskat tillstånd. Den ska också minska dessa skuldtyper över tid.

## Anti-pattern 1: Att börja med verktyget

Det vanligaste misstaget är att inleda AI-arbetet med frågan: vilken plattform eller produkt ska vi köpa? Frågan är begriplig, men den kommer för tidigt. Om myndigheten börjar med verktyget riskerar den att anpassa användningsfallen, riskbedömningen och organisationen efter en leverantörs produktlogik i stället för efter myndighetens uppdrag.

För Tullverket Aurora visar sig detta när flera avdelningar vill köpa olika AI-assistenter. En avdelning vill använda en färdig molntjänst för mötesanteckningar. En annan vill skapa en RAG-lösning för styrdokument. En tredje vill utvärdera open source-modeller för analysstöd. Alla initiativ kan vara rimliga var för sig, men utan gemensam målarkitektur blir helheten splittrad.

### Varför det händer

Verktyg är konkreta. Målarkitektur, riskklassning och governance är mer abstrakta. Leverantörer kan dessutom visa fungerande demonstrationer snabbt, medan myndighetens interna styrning tar längre tid. Det skapar ett tryck att gå direkt till lösning.

### Konsekvens

Myndigheten får en produktportfölj utan gemensam förmåga. Integration, loggning, behörighet, dataåtkomst, juridisk bedömning och förvaltning måste lösas om och om igen. Det blir svårt att avgöra vilka data som får användas var och vilka kontroller som gäller för olika AI-roller.

### Motåtgärd

Arkitekten bör vända ordningen:

1. Definiera användningsfall och AI-roll.
2. Gör juridisk triage och informationsklassning.
3. Fastställ principer och tillåtna driftmodeller.
4. Beskriv gemensamma byggblock.
5. Välj produkt eller plattform per arkitekturspår.

Produkter ska alltså väljas mot en beslutad målbild, inte ersätta målbilden.

## Anti-pattern 2: En AI-plattform för allt

Ett annat vanligt misstag är att tro att myndigheten ska hitta en enda AI-plattform som löser alla behov. Det är lockande eftersom det ger en känsla av standardisering. Men AI-användning varierar kraftigt i data, risk, användare, teknisk komplexitet och rättsliga krav.

Aurora har minst tre olika behov: lågkänslig intern produktivitet, kontrollerad kunskapssökning i interna styrdokument och känsligt beslutsstöd nära kontrollverksamheten. Dessa behov bör inte nödvändigtvis dela samma tekniska miljö, samma leverantör, samma modelltyp eller samma driftsmodell.

### Varför det händer

Organisationer vill undvika fragmentering. Därför söker de en gemensam plattform. Standardisering är bra, men den måste ske på rätt nivå. Det är ofta bättre att standardisera principer, identitet, loggning, policy enforcement, AI-gateway, modellregister och beslutsprocesser än att tvinga alla användningsfall till samma runtime.

### Konsekvens

Antingen blir plattformen för svag för känsliga användningsfall eller för tung för enkla användningsfall. Resultatet blir ofta att verksamheten går runt plattformen, att parallella lösningar växer fram eller att innovation bromsas av onödig komplexitet.

### Motåtgärd

Målarkitekturen bör tillåta flera kontrollerade arkitekturspår:

- ett spår för lågkänslig produktivitet,
- ett spår för intern kunskapssökning och RAG,
- ett spår för känsliga ärendedata,
- ett spår för analytiska modeller,
- ett spår för högkontrollerat beslutsstöd.

Gemensamma krav bör läggas där de ger återanvändning: identitet, åtkomstkontroll, loggning, riskklassning, livscykelhantering och arkitekturbeslut.

## Anti-pattern 3: AI-sandlådan som aldrig blir produktionsförmåga

Många organisationer skapar en AI-sandlåda för att komma igång. Det är ofta klokt. Problemet uppstår när sandlådan blir ett permanent sidospår utan väg till produktion.

I Aurora används en sandlåda för att testa RAG mot interna styrdokument. Teamen lär sig mycket, men efter sex månader finns ingen tydlig väg för att hantera behörighetsstyrning, loggning, incidenter, modelluppdateringar eller förvaltningsansvar. Sandlådan har skapat kunskap, men inte produktionsförmåga.

### Varför det händer

Sandlådor är enkla att starta eftersom de kan avgränsas från ordinarie processer. Produktionsförmåga kräver däremot integration med säkerhet, drift, juridik, upphandling, support, incidenthantering och förvaltning. Det är betydligt mer arbete.

### Konsekvens

Organisationen får många lyckade experiment men få införda lösningar. Verksamheten tappar förtroende när piloter inte leder vidare. Samtidigt växer teknisk och organisatorisk skuld eftersom varje pilot bygger egna antaganden.

### Motåtgärd

Sandlådan ska designas med en produktionsväg från början. Det innebär att varje pilot bör ha:

- en ägare för användningsfallet,
- en preliminär riskklassning,
- en plan för data och behörighet,
- kriterier för när piloten får gå vidare,
- en beslutad integrationsväg,
- ett förvaltningsantagande,
- ett stoppkriterium om nyttan eller kontrollen inte räcker.

Sandlådan är en lärmiljö, inte en alternativ produktionsmiljö.

## Anti-pattern 4: Juridik som efterhandsgranskning

I traditionella IT-projekt kan juridik ibland komma in sent, även om det sällan är idealiskt. I AI-projekt är det särskilt riskabelt. Data, modellroll, automatiseringsgrad, användarpåverkan och leverantörsvillkor kan helt förändra lösningens tillåtlighet.

Aurora upptäcker detta när ett team har byggt en fungerande prototyp för sammanfattning av ärendehandlingar. Först efteråt blir det tydligt att materialet innehåller personuppgifter, sekretessrisker och känsliga verksamhetsuppgifter. Lösningen måste då göras om.

### Varför det händer

Juridiska frågor uppfattas ibland som hinder snarare än designkrav. Team vill visa nytta snabbt och tror att juridisk granskning kan göras när tekniken fungerar.

### Konsekvens

Lösningar byggs på fel antaganden. Data kan ha behandlats i olämpliga miljöer, loggar kan sakna rätt skydd, leverantörsvillkor kan vara oförenliga med myndighetens krav och beslut kan sakna dokumentation.

### Motåtgärd

Juridik, dataskydd och informationssäkerhet ska in i use-case triage. Arkitekturen bör ha tydliga stoppljus:

| Bedömning | Innebörd | Arkitekturkonsekvens |
|---|---|---|
| Grön | Låg risk och låg känslighet | Kan prövas i godkänd standardmiljö |
| Gul | Oklara eller måttliga risker | Kräver fördjupad bedömning och kontroller |
| Röd | Hög känslighet eller hög påverkan | Kräver särskilt beslut, strikt miljö eller avslag |

Det juridiska arbetet ska vara en del av designen, inte en kontrollstation efter designen.

## Anti-pattern 5: Datagrunden hoppas över

AI-lösningar är beroende av data, men många initiativ börjar med modell och gränssnitt i stället för datagrund. Det kan fungera i en demonstration, men bristerna blir tydliga när lösningen ska användas i produktion.

Auroras kunskapsstöd fungerar bra på en liten uppsättning handböcker. När fler dokument läggs till uppstår problem: gamla versioner blandas med nya, dokumentägarskap är oklart, metadata saknas, vissa dokument är sekretessbelagda och behörighetsmodellen följer inte med in i sökindexet.

### Varför det händer

Modeller och chattgränssnitt är synliga. Metadata, datakvalitet, informationsägarskap och åtkomstmodeller är mindre synliga. Därför prioriteras de lätt ned.

### Konsekvens

AI-lösningen ger fel svar, visar gammal information eller exponerar material för fel användare. Förtroendet för AI-förmågan minskar och lösningen blir svår att skala.

### Motåtgärd

Målarkitekturen ska behandla data som ett primärt byggblock. För varje AI-användningsfall behöver arkitekten fråga:

- Vilka datakällor används?
- Vem äger informationen?
- Vilken version är gällande?
- Vilka metadata krävs?
- Vilka behörigheter ska följa med?
- Hur hanteras gallring, arkiv och radering?
- Hur loggas användning och åtkomst?
- Hur upptäcks felaktigt eller föråldrat innehåll?

Utan datagrund finns ingen robust AI-förmåga.

## Anti-pattern 6: RAG som universalmedicin

RAG är ett kraftfullt mönster för att kombinera språkmodeller med interna kunskapskällor. Men RAG löser inte alla problem. Det löser inte automatiskt dålig datakvalitet, otydligt informationsägarskap, komplicerade behörigheter, juridiska risker eller behov av verksamhetsvalidering.

Aurora börjar med RAG för intern kunskapssökning. Det är rimligt. Men när samma mönster föreslås för riskanalys i kontrollverksamhet blir det problematiskt. Riskanalys kräver validerade datakällor, mätbar prestanda, spårbarhet, tydlig mänsklig kontroll och dokumenterade begränsningar. En enkel RAG-lösning räcker inte.

### Varför det händer

RAG är lätt att demonstrera. Det ger snabbt upplevelsen av att myndigheten kan prata med sina dokument. Därför kan mönstret överanvändas.

### Konsekvens

Myndigheten försöker använda ett kunskapsstödmönster för beslutsstöd, analys eller automation där kraven är helt andra. Det ökar risken för felaktiga slutsatser, övertron på genererade svar och svag spårbarhet.

### Motåtgärd

RAG bör placeras i rätt arkitekturspår. Arkitekten bör skilja mellan:

- kunskapsstöd där användaren själv bedömer svaret,
- ärendestöd där svaret påverkar handläggning,
- beslutsstöd där AI-resultat påverkar prioritering eller åtgärd,
- automation där AI-resultat direkt driver processer.

Ju närmare verksamhetsbeslut lösningen ligger, desto mer krävs av validering, kontroll, dokumentation och uppföljning.

## Anti-pattern 7: Fine-tuning innan problemet är förstått

Fine-tuning kan vara relevant i vissa fall, men det är ofta ett för tidigt vägval. Många problem löses bättre med bättre promptar, bättre informationsstruktur, RAG, klassiska regler, sök, datakvalitet, processförändring eller en mindre specialiserad modell.

Aurora överväger att finjustera en språkmodell på interna ärendetexter för att få bättre sammanfattningar. Vid närmare analys visar det sig att problemet främst är att dokumenttyperna är ojämna, metadata saknas och sammanfattningsbehovet varierar mellan roller. Fine-tuning hade skapat ny risk utan att lösa grundproblemet.

### Varför det händer

Fine-tuning låter avancerat och kan uppfattas som en naturlig väg när en modell inte svarar tillräckligt bra. Men det kräver data, testuppsättningar, utvärdering, modellhantering och kontroll.

### Konsekvens

Myndigheten tar på sig modellansvar, datarisker och livscykelkomplexitet utan tydlig nytta. Lösningen blir svårare att uppdatera, förklara och validera.

### Motåtgärd

Använd en beslutsordning:

1. Förbättra informationsstruktur och datakvalitet.
2. Förbättra promptar och instruktioner.
3. Använd RAG eller verktygsanrop där kunskap behöver hämtas.
4. Utvärdera mindre eller mer specialiserade modeller.
5. Överväg fine-tuning först när mätbara krav inte nås på annat sätt.

Fine-tuning ska vara ett motiverat arkitekturbeslut, inte en reflex.

## Anti-pattern 8: Otydligt modellansvar

När AI-lösningar går i produktion behöver någon ansvara för modellen och dess beteende över tid. Det räcker inte att säga att leverantören ansvarar för modellen eller att IT ansvarar för systemet. Myndigheten ansvarar för hur AI används i den egna verksamheten.

Aurora inför ett analysstöd där modellens resultat används som underlag i prioritering. Efter några månader ändras modellens beteende när leverantören uppdaterar en komponent. Ingen har definierat vem som ska upptäcka förändringen, validera konsekvenserna eller besluta om fortsatt användning.

### Varför det händer

Traditionell systemförvaltning är ofta fokuserad på tillgänglighet, incidenter och förändringar i kod. AI kräver även uppföljning av resultatkvalitet, begränsningar, bias, drift, modellversioner och datakopplingar.

### Konsekvens

AI-lösningen förändras utan styrning. Fel kan uppstå långsamt och bli svåra att upptäcka. Ansvarsfördelningen blir oklar vid incidenter, klagomål eller tillsyn.

### Motåtgärd

Inför modellägarskap som del av AI-förmågan. En modellägare behöver inte ensam kunna allt, men rollen måste ha mandat att samordna:

- verksamhetskrav,
- modellversioner,
- test och validering,
- övervakning,
- incidenter,
- ändringsbeslut,
- avveckling.

Modellägarskap ska kopplas till systemägarskap, informationsägarskap och förvaltningsmodell.

## Anti-pattern 9: Loggning utan syfte eller skydd

AI-lösningar behöver loggning för spårbarhet, felsökning, uppföljning, säkerhet och regelefterlevnad. Men loggning kan också skapa nya risker. Prompter, svar, dokumentutdrag och användarinteraktioner kan innehålla personuppgifter, sekretessbelagd information eller känsliga verksamhetsuppgifter.

Aurora börjar logga alla prompter och svar från en intern AI-assistent. Det ger god felsökningsmöjlighet men skapar samtidigt en ny känslig datamängd som få hade riskbedömt.

### Varför det händer

Team vill kunna felsöka och förbättra lösningen. Därför loggas mycket. Samtidigt är det lätt att glömma att loggar kan bli mer känsliga än källsystemen, eftersom de kombinerar frågor, utdrag, användarbeteende och genererade svar.

### Konsekvens

Loggar blir en dold informationsrisk. De kan få för bred åtkomst, för lång retention eller otydlig gallring. Vid incident kan loggar avslöja mer än den ursprungliga tjänsten.

### Motåtgärd

Loggstrategin ska beslutas som del av målarkitekturen. För varje AI-lösning bör det vara tydligt:

- vad som loggas,
- varför det loggas,
- vem som får läsa loggarna,
- hur länge loggar sparas,
- hur känsliga fält maskas eller pseudonymiseras,
- hur loggar används för uppföljning,
- hur loggar skyddas vid incidenter och revision.

Loggning är inte bara en teknisk funktion. Det är ett informationshanteringsbeslut.

## Anti-pattern 10: Mänsklig kontroll som formulering i stället för design

Många AI-principer säger att människan ska ha kontroll. Problemet är att principen ofta stannar som formulering. Mänsklig kontroll måste designas in i arbetsflöde, gränssnitt, ansvar, utbildning, dokumentation och uppföljning.

Aurora anger i sin principlista att AI bara ska ge rekommendationer. Men i praktiken visar gränssnittet AI-svaret överst, utan källor, utan osäkerhetsmarkering och utan tydlig möjlighet för handläggaren att rapportera fel. Då blir den mänskliga kontrollen svag även om den finns på papper.

### Varför det händer

Det är lätt att skriva att AI inte fattar beslut. Det är svårare att se hur människor faktiskt agerar under tidspress, med auktoritativa systemgränssnitt och begränsad insyn i modellens begränsningar.

### Konsekvens

Användaren börjar följa AI-resultat okritiskt. Felaktiga rekommendationer kan få genomslag. Ansvarsbilden blir oklar eftersom organisationen formellt säger att människan beslutar, men systemdesignen styr användaren hårt.

### Motåtgärd

Mänsklig kontroll måste konkretiseras:

- användaren ska förstå AI-roll och begränsningar,
- AI-resultat ska visas med relevanta källor eller förklaringar där det är möjligt,
- gränssnittet ska stödja ifrågasättande,
- det ska finnas rutiner för felrapportering,
- beslut ska dokumenteras med mänsklig motivering när det krävs,
- mätning ska visa om användare överförlitar sig på AI.

Human oversight är en designfråga, inte bara en policyformulering.

## Anti-pattern 11: Leverantörsinlåsning genom bekvämlighet

AI-plattformar erbjuder ofta attraktiva helhetslösningar. Det kan vara rätt att använda dem. Problemet uppstår när myndigheten oavsiktligt låser in data, promptar, embeddings, utvärderingar, modellintegrationer och säkerhetsmönster i en leverantörsspecifik struktur utan exitstrategi.

Aurora väljer en snabb väg för sin första RAG-lösning. All indexering, promptlogik, behörighet, utvärdering och användargränssnitt byggs i en leverantörs proprietära verktyg. När myndigheten senare vill flytta ett känsligare användningsfall till en annan driftmodell blir återanvändning svår.

### Varför det händer

Helhetsplattformar minskar startfriktionen. De ger färdiga komponenter, färdigt gränssnitt och snabb utveckling. Arkitekturkonsekvenserna märks först när myndigheten vill ändra riktning.

### Konsekvens

Exit blir dyr. Myndigheten får svagare förhandlingsposition, svårare revision och sämre möjlighet att anpassa driftmodell efter informationsklassning.

### Motåtgärd

Målarkitekturen bör definiera vilka delar som får vara leverantörsspecifika och vilka som bör vara portabla. Särskilt viktiga är:

- dataformat,
- dokumentpipeline,
- metadata,
- promptmallar,
- utvärderingsdata,
- loggstruktur,
- integrationskontrakt,
- modellabstraktion,
- identitetsintegration,
- arkitekturbeslut och konfiguration.

Leverantörsoberoende betyder inte att allt måste byggas generiskt. Det betyder att inlåsning ska vara medveten, dokumenterad och accepterad.

## Anti-pattern 12: Open source utan förvaltningsmodell

Open source-modeller och ramverk kan vara mycket värdefulla. De kan ge kontroll, transparens, kostnadsfördelar och möjlighet till on-premises-drift. Men open source innebär inte automatiskt lägre risk eller lägre kostnad. Myndigheten tar själv större ansvar för drift, säkerhet, uppdatering, licenser, sårbarheter och kompetens.

Aurora vill använda en open source-modell för ett internt analysstöd i en isolerad miljö. Det kan vara rätt, men bara om myndigheten har kapacitet att hantera modellservering, patchning, prestanda, övervakning, test och avveckling.

### Varför det händer

Open source kan uppfattas som ett sätt att undvika leverantörsinlåsning och datalokaliseringsproblem. Det är delvis sant, men det flyttar också ansvar till myndigheten.

### Konsekvens

Lösningen blir beroende av ett fåtal experter. Uppdateringar uteblir, sårbarheter hanteras sent och modellen blir svår att integrera i ordinarie drift.

### Motåtgärd

Open source ska bedömas med samma professionalitet som kommersiella tjänster. Fråga:

- Vilken licens gäller?
- Vem ansvarar för uppdateringar?
- Hur hanteras sårbarheter?
- Hur testas nya modellversioner?
- Vilken hårdvara krävs?
- Hur säkras kompetens över tid?
- Hur dokumenteras begränsningar?
- Hur avvecklas modellen?

Open source är ett arkitekturval, inte ett sätt att slippa arkitektur.

## Anti-pattern 13: Decentraliserad innovation utan gemensamma guardrails

Det är bra att låta verksamhetsnära team utforska AI. Men om varje team sätter egna regler för data, verktyg, promptar, loggning, leverantörer och riskbedömning uppstår snabbt en okontrollerad AI-portfölj.

Aurora vill uppmuntra innovation i kontrollverksamhet, rättsavdelning, kundservice och intern administration. Utan gemensamma guardrails börjar teamen använda olika verktyg, olika datakällor och olika bedömningsmallar.

### Varför det händer

Central styrning uppfattas ibland som bromsande. Verksamheten vill pröva idéer snabbt. Arkitekturgruppen vill inte säga nej till allt och blir därför passiv.

### Konsekvens

Myndigheten får skugg-AI. Det blir svårt att veta vilka AI-lösningar som finns, vilka data som används, vilka leverantörer som behandlar information och vilka risker som accepterats.

### Motåtgärd

Skapa frihet inom ramar. Det kan innebära:

- en godkänd AI-sandlåda,
- en enkel use-case triage,
- förbjudna datakategorier i lågkontrollerade miljöer,
- standardiserade informationsklassningsfrågor,
- gemensamma prompt- och loggregler,
- återanvändbara integrationsmönster,
- snabb arkitekturrådgivning för team.

Målet är inte central detaljstyrning. Målet är decentraliserad innovation med gemensam kontroll.

## Anti-pattern 14: Mätning som bara handlar om modellkvalitet

Många AI-initiativ mäter bara om modellen ger bra svar i teknisk mening. Men myndighetsnytta kräver mer än modellprecision. Man behöver mäta verksamhetseffekt, användbarhet, risk, kostnad, regelefterlevnad, datakvalitet och driftstabilitet.

Auroras kunskapsassistent får goda resultat i en teknisk utvärdering. Men när den används i vardagen visar det sig att handläggare inte litar på svaren, att källhänvisningar saknas i vissa fall och att supportärenden ökar när dokumenten är gamla.

### Varför det händer

Tekniska mätetal är lättare att automatisera. Verksamhetseffekt och kontroll kräver mer tvärfunktionell uppföljning.

### Konsekvens

Lösningar ser bättre ut än de är. Myndigheten fortsätter investera i AI som inte ger faktisk nytta eller som skapar dold risk.

### Motåtgärd

Mät flera dimensioner:

| Dimension | Exempel på fråga |
|---|---|
| Nytta | Minskar lösningen ledtid, förbättrar kvalitet eller frigör tid? |
| Användning | Används lösningen av rätt målgrupp på rätt sätt? |
| Kvalitet | Ger lösningen korrekta, relevanta och begripliga resultat? |
| Risk | Har incidenter, fel eller avvikelser uppstått? |
| Kontroll | Följs krav på loggning, spårbarhet och mänsklig kontroll? |
| Kostnad | Är kostnaden rimlig i relation till nytta och risk? |

AI-förmågan ska mätas som verksamhetsförmåga, inte bara som modellprestanda.

## Anti-pattern 15: Att inte avveckla

AI-lösningar måste kunna avvecklas. Modeller blir gamla, datakällor ändras, användningsfall förlorar relevans, leverantörer byter villkor och riskbedömningar kan förändras. Ändå planeras avveckling ofta sent eller inte alls.

Aurora har en pilot för sammanfattning av administrativa dokument. När en ny gemensam dokumentplattform införs blir piloten överflödig. Eftersom ingen planerat avveckling ligger tjänsten kvar, med gamla integrationer och loggar som ingen äger.

### Varför det händer

Införande får mer uppmärksamhet än avveckling. Team vill skapa nytt, inte städa bort gammalt. Finansieringsmodeller premierar start, inte livscykelansvar.

### Konsekvens

Gamla AI-lösningar blir säkerhets- och förvaltningsrisker. Dokumentation blir felaktig, kostnader fortsätter och oklara datamängder ligger kvar.

### Motåtgärd

Varje AI-lösning bör ha avvecklingskriterier:

- när nyttan inte längre kan visas,
- när risknivån ändras,
- när datakällan byts ut,
- när leverantörsvillkor ändras,
- när modellen inte längre kan valideras,
- när kostnaden inte längre är motiverad,
- när lösningen ersätts av gemensam förmåga.

Avveckling är en del av AI-livscykeln, inte ett administrativt efterarbete.

## Samlad bild: misstag, symptom och motåtgärder

Följande tabell sammanfattar kapitlets viktigaste anti-patterns.

| Anti-pattern | Tidigt symptom | Rekommenderad motåtgärd |
|---|---|---|
| Börja med verktyget | Produktdemo driver arkitektur | Börja med användningsfall, risk och principer |
| En AI-plattform för allt | Alla behov pressas in i samma runtime | Skapa flera kontrollerade arkitekturspår |
| Sandlåda utan produktionsväg | Många piloter, få införanden | Definiera produktionskriterier från start |
| Juridik som efterhandsgranskning | Juridik kopplas in efter prototyp | Lägg juridisk triage i idéfasen |
| Datagrunden hoppas över | Bra demo men svag kvalitet i drift | Etablera metadata, ägarskap och åtkomstmodell |
| RAG som universalmedicin | RAG används för alla problem | Matcha mönster mot AI-roll och risk |
| Fine-tuning för tidigt | Modellen tränas innan problemet förstås | Pröva data, promptning och RAG först |
| Otydligt modellansvar | Ingen äger modellens beteende över tid | Inför modellägarskap |
| Loggning utan skydd | Prompter och svar sparas brett | Besluta loggstrategi och retention |
| Mänsklig kontroll som slogan | Användare följer AI okritiskt | Designa faktisk human oversight |
| Leverantörsinlåsning | All logik hamnar i proprietära verktyg | Definiera portabla artefakter och exit |
| Open source utan förvaltning | Lösningen beror på enskilda experter | Kräv livscykel- och säkerhetsmodell |
| Innovation utan guardrails | Team använder egna verktyg och regler | Skapa frihet inom gemensamma ramar |
| Snäv mätning | Endast modellkvalitet följs upp | Mät nytta, risk, kostnad och kontroll |
| Ingen avveckling | Gamla piloter ligger kvar | Definiera avvecklingskriterier |

## Exempel: Hur Aurora korrigerar tre felaktiga vägval

Efter att ha gått igenom sina första AI-initiativ ser Aurora tre tydliga riskmönster.

Det första är att flera initiativ valt verktyg innan riskklassning. Arkitekturgruppen inför därför en obligatorisk use-case triage innan plattformsval. Triage ska inte vara tung, men den ska ge ett första svar på AI-roll, datakänslighet, juridisk risk, användargrupp och tänkbar driftmodell.

Det andra är att RAG används som standardlösning för för många problem. Aurora delar därför upp RAG i två varianter: ett enklare kunskapsstödmönster för låg- och medelkänsliga styrdokument och ett striktare mönster för ärenderelaterade dokument där behörighet, loggning och källspårning måste vara starkare.

Det tredje är att pilotteamen saknar förvaltningsmottagare. Aurora beslutar att varje pilot som vill gå vidare till produktion måste ha en namngiven verksamhetsägare, systemförvaltningskoppling, informationsägare, preliminär modellägare och dokumenterade driftkrav.

Dessa korrigeringar gör inte AI-arbetet långsammare i längden. De minskar risken att myndigheten bygger lösningar som senare måste stoppas, byggas om eller avvecklas oplanerat.

## Arkitektens kontrollfrågor

När ett AI-initiativ presenteras kan arkitekten använda följande frågor för att upptäcka anti-patterns tidigt:

- Börjar initiativet med ett tydligt verksamhetsbehov eller med ett verktyg?
- Är AI-rollen tydlig: assistent, kunskapsstöd, beslutsstöd, styrande komponent eller automation?
- Är data, informationsklassning och åtkomstmodell kända?
- Är juridik, dataskydd och informationssäkerhet med från början?
- Finns en beslutad driftmodell?
- Finns en väg från pilot till produktion?
- Finns modellägarskap och förvaltningsansvar?
- Finns loggstrategi, retention och åtkomst till loggar?
- Är mänsklig kontroll designad i arbetsflödet?
- Är leverantörsinlåsning medvetet accepterad eller oavsiktlig?
- Finns exitstrategi?
- Finns mätetal för nytta, risk och kontroll?
- Finns avvecklingskriterier?

Om flera svar saknas är initiativet sannolikt inte redo för produktionsnära vägval.

## Vanliga missförstånd

- **Missförstånd: Anti-patterns betyder att myndigheten ska undvika all risk.**
  - Varför det händer: Risklistor kan uppfattas som stoppregler.
  - Hur du undviker det: Använd anti-patterns som tidig varningssignal, inte som innovationsförbud.

- **Missförstånd: En lyckad pilot bevisar att lösningen är produktionsklar.**
  - Varför det händer: Demonstrationer visar funktion men inte förvaltning, säkerhet och ansvar.
  - Hur du undviker det: Kräv produktionskriterier innan piloten skalas.

- **Missförstånd: Leverantören ansvarar för AI-riskerna.**
  - Varför det händer: Plattformen levereras som tjänst.
  - Hur du undviker det: Skilj mellan leverantörens ansvar för tjänsten och myndighetens ansvar för användningen.

- **Missförstånd: On-premises löser alla juridiska och säkerhetsmässiga problem.**
  - Varför det händer: Lokal drift uppfattas som kontroll.
  - Hur du undviker det: Bedöm även kompetens, uppdatering, loggning, behörighet, livscykel och fysisk/logisk säkerhet.

- **Missförstånd: Moln löser all skalbarhet och förvaltning.**
  - Varför det händer: Molnplattformar ger färdiga byggblock.
  - Hur du undviker det: Kontrollera datalokalitet, avtalsvillkor, konfiguration, identitet, loggning, exit och intern förmåga.

## Exempel från Tullverket Aurora

I Tullverket Aurora märks anti-patterns tidigt genom att de skapar friktion mellan verksamhet, juridik, säkerhet och IT. Ett team vill använda en färdig AI-tjänst utan klassning. Ett annat team vill bygga en helt egen modellplattform. Ett tredje team fastnar i en sandlåda som aldrig får produktionsväg.

Genom att återkomma till Aurora blir kapitlet en praktisk varningslista: varje anti-pattern kan kopplas till en konkret styrningsbrist, ett arkitekturval som saknas eller en förmåga som ännu inte är etablerad.

## Vägvalsfrågor

- Vilka anti-patterns syns redan i myndighetens befintliga AI-experiment?
- Vilka misstag beror på teknikval och vilka beror på otydlig styrning?
- Vilka risker behöver stoppas direkt och vilka kan hanteras genom kontrollerade piloter?
- Vilka återkommande beslut bör lyftas in i målarkitekturens principer och beslutsmallar?

## Vanliga fallgropar

- Att behandla anti-patterns som en lista över individuella misstag i stället för symtom på svag styrning.
- Att åtgärda ett verktygsproblem utan att ändra den bakomliggande beslutsmodellen.
- Att låta undantag bli ny standard utan arkitekturbeslut.
- Att underskatta hur snabbt lokala AI-lösningar kan bli verksamhetskritiska.

## Checklista

Innan ett AI-initiativ går från idé eller pilot till mer bindande arkitekturval bör följande vara på plats:

- Verksamhetsbehov och nyttotes är dokumenterade.
- AI-roll är tydlig.
- Informationsklassning är gjord eller planerad.
- Juridisk triage är genomförd.
- Driftmodell är preliminärt vald.
- Dataägare och informationsägare är identifierade.
- Modellägarskap är definierat där det behövs.
- Loggning, retention och åtkomst till loggar är bedömda.
- Mänsklig kontroll är designad i arbetsflödet.
- Säkerhetskrav och incidentväg är definierade.
- Leverantörsinlåsning är analyserad.
- Exitstrategi finns för kritiska beroenden.
- Mätetal omfattar nytta, risk och kontroll.
- Produktionskriterier är tydliga.
- Avvecklingskriterier är definierade.

## Koppling till målarkitekturen

Anti-patterns är inte ett separat granskningskapitel som läggs sist i en pärm. De bör användas aktivt när målarkitekturen tas fram. Varje större arkitekturbeslut kan prövas mot frågan: vilket anti-pattern riskerar detta beslut att skapa?

Om myndigheten väljer en gemensam AI-gateway bör den fråga om gatewayen minskar fragmentering eller skapar en ny flaskhals. Om myndigheten väljer open source-modeller bör den fråga om valet ger kontroll eller bara flyttar förvaltningsansvar till en underbemannad organisation. Om myndigheten väljer SaaS bör den fråga om tidsvinsten är värd de avtals-, data- och exitfrågor som följer.

För Tullverket Aurora blir kapitlets viktigaste lärdom att AI-förmåga inte bara byggs genom positiva mål. Den byggs också genom att organisationen systematiskt undviker fel vägval. En bra målarkitektur beskriver därför både vad myndigheten vill uppnå och vilka mönster den aktivt ska undvika.

## Snabb sammanfattning

- AI-anti-patterns är återkommande arbetssätt eller arkitekturval som ser rimliga ut kortsiktigt men skapar problem över tid.
- De vanligaste misstagen handlar om fel ordning: produkt före behov, teknik före juridik, modell före data och pilot före produktionsförmåga.
- En myndighet behöver hantera teknisk skuld, styrningsskuld, dataskuld och säkerhetsskuld.
- RAG, fine-tuning, moln, on-premises, open source och SaaS kan alla vara rätt val i rätt kontext men fel val om de används som standardlösning för allt.
- Mänsklig kontroll, loggning, modellägarskap, exitstrategi och avveckling måste designas, inte antas.
- Tullverket Aurora korrigerar sina riskmönster genom use-case triage, tydligare arkitekturspår och krav på produktionsmottagare.
- Nästa kapitel samlar bokens praktiska checklistor och beslutsmallar så att arkitekten kan använda dem i det faktiska målarkitekturarbetet.

## Nästa steg

Nästa kapitel fungerar som bokens praktiska verktygslåda. Där samlas mallar och checklistor för AI-use-case canvas, målarkitekturens minsta innehåll, moln/on-prem-beslutsmatris, plattformsval, RAG-beslut, leverantörsfrågor, riskfrågor och arkitekturbeslut.
