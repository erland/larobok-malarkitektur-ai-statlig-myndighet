# Kapitel 19: Målarkitektur för Tullverket Aurora

## Varför detta kapitel finns

De föregående kapitlen har beskrivit AI-förmåga, juridik, informationsklassning, governance, dataarkitektur, teknisk referensarkitektur, driftmodeller, plattformsval, säkerhetsarkitektur, upphandling och roadmap. Det här kapitlet samlar dessa delar i ett sammanhängande exempel.

Syftet är inte att presentera en färdig kopierbar målarkitektur som passar varje statlig myndighet. Syftet är att visa hur en erfaren arkitekt kan strukturera en målarkitektur så att den blir begriplig, beslutsbar och användbar. En målarkitektur för AI behöver inte vara maximal från början, men den måste vara tillräckligt tydlig för att styra användningsfall, investeringar, säkerhetskrav, juridiska bedömningar och tekniska vägval.

I kapitlet används den fiktiva tullmyndigheten Tullverket Aurora. Aurora har redan experimenterat med AI men behöver gå från lokala försök till en styrd och skalbar AI-förmåga. Exemplet visar hur myndigheten kan beskriva nuläge, målbild, principer, förmågor, byggblock, säkerhetszoner, integrationsmönster, driftmodell, arkitekturbeslut och roadmap i en samlad målarkitektur.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva vilka delar en praktisk AI-målarkitektur bör innehålla,
- koppla användningsfall och riskklasser till tekniska och organisatoriska vägval,
- formulera en målbild som inte reduceras till ett plattformsval,
- strukturera byggblock för AI-gateway, RAG, modellplattform, dataåtkomst, observability och livscykelhantering,
- visa hur moln, on-premises och hybrid kan kombineras i en styrd driftmodell,
- dokumentera arkitekturbeslut så att de blir spårbara,
- använda ett sammanhängande scenario för att förankra målarkitekturen hos verksamhet, juridik, säkerhet och IT.

## Innan vi börjar

Kapitlet utgår från att Aurora inte börjar från noll. Myndigheten har redan system, datalager, identitetslösningar, integrationsplattformar, säkerhetsprocesser, upphandlade molntjänster, interna handläggningssystem och etablerade arkitekturforum. AI-målarkitekturen ska därför inte ersätta hela IT-landskapet. Den ska beskriva hur AI-förmågan ska passa in i det befintliga landskapet och vilka nya byggblock som behöver etableras.

Det är också viktigt att förstå målarkitekturen som en styrprodukt, inte som en ritning över en enda teknisk lösning. En bra målarkitektur ska kunna styra flera lösningar:

- ett internt kunskapsstöd för regelverk och handböcker,
- sammanfattning av ärendehandlingar,
- analysstöd för strategisk planering,
- riskbedömningsstöd för kontrollverksamhet,
- administrativa textflöden,
- framtida AI-tjänster som ännu inte är definierade.

Målarkitekturen behöver därför beskriva återanvändbara förmågor, byggblock och beslut, inte bara en första pilot.

## Nuläge hos Tullverket Aurora

Aurora är en större statlig tullmyndighet med samhällskritiskt uppdrag. Myndigheten hanterar regelverk, varuflöden, ärenden, kontrollprioritering, dokumentgranskning, internationellt informationsutbyte och intern styrning. Informationslandskapet innehåller både öppna styrdokument, interna handböcker, personuppgifter, sekretessbelagda uppgifter och operativt känslig information.

AI-nuläget är typiskt för många större organisationer. Flera delar av myndigheten har testat AI, men testerna har skett på olika sätt och med olika kontrollnivå.

### Tidiga experiment

Aurora har genomfört eller diskuterat följande experiment:

- sammanfattning av långa ärendehandlingar,
- intern kunskapssökning i styrdokument och handböcker,
- stöd för att formulera administrativa texter,
- enklare analys av inkomna frågor,
- test av generativa AI-tjänster i kontorsmiljö,
- idéer om riskanalys och prioriteringsstöd.

Experimenten har skapat nyfikenhet och visat möjlig nytta. Samtidigt har de gjort myndighetens brister synliga.

### Identifierade problem

Auroras arkitekturgrupp identifierar sju huvudproblem:

- Det saknas gemensam klassning av AI-användningsfall.
- Det saknas tydliga regler för vilka data som får användas i vilka AI-miljöer.
- Juridik, dataskydd och informationssäkerhet kopplas in för sent.
- Olika team prövar olika verktyg utan samlad livscykelhantering.
- Loggning, spårbarhet och uppföljning är ojämn.
- Det finns ingen gemensam modell för RAG, modellval eller AI-gateway.
- Det saknas en långsiktig beslutsmodell för moln, on-premises och hybrid.

Detta leder till en viktig slutsats: Aurora behöver inte först och främst välja en AI-produkt. Myndigheten behöver etablera en styrd AI-förmåga.

## Målbild för AI-förmågan

Auroras målbild formuleras i verksamhetsnära termer. Den tekniska målarkitekturen ska stödja en större målbild:

> Tullverket Aurora ska kunna använda AI som ett kontrollerat, säkert och rättssäkert stöd i interna och verksamhetsnära processer, där användningsfall, data, modellval och driftmiljö styrs utifrån nytta, risk, juridik och informationsklassning.

