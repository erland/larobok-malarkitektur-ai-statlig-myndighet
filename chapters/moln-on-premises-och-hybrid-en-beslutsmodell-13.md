# Kapitel 13: Moln, on-premises och hybrid: en beslutsmodell

## Varför detta kapitel finns

När en myndighet ska etablera AI-förmåga uppstår nästan alltid frågan om driftmodell tidigt. Ska AI-tjänsterna köras i publikt moln, i en europeisk eller nationellt reglerad molnmiljö, i myndighetens egen infrastruktur, i privat moln, i en upphandlad driftmiljö eller i någon form av hybridarkitektur?

Frågan är viktig, men den ställs ofta för tidigt och för binärt. Diskussionen blir lätt en ideologisk konflikt mellan moln och on-premises, i stället för en arkitekturbedömning av användningsfall, information, rättsliga krav, säkerhetskrav, kompetens, kostnad, livscykel, integrationsbehov och operativ risk.

Detta kapitel ger en beslutsmodell för moln, on-premises och hybrid i AI-målarkitektur. Syftet är inte att ge ett universellt svar, utan att hjälpa arkitekten att göra samma typ av vägval på ett konsekvent, spårbart och riskbaserat sätt.

Kapitlet bygger vidare på kapitel 5 om informationsklassning, kapitel 10 om teknisk referensarkitektur och kapitel 12 om livscykelhantering. I de tidigare kapitlen etablerades att AI-lösningar inte bör klassas enbart efter teknik, utan efter användningsfall, data, risk, ansvar och förvaltningsbarhet. Samma princip gäller driftmodellen.

## Arkitekturproblemet

Tullverket Aurora har nu tre tydliga AI-spår:

- ett produktivitetsstöd för lågklassade arbetsuppgifter,
- ett internt RAG-baserat kunskapsstöd för styrdokument och handböcker,
- ett mer känsligt analys- och prioriteringsstöd för kontrollverksamhet.

De tre spåren har olika krav. Produktivitetsstödet behöver snabb tillgång till moderna generativa modeller, enkel användning och låg tröskel. Kunskapsstödet behöver styrda källor, behörighetsmedveten retrieval, källhänvisningar, loggning och stabil förvaltning. Analys- och prioriteringsstödet behöver starkare kontroll, tydligare dokumentation, striktare åtkomst och mer noggrann validering.

Auroras ledning ställer en till synes enkel fråga:

> Ska vår AI-plattform ligga i molnet eller i vår egen miljö?

Arkitekturgruppen inser snabbt att frågan inte kan besvaras på den nivån. Det finns inte en driftmodell för all AI. Det finns flera AI-tjänster, flera informationsklasser, flera risknivåer och flera livscykler. Vissa delar kan med fördel nyttja molntjänster. Andra delar kan behöva köras i en mer kontrollerad miljö. Ytterligare delar bör kanske börja i en isolerad sandlåda och flyttas när kraven är tydligare.

Rätt arkitekturfråga blir därför:

> Vilka AI-förmågor får använda vilken driftmodell, under vilka villkor, med vilka kontroller och med vilken exitväg?

## Centrala begrepp

### Publikt moln

Publikt moln innebär att myndigheten använder infrastruktur, plattformar eller tjänster som tillhandahålls av en extern molnleverantör och delas mellan många kunder genom teknisk separation. Det kan handla om infrastruktur som tjänst, plattformstjänster, databaser, AI-API:er, modellplattformar, utvecklingsmiljöer eller färdiga AI-tjänster.

För AI är publikt moln ofta attraktivt eftersom det ger snabb tillgång till kraftfull beräkning, moderna modeller, färdiga tjänster, skalning, säkerhetsfunktioner och integrationsmöjligheter. Samtidigt kräver det noggrann prövning av data, rättsliga förutsättningar, leverantörsvillkor, datalokalisering, underbiträden, loggning, incidenthantering och möjligheten att byta leverantör.

### SaaS, PaaS och IaaS

SaaS, software as a service, innebär att myndigheten använder en färdig applikation eller tjänst. För AI kan det vara en färdig AI-assistent, ett dokumentanalysverktyg eller ett verksamhetssystem med inbyggd AI.

PaaS, platform as a service, innebär att myndigheten använder en plattform för att bygga egna lösningar. För AI kan det vara modell-API:er, träningsmiljöer, vektordatabaser, MLOps-tjänster eller managed Kubernetes.

IaaS, infrastructure as a service, innebär att myndigheten hyr grundläggande infrastruktur, exempelvis virtuella maskiner, nätverk och lagring. För AI kan IaaS användas för att bygga mer egenkontrollerade AI-plattformar i molnet.

Skillnaden är viktig eftersom ansvarsfördelningen förändras. Ju mer färdig tjänst myndigheten använder, desto snabbare kan nyttan komma, men desto mer måste myndigheten lita på leverantörens tjänstedesign, villkor, kontroller och förändringstakt.

### Sovereign cloud och reglerad molnmiljö

