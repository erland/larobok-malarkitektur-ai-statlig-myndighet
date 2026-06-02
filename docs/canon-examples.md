# Canon: återkommande exempel och scenario

## Scenario

Namn: Tullverket Aurora

## Grundbeskrivning

Tullverket Aurora är en fiktiv större statlig tullmyndighet med samhällskritiskt uppdrag. Myndigheten arbetar med tullhantering, kontrollverksamhet, riskanalys, regelverkstolkning, ärendehandläggning och samverkan med andra nationella och internationella aktörer.

## Nuläge

- AI har testats i mindre skala.
- Testerna har främst rört generativ AI för textsammanfattning, intern kunskapssökning och enklare analysstöd.
- Det saknas en samlad AI-målarkitektur.
- Det saknas gemensam plattform, beslutsmodell och livscykelhantering.
- Juridik, informationssäkerhet och dataskydd involveras ojämnt mellan initiativ.
- Vissa team vill använda molnbaserade AI-tjänster, medan andra kräver on-premises-lösningar.

## Återkommande användningsfall

1. Intern kunskapssökning i regelverk, styrdokument och handböcker.
2. Sammanfattning av långa ärendehandlingar.
3. Riskanalys och prioriteringsstöd för kontrollverksamhet.
4. Stöd för handläggare vid tolkning av interna rutiner.
5. Analys av stora informationsmängder för strategisk planering.
6. Automatisering av administrativa textflöden.

## Scenarioregler

- Scenariot ska vara realistiskt men fiktivt.
- Undvik detaljer som kan uppfattas som operativa instruktioner för att kringgå tullkontroll.
- Fokusera på arkitektur, styrning, risk, informationshantering och teknikval.
- Återanvänd samma myndighetsnamn och samma huvudproblem genom hela boken.

## Användning i kapitel 1

Kapitel 1 använder Tullverket Aurora för att visa skillnaden mellan lokala AI-experiment och etablerad AI-förmåga. De tidiga experimenten omfattar textsammanfattning, intern kunskapssökning, analysstöd och otydligt styrd användning av publika AI-verktyg.

Kapitlet etablerar också fem mognadsnivåer för Auroras första AI-förmåga:

1. Kontrollerad användning.
2. Gemensam sandlåda.
3. Styrda piloter.
4. Produktionsförmåga.
5. Skalad och förvaltad AI-portfölj.


## Användning i kapitel 2

Kapitel 2 använder Tullverket Aurora för att visa hur en myndighet avgränsar en AI-målarkitektur utan att reducera arbetet till ett plattformsval.

Auroras arkitekturgrupp delar upp uppdraget i sex frågor:

1. Vilka AI-användningsfall ska myndigheten kunna stödja de kommande två åren?
2. Vilka risk- och informationsklasser ska hanteras?
3. Vilka gemensamma principer ska gälla?
4. Vilka byggblock behöver vara gemensamma?
5. Vilka driftmodeller är tillåtna för olika typer av data?
6. Vilka beslut måste fattas nu och vilka kan skjutas upp?

Kapitel 2 etablerar också skillnaden mellan målarkitektur, referensarkitektur, lösningsarkitektur, roadmap och arkitekturbeslut.

## Användning i kapitel 3

Kapitel 3 använder Tullverket Aurora för att visa hur en myndighet strukturerar sin AI-portfölj innan tekniska vägval görs.

Auroras arkitekturgrupp samlar in 37 AI-idéer och grupperar dem i sex portföljkategorier:

1. Intern produktivitet.
2. Kunskapsstöd.
3. Ärendestöd.
4. Analysstöd.
5. Risk- och prioriteringsstöd.
6. Externa tjänster.

Kapitlet jämför tre representativa användningsfall:

1. Intern kunskapssökning i styrdokument.
2. Sammanfattning av ärendehandlingar.
3. Riskanalys för kontrollprioritering.

Kapitlet etablerar också att Aurora behöver flera kontrollerade arkitekturspår i stället för en enda AI-lösning för alla behov.

## Användning i kapitel 4

