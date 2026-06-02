# Kapitel 15: När man väljer vad

## Varför detta kapitel finns

Efter att myndigheten har beskrivit sina användningsfall, juridiska ramar, informationsklasser, arkitekturprinciper, förmågor, tekniska byggblock och möjliga plattformskategorier återstår en svår fråga: när ska man välja vad?

Det är här många AI-satsningar tappar styrfart. Diskussionen kan bli för abstrakt, så att ingen vågar fatta beslut. Den kan också bli för konkret, så att organisationen väljer verktyg innan konsekvenserna är förstådda. En målarkitektur behöver därför inte bara beskriva målbilden. Den behöver också ge stöd för återkommande vägval.

Detta kapitel samlar de viktigaste arkitekturbesluten för en större statlig myndighet som ska etablera AI-förmåga. Fokus ligger inte på att ge ett generellt facit. Fokus ligger på att visa hur erfarna arkitekter kan strukturera beslut, jämföra alternativ, dokumentera tradeoffs och skapa en beslutslogg som går att följa upp.

Kapitlet bygger vidare på kapitel 13 om moln, on-premises och hybrid samt kapitel 14 om plattformar, produkter och ramverk. Där beskrevs möjliga drift- och plattformsspår. Här översätts de till konkreta beslut: köpa eller bygga, central eller federerad plattform, RAG eller fine-tuning, SaaS eller egen drift, en modell eller flera, gemensam AI-gateway eller separata lösningar.

## Arkitekturproblemet

Tullverket Aurora har nu flera möjliga AI-spår framför sig. En del verksamheter vill snabbt införa färdiga AI-assistenter för lågkänsliga administrativa uppgifter. Andra vill bygga ett kontrollerat RAG-baserat kunskapsstöd för interna styrdokument. Kontrollverksamheten vill undersöka avancerat analysstöd, men där är data känsligare, kraven på spårbarhet högre och felkonsekvenserna större.

Samtidigt finns flera starka drivkrafter:

- verksamheten vill se nytta snabbt,
- IT vill undvika oöverblickbar teknisk skuld,
- säkerhetsfunktionen vill minimera exponering av känslig information,
- juridik vill se tydlig ansvarsfördelning och dokumentation,
- upphandling vill undvika inlåsning och oklara avtalsvillkor,
- arkitekturfunktionen vill etablera återanvändbara mönster.

Om Aurora försöker lösa allt med ett enda beslut blir beslutet antingen för grovt eller för långsamt. Om varje team får fatta egna beslut uppstår i stället fragmentering, dubbla plattformar, otydliga loggar, svag styrning och svårförvaltade lösningar.

Arkitekturproblemet är därför att skapa en beslutsmodell som är tillräckligt tydlig för att styra, men tillräckligt flexibel för att hantera olika risknivåer och användningsfall.

## Centrala begrepp

### Arkitekturbeslut

Ett arkitekturbeslut är ett vägval som påverkar målarkitektur, lösningsarkitektur, drift, styrning, säkerhet eller förvaltning. I AI-sammanhang kan ett arkitekturbeslut handla om exempelvis modellval, driftmodell, datalagring, loggning, gränssnitt, leverantörsmodell eller mänsklig kontroll.

Beslutet bör inte bara dokumentera vad som valdes. Det bör också dokumentera varför beslutet fattades, vilka alternativ som övervägdes, vilka antaganden som låg bakom och vilka konsekvenser beslutet får.

### Architecture Decision Record

En Architecture Decision Record, ofta förkortad ADR, är ett kort dokument för ett arkitekturbeslut. Formen kan variera, men en robust ADR innehåller normalt:

- titel,
- status,
- kontext,
- beslut,
- övervägda alternativ,
- konsekvenser,
- uppföljningsdatum eller omprövningspunkt.

I en AI-målarkitektur är ADR:er särskilt värdefulla eftersom teknik, juridik, leverantörsvillkor och modellkapacitet förändras snabbt. Ett beslut som är rimligt i dag kan behöva omprövas när riskbild, regelverk eller produktmognad förändras.

### Tradeoff

En tradeoff är en avvägning där ett alternativ ger vissa fördelar men samtidigt skapar vissa nackdelar. Inom AI-arkitektur är tradeoffs ofta mer relevanta än enkla rätt/fel-frågor.

