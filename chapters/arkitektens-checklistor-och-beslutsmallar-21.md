# Kapitel 21: Arkitektens checklistor och beslutsmallar

## Varför detta kapitel finns

En målarkitektur för AI blir bara användbar om den går att omsätta i återkommande beslut. Arkitekten behöver därför mer än en målbild, en referensarkitektur och en roadmap. Arkitekten behöver också praktiska kontrollpunkter som hjälper organisationen att fatta samma typ av beslut på samma sätt över tid.

Det här kapitlet samlar bokens viktigaste checklistor och beslutsmallar. De är avsedda att användas när en myndighet går från idé till genomförande, från pilot till produktion och från enskild lösning till gemensam AI-förmåga. Mallarna ersätter inte juridisk analys, säkerhetsgranskning, dataskyddsbedömning eller arkitekturprövning. De hjälper däremot till att se när sådana analyser behövs, vilka frågor som måste besvaras och vilka beslut som bör dokumenteras.

För Tullverket Aurora fungerar kapitlet som en praktisk arbetslåda. Myndigheten har tagit fram principer, förmågekarta, teknisk referensarkitektur, säkerhetsmönster, plattformsstrategi och roadmap. Nu behöver arkitekturgruppen kunna tillämpa detta konsekvent när nya AI-idéer kommer in.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- använda en minsta gemensam mall för AI-målarkitektur,
- triagera AI-användningsfall innan tekniska lösningar väljs,
- formulera beslutsunderlag för moln, on-premises och hybrid,
- bedöma när RAG, fine-tuning, egen modellservering eller färdig tjänst är rimligt,
- skapa arkitekturbeslut som går att granska och ompröva,
- koppla checklistor till governance, risk, juridik, data, säkerhet och förvaltning,
- använda mallarna som levande styrmedel i stället för engångsdokument.

## Innan vi börjar

Checklistor kan skapa falsk trygghet om de används mekaniskt. En ifylld checklista betyder inte att ett användningsfall är säkert, lagligt eller produktionsklart. Den betyder bara att organisationen har ställt ett antal viktiga frågor.

Det är därför viktigt att skilja mellan tre typer av checklistor:

| Typ | Syfte | Exempel |
|---|---|---|
| Triagechecklista | Sortera ärenden tidigt och hitta rätt process | AI-use-case canvas, juridisk triage, informationsklassning |
| Beslutschecklista | Stödja ett faktiskt arkitekturbeslut | Moln/on-prem-beslut, RAG eller fine-tuning, köpa eller bygga |
| Kontrollchecklista | Säkerställa att lösningen är redo för nästa steg | Produktionsberedskap, säkerhetsgranskning, förvaltningsöverlämning |

I en större myndighet bör dessa checklistor inte leva i separata dokument hos enskilda projekt. De bör ingå i den gemensamma AI-governancen, kopplas till arkitekturforum, återanvändas i portföljstyrningen och sparas som beslutshistorik.

## Målarkitekturens minsta nödvändiga innehåll

En vanlig fallgrop är att målarkitekturen antingen blir för abstrakt eller för detaljerad. Om den bara innehåller visioner och principer ger den inte tillräckligt stöd för lösningsarkitektur. Om den innehåller detaljer för varje enskild implementation blir den snabbt föråldrad.

En användbar AI-målarkitektur bör minst beskriva följande:

| Område | Fråga som ska besvaras | Exempel på innehåll |
|---|---|---|
| Syfte | Varför etableras AI-förmågan? | Verksamhetsnytta, strategiska mål, avgränsningar |
| Omfattning | Vilka typer av AI-användning omfattas? | Generativ AI, analysstöd, beslutsstöd, automation |
| Principer | Vilka vägledande regler styr lösningarna? | Mänsklig kontroll, dataminimering, spårbarhet, återanvändning |
| Riskmodell | Hur klassas användningsfall och data? | Risknivåer, informationsklasser, eskaleringsvägar |
| Förmågor | Vilka organisatoriska och tekniska förmågor behövs? | Governance, dataåtkomst, modellval, test, drift, incidenthantering |
| Byggblock | Vilka gemensamma arkitekturkomponenter behövs? | AI-gateway, RAG-lager, modellplattform, loggning, policy enforcement |
| Driftmodeller | Var får olika lösningar köras? | SaaS, publikt moln, sovereign cloud, privat moln, on-premises |
| Livscykel | Hur hanteras lösningar över tid? | Modellregister, versionering, validering, övervakning, avveckling |
| Organisation | Vem beslutar, äger och förvaltar? | Roller, forum, mandat, ansvarskedjor |
| Roadmap | Hur införs målarkitekturen stegvis? | Sandlåda, piloter, plattform, produktion, skalning |

För Tullverket Aurora innebär detta att målarkitekturen inte bara beskriver en teknisk plattform. Den beskriver också vilka användningsfall som får gå genom vilket arkitekturspår, vilka data som får användas var, vilka beslut som kräver juridisk granskning och vilka byggblock som ska vara gemensamma.

## AI-use-case canvas

AI-use-case canvas är en första strukturerad beskrivning av ett användningsfall. Den ska vara tillräckligt enkel för att verksamheten ska kunna fylla i den tillsammans med arkitekt, informationsägare, säkerhet och juridik.

Syftet är inte att skriva en fullständig kravspecifikation. Syftet är att avgöra om idén är värd att utreda vidare och vilken typ av process den ska gå in i.

| Fält | Fråga | Kommentar |
|---|---|---|
| Namn | Vad kallas användningsfallet? | Undvik produktnamn som titel |
| Verksamhetsproblem | Vilket problem ska lösas? | Beskriv nuläget konkret |
| Användare | Vem använder AI-stödet? | Handläggare, analytiker, chef, medborgare eller system |
| AI-roll | Vad gör AI i processen? | Assistent, kunskapsstöd, beslutsstöd, automation |
| Data | Vilken information används? | Dokument, ärendedata, loggar, register, öppna data |
| Känslighet | Finns personuppgifter, sekretess eller skyddsvärd information? | Markera osäkerhet hellre än att gissa |
| Verksamhetspåverkan | Vad händer om AI ger fel svar? | Låg, medel, hög eller samhällskritisk påverkan |
| Mänsklig kontroll | Vem granskar och ansvarar? | Ska vara tydligt redan tidigt |
| Nytta | Vilken nytta förväntas? | Tid, kvalitet, tillgänglighet, riskreduktion, analysförmåga |
| Mätning | Hur vet vi att lösningen fungerar? | Kvalitetsmått, användning, feltyper, effektmått |
| Föreslagen drift | Var skulle lösningen kunna köras? | SaaS, moln, hybrid eller on-premises |
| Nästa beslut | Vad krävs för att gå vidare? | Juridisk triage, informationsklassning, teknisk förstudie |

### Exempel från Tullverket Aurora

Aurora använder canvasen för ett användningsfall som kallas “regelverksassistent för handläggare”. Verksamhetsproblemet är att handläggare lägger mycket tid på att söka i interna rutiner, föreskrifter och vägledningar. AI-rollen är kunskapsstöd, inte beslutsfattare. Datakällorna är styrdokument och interna handböcker. Känsligheten bedöms initialt som måttlig eftersom dokumenten är interna men inte ska innehålla ärendespecifika personuppgifter.

Canvasen leder inte direkt till tekniskt genomförande. Den leder till tre beslut:

- användningsfallet ska prövas som RAG-baserat kunskapsstöd,
- datakällorna ska kvalitetssäkras och informationsklassas,
- lösningen får inte användas för att fatta beslut i enskilda ärenden utan mänsklig bedömning.

## Triage för juridik, dataskydd och informationssäkerhet

Nästa kontrollpunkt är triage. Den avgör inte hela juridiken, men den identifierar vilka frågor som behöver fördjupas.

En praktisk triage bör ställa minst följande frågor:

| Område | Fråga | Möjlig konsekvens |
|---|---|---|
| Personuppgifter | Behandlas personuppgifter i input, kontext, loggar eller output? | Dataskyddsbedömning, rättslig grund, dataminimering |
| Sekretess | Kan uppgifter omfattas av sekretess eller särskilt skydd? | Begränsad driftmiljö, strikt åtkomst, särskild logghantering |
| Beslutspåverkan | Påverkar AI enskilda personer, företag eller kontrollåtgärder? | Mänsklig kontroll, dokumentation, förklarbarhet, validering |
| Automatisering | Fattar systemet beslut eller initierar åtgärder automatiskt? | Högre krav på rättslig analys och styrning |
| Modellleverantör | Skickas data till extern leverantör eller underbiträde? | Avtalsgranskning, datalokalisering, överföringsanalys |
| Loggning | Sparas promptar, dokumentutdrag eller modellutdata? | Klassning av loggar, gallring, åtkomstkontroll |
| Återanvändning | Kan samma komponent användas av flera användningsfall? | Behov av gemensam plattform och styrmodell |
| Granskning | Går det att i efterhand förstå hur AI-stödet användes? | Krav på spårbarhet och revisionsbarhet |

För Aurora blir triagen avgörande när ett team vill använda samma tekniska lösning för både intern kunskapssökning och sammanfattning av ärendehandlingar. Checklistan visar att användningsfallen inte kan behandlas som samma riskklass. Den första lösningen kan gå via ett kontrollerat kunskapsstödsflöde. Den andra kräver hårdare krav på dataskydd, åtkomst, loggning och mänsklig kontroll.

## Beslutsmatris för moln, on-premises och hybrid

Driftmodell är ett av de mest konsekvensrika besluten i AI-målarkitekturen. Valet bör inte reduceras till en fråga om policy eller preferens. Det bör avgöras av data, risk, funktionella behov, kompetens, ekonomi, leverantörsrisk och krav på förändringstakt.

| Fråga | Moln/SaaS talar för | On-premises talar för | Hybrid talar för |
|---|---|---|---|
| Datakänslighet | Låg eller måttlig känslighet och tydliga avtalsvillkor | Hög känslighet, starka lokaliseringskrav eller särskild skyddsnivå | Data stannar lokalt men vissa AI-funktioner används externt |
| Time-to-market | Snabb pilot och färdiga tjänster behövs | Långsiktig intern kontroll är viktigare än snabbhet | Snabb start men kontrollerad successiv förflyttning |
| Modellutbud | Behov av bred tillgång till aktuella modeller | Begränsat modellbehov eller krav på egen modellkontroll | Olika modelltyper för olika riskklasser |
| Kompetens | Myndigheten vill nyttja leverantörens driftförmåga | Myndigheten har stark intern drift- och plattformskompetens | Intern kompetens byggs upp stegvis |
| Skalbarhet | Belastningen varierar och kräver elastisk kapacitet | Belastningen är förutsägbar eller kräver isolering | Vissa arbetslaster skalar externt, andra hålls lokalt |
| Leverantörsrisk | Accepterad genom avtal, standarder och exitplan | Oacceptabel för centrala användningsfall | Reduceras genom portabilitet och lagerindelning |
| Kostnadsbild | Konsumtionsmodell passar användningsmönstret | Egen kapacitet är mer förutsägbar över tid | Kostnader optimeras per arbetslast |

Beslutet bör dokumenteras som ett arkitekturbeslut, inte som en informell rekommendation. Det bör också omprövas när lagkrav, leverantörsvillkor, dataklassning eller verksamhetsbehov förändras.

### Praktisk tumregel

- Välj inte publikt moln bara för att AI-tjänsterna är starkast där.
- Välj inte on-premises bara för att kontroll känns tryggare.
- Välj inte hybrid utan att definiera var gränserna, integrationerna och ansvaret ligger.