Kapitel 4 använder Tullverket Aurora för att visa hur juridik, ansvar och regelefterlevnad blir arkitekturdrivande.

Aurora gör juridisk triage av tre användningsfall:

1. Intern kunskapssökning i styrdokument.
2. Sammanfattning av ärendehandlingar.
3. Riskanalys för kontrollprioritering.

Kapitlet etablerar att dessa användningsfall kräver olika arkitekturspår:

1. Kontrollerad RAG-tjänst för intern kunskapssökning.
2. Striktare miljö för ärendehandlingar med personuppgifter och sekretessrisk.
3. Beslutsstödsarkitektur med tydlig mänsklig kontroll, validering och dokumentation för riskanalys.

Kapitlet etablerar också ansvarskedja, juridisk triage, mänsklig kontroll och regelefterlevnad som återkommande arkitekturbegrepp.

## Användning i kapitel 5

Kapitel 5 använder Tullverket Aurora för att visa hur informationsklassning, dataskydd och riskstyrning styr AI-arkitekturen före plattformsval.

Aurora inför en praktisk fyrnivåmodell för AI-användningsfall:

1. Nivå A: öppen eller lågkänslig information.
2. Nivå B: intern verksamhetsinformation.
3. Nivå C: skyddsvärd information och personuppgifter.
4. Nivå D: särskilt känslig, sekretessbelagd eller verksamhetskritisk information.

Tre återkommande användningsfall klassas:

1. Intern kunskapssökning i publika och interna styrdokument.
2. Sammanfattning av ärendehandlingar.
3. Riskanalys och prioriteringsstöd för kontrollverksamhet.

Kapitlet etablerar regeln att AI-flödet ska klassas från källdata till promptar, kontext, embeddings, svar, loggar, feedback och utvärderingsdata.


## Användning i kapitel 6

Kapitel 6 använder Tullverket Aurora för att visa hur arkitekturprinciper översätter juridik, informationsklassning och riskstyrning till praktiska vägval.

Auroras arkitekturgrupp etablerar en principkatalog med femton styrande principer:

1. Uppdrag före teknik.
2. Klassning före plattformsval.
3. Mänskligt ansvar designas.
4. Transparens efter risk.
5. Spårbar AI-kedja.
6. Dataminimering i hela flödet.
7. Säkerhet som plattformsförmåga.
8. Återanvändbara byggblock.
9. Modulär arkitektur.
10. Riskbaserat leverantörsoberoende.
11. Flera driftspår.
12. Mätbar produktion.
13. Spårbara beslut.
14. Styrda avvikelser.
15. Avvecklingsbarhet.

Kapitlet etablerar att Tullverket Aurora ska använda principerna i use-case triage, referensarkitektur, plattformsval, upphandling, lösningsgranskning och avvikelsehantering.


## Användning i kapitel 7

Kapitel 7 använder Tullverket Aurora för att visa hur AI-governance bör utformas som ett beslutsflöde från idé till produktion och avveckling, inte bara som ett antal forum.

Kapitlet etablerar fyra styrklasser:

1. Klass A: låg risk, interna stöd, godkända datatyper och befintligt mönster.
2. Klass B: måttlig risk, intern pilot, begränsade data och tydligt verksamhetsägarskap.
3. Klass C: högre risk, känslig information eller påverkan på ärendeprocess.
4. Klass D: mycket hög risk, möjlig påverkan på enskildas rättigheter, omfattande sekretess eller strategisk betydelse.

Kapitlet använder tre återkommande exempel:

- sammanfattning av offentliga styrdokument och interna mötesanteckningar,
- RAG-baserat kunskapsstöd för handläggare,
- prediktivt prioriteringsstöd för kontrollverksamhet.

Exemplen ska återanvändas i senare kapitel när förmågekarta, dataarkitektur, teknisk referensarkitektur, säkerhetsarkitektur och roadmap beskrivs.

## Användning i kapitel 8

Kapitel 8 använder Tullverket Aurora för att visa hur en AI-förmågekarta binder samman governance, juridik, säkerhet, data, teknik och drift.

