# Kapitel 10: Teknisk referensarkitektur

## Varför detta kapitel finns

När en myndighet har identifierat sina användningsfall, klassat informationen, formulerat principer och beskrivit nödvändiga förmågor uppstår nästa fråga: hur ska den tekniska arkitekturen se ut?

Det är frestande att börja med en produktbild. En AI-plattform från en molnleverantör, ett verktyg för RAG, en vektordatabas, ett modell-API eller en färdig AI-assistent kan snabbt ge intrycket av en fungerande målarkitektur. Men för en större statlig myndighet är en teknisk referensarkitektur något annat än en produktkatalog. Den ska visa vilka byggblock som behövs, hur de samverkar, vilka ansvar de har, vilka gränser som finns mellan dem och vilka delar som måste kunna bytas ut över tid.

Detta kapitel beskriver den tekniska referensarkitekturen för AI som en återanvändbar ritning. Den ska kunna användas av arkitekter, produktteam, säkerhetsfunktioner, jurister, upphandlare och driftansvariga när nya AI-lösningar ska bedömas, designas eller sättas i produktion.

Kapitel 9 beskrev dataarkitekturen. Detta kapitel bygger vidare på den och visar hur data, modeller, tjänster, identitet, integration, policy, loggning och drift behöver bindas samman till en teknisk helhet.

## Arkitekturproblemet

Tullverket Aurora har tre prioriterade AI-spår:

- intern kunskapssökning i styrdokument och handböcker,
- sammanfattning av ärendehandlingar,
- prediktivt prioriteringsstöd för kontrollverksamhet.

Varje spår har olika risknivå, olika datakällor, olika krav på spårbarhet och olika krav på mänsklig kontroll. Samtidigt vill myndigheten undvika att varje initiativ bygger sin egen tekniska stack. Om varje team väljer egen modell, egen vektordatabas, egen loggning, egen behörighetsmodell och egen säkerhetslösning kommer AI-förmågan snabbt att bli dyr, svårstyrd och riskfylld.

Auroras arkitekturgrupp behöver därför besvara en central fråga:

> Vilka tekniska byggblock ska vara gemensamma, vilka ska vara federerade och vilka kan vara lokala för ett enskilt användningsfall?

Frågan är viktig eftersom teknisk standardisering både kan hjälpa och skada. För lite standardisering skapar fragmentering. För mycket standardisering kan skapa flaskhalsar, onödig komplexitet och långsam innovation. Referensarkitekturen måste därför ange stabila gränssnitt och styrande mönster, men inte låsa alla team till exakt samma implementation.

## Centrala begrepp

Teknisk referensarkitektur är en återanvändbar arkitekturbeskrivning som visar de centrala tekniska byggblocken, deras ansvar, relationer och styrande integrationsmönster. Den är inte samma sak som en lösningsarkitektur för ett enskilt system.

AI-gateway är ett kontrollerat åtkomstlager mellan användande applikationer och AI-tjänster. Den kan hantera autentisering, behörighet, policykontroll, loggning, kvoter, modellval, promptfilter, kostnadskontroll och routning till olika modellleverantörer.

Modellplattform är den tekniska miljö där modeller görs tillgängliga, körs, versioneras, övervakas och förvaltas. Den kan vara en extern modell-API-tjänst, en molnplattform, en intern inferensplattform eller en kombination.

Inferens är den körning där en tränad modell tar emot indata och producerar utdata. För språkmodeller handlar det exempelvis om att generera text, klassificera innehåll eller skapa embeddings.

RAG, retrieval-augmented generation, är ett arkitekturmönster där en språkmodell kombineras med hämtad kontext från myndighetens egna informationskällor. Syftet är att ge modellen relevant underlag utan att träna om modellen.

Orkestrering innebär att flera tekniska steg kopplas samman i ett AI-flöde, till exempel klassning av fråga, hämtning av behörig kontext, promptkonstruktion, modellkörning, policykontroll och svarspresentation.

Policy enforcement innebär att tekniska regler tillämpas i systemflödet, inte bara dokumenteras i styrdokument. Det kan gälla dataklassning, åtkomst, tillåtna modeller, loggning, exportbegränsningar och mänsklig granskning.

Observability är förmågan att förstå vad som händer i systemet genom loggar, mätvärden, spårning, kostnadsdata, kvalitetsmätning och driftlarm.