En bra hybridarkitektur är en medveten fördelning av ansvar. En dålig hybridarkitektur är två halva plattformar utan tydligt ägarskap.

## Beslutsmall: RAG, fine-tuning eller egen modellservering

Många AI-diskussioner fastnar i frågan om organisationen ska använda en färdig modell, bygga egen modell, använda RAG eller finjustera. För myndigheter bör frågan börja i användningsfallet och informationshanteringen.

| Val | När det ofta passar | När det ofta inte passar |
|---|---|---|
| Promptning mot färdig modell | Lågkänslig produktivitet, generella uppgifter, tidig utforskning | När svaret måste bygga på myndighetens egna källor eller känsliga data |
| RAG | Kunskapsstöd baserat på dokument, regelverk, handböcker och interna källor | När uppgiften kräver ny modellförmåga snarare än tillgång till rätt kontext |
| Fine-tuning | När modellen behöver lära sig specifikt format, stil, klassificering eller domänmönster | När problemet egentligen är bristande datakvalitet eller källåtkomst |
| Egen modellservering | När kontroll, datalokalitet, isolering eller kostnadsprofil kräver det | När organisationen saknar driftförmåga eller när färdiga tjänster räcker |
| Traditionell ML | Prediktion, klassificering, optimering och mönsterigenkänning med strukturerade data | När uppgiften främst är språkförståelse över ostrukturerad text |
| Regelbaserad automation | Tydliga regler, hög spårbarhet och låg osäkerhet | När processen kräver tolkning, sannolikhetsbedömning eller semantisk förståelse |

För Aurora blir huvudregeln att RAG är förstahandsval för intern kunskapssökning, medan riskanalys i kontrollverksamhet inte automatiskt ska behandlas som ett generativt AI-problem. Där kan traditionell analys, statistiska modeller, regler, grafanalys eller kombinationer vara mer lämpliga beroende på datatyp och beslutspåverkan.

## Beslutsmall: köpa, bygga eller kombinera

Köpa eller bygga är sällan ett binärt val. I AI-arkitektur handlar det ofta om att köpa vissa lager, bygga andra och behålla tydliga abstraktioner mellan dem.

| Lager | Ofta rimligt att köpa | Ofta rimligt att bygga eller anpassa |
|---|---|---|
| Grundmodell | Färdig modell eller modell som tjänst | Egen servering av öppen modell vid särskilda krav |
| AI-assistent | Standardfunktioner för lågkänslig produktivitet | Anpassad assistent för myndighetsspecifika arbetsflöden |
| RAG-ramverk | Grundläggande orkestrering och indexering | Källstyrning, behörighetsfilter, kvalitetssäkring och domänlogik |
| AI-gateway | Produkt eller plattformskomponent | Policyregler, logik för myndighetens riskklasser och routing |
| Observability | Standardverktyg | AI-specifika kvalitetsmått och verksamhetsnära uppföljning |
| Governance | Stödverktyg kan köpas | Mandat, processer, beslut och ansvar måste ägas internt |

Den viktigaste principen är att myndigheten inte ska outsourca sitt ansvar. Även när plattformar, modeller och verktyg köps in måste myndigheten kunna förklara vad lösningen gör, vilka data som används, vilka risker som finns och vem som ansvarar för användningen.

## Produktionsberedskap för AI-lösningar

Innan en AI-lösning går från pilot till produktion bör den granskas mot en produktionschecklista. Checklistan bör vara gemensam för myndigheten men kunna skalas efter risknivå.

| Område | Kontrollfråga |
|---|---|
| Ägarskap | Finns verksamhetsägare, systemägare, informationsägare och modellägare? |
| Användningsgränser | Är det tydligt vad AI-lösningen får och inte får användas till? |
| Data | Är datakällor, åtkomst, kvalitet, retention och gallring hanterade? |
| Juridik | Är nödvändiga juridiska bedömningar dokumenterade? |
| Informationssäkerhet | Är skyddsnivå, behörighet, loggning och incidenthantering godkända? |
| Modell | Är modell, version, leverantör, konfiguration och beroenden dokumenterade? |
| Test | Har lösningen testats med relevanta fall, feltyper och gränsfall? |
| Mänsklig kontroll | Vet användaren när AI kan lita på, när den ska granskas och när den inte får användas? |
| Övervakning | Finns mätning av kvalitet, drift, säkerhet och användning? |
| Support | Finns rutiner för felrapportering, användarstöd och förbättring? |
| Avveckling | Finns plan för att pausa, ersätta eller stänga lösningen? |