Ett exempel är att en färdig SaaS-assistent kan ge snabb nytta och låg startkostnad, men samtidigt skapa begränsad kontroll över dataflöden, modellversioner, loggning och framtida flyttbarhet. En egen on-premises-lösning kan ge högre kontroll, men kräver mer kompetens, driftkapacitet och livscykelhantering.

### Beslutsmatris

En beslutsmatris är ett sätt att jämföra alternativ mot gemensamma kriterier. Den ska inte användas som en mekanisk poängmaskin. Den ska användas för att synliggöra varför ett alternativ är rimligt eller olämpligt.

För AI-beslut bör kriterierna normalt omfatta nytta, risk, informationsklass, rättslig komplexitet, säkerhet, kompetens, driftbarhet, kostnad, skalbarhet, leverantörsrisk och reversibilitet.

## Rekommenderat angreppssätt

Aurora väljer att inte skapa en enda stor beslutsmatris för hela AI-förmågan. I stället inför myndigheten en beslutsmodell i fyra steg.

### Steg 1: Beskriv användningsfallet utan produktnamn

Varje beslut börjar med ett användningsfall, inte med en produkt. Arkitekturen beskriver först:

- vem som ska använda lösningen,
- vilken verksamhetsprocess som påverkas,
- vilken nytta som eftersträvas,
- vilka data som behövs,
- vilken AI-roll lösningen har,
- om resultatet är rådgivande, stödjande eller styrande,
- vilka felkonsekvenser som kan uppstå.

Detta hindrar att ett produktval smyger in som lösning innan problemet är förstått.

För Aurora innebär det att intern kunskapssökning inte beskrivs som “vi behöver en viss chatbot”. Det beskrivs som “handläggare behöver söka, sammanfatta och jämföra interna styrdokument med spårbarhet till källor och utan att sekretessbelagd ärendedata exponeras”.

### Steg 2: Placera användningsfallet i ett arkitekturspår

Nästa steg är att placera användningsfallet i ett av myndighetens godkända arkitekturspår. Aurora använder exempelvis följande spår:

- personlig produktivitet med låg informationsklass,
- kontrollerat kunskapsstöd med RAG,
- ärendestöd med skyddsvärda data,
- prediktiv analys med validerade modeller,
- högrisknära beslutsstöd med mänsklig kontroll,
- experiment- och sandlådespår utan produktionsdata.

Spåret avgör vilka driftmodeller, datakällor, loggningskrav, godkännandeprocesser och plattformskomponenter som får användas.

### Steg 3: Jämför alternativ mot styrande kriterier

När spåret är valt jämförs alternativ. I detta läge kan produktkategorier och tekniska mönster diskuteras. Men jämförelsen ska ske mot gemensamma kriterier.

Aurora använder en enkel uppsättning kriterier:

- verksamhetsnytta,
- risk och konsekvens,
- informationsklass,
- rättslig komplexitet,
- säkerhetskontroll,
- integrerbarhet,
- driftbarhet,
- kompetensbehov,
- kostnadsprofil,
- leverantörsrisk,
- reversibilitet,
- tid till nytta.

Det viktigaste är inte att alla kriterier får en siffra. Det viktigaste är att beslutet går att motivera och ompröva.

### Steg 4: Dokumentera beslutet som ADR

När beslutet fattas dokumenteras det som en ADR. Det gör beslutet spårbart och minskar risken att samma diskussion återkommer i varje projekt.

En bra ADR för AI bör också innehålla villkor. Exempel:

- beslutet gäller endast lågklassade data,
- beslutet gäller endast användning med mänsklig granskning,
- beslutet ska omprövas efter sex månader,
- beslutet gäller endast om leverantörens databehandlingsvillkor uppfyller myndighetens krav,
- beslutet kräver att loggning och uppföljning är aktiverad.

## Vägval 1: Köpa, använda färdig tjänst eller bygga själv

Det första stora vägvalet är om myndigheten ska köpa en färdig tjänst, använda en plattformstjänst eller bygga en mer egen lösning.

### När färdig tjänst passar

En färdig tjänst passar när användningsfallet är vanligt, risknivån är låg till måttlig, informationsklassen är hanterbar och nyttan främst ligger i snabb införandehastighet.

Exempel kan vara:

- språkstöd för interna utkast,
- mötessammanfattning utan känsligt innehåll,
- allmänt skrivstöd,
- lågklassad intern produktivitet,
- avgränsad dokumenthantering där dataflöden och villkor är godkända.

För Aurora kan en färdig AI-assistent vara rimlig för administrativa uppgifter där sekretessbelagd information inte behandlas och där användningen styrs av tydliga riktlinjer.

### När plattformstjänst passar

En plattformstjänst passar när myndigheten behöver bygga egna AI-lösningar men vill använda etablerade tjänster för modeller, embeddings, orkestrering, drift, säkerhet eller observability.

Det passar särskilt när:

- flera användningsfall ska byggas på samma grund,
- myndigheten behöver API-styrd integration,
- säkerhets- och åtkomstkontroller kan konfigureras,
- utvecklingsteam ska kunna arbeta produktnära,
- drift och skalning inte ska byggas från grunden.

För Aurora kan detta vara relevant för ett kontrollerat RAG-baserat kunskapsstöd där myndigheten vill återanvända identitet, loggning, datakällor och AI-gateway.

### När egen lösning passar

Egen lösning passar när kraven på kontroll, datalokalitet, isolering, anpassning eller oberoende är höga. Det kan handla om egen modellservering, egen RAG-stack, egen inferensmiljö eller egen integrations- och policykomponent runt externa modeller.

Det är rimligt när:

- data är mycket skyddsvärda,
- driftmiljön måste vara starkt kontrollerad,
- leverantörsvillkor inte är acceptabla,
- myndigheten behöver detaljerad loggning och validering,
- kraven på reversibilitet och portabilitet är höga,
- användningsfallet är verksamhetskritiskt.

För Aurora kan egen drift eller starkt kontrollerad privat miljö vara relevant för riskanalys och verksamhetsnära beslutsstöd, men inte nödvändigtvis för all AI-användning.

### Fallgrop: bygg själv av principiell rädsla

En vanlig fallgrop är att myndigheten bygger själv för att man inte litar på externa tjänster, utan att först analysera driftkostnad, kompetens, säkerhetsansvar och livscykelhantering. Egen kontroll är inte gratis. Den flyttar ansvar från leverantör till myndighet.

En annan fallgrop är motsatsen: att köpa snabbt för att undvika komplexitet, men därmed flytta risker till avtalsvillkor, leverantörsinlåsning och bristande insyn.

## Vägval 2: Central eller federerad AI-plattform

Nästa vägval gäller om AI-förmågan ska byggas centralt, federerat eller som en kombination.

### När centralisering passar

Centralisering passar när myndigheten behöver gemensamma kontroller, gemensam loggning, gemensamma säkerhetsmönster och återanvändbar infrastruktur.

Det är särskilt lämpligt för:

- AI-gateway,
- identitet och åtkomst,
- modellkatalog,
- loggning och observability,
- policy enforcement,
- godkända modell- och leverantörsspår,
- gemensamma RAG-komponenter,
- standardiserad riskbedömning.

Aurora väljer att centralisera styrande byggblock eftersom de annars riskerar att få flera parallella vägar för modellåtkomst, loggning och dataexponering.

### När federation passar

Federation passar när verksamhetsområden har olika data, processer, kompetens och användningsfall, men ändå behöver följa gemensamma principer.

Det är rimligt för:

- verksamhetsspecifika kunskapsbaser,
- domänspecifika promptmallar,
- lokala produktteam,
- anpassade arbetsflöden,
- egna prioriteringar inom gemensam styrning.

För Aurora innebär detta att kontrollverksamheten, ärendehandläggningen och den administrativa stödfunktionen kan ha olika produktteam och lösningsmönster, men de använder gemensam AI-gateway, gemensam loggning och gemensamma godkännandeprocesser.

### Rekommenderad modell

För större myndigheter är en hybrid mellan central styrning och federerad utveckling ofta mest realistisk. Målarkitekturen bör därför skilja på:

- vad som måste vara gemensamt,
- vad som bör vara gemensamt,
- vad som kan vara lokalt,
- vad som inte får avvika.

Detta är ett viktigt arkitekturbeslut. Utan denna gräns blir centralisering lätt flaskhals och federation lätt fragmentering.

## Vägval 3: En modell eller flera modeller

AI-arkitektur diskuteras ofta som om organisationen måste välja en “huvudmodell”. I praktiken behöver större myndigheter ofta flera modellspår.