Guardrails är tekniska och processuella skydd som begränsar hur AI-lösningen får användas och vilket beteende den får uppvisa. Guardrails kan omfatta promptfilter, innehållsfilter, tillåtna verktyg, källkrav, svarsmallar, mänsklig granskning och spärrar mot otillåtna åtgärder.

## Referensarkitekturen som karta, inte produktlista

En teknisk referensarkitektur ska inte börja med frågan vilken produkt som är bäst. Den ska börja med frågan vilka arkitekturansvar som måste hanteras.

För en myndighet som Aurora behöver referensarkitekturen minst beskriva:

- hur användare och applikationer får åtkomst till AI-tjänster,
- hur identitet och behörighet följer med genom AI-flödet,
- hur data hämtas, filtreras, indexeras och skyddas,
- hur modeller väljs, anropas, versioneras och övervakas,
- hur promptar, kontext och svar loggas och spåras,
- hur policyregler tillämpas tekniskt,
- hur integration sker med befintliga system,
- hur lösningar testas och produktionssätts,
- hur drift, incidenter och avveckling hanteras.

Detta gör referensarkitekturen till ett beslutsunderlag. Den ska hjälpa myndigheten att bedöma om ett nytt användningsfall kan realiseras med befintliga byggblock, om ett nytt byggblock behövs eller om användningsfallet bör stoppas tills styrning, data eller säkerhet är på plats.

En god referensarkitektur gör också upphandling enklare. Den beskriver vilka ansvar en produkt eller leverantör kan få, vilka gränssnitt som krävs och vilka delar myndigheten inte bör outsourca utan kontroll.

## Översikt över byggblocken

En myndighetsgemensam AI-referensarkitektur kan beskrivas i nio huvudlager:

1. användar- och kanalager,
2. applikations- och produktlager,
3. AI-gateway och policy enforcement,
4. orkestrerings- och agentlager,
5. modell- och inferenslager,
6. RAG- och kunskapslager,
7. data- och integrationslager,
8. säkerhets-, identitets- och åtkomstlager,
9. observability, styrning och livscykelhantering.

Lagren ska inte tolkas som en strikt fysisk nätverksmodell. De beskriver ansvar. I en konkret lösning kan flera ansvar implementeras i samma produkt, samma molntjänst eller samma plattform. Det viktiga är att ansvaren inte försvinner.

### Användar- och kanalager

Användar- och kanalagret beskriver var AI-förmågan möter användaren. Det kan vara en intern chattassistent, en funktion i ett ärendehanteringssystem, ett analysgränssnitt, ett API, en kontorsapplikation eller en separat verksamhetsapplikation.

För Aurora är detta lager viktigt eftersom olika användare har olika mandat. En handläggare som söker i interna instruktioner ska inte få samma funktioner som en analytiker som arbetar med riskmodeller eller en arkitekt som testar en ny RAG-pipeline. Användarupplevelsen behöver därför spegla roll, behörighet och användningsfall.

Referensarkitekturen bör ange att AI-funktioner i detta lager ska vara tydligt märkta. Användaren ska förstå när ett svar är AI-genererat, vilket underlag som har använts, vilken osäkerhet som finns och om svaret får användas direkt eller kräver granskning.

### Applikations- och produktlager

Applikationslagret innehåller de verksamhetsnära produkter som använder AI-förmågan. Det kan vara handläggarstöd, analysverktyg, kunskapsportaler, automatiseringsflöden eller interna utvecklarverktyg.

Detta lager ska inte behöva lösa alla AI-frågor på egen hand. En produkt som använder AI bör kunna återanvända gemensamma tjänster för modellåtkomst, loggning, policy, datahämtning och övervakning. Annars uppstår parallella implementationer av samma kontroller.

För Aurora innebär detta att ett team som bygger kunskapsstöd inte ska skapa en egen lösning för modellloggning, promptpolicy och källspårning. Dessa ansvar ska i första hand tillhandahållas som gemensamma byggblock.

### AI-gateway och policy enforcement

AI-gatewayen är ett av de mest centrala byggblocken i en myndighets AI-referensarkitektur. Den fungerar som en kontrollerad passage mellan applikationer och AI-tjänster.

En AI-gateway kan hantera:

- tillåtna modeller och modellleverantörer,
- routning mellan olika modeller,
- behörighetskontroll före modellåtkomst,
- policykontroll baserad på användningsfall och informationsklass,
- prompt- och svarskontroller,
- loggning av anrop, kostnader och metadata,
- kvoter och rate limiting,
- blockering av otillåtna datatyper,
- koppling till modell- och tjänsteregister.

Gatewayen ska inte ses som en magisk säkerhetslösning. Den kan inte ensam garantera att AI-lösningen blir säker eller lagenlig. Men den kan göra det möjligt att konsekvent tillämpa kontroller som annars skulle behöva byggas om i varje applikation.

För Aurora blir AI-gatewayen ett sätt att separera verksamhetsapplikationer från underliggande modellval. Ett kunskapsstöd kan då använda en godkänd modell i ett molnspår för lågklassad information, medan ett känsligare ärendestöd kan routas till en intern modellmiljö eller en striktare driftzon.

### Orkestrerings- och agentlager

Orkestreringslagret styr hur ett AI-flöde genomförs. För ett enkelt textsvar kan flödet vara kort: ta emot fråga, skapa prompt, anropa modell och visa svar. För ett myndighetskritiskt kunskapsstöd kan flödet vara mer omfattande:

1. identifiera användare och roll,
2. klassificera användarens fråga,
3. kontrollera tillåtet användningsfall,
4. hämta behörig kontext,
5. konstruera prompt,
6. anropa modell,
7. kontrollera svar mot policy,
8. lägga till källhänvisningar,
9. logga metadata,
10. visa svar med varningar och begränsningar.

I vissa lösningar används agentmönster där en AI-komponent kan välja verktyg, anropa API:er eller genomföra flera steg. För en myndighet kräver detta särskild försiktighet. Ju mer autonomt ett AI-flöde blir, desto viktigare blir begränsningar för vilka verktyg som får användas, vilka åtgärder som kräver mänskligt godkännande och hur varje steg loggas.

Auroras referensarkitektur bör därför skilja mellan tre nivåer av orkestrering:

- enkel modellinteraktion utan verktygsanrop,
- styrd orkestrering med bestämda steg och godkända datakällor,
- agentliknande orkestrering med verktygsanrop och högre krav på kontroll.

Den tredje nivån ska inte vara standard för tidiga produktionsspår.

### Modell- och inferenslager

Modell- och inferenslagret ansvarar för tillgång till modeller. Det kan omfatta språkmodeller, embeddingsmodeller, klassificeringsmodeller, bildmodeller, prediktiva modeller och specialiserade modeller för specifika uppgifter.

En myndighets referensarkitektur bör inte anta att en enda modelltyp räcker. Olika användningsfall kräver olika egenskaper:

- generativa språkmodeller för sammanfattning, skrivstöd och dialog,
- embeddingsmodeller för semantisk sökning,
- klassificeringsmodeller för sortering och prioritering,
- prediktiva modeller för analysstöd,
- mindre specialmodeller för avgränsade uppgifter med högre kontrollkrav.

Modellagret behöver också hantera versioner. Ett AI-svar som skapades med en viss modellversion måste kunna spåras om svaret senare ifrågasätts. Detta gäller särskilt när AI används i ärendenära processer eller som underlag för beslut.

För Aurora innebär detta att modellval inte får döljas inne i en applikation. Modell, modellversion, driftmiljö, leverantör, konfigurationsprofil och tillåtet användningsområde bör registreras i ett modell- och tjänsteregister.

### RAG- och kunskapslager

RAG-lagret hanterar hämtning av relevant kontext från myndighetens egna informationskällor. Det omfattar ofta dokumentintag, textutvinning, chunking, embeddings, indexering, sökning, ranking, källurval och källpresentation.

För myndigheter är RAG-lagret ofta mer känsligt än det först verkar. Det innehåller inte bara tekniska index. Det representerar myndighetens kunskap, behörighetsregler och dokumentversioner i en form som AI-lösningen kan använda.

Referensarkitekturen bör därför kräva att RAG-lagret kan hantera:

- auktoritativa datakällor,
- dokumentversioner och giltighet,
- metadata och informationsklass,
- behörighetsmedveten retrieval,
- källhänvisning i svar,
- gallring och omindexering,
- spårning från svar till källor,
- skydd av embeddings och index.