För Aurora blir produktionsberedskap särskilt viktig när regelverksassistenten ska gå från kontrollerad pilot till bred användning. Arkitekturgruppen kräver då att varje källa i kunskapsbasen har ägare, att användarna ser källhänvisningar, att loggar klassas korrekt och att lösningen har tydliga varningar om att den inte fattar beslut.

## Mall för arkitekturbeslut

Ett arkitekturbeslut behöver inte vara långt, men det måste vara spårbart. Det ska visa varför beslutet fattades, vilka alternativ som övervägdes och vilka konsekvenser beslutet får.

En enkel mall kan se ut så här:

| Fält | Innehåll |
|---|---|
| Besluts-ID | Exempel: ADR-AI-014 |
| Titel | Kort beskrivning av beslutet |
| Status | Föreslaget, beslutat, ersatt eller omprövas |
| Datum | När beslutet fattades |
| Beslutsägare | Forum eller roll med mandat |
| Kontext | Vilket problem beslutet löser |
| Alternativ | Vilka realistiska alternativ som övervägdes |
| Beslut | Vad organisationen väljer |
| Motiv | Varför detta alternativ väljs |
| Konsekvenser | Positiva och negativa följder |
| Risker | Kvarstående risker och begränsningar |
| Giltighet | Vilka användningsfall eller riskklasser beslutet gäller |
| Omprövning | När eller vid vilka händelser beslutet ska ses över |

### Exempel på arkitekturbeslut för Aurora

**ADR-AI-014: Gemensam AI-gateway för generativa AI-anrop**

Aurora beslutar att alla generativa AI-anrop från myndighetens interna applikationer ska gå via en gemensam AI-gateway. Alternativen var direktintegration från varje applikation, separat gateway per verksamhetsområde eller gemensam gateway.

Beslutet motiveras av behovet av konsekvent loggning, policy enforcement, modellrouting, kostnadskontroll och möjlighet att byta leverantör. Konsekvensen är att teamen får en gemensam integrationspunkt men också måste följa gemensamma krav på metadata, användningsklass och loggning.

Beslutet gäller initialt interna kunskapsstöd och administrativa AI-funktioner. Det ska omprövas när lösningar för högre riskklass och mer verksamhetskritiska flöden införs.

## Checklista för leverantörsdialog och upphandling

AI-upphandling kräver att myndigheten kravställer mer än funktion. Den behöver också kravställa datahantering, modellvillkor, transparens, drift, säkerhet, exit och förändringshantering.

| Frågeområde | Exempel på fråga |
|---|---|
| Dataanvändning | Används myndighetens data för träning, förbättring eller utvärdering av leverantörens modeller? |
| Datalokalitet | Var behandlas och lagras data, loggar, metadata och supportärenden? |
| Underleverantörer | Vilka underbiträden eller tekniska leverantörer används? |
| Modelländringar | Hur informeras myndigheten om modellbyten eller större förändringar? |
| Transparens | Vilken dokumentation finns om modell, säkerhet, begränsningar och testning? |
| Loggar | Vilka loggar skapas, vem äger dem och hur länge sparas de? |
| Revision | Vilka granskningsmöjligheter har myndigheten? |
| Exit | Hur kan data, konfiguration, promptar, index och historik flyttas eller raderas? |
| Incidenter | Hur rapporteras säkerhetsincidenter och modellrelaterade fel? |
| Kostnad | Hur följs konsumtion, modellkostnad, lagring och indirekta kostnader upp? |
| Ansvar | Vilket ansvar ligger hos leverantören och vilket ligger kvar hos myndigheten? |