### När en begränsad modellkatalog passar

En begränsad modellkatalog passar när myndigheten vill minska komplexitet, förenkla styrning och skapa gemensam kompetens.

Fördelarna är:

- enklare säkerhetsgranskning,
- färre integrationsmönster,
- tydligare kostnadsuppföljning,
- enklare support,
- mer konsekvent användarupplevelse.

Detta passar tidigt i Auroras införande, när myndigheten behöver etablera styrning och minska oreglerad användning.

### När flera modeller behövs

Flera modeller behövs när användningsfallen skiljer sig väsentligt åt. En modell som är bra för textsammanfattning är inte nödvändigtvis bäst för klassificering, embeddings, kodstöd, språkstöd, bildanalys eller verksamhetsspecifik prediktion.

Flera modeller kan också behövas av skäl som:

- olika informationsklasser,
- olika driftmiljöer,
- olika språkkrav,
- olika kostnadsprofiler,
- olika förklarbarhetskrav,
- olika krav på latency och kapacitet.

Aurora bör därför inte sträva efter en enda modell för hela myndigheten. Den bör sträva efter en styrd modellkatalog med godkända modellspår, tydliga användningsvillkor och dokumenterade begränsningar.

## Vägval 4: Promptning, RAG, fine-tuning eller egen modellträning

Ett av de mest återkommande AI-besluten är hur mycket modellen ska anpassas till myndighetens kunskap och processer.

### När promptning räcker

Promptning räcker när uppgiften är generell, låg risk och inte kräver djup åtkomst till myndighetsspecifik kunskap. Det kan handla om att strukturera text, skapa utkast, formulera sammanfattningar av användarens egen text eller stödja idéarbete.

Promptning är snabbast att införa men svårast att styra om den används utan mallar, riktlinjer och loggning.

### När RAG är rätt

RAG är ofta rätt när lösningen behöver använda myndighetens dokument, regelverk, handböcker eller styrdokument utan att modellen tränas om.

RAG passar särskilt när:

- källor förändras över tid,
- svaret ska kunna kopplas till dokument,
- myndigheten vill minska hallucinationsrisk,
- kunskapen finns i interna dokument,
- det är viktigt att kunna uppdatera kunskapsbasen utan modellträning.

För Aurora är RAG ett naturligt mönster för intern kunskapssökning i styrdokument och handböcker.

### När fine-tuning är relevant

Fine-tuning kan vara relevant när modellen behöver anpassas till ett särskilt språkbruk, format, klassificeringsmönster eller domänbeteende som inte enkelt uppnås med promptning eller RAG.

Men fine-tuning löser inte alla problem. Den är inte rätt sätt att “lägga in fakta” som förändras ofta. Den kräver träningsdata, validering, versionshantering, utvärdering och tydlig livscykelhantering.

Aurora bör därför se fine-tuning som ett senare och mer kontrollerat steg, inte som standardlösning för kunskapsstöd.

### När egen modellträning är rimlig

Egen modellträning är normalt bara rimlig när myndigheten har mycket specifika krav, tillräckliga data, stark kompetens, tydlig nytta och resurser för långsiktig förvaltning.

Det kan vara relevant för specialiserade prediktiva modeller eller analysmodeller, men sällan som första steg för generativ AI.

## Vägval 5: Gemensam AI-gateway eller direkt modellåtkomst

En central fråga i målarkitekturen är om applikationer ska få anropa modeller direkt eller om all åtkomst ska gå via en gemensam AI-gateway.

### När direkt åtkomst kan accepteras

Direkt åtkomst kan accepteras i begränsade experiment, sandlådor eller lågklassade miljöer där risken är låg och syftet är lärande. Även där bör det finnas riktlinjer, kostnadskontroll och spårbarhet.

Direkt åtkomst bör däremot inte bli standard i produktionsmiljö.

### När AI-gateway behövs

En AI-gateway behövs när myndigheten vill styra modellåtkomst, logga anrop, maskera data, tillämpa policy, välja modellspår, hantera kvoter och samla observability.

För Aurora blir AI-gatewayen en av målarkitekturens viktigaste gemensamma komponenter. Den gör det möjligt att separera verksamhetsapplikationer från underliggande modellleverantörer och minska risken för inlåsning.

### Rekommendation