Sovereign cloud används här som samlingsbegrepp för molnerbjudanden som försöker möta särskilda krav på datalokalisering, jurisdiktion, kontroll, drift, åtkomst, kryptering eller separation. Begreppet är inte entydigt. Det måste alltid konkretiseras i krav: var lagras data, vem kan administrera miljön, vilka underleverantörer används, vilka rättsliga förpliktelser gäller, hur hanteras supportåtkomst och vilka tekniska kontroller kan myndigheten själv verifiera?

För en svensk statlig myndighet bör sovereign cloud inte behandlas som en magisk etikett. Det är ett möjligt svar på vissa krav, men det ersätter inte informationsklassning, rättslig prövning, säkerhetsanalys, avtalsgranskning och arkitekturbeslut.

### On-premises

On-premises innebär att lösningen körs i myndighetens egen eller särskilt kontrollerade infrastruktur. Det kan vara fysiska servrar i egna datacenter, en intern virtualiseringsplattform, intern Kubernetes, GPU-kluster eller en myndighetskontrollerad privat molnplattform.

On-premises ger större teknisk kontroll över driftmiljö, nätverk, åtkomst, dataflöden och loggning. Det kan vara nödvändigt för vissa informationsklasser, vissa säkerhetskrav eller vissa regulatoriska bedömningar. Samtidigt innebär det större ansvar för kapacitet, kompetens, uppdatering, modellservering, säkerhetshärdning, observability, kostnadskontroll och livscykel.

### Privat moln

Privat moln är en molnliknande plattform som används av en organisation eller en avgränsad grupp organisationer. Den kan drivas av myndigheten själv eller av en leverantör. Det centrala är inte vem som äger hårdvaran, utan vilka kontroll-, separations-, automatiserings- och självbetjäningsförmågor plattformen ger.

För AI kan privat moln vara relevant när myndigheten vill kombinera molnliknande arbetssätt med högre kontroll över data, nätverk och drift. Men privat moln löser inte automatiskt brist på MLOps, modellregister, GPU-kapacitet, säkerhetsprocesser eller produktteam.

### Hybridarkitektur

Hybridarkitektur innebär att olika delar av AI-förmågan körs i olika miljöer och binds samman genom styrda gränssnitt, identitet, nätverk, policy, loggning och förvaltning. Hybrid kan betyda att en AI-gateway ligger centralt, att vissa modeller anropas via externa API:er, att vissa RAG-index finns internt och att vissa analysmodeller körs on-premises.

Hybrid är ofta den realistiska målbilden för större myndigheter, men den är också den mest krävande. Den kräver tydliga arkitekturgränser, ansvarsfördelning, datakontrakt, loggning, identitet, nätverkskontroller, releaseprocesser och incidenthantering över miljögränser.

### Edge och avskild miljö

Edge eller avskild miljö innebär att AI-komponenten körs nära datakällan, nära användaren eller i en miljö med begränsad eller ingen extern uppkoppling. För myndigheter kan det vara relevant vid höga tillgänglighetskrav, skyddsvärda informationsflöden, operativa miljöer eller situationer där data inte bör lämna en viss säkerhetszon.

För generativ AI är edge inte alltid realistiskt på kort sikt, särskilt inte för mycket stora modeller, men mindre språkmodeller, klassificeringsmodeller, embeddings och specialiserade analysmodeller kan ibland köras i mer avskilda miljöer.

## Beslutsmodellens grundprincip

Driftmodell ska inte väljas utifrån teknikpreferens. Den ska väljas utifrån en kombination av sex frågor:

1. Vilket användningsfall ska stödjas?
2. Vilken information behandlas?
3. Vilken AI-roll har lösningen?
4. Vilka rättsliga och säkerhetsmässiga krav gäller?
5. Vilken operativ förmåga har myndigheten själv?
6. Vilken förändringstakt kräver lösningen?

Dessa frågor behöver besvaras tillsammans. Ett lågklassat produktivitetsstöd kan vara olämpligt on-premises om det gör lösningen dyr, långsam och tekniskt sämre utan att riskerna minskar nämnvärt. Ett ärendenära stöd med sekretesskänsliga data kan vara olämpligt som SaaS om myndigheten inte kan styra dataflöden, loggning, modellträning, supportåtkomst och underbiträden. Ett RAG-baserat kunskapsstöd kan däremot mycket väl bli hybrid: styrda dokumentkällor och index i en kontrollerad miljö, modellåtkomst via en godkänd AI-gateway och vissa komponenter som managed services.

Beslutsmodellen ska därför resultera i tillåtna arkitekturspår, inte i ett enda plattformsbeslut.

Moln, on-premises och hybrid ska inte rangordnas generellt. De ska väljas utifrån informationsklassning, rättslig bedömning, säkerhetskrav, operativ kontroll, kompetens och förmåga att hantera livscykeln. Offentlig sektor kan behöva molntjänster för effektiv digitalisering, men användningen måste vara säker, rättssäker och konkret prövad mot rollfördelning, åtkomst, personuppgiftsbiträden och eventuell åtkomst från tredje land.