Aurora använder RAG för intern kunskapssökning. Arkitekturgruppen beslutar att första versionen endast får använda godkända källor med informationsägare, tydlig giltighet och etablerad åtkomstmodell. Dokument från delade mappar utan ägare får inte indexeras i produktionsspåret.

### Data- och integrationslager

Data- och integrationslagret binder AI-förmågan till befintliga system och informationsflöden. Det kan omfatta API:er, meddelandeflöden, dataplattformar, dokumenthanteringssystem, ärendesystem, katalogtjänster och arkivlösningar.

En vanlig risk är att AI-lösningar skapar genvägar runt etablerade integrationsmönster. Ett team exporterar data manuellt, laddar upp filer till ett AI-verktyg eller bygger en direktkoppling utan gemensam styrning. Det kan vara effektivt i ett experiment men olämpligt i produktion.

Referensarkitekturen bör därför ange att produktionssatta AI-lösningar ska använda godkända integrationsmönster. Det innebär inte att alla integrationer måste vara tunga eller centraliserade, men de ska vara spårbara, ägda, säkrade och möjliga att förvalta.

### Säkerhets-, identitets- och åtkomstlager

AI-lösningar behöver ärva myndighetens säkerhetsarkitektur, inte skapa en parallell identitetsvärld.

Det innebär att referensarkitekturen behöver beskriva hur följande fungerar i AI-flöden:

- användaridentitet,
- tjänsteidentitet,
- roll- och attributbaserad behörighet,
- åtkomst till datakällor,
- åtkomst till modeller,
- secrets och nyckelhantering,
- nätverkszoner,
- kryptering,
- administratörsbehörigheter,
- separation mellan utveckling, test och produktion.

För Aurora är en särskilt viktig princip att användarens behörighet ska påverka vilken kontext som får hämtas i ett RAG-flöde. Det räcker inte att användaren får använda AI-tjänsten. Användaren måste också ha rätt att se de dokument som skickas som kontext till modellen.

### Observability, styrning och livscykelhantering

AI-förmågan behöver kunna observeras över tid. Det räcker inte att veta om tjänsten är tekniskt uppe. Myndigheten behöver också förstå kvalitet, risk, användning, kostnad och avvikelser.

Referensarkitekturen bör därför ange vilka typer av loggar och mätvärden som behövs:

- tekniska driftloggar,
- användningsstatistik,
- modell- och tjänsteanrop,
- kostnad per användningsfall,
- svarskvalitet och feedback,
- policyträffar och blockerade anrop,
- fel och incidenter,
- modellversioner,
- källor som använts i RAG-svar,
- beslut om avvikelse eller manuell överstyrning.

Loggning måste samtidigt balanseras mot dataskydd, sekretess och informationssäkerhet. Det är inte självklart att hela promptar och svar ska lagras i klartext. I vissa fall bör loggning ske med metadata, maskning, aggregering eller särskilda skyddszoner.

## Tre referensmönster för Aurora

Aurora väljer att beskriva tre tekniska referensmönster. De är inte färdiga lösningar, utan återanvändbara mönster för olika risk- och användningsklasser.

### Mönster 1: Kontrollerad AI-assistent för lågklassad information

Det första mönstret gäller intern produktivitet och lågklassad information. Exempel är hjälp med att strukturera text, sammanfatta offentliga dokument, skapa utkast till mötesanteckningar eller förklara generella begrepp.

Mönstret kan använda en godkänd SaaS- eller molnbaserad AI-tjänst, men endast inom tydliga ramar:

- användare autentiseras med myndighetens identitet,
- användningsvillkor och databehandling är granskade,
- känsliga data får inte skickas,
- användningen loggas på lämplig nivå,
- användaren får tydliga instruktioner,
- AI-genererat innehåll får inte betraktas som beslutsunderlag utan granskning.

Detta mönster ger snabb nytta men ska inte användas som bakväg för känsligare användningsfall.

### Mönster 2: RAG-baserat kunskapsstöd med behörighetsmedveten retrieval

Det andra mönstret gäller intern kunskapssökning. Här används AI för att hjälpa handläggare och experter att hitta, sammanfatta och förstå interna dokument.

Mönstret kräver fler byggblock:

- dokumentintag från godkända källor,
- metadata och informationsklassning,
- embeddings och indexering,
- behörighetsmedveten retrieval,
- promptkonstruktion med hämtad kontext,
- modellåtkomst via AI-gateway,
- källhänvisning i svar,
- loggning av källor, modellversion och policykontroller,
- användarfeedback och kvalitetsuppföljning.