Målbilden har fem delar.

### 1. Kontrollerad användning

Medarbetare ska kunna använda godkända AI-funktioner utan att behöva uppfinna egna arbetssätt. Det ska finnas tydliga regler för vilka typer av information som får användas, vilka verktyg som är godkända och när mänsklig kontroll krävs.

### 2. Gemensam AI-plattform

Aurora ska ha en gemensam teknisk förmåga för godkända AI-användningsfall. Plattformen ska inte nödvändigtvis vara en enda produkt, men den ska erbjuda gemensamma byggblock för modellåtkomst, RAG, loggning, policy, behörighet, test, driftsättning och uppföljning.

### 3. Riskbaserad driftmodell

Olika användningsfall ska kunna köras i olika miljöer. Lågkänsliga interna produktivitetsfall kan använda kontrollerade molntjänster. Mer känsliga användningsfall kan kräva avskilda moln, privat moln eller on-premises. Målarkitekturen ska göra det möjligt att välja driftmodell utan att varje projekt börjar från början.

### 4. Spårbar styrning

Beslut om användningsfall, data, modellval, leverantör, säkerhetszon och produktionssättning ska dokumenteras. Arkitekturbeslut, riskbedömningar och undantag ska vara spårbara.

### 5. Skalbar förvaltning

AI-lösningar ska inte lämnas som engångspiloter. De ska kunna förvaltas, mätas, uppdateras, avvecklas och granskas över tid. Det gäller både traditionella ML-modeller, generativa AI-lösningar, RAG-lösningar och färdiga AI-tjänster.

## Avgränsning av målarkitekturen

Aurora avgränsar målarkitekturen till myndighetsgemensam AI-förmåga. Den ska beskriva principer och byggblock som gäller brett, men den ska inte detaljdesigna varje AI-lösning.

### Ingår

Målarkitekturen omfattar:

- klassning och prioritering av AI-användningsfall,
- principer för offentlig AI,
- governance och beslutsmodell,
- dataåtkomst och informationsklassning,
- teknisk referensarkitektur,
- säkerhetszoner och driftmodeller,
- AI-gateway och modellåtkomst,
- RAG-mönster och kunskapsstöd,
- MLOps och LLMOps,
- loggning, observability och incidenthantering,
- upphandlings- och leverantörsprinciper,
- roadmap för införande.

### Ingår inte

Målarkitekturen detaljstyr inte:

- exakt användargränssnitt för varje AI-tjänst,
- exakt implementation i varje verksamhetssystem,
- val av en enda modell för alla framtida användningsfall,
- fullständig datamodell för alla källsystem,
- komplett projektplan med resursallokering.

Denna avgränsning är viktig. Om målarkitekturen blir för detaljerad blir den snabbt inaktuell. Om den blir för allmän styr den inte verkliga beslut.

## Användningsfall som styrande ingång

Aurora använder AI-portföljen som första styrande ingång till målarkitekturen. Arkitekturgruppen väljer ut fyra representativa användningsfall som får styra de första arkitekturbesluten.

### Användningsfall A: Intern kunskapssökning

Handläggare behöver kunna ställa frågor mot interna handböcker, vägledningar, rutiner och regelverk. Lösningen ska ge källhänvisningar och stödja mänsklig bedömning.

Arkitekturell betydelse:

- kräver dokumentpipeline,
- kräver sökindex och vektordatabas,
- kräver källspårbarhet,
- passar ofta för RAG,
- bör börja med icke-sekretessbelagt eller lågt klassat material,
- kräver tydlig ansvarsmodell för innehåll.

### Användningsfall B: Sammanfattning av ärendehandlingar

Handläggare vill sammanfatta längre handlingar för att snabbare förstå ärenden. Handlingarna kan innehålla personuppgifter och sekretessbelagd information.

Arkitekturell betydelse:

- kräver högre informationsklassning,
- kräver strikt åtkomstkontroll,
- kräver loggning av användning,
- kan kräva avskild driftmiljö,
- kräver tydliga regler för om sammanfattningen får sparas,
- får inte ersätta handläggarens ansvar.

### Användningsfall C: Riskanalys och prioriteringsstöd

Verksamheten vill använda AI för att identifiera mönster och stödja prioritering av kontrollinsatser. Detta kan påverka individer, företag och kontrollbeslut.

Arkitekturell betydelse:

- kan innebära hög rättslig och etisk risk,
- kräver stark dokumentation,
- kräver validering och uppföljning,
- kräver mänsklig kontroll,
- kan kräva särskild modellriskhantering,
- bör inte börja som generativ AI-pilot utan som kontrollerad analysförmåga.

### Användningsfall D: Administrativ textassistans

Medarbetare vill använda AI för utkast, sammanfattningar och språklig bearbetning av icke-känsliga texter.

Arkitekturell betydelse:

- kan ofta realiseras med godkänd SaaS eller kontorsnära AI-tjänst,
- kräver tydliga användarregler,
- kräver utbildning och informationsklassningsstöd,
- kan ge snabb nytta,
- bör hållas åtskild från känsliga verksamhetsdata.

Dessa fyra användningsfall visar varför en enda teknisk lösning inte räcker. Aurora behöver flera arkitekturspår.

