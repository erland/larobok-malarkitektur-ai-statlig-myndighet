# Faktaverifieringsrapport

## Datum

2026-06-02

## Syfte

Denna rapport dokumenterar faktaverifiering av de delar i boken som är mest beroende av aktuella regelverk, myndighetsvägledning, säkerhetsramverk och marknadsläge. Granskningen fokuserar på kapitel 4, 5, 13, 14, 16 och 17.

## Sammanfattning

Manusets huvudlinje är fortsatt hållbar: målarkitektur för AI i en större statlig myndighet bör börja med uppdrag, användningsfall, juridik, informationsklassning, riskstyrning och governance innan tekniska plattformsval görs.

Faktaverifieringen ledde till kompletteringar i sex kapitel. De viktigaste justeringarna är:

- AI Act beskrivs tydligare som ett stegvis och föränderligt regelverk där vissa delar redan gäller, andra tillämpas senare och vissa tidslinjer påverkas av EU:s förenklingsarbete.
- GDPR kopplas tydligare till hela AI-flödet, inklusive promptar, träningsdata, generativa AI-tjänster, biträden och eventuell tredjelandsåtkomst.
- Moln/on-premises/hybrid förstärks som en risk- och klassningsstyrd beslutsfråga, inte ett generellt teknikval.
- Plattformskapitlet förstärks med principen att målarkitekturen ska kravställa kategorier och kontrollpunkter snarare än låsa sig vid en statisk leverantörslista.
- Säkerhetskapitlet kompletteras med etablerade AI-specifika riskkategorier från OWASP och livscykelperspektiv från ENISA.
- Upphandlingskapitlet kompletteras med Diggs vägledning om generativ AI och LOU.

## Kontrollerade kapitel

| Kapitel | Område | Resultat |
|---|---|---|
| 4 | Juridik, ansvar och regelefterlevnad | Kompletterat med aktuell beskrivning av AI Act, stegvis tillämpning och regulatorisk bevakningspunkt. |
| 5 | Informationsklassning, dataskydd och riskstyrning | Kompletterat med tydligare GDPR-koppling till hela AI-flödet. |
| 13 | Moln, on-premises och hybrid | Kompletterat med eSam/IMY-baserad nyansering av molnfrågan. |
| 14 | Plattformar, produkter och ramverk | Kompletterat med NIST AI RMF, ISO/IEC 42001 och OWASP som stödjande ramverk. |
| 16 | Säkerhetsarkitektur för AI | Kompletterat med AI-specifika säkerhetsrisker och livscykelperspektiv. |
| 17 | Upphandling och leverantörsstyrning | Kompletterat med Diggs vägledning om köp av generativ AI enligt LOU. |

## Källor som användes

### EU AI Act och reglering

- Europeiska kommissionen, AI Act: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- AI Act Service Desk, implementation timeline: https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act
- Europeiska kommissionen, Digital Omnibus on AI Regulation Proposal: https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal
- Europeiska kommissionen, standardisering av AI Act: https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation

### Svensk offentlig förvaltning, GDPR och generativ AI

- Digg, Riktlinjer för generativ AI inom offentlig förvaltning: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai
- Digg, Köp generativ AI enligt lagen om offentlig upphandling: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai/kop-generativ-ai-enligt-lagen-om-offentlig-upphandling
- IMY, GDPR och AI: https://www.imy.se/verksamhet/ai/gdpr-och-ai/
- IMY, AI och tillämpning av GDPR: https://www.imy.se/verksamhet/dataskydd/innovationsportalen/vagledning-om-gdpr-och-ai/gdpr-och-ai/ai-och-tillampning-av-gdpr/
- IMY, Överföring av personuppgifter till tredjeland: https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/overforing-till-tredje-land/
- IMY, Användning av molntjänster inom offentlig sektor: https://www.imy.se/publikationer/anvandning-av-molntjanster-inom-offentlig-sektor--en-sammanstallning-av-en-undersokning-av-sju-myndigheter/

### Moln och digital infrastruktur

- eSam, Molnfrågan: https://www.esamverka.se/vad-vi-gor/molnfragan.html
- Digg, Ena – Sveriges digitala infrastruktur: https://www.digg.se/styrning-och-samordning/ena---sveriges-digitala-infrastruktur

### Risk, säkerhet och AI management

- NIST, AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- ISO, ISO/IEC 42001:2023: https://www.iso.org/standard/42001
- OWASP, Top 10 for Large Language Model Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- ENISA, Multilayer Framework for Good Cybersecurity Practices for AI: https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai

## Redaktionsbeslut

Boken ska inte presentera ovanstående källor som en fullständig rättsutredning. De används i stället för att säkra att arkitekturresonemangen är förenliga med aktuella offentliga riktlinjer och etablerade säkerhetsramverk.

AI Act-läget bör formuleras med försiktighet eftersom tidslinjer och stödjande standarder är under utveckling. Boken bör därför rekommendera regulatorisk bevakning och omprövningspunkter snarare än statiska datum i arkitekturbeslut.

## Kvarstående kontroll inför slutexport

- Juridiska formuleringar bör vid skarp användning granskas av jurist, dataskyddsombud och informationssäkerhetsansvarig.
- Produkt- och plattformsavsnitt bör betraktas som kategorier och beslutsstöd, inte som rekommendationer om specifika leverantörer.
- EPUB/PDF-export bör visuellt kontrolleras efter att omslag skapats.