För Aurora används checklistan både före upphandling och vid granskning av befintliga avtal. Det visar sig att vissa molnbaserade AI-funktioner tekniskt sett går att aktivera snabbt, men att avtalsvillkor, logghantering och dataanvändning måste utredas innan de kan användas i bred myndighetsmiljö.

## Checklista för förvaltning och kontinuerlig förbättring

AI-förmåga är inte färdig när första lösningen går i produktion. Modeller förändras, datakällor ändras, användarbeteenden utvecklas, hotbilden förändras och regelverken mognar. Förvaltningen måste därför vara aktiv.

| Område | Återkommande kontroll |
|---|---|
| Modellversioner | Vilka modeller används och har någon version ändrats? |
| Kvalitet | Har träffsäkerhet, användarnöjdhet eller feltyper förändrats? |
| Datakällor | Har källor uppdaterats, flyttats, avpublicerats eller fått ny ägare? |
| Behörighet | Har åtkomsträttigheter och rollmodeller förändrats? |
| Loggar | Granskas loggar för felanvändning, kvalitet och incidentindikatorer? |
| Kostnad | Har konsumtion och kostnad utvecklats enligt förväntan? |
| Risk | Har användningsfallet fått ny verksamhetspåverkan eller ny målgrupp? |
| Leverantör | Har villkor, underleverantörer eller modellbeteende ändrats? |
| Säkerhet | Har nya hot, sårbarheter eller attackmönster identifierats? |
| Avveckling | Finns lösningar som bör pausas, ersättas eller stängas? |

För Aurora placeras denna checklista i den ordinarie förvaltningsmodellen. AI-lösningar får inte bli sidoprojekt utan ägare. Varje produktionssatt AI-lösning ska ha en förvaltningsplan, en mätmodell och en definierad eskaleringsväg.

## Så används mallarna i rätt ordning

Alla mallar ska inte användas samtidigt. De bör följa livscykeln.

| Fas | Primär mall | Resultat |
|---|---|---|
| Idé | AI-use-case canvas | Första beskrivning och preliminär nytta |
| Triage | Juridik, dataskydd och informationssäkerhet | Rätt process och risknivå |
| Förstudie | Driftmodell och teknikvägval | Rekommenderad arkitekturansats |
| Arkitekturbeslut | ADR-mall | Spårbart beslut |
| Pilot | Produktionsberedskap i lätt version | Kontrollerad test med tydliga gränser |
| Produktion | Full produktionschecklista | Godkänd lösning med ägarskap och kontroller |
| Förvaltning | Kontinuerlig förbättring | Stabil drift, uppföljning och omprövning |

Denna ordning är viktig. Om myndigheten börjar med produktionschecklistan redan vid idéstadiet blir processen tung och byråkratisk. Om den väntar med triage till efter teknisk implementation blir risken att lösningen byggs på fel antaganden.

## Vanliga misstag

- **Misstag: Att använda checklistorna som ersättning för ansvar.**
  - Varför det händer: Organisationen vill ha ett enkelt godkännande.
  - Hur du undviker det: Koppla varje checklista till en ansvarig roll och ett beslutsforum.

- **Misstag: Att fylla i mallar efter att beslutet redan är fattat.**
  - Varför det händer: Dokumentation ses som efterarbete.
  - Hur du undviker det: Kräv att centrala frågor besvaras före arkitekturforum eller styrgrupp.

- **Misstag: Att ha en mall per projekt.**
  - Varför det händer: Varje team optimerar för sin egen leverans.
  - Hur du undviker det: Skapa gemensamma mallar som förvaltas av AI-governance och arkitekturforum.

- **Misstag: Att göra checklistorna för detaljerade för tidigt.**
  - Varför det händer: Organisationen försöker minska osäkerhet genom att fråga allt.
  - Hur du undviker det: Använd lätt triage tidigt och fördjupning först när risken motiverar det.