## Arkitekturprinciper för Aurora

Målarkitekturen innehåller en principkatalog. Principerna är styrande och ska användas i arkitekturgranskning, upphandling och produktionssättning.

### Princip 1: Användningsfall före verktyg

AI-lösningar ska utgå från ett dokumenterat verksamhetsbehov, inte från en vald produkt eller modell. Varje initiativ ska beskriva nytta, användare, data, risk, ansvar och förväntad livscykel.

### Princip 2: Risk styr arkitekturspår

Informationsklassning, juridisk risk och verksamhetskonsekvens ska avgöra driftmodell, modellval, loggning, mänsklig kontroll och produktionskriterier.

### Princip 3: Data får inte bli osynliga

Promptar, uppladdade dokument, embeddings, modellutdata, loggar och utvärderingsdata ska betraktas som informationsobjekt. De ska ha ägare, klassning, lagringsregler och åtkomstregler.

### Princip 4: AI ska passera styrda åtkomstpunkter

AI-tjänster ska inte integreras direkt från varje verksamhetssystem till varje extern modell. Modellåtkomst ska styras via godkända åtkomstpunkter, exempelvis AI-gateway, integrationslager eller plattforms-API.

### Princip 5: Mänskligt ansvar ska vara explicit

När AI används som stöd i handläggning, analys eller beslut ska ansvarig människa, processägare och systemägare vara tydligt angivna. AI får inte skapa otydligt ansvar.

### Princip 6: Leverantörsoberoende där risk och livslängd kräver det

Aurora ska kunna använda marknadens tjänster, men inte bygga in sig i lösningar där data, promptlogik, RAG-pipeline, utvärderingsdata eller verksamhetskritisk logik inte kan flyttas eller granskas.

### Princip 7: Piloter ska designas för lärande och återanvändning

Varje pilot ska bidra till målarkitekturen. En pilot som inte ger återanvändbara lärdomar om data, risk, teknik, process eller drift ska inte prioriteras.

## Förmågekarta för målarkitekturen

Auroras målarkitektur beskriver AI-förmågan som en uppsättning förmågor. Det gör diskussionen mindre produktcentrerad och mer styrbar.

### Styrande förmågor

- AI-portföljstyrning.
- Use-case triage.
- Juridisk och dataskyddsmässig bedömning.
- Informationsklassning.
- Arkitekturgranskning.
- Modellriskhantering.
- Beslutsdokumentation.
- Leverantörsstyrning.

### Data- och kunskapsförmågor

- Dokumentintag och dokumentklassning.
- Metadatahantering.
- Indexering och embeddings.
- Vektorsökning.
- Behörighetsstyrd retrieval.
- Källhänvisning.
- Datakvalitetsuppföljning.
- Data lineage.

### Modell- och plattformsförmågor

- Modellkatalog.
- Modellval och modellpolicy.
- AI-gateway.
- Prompt- och orkestreringslager.
- RAG-pipeline.
- Modellservering.
- Test- och utvärderingsmiljö.
- MLOps och LLMOps.

### Säkerhets- och driftförmågor

- Identitet och åtkomst.
- Secrets management.
- Säkerhetszoner.
- Loggning och observability.
- Incidenthantering.
- Red teaming.
- Guardrails och policy enforcement.
- Kontinuitet och återställning.

### Förvaltningsförmågor

- Ägarskap per AI-lösning.
- Versionshantering.
- Mätning av nytta och kvalitet.
- Livscykelbeslut.
- Avveckling.
- Granskning och revision.
- Utbildning och användarstöd.

Förmågekartan visar att AI-förmågan är mer än modeller. Modellen är bara en del av ett större styrt system.

## Teknisk målbild

Auroras tekniska målbild består av ett antal återanvändbara byggblock. De kan realiseras med olika produkter, men målarkitekturen beskriver deras ansvar och relationer.

### Översiktlig logik

En användare eller ett verksamhetssystem ska inte anropa en modell okontrollerat. Flödet ska i normalfallet gå genom styrda lager:

1. Användare eller system initierar ett godkänt användningsfall.
2. Identitet, roll och behörighet kontrolleras.
3. Användningsfall och informationsklass avgör tillåtet arkitekturspår.
4. AI-gateway eller motsvarande åtkomstpunkt väljer tillåten modell och policy.
5. Vid RAG hämtas information från godkända källor via behörighetsstyrd retrieval.
6. Prompt, kontext och svar hanteras enligt regler för loggning och lagring.
7. Svar presenteras med källor, osäkerhetsmarkering eller kontrollkrav.
8. Mätpunkter, fel, användning och incidenter följs upp.

### Centrala byggblock

