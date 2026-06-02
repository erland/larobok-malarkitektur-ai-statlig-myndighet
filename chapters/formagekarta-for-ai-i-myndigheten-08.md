# Kapitel 8: Förmågekarta för AI i myndigheten

## Varför detta kapitel finns

En målarkitektur för AI blir lätt för teknisk om den börjar med modeller, molnplattformar, vektordatabaser eller ramverk. För en större statlig myndighet är det sällan där problemet börjar. Problemet börjar med att myndigheten behöver förstå vilka förmågor som krävs för att AI ska kunna användas säkert, rättssäkert, effektivt och långsiktigt.

En förmågekarta beskriver vad myndigheten behöver kunna göra. Den är inte samma sak som en systemkarta, en organisationskarta eller en produktkatalog. Den visar vilka förmågor som behövs från idé till avveckling: att identifiera användningsfall, bedöma risk, hantera data, välja modell, bygga lösning, testa, driftsätta, övervaka, följa upp och avveckla.

Förmågekartan är därför en bro mellan governance och teknik. Kapitel 7 beskrev hur beslut fattas. Detta kapitel beskriver vilka återkommande förmågor besluten ska styra.

## Arkitekturproblemet

Tullverket Aurora har efter de första kapitlens arbete fått ordning på portfölj, riskklasser, principer och beslutsforum. Ändå saknas något viktigt. Varje AI-initiativ beskriver fortfarande sina behov på olika sätt.

Ett team talar om en intern chattbot. Ett annat talar om semantisk sökning. Ett tredje vill ha prediktiv analys. Ett fjärde vill köpa en färdig AI-assistent. Alla behöver olika tekniska komponenter, men flera underliggande förmågor är gemensamma.

Auroras arkitekturgrupp formulerar därför en ny fråga:

> Vilka AI-förmågor behöver myndigheten etablera gemensamt, oavsett om den första lösningen blir en RAG-tjänst, ett analysstöd, en AI-assistent eller en mer traditionell maskininlärningsmodell?

Utan en förmågekarta riskerar myndigheten att bygga lösning för lösning. Det leder till dubblerade plattformar, otydligt ansvar, ojämn regelefterlevnad och en AI-portfölj som inte går att förvalta.

Med en förmågekarta kan myndigheten i stället visa vilka delar som bör vara gemensamma, vilka som kan vara lokala och vilka som måste utvecklas stegvis.

## Centrala begrepp

En förmågekarta beskriver stabila verksamhets- och teknikförmågor. Den bör vara mer långlivad än en viss produkt eller leverantör.

En AI-förmågekarta beskriver de förmågor som krävs för att identifiera, utveckla, driftsätta, använda, övervaka och avveckla AI-lösningar.

En capability model är den engelska termen för en strukturerad modell över organisationens förmågor. I den här boken används främst förmågekarta, men capability model kan förekomma när etablerade arkitekturmetoder diskuteras.

AI lifecycle betyder livscykeln för en AI-lösning, från idé och riskbedömning till drift, uppföljning och avveckling.

En gemensam förmåga är en förmåga som bör etableras en gång och återanvändas av flera AI-lösningar. Exempel är use-case triage, modellregister, AI-gateway, loggning, policy enforcement och produktionsgodkännande.

En lokal förmåga är en förmåga som kan finnas nära ett specifikt produktteam eller verksamhetsområde, till exempel domänspecifik promptdesign, verksamhetsvalidering eller handläggarnära förändringsledning.

## Rekommenderat angreppssätt

Förmågekartan bör tas fram innan den tekniska referensarkitekturen detaljdesignas. Annars finns risk att målarkitekturen börjar beskriva produkter i stället för förmågor.

Ett praktiskt angreppssätt är att arbeta i fem steg.

### Steg 1: Utgå från AI-livscykeln

Börja med att beskriva livscykeln som myndigheten måste kunna hantera. En enkel livscykel kan bestå av följande steg:

1. Idé och behov.
2. Use-case triage.
3. Juridisk och informationsmässig bedömning.
4. Arkitekturell vägledning.
5. Dataförberedelse.
6. Modell- eller tjänsteval.
7. Lösningsdesign.
8. Utveckling och konfiguration.
9. Test och validering.
10. Produktionsgodkännande.
11. Drift och övervakning.
12. Uppföljning och förbättring.
13. Incidenthantering.
14. Avveckling eller ersättning.

Livscykeln ska inte vara en tung projektmodell. Den ska visa vilka förmågor som alltid behöver finnas, även när olika användningsfall genomförs med olika metodik.

### Steg 2: Gruppera förmågorna

Nästa steg är att gruppera förmågor i ett fåtal områden. För en större myndighet är följande struktur användbar:

| Förmågeområde | Exempel på förmågor | Typisk ansvarstyngd |
|---|---|---|
| Styrning och portfölj | AI-portfölj, styrklassning, prioritering, beslutslogg | Verksamhetsledning, AI-governance och arkitektur |
| Juridik och regelefterlevnad | Juridisk triage, dataskydd, dokumentation, granskningsspår | Juridik, dataskydd, informationsägare |
| Risk och säkerhet | Informationsklassning, hotmodellering, säkerhetskrav, incidenthantering | Säkerhet, dataskydd, arkitektur och drift |
| Data och kunskap | Dataåtkomst, metadata, kvalitet, lineage, indexering, kunskapskällor | Informationsägare, dataförvaltning och produktteam |
| Modell och AI-tjänst | Modellval, modellregister, promptmönster, RAG, validering | AI-plattform, arkitektur och produktteam |
| Plattform och integration | AI-gateway, API:er, identitet, orkestrering, policy enforcement | Plattformsteam och integrationsarkitektur |
| Drift och livscykel | MLOps, LLMOps, observability, versionshantering, avveckling | Drift, plattformsteam och modellägare |
| Förändring och användning | utbildning, användarstöd, instruktioner, återkoppling, effektuppföljning | Verksamhet, produktägare och förändringsledning |

Tabellen är inte tänkt att bli organisationens nya linjestruktur. Den är ett arkitekturverktyg för att se vad som behöver etableras.

### Steg 3: Markera gemensamt, federerat och lokalt

Alla förmågor ska inte centraliseras. En AI-förmåga som blir för centraliserad skapar flaskhalsar. En AI-förmåga som blir för decentraliserad skapar risk, dubbelarbete och inkonsekvens.

Aurora använder därför tre nivåer:

| Nivå | Betydelse | Exempel |
|---|---|---|
| Gemensam | Ska finnas som myndighetsgemensam förmåga | AI-principer, AI-gateway, modellregister, produktionsgodkännande |
| Federerad | Ska följa gemensamma regler men utföras nära domänen | verksamhetsvalidering, riskbedömning, promptmönster, datakvalitet |
| Lokal | Kan lösas av enskilt team inom givna ramar | användarstöd, domänspecifika instruktioner, lokala nyttomått |

Det viktiga är inte att allt placeras rätt från början. Det viktiga är att målarkitekturen visar vilken styrmodell som gäller för varje förmåga.

### Steg 4: Koppla förmågor till styrklasser

Kapitel 7 införde styrklasserna A till D. Förmågekartan bör visa hur kraven ökar med styrklass.

En låg risk-lösning i klass A kan använda en godkänd standardplattform, förenklad granskning och en återanvänd referensarkitektur. En klass C-lösning kan kräva djupare juridisk bedömning, mer omfattande test, särskild loggning, striktare åtkomstkontroll och produktionsgodkännande i flera forum. En klass D-lösning kan kräva strategiskt beslut, särskild oberoende granskning och mycket tydliga krav på mänsklig kontroll.

Det innebär att samma förmågekarta används för alla AI-initiativ, men med olika djup.

### Steg 5: Identifiera gap och roadmap

När förmågekartan finns kan arkitekturgruppen markera nuläge, målbild och gap.

Ett enkelt mognadsspråk räcker ofta:

| Status | Betydelse |
|---|---|
| Saknas | Förmågan finns inte eller är informell |
| Fragmenterad | Förmågan finns i vissa team men inte gemensamt |
| Definierad | Förmågan är beskriven men inte etablerad i produktion |
| Etablerad | Förmågan används i flera initiativ |
| Förvaltad | Förmågan har ägare, mätetal, förbättringsprocess och finansiering |

Denna mognadsbedömning gör förmågekartan praktisk. Den visar vad som måste byggas först och vad som kan utvecklas senare.

## Exempel från Tullverket Aurora

Aurora tar fram sin första förmågekarta efter att tre användningsfall har prioriterats:

- intern kunskapssökning i styrdokument,
- sammanfattning av ärendehandlingar,
- prediktivt prioriteringsstöd för kontrollverksamhet.

Arkitekturgruppen upptäcker att användningsfallen är olika, men att de kräver flera gemensamma förmågor.

Intern kunskapssökning kräver kontrollerade kunskapskällor, RAG-mönster, behörighetsstyrd retrieval, loggning och användarstöd.

Sammanfattning av ärendehandlingar kräver hantering av personuppgifter, tydlig dataskyddsbedömning, striktare miljö, spårbarhet och rutiner för att inte sammanfattningen blir en otillåten beslutsgrund.

Prediktivt prioriteringsstöd kräver modellvalidering, träningsdatahantering, uppföljning av utfall, mänsklig kontroll, dokumentation av modellversioner och tydlig ansvarskedja.

Aurora ser att en produkt per användningsfall inte räcker. Myndigheten behöver minst följande gemensamma eller federerade förmågor:

| Förmåga | Nuläge | Målbild |
|---|---|---|
| AI-portföljstyrning | Fragmenterad | Gemensam portfölj med styrklasser och prioritering |
| Use-case triage | Definierad | Etablerad som obligatorisk första grind |
| Juridisk triage | Fragmenterad | Återanvändbar process kopplad till AI-portföljen |
| Informationsklassning av AI-flöde | Definierad | Etablerad för data, promptar, svar, embeddings och loggar |
| AI-gateway | Saknas | Gemensam kontrollerad åtkomstpunkt till modeller och AI-tjänster |
| Modell- och tjänsteregister | Saknas | Gemensam överblick över modeller, tjänster, versioner och villkor |
| RAG-förmåga | Fragmenterad | Gemensamma mönster för retrieval, indexering och behörighet |
| Test och validering | Fragmenterad | Riskbaserade testkrav per styrklass |
| Observability för AI | Saknas | Loggning, mätning, larm och uppföljning för AI-lösningar |
| Avveckling | Saknas | Krav på exit, datahantering och ersättning av modeller eller tjänster |

Detta blir inte den tekniska referensarkitekturen ännu. Det blir underlaget för nästa steg: att beskriva vilka byggblock som måste stödja förmågorna.

## Vägvalsfrågor

När en myndighet tar fram sin AI-förmågekarta bör arkitekten ställa följande frågor:

1. Vilka AI-användningsfall ska förmågekartan kunna stödja under de kommande två till tre åren?
2. Vilka förmågor krävs för alla användningsfall, oavsett teknik?
3. Vilka förmågor bör vara gemensamma för hela myndigheten?
4. Vilka förmågor bör vara federerade till verksamhetsområden eller produktteam?
5. Vilka förmågor får vara lokala, och vilka miniminivåer gäller då?
6. Vilka förmågor är redan etablerade i befintlig IT-, data- eller säkerhetsorganisation?
7. Vilka förmågor saknas helt?
8. Vilka förmågor behöver etableras innan den första produktionssättningen?
9. Vilka förmågor kan växa fram under kontrollerade piloter?
10. Hur ska förmågekartan kopplas till finansiering, ansvar och roadmap?

Den sista frågan är ofta avgörande. En förmågekarta utan finansiering och ansvar blir en presentation. En förmågekarta med ansvar, mognadsbedömning och roadmap blir ett styrande arkitekturunderlag.

## Vanliga fallgropar

- **Fallgrop: Att rita system innan förmågor.**
  - Varför det händer: Teknikval känns mer konkret än förmågemodellering.
  - Hur det undviks: Beskriv först vad myndigheten behöver kunna göra, sedan vilka byggblock som stödjer det.

- **Fallgrop: Att göra förmågekartan till organisationsschema.**
  - Varför det händer: Förmågor och ansvar blandas ihop.
  - Hur det undviks: Visa ansvar separat. En förmåga kan kräva flera roller och forum.

- **Fallgrop: Att centralisera allt.**
  - Varför det händer: AI-risker gör att organisationen vill kontrollera varje detalj.
  - Hur det undviks: Skilj på gemensamma, federerade och lokala förmågor.

- **Fallgrop: Att låta varje pilot bygga egen livscykel.**
  - Varför det händer: Piloter drivs snabbt och lokalt.
  - Hur det undviks: Kräv gemensam miniminivå för triage, risk, loggning, test och produktionsgodkännande.

- **Fallgrop: Att glömma avveckling.**
  - Varför det händer: Fokus ligger på att komma igång.
  - Hur det undviks: Lägg in avveckling, modellbyte och exit som egna förmågor redan i målarkitekturen.

## Checklista

En AI-förmågekarta för en större myndighet bör minst besvara följande:

- Finns en tydlig AI-livscykel från idé till avveckling?
- Är förmågorna grupperade så att både styrning, juridik, säkerhet, data, teknik, drift och användning täcks?
- Framgår vad som är gemensamt, federerat och lokalt?
- Är förmågorna kopplade till styrklasser eller risknivåer?
- Finns en nulägesbedömning av varje viktig förmåga?
- Finns en målbild för vilka förmågor som ska vara etablerade inom 6, 12 och 24 månader?
- Har varje prioriterad förmåga en ansvarig ägare eller mottagare?
- Är förmågekartan oberoende av en viss leverantör eller produkt?
- Kan förmågekartan användas som underlag för referensarkitektur och plattformsval?
- Finns avveckling, incidenthantering och uppföljning med från början?

## Övergång till nästa kapitel

Det här kapitlet visar vilken del av målarkitekturen som behöver vara tydlig innan nästa vägval görs. I nästa kapitel byggs resonemanget vidare så att Tullverket Aurora stegvis går från princip och struktur till genomförbar AI-förmåga.

## Koppling till målarkitekturen

Förmågekartan är en central del av målarkitekturen. Den visar inte exakt hur lösningen ska byggas, men den visar vilka byggblock, processer, roller och styrmekanismer som måste finnas.

För Tullverket Aurora blir förmågekartan ett sätt att undvika tre vanliga misstag:

1. Att göra AI till en ren plattformsfråga.
2. Att låta varje användningsfall skapa sin egen infrastruktur.
3. Att underskatta de förmågor som behövs efter första produktionssättningen.

Nästa kapitel går vidare till dataarkitekturen. Där blir frågan mer konkret: vilka datakällor, metadata, åtkomstmodeller, index, kunskapsbaser och datakvalitetsförmågor krävs för att AI-förmågan ska fungera i praktiken?