I detta mönster blir RAG-lagret en del av myndighetens informationsarkitektur. Det ska inte förvaltas som en isolerad teknisk komponent.

### Mönster 3: Analys- och prioriteringsstöd med högre kontrollkrav

Det tredje mönstret gäller prediktivt eller statistiskt stöd för riskanalys och kontrollprioritering. Detta är mer känsligt eftersom resultaten kan påverka hur myndigheten prioriterar resurser eller granskar ärenden.

Mönstret kräver starkare styrning:

- tydligt verksamhetsägarskap,
- dokumenterad modellbeskrivning,
- kvalitetssäkrade tränings- och testdata,
- validering och oberoende granskning,
- mätning av feltyper och biasrisker,
- mänsklig kontroll,
- spårbarhet från modellresultat till datakällor och modellversion,
- kontrollerad driftsättning,
- incident- och avvikelsehantering.

Detta mönster ska inte realiseras genom att en generativ AI-modell får fri åtkomst till verksamhetsdata. Det kräver en mer traditionell modell- och dataförvaltningsdisciplin, kompletterad med AI-specifika kontroller.

## Beslutspunkt: vad ska vara gemensamt?

En teknisk referensarkitektur behöver ange vilka byggblock som bör vara gemensamma. För Aurora väljer arkitekturgruppen följande grundprincip:

Gemensamt ska vara det som bär risk, styrning, spårbarhet, återanvändning eller leverantörsoberoende.

Det leder till att följande byggblock bör vara gemensamma eller starkt standardiserade:

- AI-gateway,
- modell- och tjänsteregister,
- policy enforcement,
- loggning och observability,
- grundmönster för RAG,
- identitets- och behörighetsintegration,
- säkerhetszoner och godkända driftspår,
- arkitekturbeslutsmallar,
- krav på modell- och datadokumentation.

Följande kan däremot ofta vara federerat:

- verksamhetsspecifika RAG-index,
- specialiserade analysmodeller,
- användargränssnitt,
- domänspecifika promptmallar,
- lokala utvärderingsmått,
- integrationer med domänsystem.

Följande bör normalt vara lokalt för en enskild lösning:

- specifik användarupplevelse,
- detaljerad processlogik,
- presentation av resultat,
- verksamhetsspecifika arbetsflöden,
- lösningsspecifika konfigurationer inom godkända ramar.

Denna uppdelning hindrar både övercentralisering och fragmentering.

## Policy som körbar arkitektur

Många myndigheter har policyer, men AI kräver att vissa policyer blir tekniskt verkställbara. Det räcker inte att skriva att sekretessbelagd information inte får skickas till otillåtna modeller. Arkitekturen måste göra det svårt eller omöjligt.

I praktiken innebär det att referensarkitekturen bör kunna uttrycka regler som:

- användningsfall i styrklass A får använda modellprofil X,
- användningsfall i styrklass C kräver modellprofil Y och särskild loggning,
- dokument med viss informationsklass får inte lämna angiven driftzon,
- RAG-flöden måste filtrera kontext utifrån användarens behörighet,
- svar från vissa AI-flöden måste visa källor,
- agentflöden får endast anropa godkända verktyg,
- promptar med misstänkt känslig information ska blockeras eller eskaleras.

Denna typ av policy enforcement kan implementeras på flera sätt: i gateway, orkestreringslager, datalager, API-lager eller applikation. Referensarkitekturen ska inte nödvändigtvis föreskriva exakt produkt, men den ska ange var kontrollen måste finnas och vem som äger den.

## Arkitektur för flera driftspår

Kapitel 6 etablerade principen flera driftspår. Den tekniska referensarkitekturen behöver göra denna princip konkret.

Aurora beskriver tre driftspår:

1. molnbaserat standardspår för godkända låg- och mellanriskfall,
2. skyddat hybridspår för känsligare interna användningsfall,
3. internt eller särskilt kontrollerat spår för högriskfall och skyddsvärda data.

Driftspåren ska inte vara tre helt separata världar. De bör dela principer, styrmodell, metadata, modellregister, arkitekturbeslut och vissa mönster. Men de kan skilja sig i modellleverantör, nätverkszon, loggningskrav, dataåtkomst och driftsansvar.