| Byggblock | Ansvar | Kommentar |
|---|---|---|
| AI-gateway | Styr modellåtkomst, policy, loggning och routing | Minskar behovet av direkta modellintegrationer |
| Identitets- och behörighetslager | Säkerställer att användaren får använda aktuell data och funktion | Måste fungera även i RAG-flöden |
| Use-case register | Håller godkända användningsfall, riskklass och ägare | Binder samman governance och teknik |
| Modellkatalog | Beskriver godkända modeller, villkor, miljöer och begränsningar | Ska innehålla både externa och interna modeller |
| RAG-lager | Hanterar dokumentintag, chunking, embeddings, retrieval och källor | Ska vara behörighetsstyrt |
| Vektordatabas eller sökindex | Stödjer semantisk sökning och återhämtning av kontext | Ska följa dataklassning och retention |
| Prompt- och orkestreringslager | Hanterar promptmallar, verktygsanrop och arbetsflöden | Ska versionshanteras |
| Observability-plattform | Följer upp användning, kvalitet, kostnad, fel och riskindikatorer | Behövs för drift och granskning |
| MLOps/LLMOps | Stödjer test, deployment, versionering och livscykel | Gäller både traditionell ML och LLM-lösningar |
| Policy enforcement | Upprätthåller regler för data, modell, svar och användning | Kan ligga i flera lager |

Tabellen är inte en produktlista. Den är en ansvarskarta. Produkter kan bytas, men ansvaret måste finnas någonstans i arkitekturen.

## Säkerhetszoner och driftspår

Aurora definierar fyra arkitekturspår. De är tillräckligt konkreta för att styra vägval men tillräckligt generella för att kunna utvecklas.

### Spår 1: Kontorsnära AI för lågkänslig information

Detta spår omfattar administrativa och produktivitetsnära funktioner där data är lågkänslig och användningen är intern.

Exempel:

- språkgranskning,
- sammanfattning av öppna texter,
- utkast till interna presentationer,
- strukturering av icke-känsliga mötesanteckningar.

Möjlig driftmodell:

- godkänd SaaS eller molntjänst,
- tydliga användarregler,
- central konfiguration,
- begränsad integration med kärnsystem,
- loggning enligt fastställd policy.

Viktigt arkitekturbeslut:

- Detta spår får inte användas för sekretessbelagda ärenden eller känsliga personuppgifter.

### Spår 2: Myndighetsintern RAG för styrd kunskapssökning

Detta spår omfattar intern kunskapssökning i godkända dokumentkällor.

Exempel:

- handböcker,
- interna riktlinjer,
- verksamhetsrutiner,
- regelstöd,
- utbildningsmaterial.

Möjlig driftmodell:

- kontrollerad moln- eller hybridmiljö,
- behörighetsstyrd retrieval,
- källhänvisning,
- dokumentägare per källa,
- loggning av frågor och svar enligt klassning,
- regelbunden utvärdering av träffsäkerhet.

Viktigt arkitekturbeslut:

- RAG-lagret ska inte kringgå befintlig dokumentstyrning. Om ett dokument inte får ses av användaren ska det inte heller användas som kontext i AI-svaret.

### Spår 3: Känsligt handläggarstöd

Detta spår omfattar AI-stöd där ärendeinformation, personuppgifter eller sekretessbelagd information kan ingå.

Exempel:

- sammanfattning av ärendehandlingar,
- stöd vid dokumentgranskning,
- strukturerad extraktion av information,
- förslag till intern arbetsanteckning.

Möjlig driftmodell:

- avskild molnmiljö, privat moln eller on-premises beroende på klassning,
- stark åtkomstkontroll,
- strikt logghantering,
- begränsad modellåtkomst,
- tydliga regler för lagring av promptar och svar,
- mänsklig kontroll före användning i ärendeprocess.

Viktigt arkitekturbeslut:

- AI-utdata ska vara stödmaterial, inte automatiskt myndighetsbeslut.

### Spår 4: Analys- och riskmodeller med hög konsekvens

Detta spår omfattar AI eller avancerad analys som kan påverka prioriteringar, kontroller eller bedömningar.

Exempel:

- riskindikatorer,
- prioriteringsstöd,
- mönsteranalys,
- strategisk analys.

Möjlig driftmodell:

- högkontrollerad miljö,
- formell modellvalidering,
- dokumenterad datagrund,
- test mot historiska data,
- uppföljning av kvalitet och bias,
- mänsklig beslutspunkt,
- särskild modellriskhantering.

Viktigt arkitekturbeslut:

- Sådana modeller ska inte införas genom samma förenklade väg som administrativ generativ AI.

## Integrationsmönster

Auroras målarkitektur innehåller tre huvudsakliga integrationsmönster.

### Mönster 1: Användarinitierad AI-assistent

En användare arbetar i ett godkänt gränssnitt och ställer frågor eller ber om stöd. Lösningen kontrollerar behörighet och användningsfall innan modellen anropas.

Passar för:

- intern kunskapssökning,
- administrativ textassistans,
- enklare sammanfattning,
- stöd till handläggare.

Risker:

- användaren kan mata in fel data,
- svar kan övertolkas,
- källor kan vara ofullständiga,
- loggar kan innehålla känslig information.

Kontroller:

- tydliga användarregler,
- informationsklassningsstöd,
- källhänvisningar,
- varningar och osäkerhetsmarkering,
- loggning och uppföljning.

### Mönster 2: Systemintegrerad AI-tjänst

Ett verksamhetssystem anropar en AI-funktion via API. Anropet går genom integrationslager och AI-gateway.

Passar för:

- dokumentklassificering,
- sammanfattning i ärendesystem,
- automatiserad extraktion,
- kvalitetssäkring av dataflöden.

Risker:

- AI blir osynlig för användaren,
- fel kan spridas automatiskt,
- ansvar kan bli otydligt,
- integrationer kan bli svåra att ändra.

