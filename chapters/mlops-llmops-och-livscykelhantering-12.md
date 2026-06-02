# Kapitel 12: MLOps, LLMOps och livscykelhantering

## Varför detta kapitel finns

En AI-lösning blir inte produktionsbar bara för att modellen fungerar i ett test. För en större statlig myndighet är det ofta först när lösningen ska förvaltas över tid som de verkliga arkitekturfrågorna blir synliga. Vem ansvarar för modellen? Hur vet vi vilken version som användes vid ett visst tillfälle? Hur upptäcker vi försämrad kvalitet? Hur hanterar vi nya modellversioner från en leverantör? Hur testar vi att en ändrad prompt inte ger sämre svar? Hur avvecklar vi en modell som inte längre får användas?

Detta kapitel behandlar MLOps, LLMOps och livscykelhantering som en del av målarkitekturen. Fokus ligger inte på en viss verktygskedja, utan på vilka förmågor, processer och arkitekturkomponenter som behöver finnas för att AI ska kunna utvecklas, driftsättas, följas upp och avvecklas på ett kontrollerat sätt.

MLOps används här som samlingsnamn för arbetssätt, processer och tekniska mekanismer för maskininlärningsmodellers livscykel. LLMOps används för motsvarande förmågor kring stora språkmodeller, generativ AI, promptar, RAG-flöden, utvärderingar och modellinteraktioner. I praktiken behöver en myndighet ofta båda perspektiven, även om de första AI-användningsfallen främst är generativa.

Kapitlet bygger vidare på kapitel 9 om dataarkitektur, kapitel 10 om teknisk referensarkitektur och kapitel 11 om generativ AI, RAG och kunskapsstöd.

## Arkitekturproblemet

Tullverket Aurora har tagit fram ett internt kunskapsstöd baserat på RAG. Lösningen används av ett begränsat antal handläggare för att söka i interna styrdokument, handböcker och rutiner. Piloten fungerar tillräckligt bra för att verksamheten vill gå vidare.

När arkitekturgruppen börjar planera produktionssättning uppstår nya frågor:

- Vem äger promptarna?
- Vem godkänner vilka dokument som får indexeras?
- Hur testas en ny version av vektordatabasen eller embeddingmodellen?
- Hur vet man om svarskvaliteten försämras över tid?
- Hur hanteras modelluppdateringar när leverantören byter modell bakom ett API?
- Hur spåras vilken modell, prompt, källversion och konfiguration som användes för ett visst svar?
- Hur gör man rollback om en ändring orsakar felaktiga eller riskabla svar?
- Hur separeras experimentmiljö, testmiljö och produktionsmiljö?
- Vilka händelser ska loggas, och vilka får inte loggas av dataskyddsskäl?
- Hur avvecklas ett användningsfall när dess rättsliga grund, datakälla eller modellstöd inte längre håller?

Det blir tydligt att AI-lösningen inte bara består av modell och gränssnitt. Den består av en livscykel: idé, riskbedömning, datagrund, utveckling, test, driftsättning, övervakning, förbättring, incidenthantering och avveckling.

För Tullverket Aurora blir arkitekturfrågan:

> Hur etablerar vi en livscykelmodell där AI-lösningar kan förändras snabbt utan att myndigheten tappar kontroll över kvalitet, ansvar, spårbarhet och risk?

## Centrala begrepp

### MLOps

MLOps är den samlade förmågan att utveckla, testa, driftsätta, övervaka och förvalta maskininlärningsmodeller på ett reproducerbart och kontrollerat sätt. Det handlar om mer än automatiserad deployment. Det omfattar även datakvalitet, experimenthantering, modellregister, validering, övervakning, drift, incidenter och avveckling.

För traditionella maskininlärningsmodeller är dataversioner, träningskod, modellartefakter och mätvärden centrala. Exempel är en modell som förutser köbildning, prioriterar kontroller eller klassificerar dokument.

### LLMOps

LLMOps är motsvarande livscykelperspektiv för stora språkmodeller och generativa AI-lösningar. Här behöver man hantera modellval, promptar, systeminstruktioner, RAG-konfiguration, källindex, embeddings, utvärderingsdataset, testfrågor, svarskvalitet, hallucinationer, källhänvisningar, kostnad, latens och användningsmönster.

I många myndighetslösningar är promptar, retrieval-logik och källurval lika viktiga som själva språkmodellen. En ändring i chunkingstrategi, systemprompt eller dokumentindex kan påverka lösningen lika mycket som ett modellbyte.