Aurora utgår från tre prioriterade användningsfall:

- intern kunskapssökning i styrdokument,
- sammanfattning av ärendehandlingar,
- prediktivt prioriteringsstöd för kontrollverksamhet.

Kapitlet etablerar att dessa användningsfall kräver olika lösningsarkitekturer men flera gemensamma eller federerade förmågor, bland annat AI-portföljstyrning, use-case triage, juridisk triage, informationsklassning av AI-flöden, AI-gateway, modell- och tjänsteregister, RAG-förmåga, test och validering, observability och avveckling.

Aurora använder tre nivåer för ansvar och etablering:

1. Gemensam förmåga.
2. Federerad förmåga.
3. Lokal förmåga.

Kapitlet etablerar också en enkel mognadsskala för förmågor:

1. Saknas.
2. Fragmenterad.
3. Definierad.
4. Etablerad.
5. Förvaltad.

Denna förmågekarta ska återanvändas i kapitel 9 och 10 när dataarkitektur och teknisk referensarkitektur beskrivs.


## Användning i kapitel 9

Kapitel 9 använder Tullverket Aurora för att visa hur dataarkitektur blir en central del av AI-målarkitekturen.

Aurora prioriterar intern kunskapssökning i regelverk, styrdokument, processbeskrivningar och handböcker. Arkitekturgruppen väljer att inte börja med modellval eller vektordatabas, utan med en datakarta över källor, informationsägare, informationsklass, åtkomstregler, versioner och metadata.

Kapitlet etablerar följande regler för Auroras första produktionsspår:

1. AI-index ska byggas från auktoritativa källor.
2. Dokument utan informationsägare får inte användas i produktionssatt kunskapsstöd.
3. Index, embeddings, promptar, svar och loggar ska klassas som delar av samma informationsflöde.
4. Retrieval ska vara behörighetsmedveten och filtrera kontext innan den skickas till modellen.
5. AI-svar ska kunna spåras till källor, dokumentversioner, modellversion och tillämpade policyregler.

Kapitlet etablerar också att vektordatabaser och embeddings ska behandlas som skyddsvärda komponenter, inte som neutrala tekniska mellanprodukter.


## Användning i kapitel 10

Kapitel 10 använder Tullverket Aurora för att visa hur en teknisk AI-referensarkitektur kan formuleras som byggblock, ansvar och styrande mönster snarare än som en produktlista.

Aurora beskriver nio huvudlager i referensarkitekturen:

1. Användar- och kanalager.
2. Applikations- och produktlager.
3. AI-gateway och policy enforcement.
4. Orkestrerings- och agentlager.
5. Modell- och inferenslager.
6. RAG- och kunskapslager.
7. Data- och integrationslager.
8. Säkerhets-, identitets- och åtkomstlager.
9. Observability, styrning och livscykelhantering.

Kapitlet etablerar tre tekniska referensmönster för Aurora:

1. Kontrollerad AI-assistent för lågklassad information.
2. RAG-baserat kunskapsstöd med behörighetsmedveten retrieval.
3. Analys- och prioriteringsstöd med högre kontrollkrav.

Aurora beslutar att AI-gateway, modell- och tjänsteregister, policy enforcement, loggning, driftspår och grundmönster för RAG ska vara gemensamma eller starkt standardiserade. Verksamhetsspecifika RAG-index, specialiserade analysmodeller och användargränssnitt kan vara federerade inom gemensamma ramar.

Kapitlet etablerar också att agentliknande lösningar med verktygsanrop inte ska produktionssättas förrän kontroller för verktygsbehörighet, mänskligt godkännande och åtgärdsloggning finns på plats.


## Användning i kapitel 11

Kapitel 11 använder Tullverket Aurora för att visa hur generativ AI, RAG och kunskapsstöd kan arkitektureras i en myndighetsmiljö.

Aurora vill bygga ett internt kunskapsstöd för handläggare inom varuflödeskontroll. Stödet ska kunna besvara frågor med grund i styrdokument, handböcker och regelverksmaterial, men det får inte fatta beslut eller ersätta handläggarens ansvar.