Kontroller:

- tydlig systemägare,
- versionshanterade promptar och modeller,
- testsviter,
- fallback,
- gränsvärden,
- spårbarhet per anrop.

### Mönster 3: Analysmodell i kontrollerad datamiljö

Data bearbetas i en kontrollerad analysmiljö där modeller utvecklas, testas, valideras och används för analysstöd.

Passar för:

- riskanalys,
- strategisk planering,
- trendanalys,
- modellutvärdering.

Risker:

- felaktiga datagrunder,
- bias,
- svårförklarade modeller,
- överautomatisering,
- sammanblandning av analys och beslut.

Kontroller:

- dokumenterad datagrund,
- modellvalidering,
- analysprotokoll,
- mänsklig granskning,
- regelbunden uppföljning,
- avvecklingskriterier.

## Dataarkitektur i målbilden

Aurora beslutar att dataarkitekturen för AI ska följa fyra regler.

### Regel 1: AI ska använda godkända datakällor

AI-lösningar får inte bygga egna skuggkopior av verksamhetsdata utan tydligt ägarskap. Dokument, ärendedata och analysdata ska komma från godkända källor eller godkända datauttag.

### Regel 2: Metadata är en säkerhetskomponent

Varje dokument eller datapost som används i AI-sammanhang ska bära metadata om källa, ägare, klassning, giltighet, version och behörighet där det är relevant. Utan metadata kan RAG och analysmodeller inte styras på ett säkert sätt.

### Regel 3: Embeddings är inte neutrala

Embeddings och vektorindex ska hanteras enligt datats skyddsvärde. Om källmaterialet är känsligt kan även index, chunkar och mellanrepresentationer vara känsliga.

### Regel 4: Retention ska bestämmas före drift

Aurora ska besluta hur länge promptar, svar, dokumentutdrag, utvärderingsdata och loggar sparas. Detta ska inte lämnas till standardinställningar i en produkt.

## RAG-målarkitektur för kunskapsstöd

För intern kunskapssökning väljer Aurora ett RAG-mönster som första större gemensamma AI-förmåga. Det ger nytta utan att kräva att myndigheten tränar en egen språkmodell.

### RAG-flöde

1. Dokumentägare godkänner källor.
2. Dokument klassas och metadata kontrolleras.
3. Dokument delas upp i chunkar.
4. Embeddings skapas i godkänd miljö.
5. Chunkar och metadata lagras i sökindex eller vektordatabas.
6. Användaren ställer en fråga i ett godkänt gränssnitt.
7. Behörighetskontroll avgör vilka källor användaren får söka i.
8. Relevant kontext hämtas.
9. Modellanrop sker via AI-gateway.
10. Svaret presenteras med källhänvisningar.
11. Användning, kvalitet och fel följs upp.

### RAG-beslut

Aurora dokumenterar följande beslut:

| Beslut | Val | Motivering |
|---|---|---|
| Första källor | Handböcker och interna riktlinjer med låg eller måttlig känslighet | Ger nytta och hanterbar risk |
| Källhänvisning | Obligatorisk | Minskar risken att svar uppfattas som auktoritativa utan grund |
| Behörighet | Retrieval ska respektera användarens åtkomst | Förhindrar indirekt informationsläckage |
| Modellval | Godkända modeller via AI-gateway | Undviker direkta och ostrukturerade modellintegrationer |
| Loggning | Frågor, svar och källor loggas enligt fastställd policy | Krävs för felsökning, förbättring och uppföljning |
| Utvärdering | Testfrågor och kvalitetsmått etableras före bred lansering | Gör kvalitet mätbar |

## Modellstrategi

Aurora väljer inte en enda modellstrategi för hela myndigheten. I stället definieras en modellpolicy.

### Modellkategorier

Målarkitekturen skiljer mellan:

- färdiga AI-funktioner i godkända verksamhets- eller kontorsplattformar,
- externa generativa modeller via kontrollerade API:er,
- öppna eller kommersiella modeller som körs i kontrollerad miljö,
- traditionella ML-modeller för analys och prediktion,
- specialiserade modeller för dokumentförståelse, klassificering eller extraktion.

### Modellpolicy

Modellval ska baseras på:

- användningsfall,
- dataklass,
- rättslig risk,
- krav på transparens,
- krav på datalokalisering,
- prestanda och kvalitet,
- kostnad och skalbarhet,
- kompetens och förvaltningsförmåga,
- exitmöjlighet.

Målarkitekturen förbjuder inte molnmodeller. Den förbjuder okontrollerad modellåtkomst. Skillnaden är central.

## Moln, on-premises och hybrid i Auroras målbild

Aurora väljer en hybrid målbild. Det innebär inte att allt ska byggas dubbelt. Det innebär att myndigheten definierar tydliga driftspår.

### Moln används när

- dataklassen tillåter det,
- leverantörens villkor är godkända,
- loggning och konfiguration kan styras,
- nyttan av snabb etablering är stor,
- användningsfallet är administrativt eller lågkänsligt,
- exitstrategi är dokumenterad.

### On-premises eller privat drift används när

- informationens skyddsvärde kräver det,
- datalokalisering och kontroll är avgörande,
- integrationsberoenden är starka,
- användningsfallet är verksamhetskritiskt,
- modell eller data inte får lämna kontrollerad miljö,
- incident- och kontinuitetskrav är höga.