För en större statlig myndighet bör produktionssatta AI-lösningar normalt gå via en styrd åtkomstpunkt. Det behöver inte alltid vara en tekniskt avancerad gateway från dag ett, men målarkitekturen bör etablera mönstret tidigt.

## Vägval 6: Moln, on-premises eller hybrid för ett specifikt användningsfall

Kapitel 13 beskrev driftmodeller på övergripande nivå. I praktiken måste valet göras per användningsfall och per dataflöde.

### Moln när nytta, mognad och kontroll sammanfaller

Moln kan vara lämpligt när data och användningsfall tillåter det, när leverantörsvillkor är godkända, när säkerhetsfunktioner är tillräckliga och när myndigheten behöver snabb skalning eller tillgång till avancerade modellförmågor.

Det kan särskilt passa för låg- till medelriskanvändning, förutsatt att avtal, datalokalitet, loggning, åtkomstkontroll och styrning är hanterade.

### On-premises när kontrollkraven dominerar

On-premises kan vara lämpligt när data är mycket skyddsvärda, när extern behandling inte är acceptabel, när driftsäkerhetskrav kräver stark isolering eller när myndigheten behöver full kontroll över modell- och datamiljö.

Men on-premises kräver kapacitet för drift, patchning, modelluppdatering, säkerhetsövervakning, prestanda och kompetensförsörjning.

### Hybrid när användningsfallen skiljer sig åt

Hybrid är ofta mest realistiskt. Då kan lågklassade användningsfall använda godkända molntjänster, medan känsligare användningsfall hanteras i mer kontrollerade miljöer.

Aurora landar i att hybrid inte är en kompromiss av bekvämlighet, utan en medveten konsekvens av olika risknivåer.

## Exempel från Tullverket Aurora

Aurora skapar en beslutslogg för sin AI-målarkitektur. De första besluten är inte produktnamn utan styrande arkitekturbeslut.

| Beslut | Val | Villkor | Konsekvens |
|---|---|---|---|
| Plattformsmönster | Central styrning med federerade produktteam | Gemensam AI-gateway, loggning och risktriage | Team kan utveckla lokalt men inte kringgå gemensamma kontroller |
| Modellstrategi | Begränsad modellkatalog | Modeller godkänns per användningsklass | Minskar komplexitet och förenklar uppföljning |
| Kunskapsstöd | RAG före fine-tuning | Källor ska vara spårbara och åtkomststyrda | Passar styrdokument och handböcker |
| Driftmodell | Hybrid | Moln endast för godkända informationsklasser och villkor | Olika spår för olika risknivåer |
| Modellåtkomst | AI-gateway som målbild | Direkt åtkomst endast i sandlåda | Ger spårbarhet, policykontroll och leverantörsabstraktion |
| Bygga/köpa | Plattformstjänst där möjligt, egen kontroll där nödvändigt | Avvikelser dokumenteras som ADR | Undviker både överbyggande och okritisk SaaS-användning |

Denna beslutslogg blir inte statisk. Den blir ett levande styrinstrument. När nya användningsfall kommer in jämförs de med befintliga beslut. Om ett användningsfall kräver avvikelse skapas en ny ADR.

## Vägvalsfrågor

När arkitekten står inför ett AI-val bör följande frågor ställas innan produkt eller teknik väljs:

- Vilket användningsfall och vilken verksamhetsförmåga stödjer beslutet?
- Vilken AI-roll har lösningen: assistent, kunskapsstöd, beslutsstöd eller automatiserad aktör?
- Vilka data behandlas i promptar, filer, embeddings, loggar och modellutdata?
- Vilken informationsklass och rättslig risk gäller?
- Kräver lösningen mänsklig kontroll, motivering eller källspårbarhet?
- Är användningsfallet tillräckligt generellt för en färdig tjänst?
- Behöver myndigheten bygga ovanpå en plattformstjänst?
- Kräver användningsfallet egen drift eller stark isolering?
- Går beslutet att ompröva utan orimlig kostnad?
- Hur dokumenteras beslutet och vem äger uppföljningen?

## Vanliga fallgropar

- **Fallgrop: Att välja produkt före arkitekturspår.**
  - Varför det händer: Produktdemo och verksamhetstryck gör beslutet konkret.
  - Hur det undviks: Kräv use-case triage och arkitekturspår innan produktjämförelse.