Kapitlet etablerar fyra nivåer av generativt stöd:

1. Produktivitetsstöd för lågklassad formulering och strukturering.
2. Internt kunskapsstöd med RAG och källhänvisningar.
3. Ärendenära stöd med högre kontroll och loggning.
4. Beslutsnära stöd som kräver särskild riskprövning och stark governance.

Aurora väljer ett RAG-mönster med styrda dokumentkällor, metadata, behörighetsmedveten retrieval, AI-gateway, promptkonstruktion, modellkörning, källhänvisningar, loggning och produktförvaltning.

Kapitlet etablerar att Auroras produktionssatta kunskapsstöd bara får bygga på källor som har informationsägare, informationsklass, dokumenterad giltighet, versionshantering, definierade åtkomstregler, känd uppdateringsprocess och spårbarhet från svar till källa.

Aurora beslutar också att finjustering inte ska användas som förstahandslösning för kunskapsbrist. RAG är förstahandsmönster när svaren ska grundas i aktuella myndighetskällor. Finjustering kan övervägas senare för format, stil eller återkommande klassificeringsmönster.

## Användning i kapitel 12

Kapitel 12 använder Tullverket Aurora för att visa hur MLOps, LLMOps och livscykelhantering behöver etableras innan ett AI-kunskapsstöd kan bli en kontrollerad produktionsförmåga.

Aurora inför en minsta nödvändig LLMOps-förmåga för det interna kunskapsstödet:

1. Register över AI-användningsfall.
2. Register över modeller och modellendpoints.
3. Versionerade systempromptar.
4. Kontrollerad dokumentpublicering till RAG-index.
5. Testfrågebank för kunskapsstödet.
6. Godkännande av källsamlingar.
7. Loggning av modell, promptversion, källor och policyträffar.
8. Dashboard för användning, fel, kostnad och källträffar.
9. Releaseprocess för ändrade promptar och index.
10. Rollback till tidigare prompt- och indexversion.
11. Incidentprocess för felaktiga eller olämpliga svar.

Kapitlet etablerar att promptar, RAG-konfigurationer, index, embeddingmodeller, testfrågor och policyregler ska behandlas som styrda artefakter. Även små ändringar, till exempel ändrad chunkingstrategi, kan påverka svarskvalitet, källhänvisning, kostnad och risk.

Aurora väljer en federerad modell för AI-livscykelhantering: gemensamma principer, register, minimikrav, AI-gateway och releasekrav kombineras med verksamhetsnära produktteam som ansvarar för sina användningsfall inom gemensamma ramar.


## Användning i kapitel 13

Kapitel 13 använder Tullverket Aurora för att visa att driftmodell inte ska väljas som ett generellt ja eller nej till moln, utan som ett riskbaserat arkitekturbeslut per användningsfall, informationsflöde och AI-roll.

Aurora etablerar fyra arkitekturspår:

1. Kontrollerad SaaS för lågklassat produktivitetsstöd.
2. Molnbaserad AI-plattform för kontrollerade piloter.
3. Hybrid RAG för styrt internt kunskapsstöd.
4. Kontrollerad intern eller privat miljö för känsliga och beslutsnära flöden.

Kapitlet etablerar att hybrid är Auroras realistiska målbild, men bara som styrd hybridarkitektur. AI-gateway, modellregister, identitet, loggning, policy enforcement, datakontrakt och exitstrategi behövs för att binda samman miljöerna.

Aurora beslutar att moln får användas där informationsklassning, rättslig bedömning, leverantörsvillkor och säkerhetskontroller tillåter det. On-premises eller privat drift ska användas där känsliga data, beslutsnära flöden eller kontrollkrav kräver det. Beslutet dokumenteras som tillåtna arkitekturspår snarare än som ett enda plattformsval.


## Användning i kapitel 14

Kapitel 14 använder Tullverket Aurora för att visa hur en myndighet bedömer plattformar, produkter och ramverk utan att reducera målarkitekturen till en produktlista.