- **Misstag: Att inte ompröva beslut.**
  - Varför det händer: Arkitekturbeslut behandlas som permanenta.
  - Hur du undviker det: Sätt omprövningspunkt i varje viktigt AI-relaterat beslut.

## Vägvalsfrågor

- Vilka checklistor ska vara obligatoriska inför pilot, produktion och upphandling?
- Vilka mallar ska ägas av arkitektur, juridik, informationssäkerhet respektive verksamhet?
- Hur mycket dokumentation krävs för olika risknivåer?
- Hur säkerställs att mallarna används som beslutsstöd och inte som administrativt efterarbete?

## Vanliga fallgropar

- Att skapa mallar som är för omfattande för att användas i verkliga beslut.
- Att låta varje funktion skapa egna checklistor utan gemensam begreppsmodell.
- Att sakna tydlig koppling mellan checklista, arkitekturprincip och beslutspunkt.
- Att inte uppdatera mallarna när lagstiftning, plattformar eller interna arbetssätt förändras.

## Checklista

Innan bokens målarkitektur går från dokument till styrande arbetssätt bör arkitekten kunna svara ja på följande:

- Finns en gemensam mall för att beskriva AI-användningsfall?
- Finns triage för juridik, dataskydd och informationssäkerhet?
- Finns en beslutsmodell för moln, on-premises och hybrid?
- Finns en mall för arkitekturbeslut som används i praktiken?
- Finns en produktionschecklista för AI-lösningar?
- Finns en förvaltningschecklista för modell, data, loggning, kvalitet och kostnad?
- Är checklistorna kopplade till tydliga roller och forum?
- Är checklistorna anpassade efter risknivå så att enkla användningsfall inte överbelastas?
- Sparas beslut och underlag så att de kan granskas och återanvändas?
- Finns en process för att uppdatera checklistorna när regelverk, teknik eller hotbild förändras?

## Koppling till målarkitekturen

Det här kapitlet gör målarkitekturen operativ. Tidigare kapitel har beskrivit principer, risk, data, tekniska byggblock, plattformar, säkerhet, upphandling och roadmap. Checklistorna binder ihop dessa delar i ett praktiskt arbetssätt.

För Tullverket Aurora innebär det att målarkitekturen inte bara blir en presentation eller ett styrdokument. Den blir en uppsättning återkommande beslutspunkter:

- varje AI-idé beskrivs med samma canvas,
- varje känsligt användningsfall triageras tidigt,
- varje större vägval dokumenteras som ADR,
- varje lösning måste klara rätt produktionsberedskap,
- varje produktionssatt lösning får aktiv förvaltning,
- varje checklistemall ägs och förbättras över tid.

Det är först när målarkitekturen används på detta sätt som den blir en faktisk förmåga.

## Snabb sammanfattning

- Checklistor och beslutsmallar gör målarkitekturen praktiskt användbar.
- De ska användas som stöd för ansvar, inte som ersättning för ansvar.
- AI-use-case canvas hjälper myndigheten att beskriva användningsfall innan teknik väljs.
- Juridisk, dataskydds- och säkerhetstriage avgör vilken process ett användningsfall ska följa.
- Driftmodell, RAG-val, köpa/bygga och produktionsberedskap bör dokumenteras som arkitekturbeslut.
- Produktionssatta AI-lösningar kräver aktiv förvaltning eftersom modeller, data, risker och leverantörsvillkor förändras.
- Mallarna bör förvaltas gemensamt av AI-governance och arkitekturforum.
- Den bästa checklistan är inte den längsta, utan den som leder till rätt beslut vid rätt tidpunkt.

## Nästa steg

Efter detta kapitel finns ett komplett första manusutkast för bokens planerade huvudkapitel. Nästa naturliga steg är att granska helheten: kontrollera progression, jämna ut terminologi, säkerställa att Tullverket Aurora används konsekvent och därefter förbereda export till EPUB eller PDF.