## Steg 1: Utgå från användningsfall och AI-roll

Det första steget är att bestämma vad AI-lösningen faktiskt gör. Driftmodell kan inte väljas utan att förstå AI-rollen.

En praktisk indelning är:

- produktivitetsstöd,
- kunskapsstöd,
- ärendenära stöd,
- beslutsnära stöd,
- automatiserande stöd,
- modellutveckling och analysmiljö.

Produktivitetsstöd kan ofta använda mer standardiserade tjänster om informationen är lågklassad och policykontrollerna är tydliga. Kunskapsstöd kräver ofta mer styrda källor och behörighetsmedveten retrieval. Ärendenära stöd kräver starkare dataskydd, spårbarhet och loggning. Beslutsnära stöd kräver särskild kontroll, dokumentation, validering och mänsklig granskning. Automatiserande stöd kräver ofta ännu striktare begränsning av åtgärder, behörigheter och rollback. Modellutveckling och analysmiljöer behöver egna krav på dataåtkomst, experimentkontroll och reproducerbarhet.

Tullverket Aurora använder därför inte driftmodell som första klassificering. De klassificerar först användningsfallets AI-roll. Först därefter bedömer de vilka driftmodeller som kan vara tillåtna.

## Steg 2: Klassificera informationen som flöde, inte som etikett

Ett vanligt misstag är att säga att ett användningsfall behandlar en viss informationsklass och sedan välja driftmodell utifrån den etiketten. För AI räcker det inte. Informationen rör sig genom flera steg:

- användarens fråga eller prompt,
- hämtade källor,
- mellanliggande kontext,
- embeddings,
- modellens svar,
- loggar,
- utvärderingsdata,
- tränings- eller finjusteringsdata,
- support- och felsökningsdata,
- telemetry och kostnadsdata.

Varje steg kan ha olika skyddsvärde. En lågklassad fråga kan tillsammans med hämtade källor bli skyddsvärd. En logg kan bli känslig om den innehåller promptar, källutdrag eller personuppgifter. Embeddings kan vara svåra att tolka för människor men ändå representera information från skyddsvärda dokument. Ett felaktigt modellutdata kan skapa verksamhetsrisk även om indatat inte var särskilt känsligt.

För driftmodell innebär detta att arkitekten behöver rita informationsflödet innan valet görs. Molnfrågan gäller inte bara var modellen körs. Den gäller även var promptar, index, loggar, nycklar, källor, metadata och utvärderingsdata hamnar.

Tullverket Aurora gör därför en informationsflödeskarta för varje prioriterat AI-spår. Kartan visar vilka data som skapas, var de lagras, vilka externa tjänster som anropas, vilka loggar som genereras och vilka administratörer som kan komma åt informationen.

## Steg 3: Bedöm rättsliga och avtalsmässiga villkor

Rättslig prövning ska inte ske efter att driftmodellen redan är vald. Den ska vara en del av valet.

För AI-drift behöver myndigheten åtminstone bedöma:

- personuppgiftsbehandling,
- sekretess och skyddsvärda uppgifter,
- rättslig grund och ändamål,
- överföring eller åtkomst från andra jurisdiktioner,
- personuppgiftsbiträden och underbiträden,
- leverantörens användning av kunddata,
- supportåtkomst och driftadministration,
- loggning och felsökning,
- lagringstid och radering,
- möjlighet till revision och insyn,
- avtalsvillkor för modellförändringar,
- ansvar vid felaktigt eller skadligt utdata.

Det räcker inte att fråga om data används för träning. Den frågan är viktig, men för smal. Även om leverantören inte tränar på kunddata kan data behandlas i promptar, loggar, säkerhetsfilter, supportverktyg, telemetry, incidenthantering eller underliggande driftmiljöer.

För Tullverket Aurora blir detta särskilt viktigt när de jämför en färdig AI-assistent med ett eget RAG-baserat kunskapsstöd. Den färdiga assistenten kan vara lämplig för lågklassade produktivitetsuppgifter, men inte nödvändigtvis för ärendenära data. Det egna kunskapsstödet kräver mer arbete, men ger bättre kontroll över källor, åtkomst och loggning.

## Steg 4: Bedöm säkerhetsarkitektur och kontrollbehov

Driftmodellvalet måste stödja den säkerhetsarkitektur som användningsfallet kräver. Några centrala frågor är:

- Kan identitet och behörighet integreras med myndighetens IAM?
- Kan åtkomst styras på roll, informationsklass och användningsfall?
- Kan nätverkstrafik begränsas och övervakas?
- Kan data krypteras med nyckelhantering som myndigheten accepterar?
- Kan administratörsåtkomst kontrolleras och loggas?
- Kan loggar skickas till myndighetens säkerhetsövervakning?
- Kan policyregler verkställas tekniskt?
- Kan lösningen isoleras från andra informationsklasser?
- Kan incidenter upptäckas och hanteras i myndighetens processer?
- Kan leverantörsändringar följas upp och riskbedömas?