### Hybrid används när

- användningsfall har olika risknivåer,
- RAG-källor ligger internt men modellåtkomst kan vara extern under kontroll,
- vissa modeller behöver köras nära data,
- myndigheten vill undvika att en enda driftmodell styr alla framtida vägval.

Auroras målarkitektur uttrycker detta som en beslutsregel:

> Driftmodell väljs per arkitekturspår, inte per organisationsenhet och inte per leverantörspreferens.

## Governance i målarkitekturen

Målarkitekturen innehåller en beslutsmodell som gör att AI-initiativ kan röra sig från idé till produktion.

### Beslutsflöde

1. Verksamheten beskriver användningsfall.
2. Use-case triage gör första bedömning.
3. Informationsklassning och juridisk bedömning initieras.
4. Arkitekturforum föreslår arkitekturspår.
5. Säkerhet och dataskydd granskar kontroller.
6. AI governance board beslutar om pilot eller avslag.
7. Pilot genomförs med mätpunkter.
8. Produktionskriterier granskas.
9. Förvaltningsägare tar över vid produktionssättning.
10. Lösningen följs upp och omprövas.

### Roller

| Roll | Ansvar i målarkitekturen |
|---|---|
| Verksamhetsägare | Äger behov, nytta och processförändring |
| Informationsägare | Äger klassning och tillåten användning av data |
| Systemägare | Äger systemintegration och driftansvar |
| Modellägare | Äger modellens kvalitet, begränsningar och livscykel |
| Arkitekt | Säkerställer att lösningen följer målarkitektur och principer |
| Dataskyddsfunktion | Granskar personuppgiftsbehandling och dataskyddsrisk |
| Informationssäkerhet | Granskar säkerhetskontroller och risker |
| Juridik | Bedömer rättsliga förutsättningar och ansvar |
| Leverantörsstyrning | Följer upp avtal, villkor, ändringar och exit |
| AI governance board | Fattar prioriterings- och undantagsbeslut |

Tabellen gör ansvar synligt. Den viktigaste effekten är att AI inte blir ett rent teknikärende.

## Arkitekturbeslut för Aurora

Aurora dokumenterar ett antal centrala arkitekturbeslut. Nedan visas ett urval.

### ADR-001: AI-gateway som gemensam åtkomstpunkt

Beslut: AI-modeller som används i myndighetsgemensamma lösningar ska i normalfallet anropas via en gemensam AI-gateway eller motsvarande kontrollerad åtkomstpunkt.

Motivering:

- central policy,
- spårbar modellåtkomst,
- enklare leverantörsbyte,
- gemensam loggning,
- kostnadsuppföljning,
- möjlighet att styra modellval per användningsfall.

Konsekvens:

- vissa pilotteam får längre startsträcka,
- gatewayen blir en kritisk komponent,
- tydlig produktägare och driftansvar krävs.

### ADR-002: RAG före finjustering för första kunskapsstödet

Beslut: För intern kunskapssökning ska Aurora i första hand använda RAG, inte finjustering av modell.

Motivering:

- kunskapen finns i dokument,
- källor behöver kunna uppdateras,
- svar behöver kunna hänvisa till källa,
- finjustering löser inte behörighetsstyrning,
- risk och komplexitet blir lägre i första steget.

Konsekvens:

- dokumentkvalitet och metadata blir centrala,
- retrieval-kvalitet måste mätas,
- RAG-lagret behöver förvaltas.

### ADR-003: Fyra arkitekturspår för drift och risk

Beslut: AI-användningsfall ska klassas till ett av fyra arkitekturspår: kontorsnära AI, myndighetsintern RAG, känsligt handläggarstöd eller analys- och riskmodeller med hög konsekvens.

Motivering:

- förenklar beslutsprocessen,
- gör riskstyrning praktiskt användbar,
- undviker att varje projekt skapar egen driftmodell,
- stödjer både snabb nytta och hög kontroll.

Konsekvens:

- klassningskriterier måste hållas aktuella,
- undantag måste beslutas formellt,
- arkitekturspåren behöver återkommande granskning.

### ADR-004: Hybrid målbild

Beslut: Aurora ska etablera en hybrid AI-arkitektur där moln, avskild molnmiljö, privat drift och on-premises kan användas beroende på klassning och användningsfall.

Motivering:

- alla användningsfall har inte samma risk,
- moln kan ge snabb nytta för lågkänsliga fall,
- känsliga fall kräver starkare kontroll,
- myndigheten behöver undvika både molnförbud och molnslentrian.

Konsekvens:

- plattformsarkitekturen blir mer komplex,
- gemensamma principer och gränssnitt blir viktiga,
- kompetens behövs för flera driftmodeller.

### ADR-005: Källhänvisning som standard för kunskapsstöd

Beslut: AI-svar som bygger på myndighetens dokument ska i normalfallet visa källhänvisning eller annan spårbar grund.

Motivering:

- stärker tillit,
- gör svar granskningsbara,
- minskar risken för hallucinationer,
- stödjer handläggarens ansvar.

Konsekvens:

- dokumentstruktur och metadata måste förbättras,
- vissa svar kan behöva avvisas om källstöd saknas,
- kvalitet mäts inte bara i språklig form utan i spårbarhet.

## Målarkitekturens dokumentpaket

Aurora beslutar att målarkitekturen inte ska vara ett enda långt dokument. Den delas upp i ett dokumentpaket.

### Styrande dokument

- AI-målarkitektur.
- Arkitekturprinciper för AI.
- AI-governance och beslutsmodell.
- Klassningsmodell för AI-användningsfall.
- Godkända arkitekturspår.
- Modellpolicy.
- Drift- och säkerhetszoner.

### Fördjupande dokument

- Teknisk referensarkitektur.
- RAG-referensarkitektur.
- MLOps- och LLMOps-riktlinje.
- Loggning och observability för AI.
- Upphandlings- och leverantörskrav.
- Säkerhetsmönster för AI.

### Operativa mallar

- AI-use-case canvas.
- Informationsklassningsfrågor.
- Juridisk triagemall.
- ADR-mall.
- Produktionskriterier.
- Pilotutvärdering.
- Modellkort eller systemkort.
- Exit-checklista.

Detta dokumentpaket gör målarkitekturen lättare att underhålla. Principer ändras sällan. Produktval och tekniska profiler kan ändras oftare.

## Roadmap kopplad till målarkitekturen

Aurora använder målarkitekturen för att styra sin 24-månaders roadmap.

### Fas 1: Grundkontroll

Under de första månaderna etableras:

- AI-principer,
- use-case triage,
- interimistiska användarregler,
- register över AI-experiment,
- första informationsklassningsmodell,
- beslut om arkitekturspår,
- prioriterad pilotportfölj.

Målarkitekturens roll:

- sätta gränser för vad som får testas,
- hindra att okontrollerade lösningar skalar,
- skapa gemensamt språk.

### Fas 2: Sandlåda och referensmönster

Aurora etablerar en kontrollerad AI-sandlåda och första referensmönster.

Målarkitekturens roll:

- beskriva godkända miljöer,
- definiera RAG-mönster,
- tydliggöra modellåtkomst,
- skapa krav på loggning och utvärdering.

### Fas 3: Styrda piloter

Aurora genomför piloter för kunskapssökning, sammanfattning och administrativ textassistans.

Målarkitekturens roll:

- koppla piloter till arkitekturspår,
- pröva produktionskriterier,
- validera governance,
- fånga lärdomar som uppdaterar målarkitekturen.

### Fas 4: Produktionssättning

Godkända piloter förs över till förvaltning.

Målarkitekturens roll:

- säkerställa ägarskap,
- kräva livscykelhantering,
- följa upp nytta och risk,
- dokumentera undantag.

### Fas 5: Skalad AI-portfölj

Aurora har flera AI-lösningar i produktion och en styrd portfölj.

Målarkitekturens roll:

- prioritera nya användningsfall,
- hantera modell- och leverantörsförändringar,
- uppdatera arkitekturspår,
- styra investeringar.

## Vägvalsfrågor för arkitekten

När Auroras arkitekter granskar ett AI-initiativ använder de följande frågor.

### Om användningsfallet

- Vilket verksamhetsproblem ska lösas?
- Vem använder AI-stödet?
- Vilken AI-roll har lösningen: assistent, kunskapsstöd, beslutsstöd eller automatiserad komponent?
- Vilken nytta ska mätas?
- Vad händer om AI-svaret är fel?

### Om data

- Vilka datakällor används?
- Vem äger informationen?
- Vilken klassning har data, promptar, svar, embeddings och loggar?
- Behövs personuppgifter?
- Behövs sekretessbelagd information?
- Hur länge ska mellanresultat sparas?

### Om teknik

- Krävs RAG, finjustering, traditionell ML eller färdig AI-funktion?
- Vilka modeller är tillåtna?
- Ska modellen köras i moln, privat miljö eller on-premises?
- Hur sker integration?
- Hur hanteras versionering och test?

### Om styrning

- Vem äger lösningen efter pilot?
- Vilket arkitekturspår gäller?
- Vilka kontroller krävs före produktion?
- Vilka beslut behöver dokumenteras?
- Finns exitstrategi?

## Vanliga fallgropar i exemplet

Aurora identifierar flera fallgropar som målarkitekturen ska motverka.

### Fallgrop 1: Att beskriva målarkitekturen som produktval

Om målarkitekturen bara säger vilken AI-plattform som ska användas saknas styrning för data, juridik, säkerhet, organisation och livscykel.

Motåtgärd:

- beskriv förmågor och byggblock före produktnamn,
- dokumentera produktval som realisering av ett byggblock,
- håll principer och ansvar separerade från leverantörsspecifika detaljer.

### Fallgrop 2: Att låta lågkänsliga användningsfall styra hela arkitekturen

Administrativ textassistans kan vara en bra start, men den säger inte tillräckligt om hur känsligt handläggarstöd eller riskanalys ska hanteras.

Motåtgärd:

- definiera flera arkitekturspår,
- pröva minst ett användningsfall med högre kontrollbehov,
- gör driftmodell och säkerhetszon beroende av klassning.

### Fallgrop 3: Att underskatta dokument- och metadatakvalitet

RAG fungerar dåligt om dokumenten är gamla, dubblerade, otydliga, felklassade eller saknar ägare.