### Modellregister

Ett modellregister är en kontrollerad katalog över modeller och modellrelaterade artefakter. För en traditionell ML-modell kan registret innehålla modellversion, träningsdatareferens, kodversion, mätvärden, godkännandestatus och produktionsstatus. För generativ AI kan registret även behöva innehålla leverantörsmodell, endpoint, policyvillkor, fallbackmodell, godkända användningsfall och begränsningar.

I en myndighet bör modellregistret inte enbart vara ett tekniskt verktyg. Det bör vara kopplat till ansvar, riskklassning, dokumentation och förvaltningsbeslut.

### Experiment, kandidat och produktionsmodell

En modell eller AI-konfiguration bör inte gå direkt från idé till produktion. Ett enkelt livscykelspråk kan vara:

- **Experiment:** används för teknisk och verksamhetsmässig prövning.
- **Kandidat:** har visat lovande resultat och genomgår strukturerad validering.
- **Godkänd för pilot:** får användas i avgränsad kontrollerad miljö.
- **Godkänd för produktion:** får användas enligt definierad användning, risknivå och driftmodell.
- **Begränsad:** får bara användas i vissa sammanhang eller med särskilda kontroller.
- **Avvecklad:** får inte längre användas.

Samma livscykel kan användas för modeller, promptpaket, RAG-konfigurationer och AI-tjänster.

### Modellkort och systemkort

Ett modellkort beskriver en modell: syfte, träningsdata på övergripande nivå, begränsningar, lämpliga och olämpliga användningsområden, kända risker, mätvärden och godkänd användning. Ett systemkort beskriver en AI-lösning i sitt sammanhang: användare, process, datakällor, integrationer, mänsklig kontroll, loggning, drift, ansvar och riskhantering.

För en myndighet är systemkortet ofta viktigare än modellkortet, eftersom risk uppstår i kombinationen av modell, data, användare, process och beslutssituation.

### Drift, driftövervakning och modellövervakning

Traditionell driftövervakning svarar på frågor som: är tjänsten uppe, svarar den snabbt och klarar den last? Modellövervakning svarar på andra frågor: ger lösningen fortfarande rimliga svar, ökar felaktiga svar, förändras indata, förändras användningen, uppstår bias, driftar modellen eller försämras retrieval-kvaliteten?

AI-drift behöver båda perspektiven. En AI-tjänst kan vara tekniskt tillgänglig men ändå olämplig att använda om kvaliteten försämrats.

### Modellrisk och förändringsrisk

Modellrisk handlar om risken att AI-komponenten ger felaktiga, otillräckliga, partiska, otillåtna eller svårförklarliga resultat. Förändringsrisk handlar om risken att en ändring i data, modell, prompt, index, konfiguration, beroenden eller användningsmönster förändrar lösningens beteende.

I AI-arkitektur måste förändringsrisk behandlas mer uttryckligt än i många traditionella system. En liten ändring i ett promptflöde kan få stor effekt på resultatet.

## Rekommenderat angreppssätt

### Börja med livscykelkraven, inte verktygen

Det är lockande att börja med att välja ett MLOps-verktyg eller en LLMOps-plattform. Det är sällan rätt första steg. Målarkitekturen bör börja med att definiera vilka livscykelkrav myndigheten har.

För varje AI-användningsfall bör arkitekten kunna svara på följande frågor:

- Vilken typ av AI-komponent används?
- Vilken risknivå har användningsfallet?
- Vilka data används i utveckling, test och produktion?
- Vem äger modellen eller AI-konfigurationen?
- Vem godkänner produktionssättning?
- Vilka tester krävs före release?
- Vilken spårbarhet krävs efter release?
- Vilka mätvärden följs upp?
- När måste lösningen omprövas?
- Hur kan lösningen pausas, rullas tillbaka eller avvecklas?

När dessa krav är tydliga blir verktygsvalet mer rationellt.

### Dela livscykeln i separata men sammanhängande spår

En praktisk målarkitektur bör hantera minst sex livscykelspår.

**Use-case-livscykel:** från idé till godkänt, produktionssatt eller avvecklat användningsfall.

**Datalivscykel:** från källidentifiering till dataåtkomst, kvalitetssäkring, indexering, retention och avpublicering.