Publika molntjänster kan ha mycket starka säkerhetsförmågor, men det betyder inte automatiskt att de passar alla informationsflöden. Interna miljöer kan ge hög kontroll, men det betyder inte automatiskt att de är säkra om de saknar härdning, patchning, övervakning, separation och incidentförmåga.

En mogen beslutsmodell jämför faktisk kontrollförmåga, inte känslan av kontroll.

## Steg 5: Bedöm kapacitet, kompetens och livscykel

AI kräver ofta särskild infrastrukturkompetens. Om myndigheten väljer on-premises behöver den kunna hantera:

- GPU- eller acceleratorresurser,
- kapacitetsplanering,
- modellservering,
- driftsäkerhet,
- skalning,
- patchning,
- säkerhetsuppdateringar,
- modelloptimering,
- containerplattformar,
- observability,
- kostnadsuppföljning,
- livscykel för hårdvara och modeller.

Det är lätt att underskatta detta. En on-premises-lösning kan ge större kontroll över data, men samtidigt skapa långsam förändringstakt, resursbrist och teknisk skuld om organisationen saknar rätt kompetens och finansieringsmodell.

Molntjänster kan minska behovet av egen infrastrukturdrift och ge snabbare tillgång till nya modeller, men de skapar andra krav: leverantörsstyrning, kostnadskontroll, arkitekturell inlåsning, avtalsuppföljning, kontinuerlig riskbedömning och förståelse för leverantörens förändringstakt.

Hybrid kräver båda kompetenserna. Det är därför hybrid inte ska väljas för att skjuta upp beslut. Hybrid ska väljas när olika användningsfall faktiskt behöver olika driftmodeller och myndigheten är beredd att förvalta integrationerna mellan dem.

## Steg 6: Bedöm förändringstakt och innovationsbehov

AI-marknaden förändras snabbt. Nya modeller, modellversioner, säkerhetsfunktioner, API:er, kostnadsmodeller och verktyg introduceras löpande. Driftmodellen påverkar hur snabbt myndigheten kan dra nytta av detta.

Publika moln och färdiga AI-tjänster ger ofta snabb tillgång till nya funktioner. Det kan vara avgörande för produktivitetsstöd, prototyper, utvärdering och mindre riskfyllda användningsfall. On-premises ger mer kontroll men ofta långsammare tillgång till de senaste modellerna och större krav på egen optimering. Hybrid kan ge både snabbhet och kontroll om gränserna är rätt dragna.

För Tullverket Aurora innebär detta att målarkitekturen inte får låsa fast hela myndigheten vid en enda modell eller en enda driftmiljö. Den behöver en AI-gateway och ett modellregister som gör det möjligt att byta eller komplettera modellendpoints utan att varje applikation byggs om.

## Beslutsmatris för driftmodell

Följande matris är inte ett facit, men den hjälper arkitekten att strukturera vägvalet.

| Situation | Moln kan vara lämpligt när | On-premises kan vara lämpligt när | Hybrid kan vara lämpligt när |
|---|---|---|---|
| Produktivitetsstöd | Informationen är lågklassad, tjänsten är godkänd och policy kan verkställas | Myndigheten har särskilda krav på isolering eller saknar godkänt molnalternativ | Standardiserad assistent används för låg risk medan känsligare flöden hålls separata |
| Internt kunskapsstöd | Källor och promptar kan hanteras inom godkänd molnzon och åtkomst/loggning är styrd | Källorna är skyddsvärda eller kräver intern indexering och strikt kontroll | Index och källor finns internt medan modellåtkomst sker via kontrollerad gateway |
| Ärendenära stöd | Endast om dataskydd, sekretess, loggning och leverantörsvillkor är godkända | Ärendedata är känsliga och bör hållas i starkt kontrollerad miljö | Ärendedata stannar internt medan vissa modellfunktioner används externt med maskerad eller minimerad kontext |
| Beslutsnära stöd | Endast vid låg informationsrisk och stark dokumentation, validering och kontroll | Hög konsekvens, känsliga data eller krav på strikt reproducerbarhet | Modellutveckling eller stödkomponenter kan vara externa, men beslutsnära körning sker kontrollerat |
| Modellutveckling | Molnet ger skalbar beräkning, experimentmiljö och färdiga MLOps-tjänster | Träningsdata får inte lämna kontrollerad miljö eller kräver särskild isolering | Anonymiserade eller syntetiska data används i moln medan skarpa data och validering sker internt |
| RAG-index | Managed services ger snabb etablering och driftfördelar | Indexet representerar skyddsvärda dokument eller kräver intern åtkomstkontroll | Källsystem och index separeras, och endast minimerad kontext skickas till modell |

Matrisen bör anpassas till myndighetens egna informationsklasser, regelverk och tekniska miljö. Den viktiga poängen är att driftmodell väljs per arkitekturspår, inte per bokstavlig teknikkomponent.

## Rekommenderade arkitekturspår

För en större statlig myndighet är det ofta bättre att definiera ett antal godkända arkitekturspår än att fatta varje driftbeslut från början.