- **Fallgrop: Att behandla alla AI-användningsfall lika.**
  - Varför det händer: Organisationen vill ha en enkel standard.
  - Hur det undviks: Dela upp användningsfall efter risk, data, AI-roll och konsekvens.

- **Fallgrop: Att dokumentera beslut utan konsekvenser.**
  - Varför det händer: Beslutsdokument blir ofta administrativa efterhandsprodukter.
  - Hur det undviks: Varje ADR ska innehålla konsekvenser, villkor och omprövningspunkt.

- **Fallgrop: Att göra beslutsmatrisen till en poängmaskin.**
  - Varför det händer: Poäng ger skenbar objektivitet.
  - Hur det undviks: Använd matrisen för resonemang, inte för att dölja ansvar.

- **Fallgrop: Att se hybrid som ett otydligt mellanläge.**
  - Varför det händer: Hybrid används ibland som ord för att slippa välja.
  - Hur det undviks: Definiera exakt vilka användningsfall, dataflöden och komponenter som hör hemma i respektive driftspår.

## Checklista

Använd denna checklista när ett nytt AI-vägval ska fattas.

- Är användningsfallet beskrivet utan produktnamn?
- Är AI-rollen tydlig?
- Är dataflödena identifierade, inklusive promptar, embeddings, loggar och utdata?
- Är informationsklassning och juridisk triage genomförd?
- Är användningsfallet placerat i ett godkänt arkitekturspår?
- Är minst två realistiska alternativ jämförda?
- Är konsekvenser, risker och beroenden dokumenterade?
- Är beslutet förenligt med arkitekturprinciperna?
- Är beslutet dokumenterat som ADR?
- Finns en ägare och en tidpunkt för omprövning?
- Finns villkor för när beslutet inte längre gäller?
- Är det tydligt vad som är gemensamt, lokalt och förbjudet?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Kapitlets viktigaste bidrag till målarkitekturen är att göra vägval styrbara. Målarkitekturen bör därför innehålla en tydlig beslutsmodell och en uppsättning obligatoriska ADR:er för AI.

Minst följande beslut bör finnas i målarkitekturen:

- godkända arkitekturspår för AI-användningsfall,
- strategi för köpa, använda plattformstjänst eller bygga själv,
- princip för central kontra federerad AI-förmåga,
- modellstrategi och modellkatalog,
- strategi för RAG, fine-tuning och egen modellträning,
- mönster för modellåtkomst och AI-gateway,
- driftmodell per informationsklass och användningsfall,
- krav på loggning, observability och uppföljning,
- villkor för undantag och avvikelser,
- process för omprövning av beslut.

När dessa beslut finns på plats blir målarkitekturen mer än en bild över tekniska komponenter. Den blir ett praktiskt styrinstrument som hjälper myndigheten att fatta konsekventa beslut när nya AI-behov uppstår.

För Tullverket Aurora innebär detta att varje nytt AI-initiativ inte börjar från noll. Det börjar med en fråga: vilket redan godkänt arkitekturspår passar detta användningsfall, och krävs ett nytt arkitekturbeslut?

## Snabb sammanfattning

- AI-målarkitektur behöver vägvalslogik, inte bara komponentbilder.
- Beslut bör utgå från användningsfall, data, risk och AI-roll innan produktnamn diskuteras.
- En ADR gör arkitekturbeslut spårbara, omprövningsbara och lättare att återanvända.
- Större myndigheter behöver ofta central styrning kombinerad med federerad utveckling.
- RAG, fine-tuning, promptning och egen modellträning löser olika problem och ska inte blandas ihop.
- AI-gateway är ofta ett centralt mönster för styrd modellåtkomst.
- Hybridarkitektur är rimlig när den är kopplad till tydliga informationsklasser och användningsfall.
- Beslutsmatriser ska stödja ansvarstagande resonemang, inte ersätta arkitektens bedömning.

## Nästa steg

Nästa kapitel går vidare från vägval till säkerhetsarkitektur. Där behandlas hot, skyddsåtgärder och driftsäkerhet i AI-lösningar, bland annat prompt injection, data leakage, red teaming, guardrails och incidenthantering. Kapitlet bygger direkt på de beslut som etablerats här: särskilt AI-gateway, modellåtkomst, driftspår, loggning och riskbaserad styrning.