**Modellivscykel:** från modellval eller träning till validering, produktionssättning, övervakning och avveckling.

**Prompt- och konfigurationslivscykel:** från promptutkast till testad, versionerad och godkänd instruktion.

**RAG-livscykel:** från dokumenturval till chunking, embedding, indexering, retrieval-testning, källkontroll och uppdatering.

**Tjänstelivscykel:** från teknisk implementation till deployment, drift, support, incidenthantering och förvaltning.

Dessa spår måste kopplas ihop. Ett svar från en RAG-lösning kan bero på en viss modellversion, en viss systemprompt, ett visst dokumentindex, en viss chunkingstrategi, en viss behörighet och en viss användarfråga. Om kedjan inte är spårbar blir det svårt att utreda fel.

### Skapa en gemensam AI-releaseprocess

En myndighet behöver inte göra varje AI-release tungrodd. Däremot behöver releaseprocessen vara tydlig och riskbaserad. Lågriskanvändning, till exempel ett internt produktivitetsstöd med lågklassad information, kan ha en lättare process. Ett ärendenära eller beslutsnära stöd behöver hårdare kontroll.

En enkel releaseprocess kan innehålla:

1. registrera ändringen,
2. beskriva påverkat användningsfall,
3. koppla ändringen till risknivå,
4. köra automatiserade tester,
5. genomföra verksamhetsgranskning vid behov,
6. genomföra juridisk eller säkerhetsmässig kontroll vid behov,
7. godkänna release,
8. driftsätta kontrollerat,
9. följa upp mätvärden efter release,
10. dokumentera beslut och utfall.

För generativ AI bör releaseprocessen inte bara omfatta kod. Den bör även omfatta ändringar i promptar, modellval, källindex, guardrails, retrieval-regler och policykonfiguration.

### Gör versionering till en grundprincip

Versionering är en av de viktigaste byggstenarna i AI-livscykeln. Utan versionering går det inte att veta vad som faktiskt användes.

Följande bör versioneras eller åtminstone spåras:

- modell eller modellendpoint,
- modellparametrar och konfiguration,
- promptar och systeminstruktioner,
- RAG-konfiguration,
- embeddingmodell,
- chunkingstrategi,
- dokumenturval och källversioner,
- vektorindex,
- kod och beroenden,
- policyregler och guardrails,
- testdataset,
- utvärderingsresultat,
- godkännandebeslut.

För Tullverket Aurora innebär detta att ett svar i kunskapsstödet ska kunna kopplas till rätt version av källmaterial, prompt, modell och retrieval-konfiguration. Det betyder inte nödvändigtvis att varje token måste bevaras för alltid, men arkitekturen måste ge tillräcklig spårbarhet för revision, felsökning och kvalitetsförbättring.

### Skilj mellan teknisk validering och verksamhetsvalidering

AI-lösningar behöver testas på flera nivåer. Teknisk validering visar att lösningen fungerar tekniskt: API:er svarar, integrationer fungerar, åtkomstkontroll tillämpas och latens håller sig inom acceptabla gränser.

Verksamhetsvalidering visar att lösningen är lämplig i sitt sammanhang: svaren är användbara, källorna är relevanta, instruktioner följs, osäkerhet hanteras och användaren kan agera rätt.

För ett AI-baserat kunskapsstöd kan testningen exempelvis omfatta:

- tekniska integrationstester,
- behörighetstester,
- retrieval-tester,
- källhänvisningstester,
- hallucinationstester,
- robusthetstester mot otydliga frågor,
- tester för förbjudna frågor,
- tester av språk och ton,
- användartester med handläggare,
- granskning av juridik och informationssäkerhet.

För beslutsnära AI-stöd krävs dessutom starkare kontroll av felkonsekvenser, bias, förklarbarhet, mänsklig granskning och dokumentation.

### Inför utvärderingsdataset för generativ AI

Generativ AI kräver andra testmetoder än traditionella deterministiska system. Ett testfall kan inte alltid jämföra svaret med en exakt sträng. Därför behöver myndigheten skapa utvärderingsdataset med realistiska frågor, förväntade källor, oacceptabla svar, kvalitetskriterier och granskningsregler.

För Auroras kunskapsstöd kan ett sådant dataset innehålla:

- frågor där svaret finns tydligt i en källa,
- frågor där flera källor måste kombineras,
- frågor där källorna är motstridiga,
- frågor där användaren saknar behörighet till svaret,
- frågor där svaret inte bör ges,
- frågor som försöker kringgå instruktioner,
- frågor om gamla dokumentversioner,
- frågor där modellen bör säga att den inte vet.