Motåtgärd:

- gör dokumentstyrning till del av AI-förmågan,
- etablera källägare,
- mät retrieval-kvalitet,
- rensa och prioritera källor före bred lansering.

### Fallgrop 4: Att sakna livscykel för promptar och modeller

En AI-lösning förändras när promptar, modeller, data, leverantörsvillkor eller användningsmönster förändras.

Motåtgärd:

- versionshantera promptar och konfiguration,
- dokumentera modellval,
- följ upp kvalitet över tid,
- ha omprövningspunkter.

### Fallgrop 5: Att governance blir en broms utan beslutsförmåga

Om varje AI-initiativ fastnar i oklara samråd skapas skugg-IT och informella genvägar.

Motåtgärd:

- skapa tydliga arkitekturspår,
- definiera snabbspår för låg risk,
- definiera striktare spår för hög risk,
- ge AI governance board tydligt mandat.

## Checklista: minsta innehåll i Auroras AI-målarkitektur

En första version av målarkitekturen bör minst innehålla:

- nulägesbeskrivning,
- målbild för AI-förmågan,
- avgränsning,
- användningsfallskategorier,
- risk- och klassningsmodell,
- arkitekturprinciper,
- governance och beslutsmodell,
- förmågekarta,
- teknisk referensarkitektur,
- dataarkitekturprinciper,
- RAG-mönster,
- modellpolicy,
- säkerhetszoner,
- driftspår,
- integrationsmönster,
- MLOps- och LLMOps-principer,
- loggning och observability,
- leverantörs- och upphandlingsprinciper,
- centrala ADR:er,
- roadmap,
- öppna beslut och undantag.

## Sammanhängande arkitekturbeskrivning

En sammanfattande målarkitekturbeskrivning för Aurora kan formuleras så här:

Tullverket Aurora etablerar en myndighetsgemensam AI-förmåga som styrs av användningsfall, risk, juridik och informationsklassning. AI-användning delas in i godkända arkitekturspår, från lågkänslig kontorsnära AI till högkontrollerade analys- och riskmodeller. Gemensamma byggblock etableras för AI-gateway, modellkatalog, RAG, dataåtkomst, loggning, observability, MLOps, LLMOps och policy enforcement.

Målarkitekturen är hybrid. Molntjänster används där informationsklassning, avtalsvillkor och risk tillåter det. On-premises eller privat drift används där känslighet, kontrollkrav eller verksamhetskritikalitet kräver det. RAG används som första huvudsakliga mönster för intern kunskapssökning, medan mer konsekvensrika analysmodeller hanteras i särskilda kontrollerade miljöer.

AI-lösningar får inte skala till produktion utan dokumenterad ägare, användningsfall, dataklassning, modellval, säkerhetskontroller, loggning, uppföljning och förvaltningsplan. Arkitekturbeslut dokumenteras som ADR:er och uppdateras när lagkrav, leverantörsvillkor, modeller eller verksamhetsbehov förändras.

## Koppling till målarkitekturen

Kapitlet fungerar som bryggan mellan bokens principer och en användbar målarkitekturartefakt. När Aurora-exemplet är färdigt ska läsaren kunna se hur målbild, principer, förmågor, byggblock, driftmodeller och roadmap hänger ihop.

För en verklig myndighet bör motsvarande kapitel eller dokument kompletteras med myndighetens egna klassningsmodeller, styrande dokument, systemlandskap, avtalsförutsättningar och beslutade arkitekturprinciper.

## Snabb sammanfattning

- En AI-målarkitektur ska beskriva förmåga, styrning, data, teknik, drift och livscykel, inte bara produktval.
- Tullverket Aurora behöver flera arkitekturspår eftersom användningsfallen har olika risk, dataklass och konsekvens.
- RAG är ett lämpligt första mönster för intern kunskapssökning, men det kräver dokumentstyrning, metadata, behörighetskontroll och kvalitetssäkring.
- AI-gateway, modellkatalog, RAG-lager, observability och MLOps/LLMOps är centrala byggblock i målbilden.
- Hybrid arkitektur gör det möjligt att använda moln där det är lämpligt och on-premises eller privat drift där kontrollkraven är högre.
- Arkitekturbeslut behöver dokumenteras så att målarkitekturen kan styra både piloter, upphandlingar och produktionssättning.
- Målarkitekturen blir mest användbar när den kopplas till roadmap, governance och praktiska beslutsmallar.

## Nästa steg

Nästa kapitel behandlar vanliga misstag och anti-patterns. Där vänds perspektivet från hur Aurora bör bygga sin målarkitektur till vad som ofta går fel när organisationer försöker etablera AI-förmåga utan tillräcklig styrning, klassning, arkitektur och livscykelhantering.

## Exempel från Tullverket Aurora

Detta kapitel är bokens sammanhållna scenario. Det ska läsas som ett exempel på hur föregående kapitel omsätts i en faktisk målarkitektur: från användningsfall och principer till byggblock, driftmodell, governance och roadmap.

Aurora-exemplet är avsiktligt förenklat men bör vara tillräckligt konkret för att en arkitekt ska kunna översätta strukturen till en verklig myndighet med andra uppdrag, informationsklasser och tekniska förutsättningar.