Auroras arkitekturgrupp delar in AI-landskapet i fyra nivåer:

1. Användarnära AI-stöd för lågklassad produktivitet.
2. Gemensam AI-plattform för kontrollerade lösningar.
3. Kontrollerad intern AI-zon för känsligare användningsfall.
4. Experiment- och utvärderingsmiljö för styrd utforskning.

Kapitlet etablerar att plattformsval ska kopplas till byggblock, informationsklassning, driftspår, livscykelhantering och arkitekturbeslut. Tullverket Aurora väljer därför inte en enda AI-produkt, utan en plattformskarta med flera tillåtna arkitekturspår och tydliga beslutsregler.

## Användning i kapitel 15

Kapitel 15 använder Tullverket Aurora för att visa hur en myndighet gör AI-vägval utan att reducera målarkitekturen till produktval.

Aurora skapar en beslutslogg för sin AI-målarkitektur med bland annat följande beslut:

1. Central styrning med federerade produktteam.
2. Begränsad modellkatalog med godkända modellspår.
3. RAG före fine-tuning för styrdokument och handböcker.
4. Hybrid driftmodell kopplad till informationsklass och användningsfall.
5. AI-gateway som målbild för produktionssatt modellåtkomst.
6. Plattformstjänst där möjligt och egen kontroll där nödvändigt.

Kapitlet etablerar att varje nytt AI-initiativ ska placeras i ett godkänt arkitekturspår eller dokumenteras som avvikelse genom en ny ADR.

## Kapitel 16: Säkerhetsarkitektur för AI

Tullverket Aurora använder två etapper för sitt RAG-baserade kunskapsstöd.

I första etappen används lågkänsliga dokument som publika regelverk, godkända handböcker och processbeskrivningar. Lösningen får använda kontrollerad molndrift med AI-gateway, källhänvisning, loggning och begränsade datakällor.

I andra etappen vill Aurora använda ärendenära information. Arkitekturteamet inför då separata index per informationsklass, behörighetsfiltrering före retrieval, striktare loggskydd, avskild driftmiljö, mänsklig granskning och testning mot indirekt prompt injection. Verktygsanrop mot ärendesystem stoppas tills särskilt arkitekturbeslut finns.

## Kapitel 17: Upphandling och leverantörsstyrning

Tullverket Aurora använder tre anskaffningssituationer för att visa att AI-upphandling måste vara flerspårig.

Det första behovet är ett internt skriv- och sammanfattningsstöd för lågkänsligt administrativt arbete. Här kan befintligt avtal eller färdig SaaS vara rimligt om AI-villkor, dataskydd, loggning och användningspolicy är granskade.

Det andra behovet är ett RAG-baserat kunskapsstöd för handläggare. Här behöver Aurora ställa krav på behörighetsstyrd retrieval, källhänvisning, loggning, datalokalisering, indexseparering, integration med identitet och möjlighet att exportera konfiguration.

Det tredje behovet är ett analysstöd för riskbedömning i kontrollverksamheten. Här blir kraven betydligt hårdare: dokumentation, validering, revision, modellstyrning, spårbarhet, incidenthantering, leverantörskedja, exitstrategi och stark intern förvaltningsförmåga.

Kapitlet etablerar principen att konsulten får accelerera införandet, men inte äga AI-förmågan. Aurora kräver därför dokumentation, kunskapsöverföring, arkitekturbeslut, exportmöjligheter och löpande leverantörsstyrning.

## Kapitel 18: Roadmap från nuläge till etablerad AI-förmåga

Kapitel 18 använder Tullverket Aurora för att visa hur målarkitekturen omsätts i en 24-månaders införandeplan.

Aurora delar upp etableringen i sex faser:

1. Månad 0–3: nulägesbild, mandat, första AI-forum och preliminära principer.
2. Månad 3–6: kontrollerad sandlåda och triage av användningsfall.
3. Månad 6–9: första referensarkitektur och styrda piloter.
4. Månad 9–12: produktionsförmåga för låg till måttlig risk.
5. Månad 12–18: skalning genom arkitekturspår och differentierade driftmodeller.
6. Månad 18–24: mognad, revision, portföljstyrning och kontinuerlig förbättring.