Utvärderingsdatasetet bör förvaltas som en produktionsnära artefakt. Det ska versioneras, ägas och uppdateras när källor, regler eller användningsmönster förändras.

### Övervaka både kvalitet och användning

I en traditionell applikation övervakas ofta teknisk hälsa: CPU, minne, svarstid, felkoder och tillgänglighet. För AI behöver övervakningen även omfatta kvalitet, beteende, risk och nytta.

Exempel på mätområden:

| Mätområde | Exempel på mått | Arkitekturrelevans |
|---|---|---|
| Tillgänglighet | upptid, felgrad, timeout | Visar om tjänsten fungerar tekniskt |
| Prestanda | svarstid, kötid, tokens per minut | Påverkar användbarhet och kapacitetsplanering |
| Kostnad | kostnad per fråga, total förbrukning, toppar | Viktigt vid molnbaserad inferens och skalning |
| Retrieval-kvalitet | träffprecision, källrelevans, saknade källor | Avgör om RAG-lösningen ger grundade svar |
| Svarskvalitet | användarbetyg, granskningsresultat, felrapporter | Visar om lösningen stödjer verksamheten |
| Riskhändelser | blockerade frågor, policyträffar, incidenter | Behövs för säkerhet och governance |
| Användningsmönster | aktiva användare, användningsfall, avvikande beteende | Visar nytta och potentiell felanvändning |
| Modellbeteende | hallucinationer, formatfel, vägran, osäkerhet | Behövs för LLMOps och kvalitetsstyrning |

Mätningen ska inte bli övervakning av enskilda användare utan tydligt syfte. Loggning och uppföljning måste balanseras mot dataskydd, sekretess och arbetsrättsliga hänsyn.

## Exempel från Tullverket Aurora

### Auroras första produktionsnära AI-livscykel

Efter kapitel 11 har Tullverket Aurora beslutat att det interna kunskapsstödet ska bli första kontrollerade AI-produkten. Arkitekturgruppen etablerar därför en minsta nödvändig LLMOps-förmåga.

Den första versionen omfattar:

- ett register över AI-användningsfall,
- ett register över modeller och modellendpoints,
- versionerade systempromptar,
- kontrollerad dokumentpublicering till RAG-index,
- testfrågor för kunskapsstödet,
- godkännande av källsamlingar,
- loggning av modell, promptversion, källor och policyträffar,
- dashboard för användning, fel, kostnad och källträffar,
- releaseprocess för ändrade promptar och index,
- rollback till tidigare prompt- och indexversion,
- incidentprocess för felaktiga eller olämpliga svar.

Aurora väljer medvetet att inte börja med en avancerad fullskalig MLOps-plattform för alla tänkbara AI-typer. I stället etableras en smal men styrd livscykel kring det användningsfall som ska produktionssättas först. Målarkitekturen beskriver samtidigt hur samma mönster kan utökas till prediktiva modeller, dokumentklassificering och riskanalys.

### Modellregistret i praktiken

För Auroras kunskapsstöd registreras inte bara språkmodellen. Följande poster hanteras som styrda artefakter:

| Artefakt | Exempel | Ägare |
|---|---|---|
| AI-användningsfall | Internt kunskapsstöd för handläggare | Verksamhetsägare |
| Modellendpoint | Godkänd språkmodell via AI-gateway | Teknisk tjänsteägare |
| Systemprompt | Instruktion för källbunden rådgivning | Produktteam |
| RAG-index | Index för handböcker och rutiner | Informationsägare och produktteam |
| Testfrågor | Frågebank för kvalitetstest | Verksamhet och kvalitet |
| Policyregler | Blockering av otillåtna frågetyper | Säkerhet och juridik |
| Releasebeslut | Godkännande av version 1.0 | AI governance board eller delegerat forum |

Det viktiga är inte att allt ligger i samma verktyg. Det viktiga är att relationerna finns dokumenterade och att de kan användas vid ändring, revision och incident.

### En ändring som verkar liten men inte är det

Auroras produktteam vill förbättra svarskvaliteten genom att ändra chunkingstrategin i dokumentindexet. Tidigare delades dokument i ganska stora textstycken. Nu vill teamet skapa mindre chunks för bättre precision.