En viktig arkitekturpoäng är att driftspår ska väljas efter användningsfall och informationsflöde, inte efter vilken produkt som råkar vara enklast att börja med.

## Integration med befintlig företagsarkitektur

AI-referensarkitekturen måste kopplas till myndighetens befintliga företagsarkitektur. Annars riskerar AI att bli ett sidospår.

Det innebär att AI-byggblock bör relateras till befintliga arkitekturdomäner:

- verksamhetsarkitektur: processer, förmågor, roller och ansvar,
- informationsarkitektur: informationsobjekt, klassning, ägarskap och livscykel,
- applikationsarkitektur: system, produkter, API:er och användargränssnitt,
- teknikarkitektur: plattformar, nätverk, driftmiljöer och säkerhetszoner,
- säkerhetsarkitektur: identitet, åtkomst, kryptering, loggning och incidenthantering,
- styrningsarkitektur: forum, beslut, riskacceptans och avvikelsehantering.

För Aurora innebär det att AI-förmågan inte ska ritas som ett separat moln vid sidan av befintlig arkitektur. Den ska placeras i samma arkitekturmodell som myndighetens övriga digitala förmågor.

## Exempel: Auroras första tekniska målbild

Auroras arkitekturgrupp formulerar en första teknisk målbild för de kommande tolv månaderna.

Myndigheten ska etablera en gemensam AI-gateway som all produktionssatt modellåtkomst går via. Gatewayen ska kunna routa anrop till minst två godkända modellprofiler: ett molnbaserat standardspår och ett skyddat internt spår. Modeller och AI-tjänster ska registreras i ett gemensamt modell- och tjänsteregister.

För RAG ska Aurora etablera ett gemensamt referensmönster med dokumentintag, metadata, behörighetsmedveten retrieval, källhänvisning och loggning. Varje verksamhetsområde får äga sina källor och index, men måste följa gemensamma krav på metadata, informationsägarskap och åtkomstkontroll.

För observability ska varje AI-lösning rapportera grundläggande metadata: användningsfall, modellprofil, modellversion, driftspår, källor, policyträffar, fel, kostnader och användarfeedback. Full prompt- och svarstext får bara loggas där informationsklassning och dataskydd tillåter det.

Aurora beslutar också att agentliknande lösningar med verktygsanrop inte får produktionssättas förrän särskilda kontroller för verktygsbehörighet, mänskligt godkännande och åtgärdsloggning finns på plats.

## Exempel från Tullverket Aurora

I Tullverket Aurora används referensarkitekturen för att undvika att varje pilot bygger sin egen AI-stack. Ett RAG-baserat kunskapsstöd, ett internt analysstöd och en modell för ärendeprioritering delar inte samma riskprofil, men de behöver ändå återanvända gemensamma byggblock för identitet, loggning, policykontroll, datakatalog, modellregister och integrationsmönster.

Den redaktionella poängen i scenariot är att målarkitekturen inte pekar ut en enda lösning för alla behov. Den pekar ut vilka byggblock som ska vara gemensamma, vilka delar som får variera och vilka beslut som måste dokumenteras.

## Vägvalsfrågor

När arkitekturgruppen tar fram eller granskar en teknisk referensarkitektur bör den ställa följande frågor:

- Vilka AI-byggblock ska vara gemensamma, federerade respektive lokala?
- Måste all modellåtkomst gå via en AI-gateway?
- Hur kopplas användarens identitet och behörighet till RAG och modellanrop?
- Vilka driftspår finns och vilka informationsklasser får hanteras i respektive spår?
- Hur registreras modeller, modellversioner, tjänster och tillåtna användningsområden?
- Vilken loggning behövs för spårbarhet, kvalitet, kostnad och incidenthantering?
- Vilka delar av promptar, kontext och svar får lagras?
- Hur skiljer arkitekturen mellan experiment, pilot och produktion?
- Vilka kontroller måste ligga i gateway, orkestrering, datalager respektive applikation?
- Hur undviker myndigheten att varje AI-team bygger egen säkerhet, egen loggning och egen modellåtkomst?
- Vilka komponenter måste kunna bytas ut utan att hela målarkitekturen görs om?
- Vilka agent- eller verktygsanrop är tillåtna och vilka kräver mänskligt godkännande?