Tullverket Aurora inför fyra arkitekturspår.

### Spår A: Kontrollerad SaaS för lågklassat produktivitetsstöd

Detta spår används för generella arbetsuppgifter med låg informationsrisk, till exempel språkstöd, strukturering av egna anteckningar, idéutkast och sammanfattning av öppet eller lågklassat material.

Krav i spåret:

- tydlig användarpolicy,
- godkända tjänstevillkor,
- spärr mot känsliga data,
- central identitet och åtkomststyrning,
- loggning på lämplig nivå,
- kostnadskontroll,
- utbildning och användarstöd,
- incidentväg vid felaktig användning.

Spåret ska inte användas för sekretessbelagda ärenden, beslutsnära rekommendationer eller känsliga personuppgifter utan särskilt beslut.

### Spår B: Molnbaserad AI-plattform för kontrollerade piloter

Detta spår används för utveckling, test och piloter där molnets utvecklingshastighet, modellutbud och plattformstjänster ger tydlig nytta. Det kan omfatta modell-API:er, vektordatabaser, orkestrering, testverktyg och MLOps-tjänster.

Krav i spåret:

- användningsfall ska vara triagerade,
- data ska vara godkända för miljön,
- personuppgifts- och sekretessbedömning ska vara genomförd,
- miljön ska ha tydlig separation mellan experiment och produktion,
- modell- och tjänsteanrop ska gå via kontrollerade gränssnitt,
- kostnad och användning ska följas upp,
- piloter ska ha exitbeslut: avbryt, skala, bygg om eller flytta.

Spåret är särskilt användbart när myndigheten behöver lära snabbt men ändå behålla styrning.

### Spår C: Hybrid RAG för styrt kunskapsstöd

Detta spår används när myndigheten vill kombinera styrda interna källor med moderna språkmodeller. Källsystem, dokumentpublicering, metadata och ibland vektorindex hanteras i kontrollerad miljö. Modellanrop kan ske via en godkänd modellendpoint, intern eller extern, beroende på informationsklass och risk.

Krav i spåret:

- källor ska ha informationsägare,
- dokument ska vara versionerade och klassade,
- retrieval ska vara behörighetsmedveten,
- promptar och konfigurationer ska vara versionerade,
- modellåtkomst ska gå via AI-gateway,
- loggning ska stödja spårbarhet utan att skapa onödig dataskyddsrisk,
- svar ska ha källhänvisningar,
- produktteam ska ansvara för kvalitet och förvaltning.

Detta blir Auroras huvudspår för det interna kunskapsstödet.

### Spår D: Kontrollerad intern eller privat miljö för känsliga och beslutsnära flöden

Detta spår används för användningsfall med högre krav på kontroll, exempelvis ärendenära sammanfattning, känslig analys, prioriteringsstöd eller modeller som påverkar verksamhetsbeslut.

Krav i spåret:

- strikt informationsklassning,
- dokumenterad rättslig bedömning,
- tydlig mänsklig kontroll,
- stark åtkomststyrning,
- separata miljöer för utveckling, test och produktion,
- modell- och data lineage,
- valideringsprocess,
- incidenthantering,
- revisionsbarhet,
- formella arkitekturbeslut för modell, data, drift och integration.

Spåret kan använda on-premises, privat moln eller särskilt reglerad drift. Det viktiga är inte etiketten, utan att kontrollkraven faktiskt uppfylls.

Målarkitekturen bör därför beskriva flera tillåtna driftspår i stället för ett enda standardsvar. Varje spår bör ange datalokalisering, åtkomstmodell, loggning, revision, kryptering, driftansvar, incidenthantering och vilka informationsklasser och användningsfall spåret är avsett för.

## Moln som förstahandsval när snabbhet och modellutbud styr

Moln bör övervägas när myndigheten behöver snabb tillgång till moderna modeller, skalbar beräkning, färdiga AI-tjänster eller managed services som annars skulle ta lång tid att bygga.

Det kan vara särskilt relevant för:

- lågklassat produktivitetsstöd,
- kontrollerade sandlådor,
- tidiga piloter,
- modellutvärdering,
- utvecklingsmiljöer,
- syntetiska eller anonymiserade dataset,
- vissa RAG-komponenter,
- MLOps-verktyg,
- analys där data är godkända för miljön.

Molnets styrka är inte bara kapacitet. Det är också ekosystem, standardiserade säkerhetsfunktioner, automatisering, globalt modellutbud, hög förändringstakt och möjlighet att snabbt testa flera alternativ.

Men moln bör inte väljas enbart för att det är modernt. För myndigheter måste molnvalet stödjas av styrda landningszoner, tydlig identitet, nätverkskontroller, loggning, avtal, dataskydd, kostnadsstyrning och exitstrategi.

## On-premises när kontrollbehovet väger tyngre än snabbheten

On-premises eller starkt kontrollerad privat drift bör övervägas när information, verksamhetsrisk eller rättsliga krav gör extern behandling olämplig eller svår att motivera.

Det kan vara relevant för:

- känsliga ärendedata,
- sekretessbelagda dokument,
- beslutsnära analys,
- höga krav på reproducerbarhet,
- avskilda säkerhetszoner,
- modeller som behöver köras nära datakällan,
- miljöer där extern åtkomst är oacceptabel,
- användningsfall där incidentkonsekvenserna är höga.

On-premises ska dock inte ses som gratis kontroll. Kontroll måste realiseras genom arkitektur och driftförmåga. Om myndigheten inte kan patcha, övervaka, skala, testa, dokumentera, säkra och förvalta AI-plattformen kan en intern lösning bli mindre säker och mindre styrbar än ett välkontrollerat molnalternativ.

För Tullverket Aurora blir on-premises aktuellt för de mest känsliga analys- och prioriteringsflödena, men inte som standard för all generativ AI. Myndigheten vill undvika att bygga en dyr intern plattform för lågklassade produktivitetsbehov som bättre hanteras genom en godkänd SaaS-lösning.

## Hybrid som målbild när olika krav måste samexistera

För större myndigheter är hybrid ofta den mest realistiska målbilden. Skälet är enkelt: alla AI-användningsfall har inte samma risk, samma data, samma förändringstakt eller samma integrationsbehov.

En god hybridarkitektur kräver dock tydliga principer:

- gemensam identitet och behörighetsmodell,
- tydliga nätverks- och säkerhetszoner,
- AI-gateway för kontrollerad modellåtkomst,
- modell- och tjänsteregister,
- gemensam loggnings- och observabilitystrategi,
- datakontrakt mellan miljöer,
- policy enforcement vid gränser,
- dokumenterade arkitekturbeslut,
- gemensamma release- och incidentprocesser.

Hybrid utan dessa förmågor blir snabbt en samling undantag. Hybrid med rätt styrning kan däremot ge en balanserad målarkitektur: snabbhet där det är möjligt, kontroll där det är nödvändigt och återanvändbara gränssnitt mellan spåren.

## Viktiga arkitekturbeslut

När driftmodell ska dokumenteras bör arkitekten minst fatta följande beslut:

1. Vilka informationsklasser får behandlas i vilka miljöer?
2. Vilka AI-roller är tillåtna i SaaS, PaaS, IaaS, privat moln och on-premises?
3. Vilka modellendpoints är godkända för vilka användningsfall?
4. Får promptar och modellutdata loggas, och i så fall var och hur länge?
5. Får källmaterial indexeras i extern tjänst?
6. Får embeddings lagras utanför myndighetens interna miljö?
7. Får ärendedata skickas till extern modellendpoint?
8. Vilka krav gäller för kryptering och nyckelhantering?
9. Vilka krav gäller för supportåtkomst och administratörsåtkomst?
10. Vilken exitväg finns om leverantör, modell eller driftmodell inte längre är acceptabel?
11. Vilken miljö är godkänd för experiment, test respektive produktion?
12. Vilken del av AI-förmågan ska vara gemensam och vilken får vara federerad?

Dessa beslut bör dokumenteras som arkitekturbeslut, inte bara som löpande anteckningar. De påverkar framtida upphandling, plattformsval, integrationsmönster och säkerhetsdesign.

## Exempel: Auroras vägval

Tullverket Aurora väljer inte ett enda svar på molnfrågan. I stället beslutar myndigheten om en differentierad målbild.

För lågklassat produktivitetsstöd godkänner Aurora en kontrollerad SaaS-tjänst. Tjänsten får användas för textbearbetning, strukturering och idéarbete med tydliga begränsningar. Användarna utbildas i vad som inte får matas in, och tjänsten integreras med myndighetens identitetshantering.

För det interna kunskapsstödet väljer Aurora ett hybridspår. Dokumentkällor, metadata och publiceringsprocess hanteras i kontrollerad miljö. Retrieval ska vara behörighetsmedveten. Modellanrop går via AI-gateway och endast den kontext som är godkänd för aktuell användare och användningssituation skickas vidare. Om informationsklassningen kräver det ska modellen kunna bytas till intern eller mer reglerad endpoint.

För ärendenära sammanfattning beslutar Aurora att skarpa ärendedata inte får användas i den generella SaaS-tjänsten. Ett separat spår etableras med striktare åtkomst, mer detaljerad loggning, tydligare mänsklig granskning och särskild rättslig bedömning. Driftmodellen kan bli privat moln eller on-premises beroende på vilka data som ska behandlas.

För prioriterings- och analysstöd väljer Aurora ett kontrollerat analysmiljöspår. Modellutveckling får ske med syntetiska eller avidentifierade dataset i mer flexibla miljöer, men validering mot känsligare data sker i kontrollerad miljö. Produktionskörning av beslutsnära stöd kräver särskilt arkitekturbeslut och dokumenterad mänsklig kontroll.

Auroras målarkitektur beskriver därför inte “moln eller on-premises”. Den beskriver vilka driftmodeller som är tillåtna för vilka arkitekturspår.

## När moln inte ska användas

Moln bör inte användas när myndigheten inte kan besvara grundläggande kontrollfrågor. Exempel:

- Det är oklart vilken information som skickas till tjänsten.
- Det är oklart var data lagras eller behandlas.
- Leverantörens villkor för kunddata är otydliga.
- Supportåtkomst kan inte kontrolleras eller följas upp.
- Loggar kan innehålla skyddsvärd information utan tillräcklig kontroll.
- Myndigheten kan inte integrera identitet och åtkomst på godtagbart sätt.
- Exitstrategi saknas.
- Lösningen kräver behandling av information som inte är godkänd för miljön.
- Verksamheten kan inte acceptera leverantörens förändringstakt.
- Rättslig eller säkerhetsmässig bedömning saknas.

I dessa fall är slutsatsen inte nödvändigtvis att moln aldrig kan användas. Slutsatsen är att moln inte kan användas för just det användningsfallet i den aktuella formen.

## När on-premises inte ska användas

On-premises bör inte användas bara för att det känns tryggt. Det kan vara fel väg när:

- användningsfallet har låg informationsrisk,
- molntjänst redan är godkänd och mer ändamålsenlig,
- myndigheten saknar GPU- och modellserveringskompetens,
- intern kapacitet blir en flaskhals,
- modellutbudet blir för begränsat,
- livscykelhanteringen blir svagare än i ett managed-alternativ,
- kostnaden blir hög utan motsvarande riskreduktion,
- interna plattformen saknar observability, releaseprocess och säkerhetskontroller,
- lösningen riskerar att bli ett isolerat specialbygge.

En intern driftmodell måste kunna motiveras med faktisk riskreduktion eller faktisk verksamhetsnytta, inte enbart med principen att data ska stanna internt.

## När hybrid inte ska användas

Hybrid bör inte användas som kompromiss utan arkitektur. Den är olämplig när:

- gränserna mellan miljöerna är oklara,
- ansvarsfördelningen är otydlig,
- loggning och incidenthantering inte fungerar över miljögränser,
- dataflöden inte är kartlagda,
- identitet och behörighet inte är sammanhängande,
- teamen saknar kompetens att förvalta flera driftmodeller,
- integrationerna blir mer riskfyllda än nyttan motiverar,
- varje användningsfall får en egen speciallösning.

Hybrid är ett arkitekturmönster, inte en ursäkt för att undvika vägval.

## Kostnad och finansiering

AI-driftmodeller skapar olika kostnadsprofiler. Moln kan ge låg startkostnad men hög rörlig kostnad. On-premises kan ge hög startkostnad och längre anskaffningscykel men lägre marginalkostnad vid vissa stabila arbetslaster. Hybrid kan ge bäst balans men också högre integrations- och styrkostnad.

För AI är kostnaden dessutom svår att bedöma tidigt eftersom den påverkas av:

- antal användare,
- antal modellanrop,
- promptlängd,
- kontextstorlek,
- embeddings och indexering,
- modellval,
- latencykrav,
- lagring av loggar och källor,
- test- och utvärderingskörningar,
- reservkapacitet,
- krav på tillgänglighet,
- kostnad för kompetens och förvaltning.

Tullverket Aurora inför därför kostnadsstyrning i AI-gateway och observability. Varje produktteam ska kunna följa användning, kostnad per användningsfall, kostnad per modellendpoint och effekter av ändrad prompt- eller retrievalstrategi.

## Exit och portabilitet

Driftmodellbeslut behöver alltid innehålla exitfrågan. AI-plattformar, modeller, API:er, licensvillkor och regulatoriska bedömningar kan förändras. Myndigheten bör därför undvika arkitektur där ett enda leverantörsval blir omöjligt att lämna.

Praktiska exitkrav kan vara:

- dokumenterade modellendpoints,
- abstraherad åtkomst via AI-gateway,
- möjlighet att byta modell utan att skriva om alla applikationer,
- export av promptar, konfigurationer och testdataset,
- separata data- och modellregister,
- standardiserade API-gränssnitt där det är möjligt,
- portabla RAG-pipelines,
- tydliga avtal för datauttag och radering,
- dokumenterad fallback om en tjänst stängs eller blir otillåten.

Exitstrategi betyder inte att all teknik måste vara leverantörsneutral från dag ett. Det betyder att myndigheten vet vilka delar som är inlåsta, varför det är acceptabelt och hur risken ska hanteras.

## Checklista

Använd denna checklista innan driftmodell beslutas för ett AI-användningsfall.

- Är användningsfallet beskrivet och klassat?
- Är AI-rollen tydlig: produktivitetsstöd, kunskapsstöd, ärendenära stöd, beslutsnära stöd eller automation?
- Är informationsflödet ritat från prompt till logg?
- Är personuppgifter, sekretess och skyddsvärda uppgifter identifierade?
- Är rättslig bedömning genomförd på rätt nivå?
- Är leverantörens datahantering, supportåtkomst och underbiträden bedömda?
- Är identitet och behörighet integrerbara med myndighetens IAM?
- Är loggning, observability och incidenthantering definierade?
- Är modellendpoints och tillåtna miljöer dokumenterade?
- Är experiment, test och produktion separerade?
- Är kostnadsstyrning på plats?
- Finns exitstrategi?
- Är beslutet dokumenterat som arkitekturbeslut?
- Är driftmodellen kopplad till AI-portföljen och målarkitekturen?