Tekniskt är ändringen enkel. Arkitektoniskt är den större. Den kan påverka:

- vilka källor som hittas,
- hur sammanhang bevaras,
- hur väl svaret citerar rätt avsnitt,
- hur modellen tolkar undantag och villkor,
- hur gamla testresultat kan jämföras med nya,
- hur kostnaden påverkas genom fler retrieval-träffar.

Aurora klassar därför ändringen som en AI-konfigurationsrelease. Den kräver inte fullständig omprövning av användningsfallet, men den kräver regressionstest mot frågebanken, granskning av ett urval svar och möjlighet att rulla tillbaka till föregående indexversion.

Detta är ett konkret exempel på varför LLMOps inte kan reduceras till teknisk deployment. Även innehålls- och konfigurationsändringar kan påverka myndighetens riskbild.

## Vägvalsfrågor

### Centraliserad eller federerad livscykelhantering

En större myndighet behöver ofta både central kontroll och verksamhetsnära utveckling. Om all AI-livscykelhantering centraliseras kan arbetet bli långsamt. Om varje verksamhetsområde bygger sin egen process tappar myndigheten spårbarhet och återanvändning.

En rimlig målbild är ofta federerad förvaltning inom gemensamma ramar:

- gemensamma principer,
- gemensamma minimikrav,
- gemensamt register,
- gemensam AI-gateway eller plattformskärna,
- gemensamma test- och loggningskrav,
- delegerad produktförvaltning,
- riskbaserad granskning.

Det ger utrymme för verksamhetsnära team men behåller myndighetsgemensam styrbarhet.

### En MLOps-plattform eller flera verktyg

Det finns sällan ett enda verktyg som löser hela AI-livscykeln. En målarkitektur bör därför beskriva förmågor och gränssnitt snarare än att låsa allt till ett produktnamn.

Minsta uppsättning förmågor kan vara:

- kod- och konfigurationsversionering,
- pipeline-automatisering,
- artefaktlagring,
- modellregister,
- test- och valideringsmiljö,
- deploymentmekanism,
- loggning och observability,
- åtkomststyrning,
- dokumentation och godkännandeflöde.

För LLMOps tillkommer ofta:

- promptversionering,
- prompttestning,
- utvärderingsdataset,
- RAG-indexhantering,
- källspårning,
- kostnadsuppföljning,
- policy- och guardrail-konfiguration,
- utvärdering av svarskvalitet.

Myndigheten kan realisera dessa med en plattform, flera integrerade verktyg eller en kombination av befintliga DevOps-verktyg och AI-specifika komponenter.

### Automatiserad eller manuell kvalitetsgranskning

Automatiserad utvärdering är nödvändig för att kunna arbeta snabbt, men den räcker inte alltid. För riskfyllda användningsfall behövs mänsklig granskning, särskilt när konsekvensen av fel är hög.

En praktisk modell är:

- automatiska tester för varje ändring,
- manuell granskning vid större ändringar,
- expertgranskning för juridiskt eller verksamhetsmässigt känsliga områden,
- governance-granskning för nya användningsfall eller ändrad risknivå.

För Auroras kunskapsstöd kan mindre promptjusteringar testas automatiskt och godkännas av produktägaren. En ny datakälla med sekretessbelagd information kräver däremot informationsägare, säkerhet och juridik.

### Leverantörsstyrd eller myndighetsstyrd modellversion

När en myndighet använder en molnbaserad modell via API kan leverantören ibland uppdatera modellen eller erbjuda nya versioner. Det kan förbättra kvaliteten, men också förändra beteendet.

Målarkitekturen bör därför kräva tydlighet kring:

- om modellversioner är fasta eller flytande,
- hur länge en version stöds,
- hur versionbyte aviseras,
- hur testning inför versionbyte sker,
- hur rollback eller fallback fungerar,
- hur kostnad och prestanda förändras,
- hur villkor och databehandling påverkas.

För myndighetskritiska användningsfall bör en modellversion inte bytas utan kontrollerad test och godkännande.

### Hur mycket ska loggas?

AI-lösningar behöver loggning för spårbarhet, säkerhet, felsökning och förbättring. Samtidigt kan promptar, svar och källor innehålla personuppgifter eller sekretessbelagd information. Loggning får därför inte utformas slentrianmässigt.

Arkitekten behöver väga:

- revisionsbehov,
- incidentutredning,
- dataskydd,
- sekretess,
- användarintegritet,
- retention,
- åtkomst till loggar,
- anonymisering eller pseudonymisering,
- behov av aggregerade mätvärden.

En möjlig princip är att logga tillräckligt för att förstå och utreda lösningens beteende, men inte mer innehåll än vad risk, rättslig grund och ändamål motiverar.

## Vanliga fallgropar

- **Fallgrop: Att behandla AI som vanlig applikationsdrift.**
  - Varför det händer: Organisationen har redan etablerade DevOps-processer och antar att samma processer räcker.
  - Hur du undviker det: Behåll DevOps-grunden men komplettera med modell-, data-, prompt-, RAG- och kvalitetslivscykel.

- **Fallgrop: Att inte versionera promptar och RAG-konfiguration.**
  - Varför det händer: Promptar ses som text, inte som styrande systemartefakter.
  - Hur du undviker det: Hantera promptar, systeminstruktioner och retrieval-regler som kodnära konfiguration med versionshantering och releaseprocess.

- **Fallgrop: Att övervaka teknik men inte kvalitet.**
  - Varför det händer: Driftorganisationen mäter tillgänglighet och svarstid men saknar mätvärden för AI-beteende.
  - Hur du undviker det: Lägg till mätvärden för svarskvalitet, källrelevans, policyträffar, felrapporter och verksamhetsnytta.

- **Fallgrop: Att sakna rollback för AI-konfiguration.**
  - Varför det händer: Ändringar i promptar och index uppfattas som enkla och riskfria.
  - Hur du undviker det: Kräv att tidigare godkända versioner av promptar, index och konfiguration kan återställas.

- **Fallgrop: Att låta leverantörens modellversioner styra okontrollerat.**
  - Varför det händer: API-tjänsten fungerar som en svart låda och uppdateringar betraktas som leverantörens ansvar.
  - Hur du undviker det: Kräv modellversionspolicy, test inför versionbyte och dokumenterad fallbackstrategi.

- **Fallgrop: Att förbättra modellen utan att förstå datagrunden.**
  - Varför det händer: Teamet fokuserar på modellprestanda men missar brister i källor, metadata eller behörighet.
  - Hur du undviker det: Koppla modellvalidering till datakvalitet, källförvaltning och informationsägarskap.

- **Fallgrop: Att inte planera avveckling.**
  - Varför det händer: Projekt fokuserar på införande och glömmer vad som händer när användningsfallet, modellen eller rättsliga förutsättningar förändras.
  - Hur du undviker det: Lägg in omprövningspunkter, avvecklingskriterier och ansvar för stängning redan i målarkitekturen.

## Checklista

Använd följande checklista när målarkitekturen beskriver MLOps, LLMOps och livscykelhantering.

### Livscykel och ansvar

- Finns en definierad livscykel från idé till avveckling?
- Finns separata men kopplade livscykler för användningsfall, data, modell, prompt, RAG och tjänst?
- Finns utsedd ägare för varje produktionssatt AI-lösning?
- Finns modellägare eller motsvarande ansvarig roll?
- Finns informationsägare för data och källor?
- Finns ett forum som kan godkänna högriskändringar?
- Finns tydliga omprövningspunkter?

### Versionering och spårbarhet

- Versioneras modell, prompt, konfiguration och kod?
- Spåras vilka källor och indexversioner som användes?
- Finns modellregister eller motsvarande katalog?
- Finns systemkort eller lösningsdokumentation?
- Kan ett historiskt svar kopplas till relevant modell- och konfigurationsversion?
- Finns dokumenterade arkitekturbeslut för viktiga vägval?

### Test och validering

- Finns testdataset eller frågebank för generativ AI?
- Finns regressionstester vid ändrad prompt, modell eller RAG-konfiguration?
- Testas behörighet och informationsåtkomst?
- Testas källhänvisningar och grounding?
- Testas otillåtna frågor och prompt injection-liknande försök?
- Finns manuell expertgranskning för riskfyllda användningsfall?
- Dokumenteras testresultat före release?

### Drift och övervakning

- Övervakas tillgänglighet, svarstid och fel?
- Övervakas kostnad och kapacitetsförbrukning?
- Övervakas svarskvalitet och användarfeedback?
- Övervakas retrieval-kvalitet för RAG?
- Finns larm eller process för avvikande beteende?
- Finns incidentprocess för felaktiga eller otillåtna AI-svar?
- Är loggningen förenlig med dataskydd och sekretess?