## Vanliga fallgropar

- **Att kalla en produkt för referensarkitektur.**
  - Varför det händer: En plattform kan visa många byggblock i samma vy.
  - Hur du undviker det: Beskriv ansvar, gränssnitt, kontroller och vägval innan produktnamn anges.

- **Att låta varje pilot skapa egen modellåtkomst.**
  - Varför det händer: Det går snabbt att anropa ett modell-API direkt.
  - Hur du undviker det: Inför tidigt en minsta gemensam väg för modellåtkomst, loggning och policy.

- **Att separera RAG från informationsarkitekturen.**
  - Varför det händer: RAG uppfattas som en teknisk sökfunktion.
  - Hur du undviker det: Behandla index, embeddings och källmetadata som delar av myndighetens informationsflöde.

- **Att logga för mycket utan dataskyddsanalys.**
  - Varför det händer: Team vill kunna felsöka och förbättra kvalitet.
  - Hur du undviker det: Bestäm loggningsnivå per informationsklass och användningsfall.

- **Att övercentralisera all AI-utveckling.**
  - Varför det händer: Central styrning känns trygg i ett nytt riskområde.
  - Hur du undviker det: Standardisera gemensamma kontroller men låt domänteam äga verksamhetsnära lösningar inom tydliga ramar.

- **Att släppa in agentmönster för tidigt.**
  - Varför det händer: Agentfunktioner demonstrerar snabbt imponerande automation.
  - Hur du undviker det: Kräv verktygsbegränsning, åtgärdsloggning och mänsklig kontroll innan agentflöden produktionssätts.

## Checklista

En teknisk referensarkitektur för AI bör minst innehålla:

- beskrivning av centrala byggblock,
- ansvarsfördelning mellan gemensamma, federerade och lokala komponenter,
- godkända driftspår,
- princip för AI-gateway och modellåtkomst,
- modell- och tjänsteregister,
- RAG-mönster inklusive metadata, behörighet och källspårning,
- integrationsmönster mot befintliga system,
- identitets- och åtkomstmodell,
- policy enforcement-punkter,
- loggnings- och observability-krav,
- krav på separation mellan experiment, test och produktion,
- krav på modellversionering och spårbarhet,
- vägledning för agent- och verktygsanrop,
- koppling till informationsklassning och riskstyrning,
- koppling till upphandling och leverantörsstyrning.

Om dessa delar saknas är referensarkitekturen sannolikt för lös, för produktcentrerad eller för svår att använda som styrande underlag.

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Den tekniska referensarkitekturen är inte hela målarkitekturen. Den är den tekniska delen av en bredare målbild som också omfattar juridik, principer, governance, data, organisation, arbetssätt, upphandling och införande.

I målarkitekturen bör den tekniska referensarkitekturen användas för att:

- beskriva gemensamma AI-byggblock,
- styra lösningsarkitektur för nya användningsfall,
- underlätta konsekventa plattformsval,
- skapa återanvändbara säkerhets- och loggningsmönster,
- ge upphandlare tydligare tekniska krav,
- visa vilka förmågor som måste etableras före skalning,
- möjliggöra spårbara arkitekturbeslut.

För Aurora blir kapitel 10 en brygga mellan den tidigare data- och förmågediskussionen och de kommande kapitlen om generativ AI, RAG, MLOps, LLMOps, driftmodeller, plattformar och säkerhet. Referensarkitekturen ger en gemensam karta. Nästa steg är att gå djupare i ett av de mest aktuella mönstren: generativ AI och RAG i myndighetsmiljö.

## Snabb sammanfattning

En teknisk AI-referensarkitektur ska beskriva byggblock, ansvar, gränssnitt och kontroller, inte bara produkter. För en större statlig myndighet är AI-gateway, modell- och tjänsteregister, RAG-lager, policy enforcement, identitet, behörighet, observability och driftspår centrala delar av målbilden.

Det viktigaste vägvalet är inte om myndigheten ska använda moln, on-premises eller en viss produkt. Det viktigaste är att etablera en arkitektur där juridik, informationsklassning, säkerhet, data och modellåtkomst kan styras tekniskt och följas upp över tid.

Tullverket Aurora väljer därför en referensarkitektur som kombinerar gemensamma kontroller med federerad verksamhetsnära utveckling. Det gör AI-förmågan både styrbar och användbar.