Aurora väljer att produktionssätta ett avgränsat RAG-baserat kunskapsstöd före mer känsliga användningsfall som kontrollprioritering. Det senare placeras i ett särskilt utredningsspår tills juridik, modellvalidering, säkerhetsarkitektur och mänsklig kontroll är tillräckligt mogna.

Kapitlet etablerar att roadmapen är målarkitekturens genomförandelogik. Den visar inte bara när teknik ska införas, utan i vilken ordning styrning, data, juridik, plattform, produktteam, säkerhet och förvaltning behöver mogna.


## Användning i kapitel 19

Kapitel 19 samlar tidigare delar i ett sammanhängande målarkitekturexempel för Tullverket Aurora.

Auroras målbild formuleras som att myndigheten ska kunna använda AI som ett kontrollerat, säkert och rättssäkert stöd i interna och verksamhetsnära processer, där användningsfall, data, modellval och driftmiljö styrs utifrån nytta, risk, juridik och informationsklassning.

Kapitlet etablerar fyra arkitekturspår:

1. Kontorsnära AI för lågkänslig information.
2. Myndighetsintern RAG för styrd kunskapssökning.
3. Känsligt handläggarstöd.
4. Analys- och riskmodeller med hög konsekvens.

Kapitlet etablerar också följande centrala arkitekturbeslut för Aurora:

1. AI-gateway som gemensam åtkomstpunkt.
2. RAG före finjustering för första kunskapsstödet.
3. Fyra arkitekturspår för drift och risk.
4. Hybrid målbild.
5. Källhänvisning som standard för kunskapsstöd.

Scenariot ska fortsatt undvika operativa detaljer om tullkontroll. Fokus ska ligga på målarkitektur, styrning, data, risk, säkerhet, driftmodell och förvaltning.


## Användning i kapitel 20

Kapitel 20 använder Tullverket Aurora för att visa vanliga misstag och anti-patterns när en myndighet etablerar AI-förmåga.

Aurora korrigerar särskilt tre riskmönster:

1. Team som väljer AI-verktyg innan användningsfall, risk och data är tillräckligt bedömda.
2. Överanvändning av RAG som lösning för både kunskapsstöd och mer känsligt beslutsstöd.
3. Piloter som saknar tydlig produktionsväg, förvaltningsmottagare och modellägarskap.

Kapitlet etablerar fyra skuldtyper som ska kunna användas i senare granskning och checklistor:

1. Teknisk skuld.
2. Styrningsskuld.
3. Dataskuld.
4. Säkerhetsskuld.

## Användning i kapitel 21

Kapitel 21 använder Tullverket Aurora för att visa hur målarkitekturen omsätts i återkommande checklistor och beslutsmallar.

Aurora använder följande mallar som praktiska styrmedel:

1. AI-use-case canvas för att beskriva nya AI-idéer.
2. Triage för juridik, dataskydd och informationssäkerhet.
3. Beslutsmatris för moln, on-premises och hybrid.
4. Beslutsmall för RAG, fine-tuning och egen modellservering.
5. Mall för arkitekturbeslut.
6. Produktionsberedskap för AI-lösningar.
7. Förvaltningschecklista för produktionssatta AI-lösningar.

Kapitlet etablerar att målarkitekturen blir en faktisk förmåga först när den används i återkommande beslut, inte bara när den dokumenteras.


## Slutredaktionell scenarioregel

Efter slutredigeringen ska Tullverket Aurora användas konsekvent som röd tråd när boken behöver konkretisera:

- skillnaden mellan experiment och förmåga,
- klassning av informationsflöden,
- juridik och ansvar,
- tekniska byggblock,
- moln/on-premises/hybrid-vägval,
- upphandling och leverantörsstyrning,
- roadmap och införande,
- anti-patterns och checklistor.

Scenariot ska fortsatt vara arkitektoniskt och styrningsmässigt, inte operativt.