### Release och förändring

- Finns releaseprocess för AI-ändringar?
- Omfattar releaseprocessen promptar, index, modeller och policyregler?
- Finns riskbaserad granskning?
- Kan ändringar rullas tillbaka?
- Finns fallbackmodell eller alternativt arbetssätt?
- Finns tydliga kriterier för när en ändring kräver ny juridisk eller säkerhetsmässig bedömning?

### Avveckling

- Finns kriterier för när en modell eller AI-lösning ska avvecklas?
- Finns process för att ta bort modellåtkomst, index, datakopplingar och integrationer?
- Hanteras retention av loggar och dokumentation?
- Informeras användare när en AI-funktion avvecklas eller ersätts?
- Bevaras den dokumentation som krävs för revision och lärande?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

MLOps och LLMOps bör inte beskrivas som en separat teknisk bilaga. De är en central del av målarkitekturen för AI-förmågan. Utan livscykelhantering blir målarkitekturen statisk och bräcklig. Med livscykelhantering kan myndigheten förändra AI-lösningar kontrollerat.

I målarkitekturen bör kapitlets innehåll synas på minst fem ställen.

### Förmågekartan

Förmågekartan bör innehålla förmågor för modellhantering, promptförvaltning, RAG-förvaltning, test, validering, release, övervakning, incidenthantering och avveckling.

### Referensarkitekturen

Den tekniska referensarkitekturen bör visa komponenter för modellregister, artefaktlagring, pipeline, deployment, observability, loggning, policy enforcement och testmiljöer. För generativ AI bör den också visa promptlager, utvärderingsdataset och källindex.

### Governance-modellen

Governance-modellen bör beskriva vem som får godkänna nya modeller, ändrade promptar, nya källor, höjd risknivå och produktionssättning. Den bör även beskriva när juridik, dataskydd, säkerhet och arkitektur måste involveras.

### Roadmapen

Roadmapen bör införa livscykelförmågan stegvis. En rimlig ordning är:

1. register över AI-användningsfall,
2. grundläggande modell- och promptregister,
3. versionshantering för RAG och promptar,
4. testfrågebank för första produktionsnära användningsfallet,
5. releaseprocess,
6. observability och kostnadsuppföljning,
7. incident- och avvecklingsprocess,
8. mer avancerad MLOps för tränade och verksamhetsnära modeller.

### Arkitekturbesluten

Viktiga beslut bör dokumenteras som architecture decision records. Exempel:

- vilken livscykelmodell som används,
- vilket modellregister eller registermönster som väljs,
- hur promptar versioneras,
- hur RAG-index versioneras,
- vilka loggar som sparas,
- hur modellversioner från leverantörer hanteras,
- vilka AI-ändringar som kräver governance-granskning,
- hur rollback och fallback ska fungera.

## Sammanfattning

MLOps och LLMOps handlar om att göra AI förändringsbar utan att den blir okontrollerbar. För en statlig myndighet är detta särskilt viktigt eftersom AI-lösningar måste kunna granskas, förklaras, förbättras, stoppas och avvecklas.

Det viktigaste är inte att införa en stor plattform från dag ett. Det viktigaste är att etablera rätt livscykelprinciper:

- AI-användningsfall ska ha ägare, risknivå och livscykelstatus.
- Modeller, promptar, RAG-konfigurationer och källindex ska vara styrda artefakter.
- Testning ska omfatta både teknik och verksamhetskvalitet.
- Produktionssättning ska vara riskbaserad och spårbar.
- Driftövervakning ska mäta både teknisk hälsa och AI-kvalitet.
- Loggning ska stödja revision och incidenthantering utan att skapa onödig dataskyddsrisk.
- Ändringar ska kunna rullas tillbaka.
- Avveckling ska vara en planerad del av arkitekturen.

För Tullverket Aurora blir livscykelhanteringen den mekanism som gör att myndigheten kan gå från en lyckad pilot till en kontrollerad AI-produkt. Den gör också att framtida AI-lösningar kan återanvända samma grundmönster, även när användningsfallen blir mer verksamhetsnära och risknivån högre.

Nästa kapitel tar vid där detta slutar. När livscykelkraven är tydliga blir det möjligt att diskutera driftmodell: när AI bör köras i moln, när on-premises är nödvändigt och när hybridarkitektur är den mest realistiska målbilden.