## Exempel från Tullverket Aurora

För Tullverket Aurora blir moln/on-premises-frågan olika beroende på användningsfall. Ett internt stöd för att sammanfatta öppna styrdokument kan prövas i en mer standardiserad molntjänst om avtalsvillkor och dataskydd är hanterade. Ett stöd som behandlar sekretessbelagda kontrolluppgifter kan däremot kräva striktare driftmiljö, egen nyckelhantering, begränsad modellåtkomst eller en on-premises-/hybridlösning.

Scenariot visar varför målarkitekturen bör formulera en beslutsmodell snarare än ett generellt förbud eller ett generellt molnmandat.

## Vägvalsfrågor

- Vilka informationsklasser får hanteras i publikt moln, privat moln, sovereign cloud respektive on-premises?
- Vilka användningsfall kräver egen nyckelhantering, särskild loggkontroll eller begränsad modellåtkomst?
- När är time-to-market viktigare än maximal teknisk kontroll?
- När innebär egen drift större risk än kontrollerad användning av molntjänst?
- Vilka beslut måste kunna omprövas när lagkrav, hotbild eller leverantörsvillkor förändras?

## Vanliga fallgropar

- Att göra molnfrågan ideologisk i stället för riskbaserad.
- Att välja moln för skarpa data eftersom piloten fungerade bra med testdata.
- Att välja on-premises utan att ha drift-, GPU- och MLOps-förmåga.
- Att behandla sovereign cloud som ett färdigt svar utan konkret kravanalys.
- Att glömma att promptar, loggar, embeddings och källutdrag också är informationsflöden.
- Att låta varje AI-team välja egen driftmodell utan gemensamma arkitekturspår.
- Att sakna exitstrategi från modellleverantör eller plattform.
- Att underskatta kostnaden för hybridintegration.
- Att blanda experiment- och produktionsmiljö.
- Att fokusera på var modellen körs men glömma var data, index, loggar och nycklar finns.

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Målarkitekturen bör innehålla en tydlig driftmodellkarta. Den ska inte bara säga att myndigheten använder moln, on-premises eller hybrid. Den ska ange:

- tillåtna driftmodeller per AI-roll,
- tillåtna informationsklasser per miljö,
- krav på AI-gateway och modellåtkomst,
- krav på RAG-index och källdata,
- krav på loggning och observability,
- krav på IAM, nätverk och säkerhetszoner,
- krav på experiment-, test- och produktionsmiljö,
- krav på exit och portabilitet,
- vilka beslut som är centrala och vilka som får fattas av produktteam inom givna ramar.

För Tullverket Aurora blir slutsatsen att hybrid är målbilden, men inte som ett otydligt mellanting. Hybrid betyder fyra styrda arkitekturspår: kontrollerad SaaS för lågklassat produktivitetsstöd, molnbaserad plattform för kontrollerade piloter, hybrid RAG för internt kunskapsstöd och kontrollerad intern eller privat miljö för känsliga och beslutsnära flöden.

Detta ger myndigheten både handlingsfrihet och kontroll. Arkitekturen kan utnyttja molnets snabbhet där det är rimligt, behålla intern kontroll där det är nödvändigt och undvika att varje AI-initiativ uppfinner sin egen driftmodell.


## Snabb sammanfattning

- Driftmodell ska väljas per användningsfall, informationsflöde och AI-roll, inte som ett generellt ja eller nej till moln.
- Publikt moln kan ge snabbhet, modellutbud och skalbarhet, men kräver stark leverantörsstyrning, rättslig prövning och kontroll över dataflöden.
- On-premises kan ge högre kontroll för känsliga flöden, men kräver egen kapacitet, kompetens och livscykelhantering.
- Hybrid är ofta realistiskt för större myndigheter, men bara om gränser, ansvar, identitet, loggning och policy enforcement är tydliga.
- Sovereign cloud och reglerade molnerbjudanden måste bedömas utifrån konkreta krav, inte utifrån etiketten.
- Målarkitekturen bör definiera tillåtna arkitekturspår och driftmodeller för olika AI-roller.
- Tullverket Aurora väljer en differentierad målbild med SaaS för låg risk, moln för kontrollerade piloter, hybrid RAG för kunskapsstöd och kontrollerad intern eller privat miljö för känsliga beslutsnära flöden.

## Nästa steg

Nästa kapitel behandlar plattformar, produkter och ramverk att överväga. Där flyttas fokus från driftmodell till vilka produkt- och tekniktyper som kan fylla målarkitekturens byggblock: AI-assistenter, modellplattformar, RAG-komponenter, vektordatabaser, orchestreringsramverk, MLOps- och LLMOps-verktyg, säkerhetslager och europeiska eller öppna alternativ.
