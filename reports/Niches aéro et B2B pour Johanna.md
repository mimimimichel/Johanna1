# Teste trois niches, n'en garde qu'une

**Explore en priorité trois niches : (1) un agent qui transforme les demandes de prix (RFQ) en devis pour les petits vendeurs de pièces aéro européens ; (2) un outil « contrat de service → facture » pour les PME qui vendent de la maintenance, de la location ou des prestations récurrentes ; (3) une matrice d'autorisations et de compétences pour les petits ateliers Part-145 et CAMO.** Sur une grille de 8 critères notée sur 50, elles obtiennent 37 à 38 points, devant 20 autres niches tirées des notes. Elles restent en tête sous les trois pondérations testées. Elles ont ce qui manquait à l'export control : elles s'appuient sur tes vraies compétences (devis, catalogue, quote-to-cash, pénuries aéro), répondent à une douleur chiffrée ou à un déclencheur daté (l'émission obligatoire de la facture électronique pour les PME au **01/09/2027**), et des acquéreurs rachètent déjà ce type d'outil. Le portail aftersales pour ETI industrielles fait jeu égal (38). Mais ses intégrations ERP et ses longs cycles de vente le réservent à l'après-2030, comme extension de la n° 2. Aucune de ces niches n'est validée : aucun prix n'a été testé auprès de clients, et le nombre de cibles (petits brokers, ateliers Part-145) reste inconnu. D'où la méthode : trois tests à moins de 2 k€ chacun d'ici mars 2027, puis une seule V1. Changer de niche améliore ton adéquation et réduit le risque employeur, mais ne change pas l'arithmétique. 10 M€ en 2036 exigent toujours ~2-4 M€ d'ARR, donc une suite de modules et une bascule à plein temps vers 2030.

> **Lecture.** Un lien entre parenthèses = fait sourcé. « (estim.) » = estimation tirée des notes ou de mon calcul, non validée par des clients. Toutes les notes de la grille sont mes jugements, argumentés à partir des notes de recherche.

## Devis aéro, facture de services, autorisations Part-145 : le podium

| Rang | Niche | /50 | Pourquoi elle |
|---|---|---|---|
| 1 | P1 · Agent devis, vendeurs de pièces aéro | 38 | Ton croisement rare : vente B2B × pénurie de pièces |
| 2 | B1 · Contrat de service → facture | 38 | Ton cœur de métier + échéance 09/2027 |
| 3 | A1 · Matrice d'autorisations Part-145 | 37 | Espace le plus libre, obligation réglementaire |
| 4 | B2 · Portail aftersales ETI | 38 | Meilleur plafond, trop lourd avant 2030 |
| 5 | P2 · Pré-contrôle des certificats de pièces | 35 | Aucun concurrent direct, module de 1 et 3 |

**P1 passe devant B1 à égalité de points pour trois raisons.** Sa douleur dure au-delà de 2030, alors que l'échéance de B1 ne joue qu'une fois. Son marché est international dès le départ, en anglais. Et peu de fondateurs savent à la fois digitaliser un devis et parler l'aftermarket aéro.

**P1 : la pénurie fabrique des devis.** La crise des pièces a coûté **plus de 11 Md$** aux compagnies en 2025 ([AVweb](https://avweb.com/aviation-news/airline-supply-chain-to-add-11-billion/)). Pour la deuxième année, les pénuries de matière sont le premier facteur de perturbation cité par les dirigeants MRO ([Oliver Wyman](https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html)). L'industrie répond par plus de stock, d'USM et de PMA, et par un « recours accru aux brokers et distributeurs » ([Oliver Wyman 2025](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)). Autant de RFQ et de devis en plus chez de petits acteurs. Rotabull prouve que des vendeurs paient pour répondre plus vite (clients affichés : AAR, Chromalloy, Magnetic MRO), mais vise surtout des vendeurs déjà équipés d'un ERP ([Rotabull](https://rotabull.com/)).

**B1 : la réforme oblige chaque PME à revoir son cycle devis-facture.** Les PME devront **émettre** leurs factures en électronique au 01/09/2027 ([Konformy](https://konformy.com/blog/facturation-electronique-2026-qui-est-concerne)). L'amende passe à **50 € par facture**, plafonnée à 15 000 €/an ([CAPEB](https://www.capeb.fr/actualites/des-sanctions-plus-severes-en-cas-de-non-respect-de-la-facturation-electronique-vesr0i)). La facture elle-même est déjà couverte par **163 plateformes agréées (PA)** ([Why](https://www.why.eu/facture-electronique/), éditeur). Le trou se situe en amont : catalogue de services, devis, indexation, facturation récurrente ou à l'usage. Aucun outil dédié n'a été trouvé, et un CPQ coûte **44 400 $/an en médiane** chez DealHub ([Vendr](https://www.vendr.com/marketplace/dealhub)). C'est presque mot pour mot ton expérience de vente de services.

**A1 : la réglementation crée l'obligation de tracer.** Chaque mécanicien, **y compris sous-traité**, doit voir sa compétence évaluée **avant son autorisation** ([UK CAA, AMC1 145.A.30(e)](https://regulatorylibrary.caa.co.uk/1321-2014/Content/AMC%20GM/AMC1%20145%20A%2030%20e%20Personnel.htm)). Écart d'audit classique : des évaluations qui existent sur le papier sans avoir été conduites ([Sofema FAQ](https://sofemafaq.netlify.app/knowledge/part-145-a-30-personnel-requirements/)). Les suites MRO couvrent le sujet, mais lourdement, et aucun outil léger centré EASA n'a été trouvé. Ton adéquation n'est que de 3/5 : il te faudra un ancien Quality Manager comme conseiller.

**Pourquoi B2 reste hors du top 3.** Il fait 38 points, mais seulement 2/5 en faisabilité et en automatisation : nomenclatures à nettoyer, intégrations ERP, cycles de vente de 3 à 9 mois (estim.). C'est la bonne extension de B1 après 2030, pas une V1 à 10 h par semaine.

### Séquence proposée : tester, trancher, construire

| Quand | Quoi | Budget |
|---|---|---|
| Nov. 2026-janv. 2027 | Test B1 d'abord (fenêtre 2027), P1 et A1 en parallèle | ≤ 2 k€ chacun |
| Fév.-mars 2027 | Gate : garder une seule niche | 0 |
| Avr.-sept. 2027 | V1 + 3-5 pilotes payants ; société créée au 1er encaissement | 6-19 k€ |
| 2028-2029 | 30-60 clients, ~0,1-0,2 M€ d'ARR (estim.) | autofinancé |
| 2030-2031 | Bascule plein temps si le gate 2029 est franchi | — |

**Critères du gate de mars 2027 (proposition).** Au moins 10 entretiens. Au moins 3 prospects sur 10 qui signent un pilote prépayé ou une lettre d'intention à ≥ 150 €/mois. Un gain de temps mesuré ≥ 50 % sur la tâche visée. Au moins ~1 000 cibles comptées en Europe. Les trois tests coûtent ≤ 6 k€ sur les ~25 k€ du moteur, et ~50 h chacun à 10 h/semaine (estim.). Aucun prêt avant la signature du prêt maison : tout reste autofinancé.

## La grille : huit critères, adéquation et plafond comptent double

| Code | Critère | 5/5 signifie |
|---|---|---|
| D | Douleur, urgence | douleur chiffrée + déclencheur daté |
| € | Capacité à payer | budget ≥ ~6 k€/an par client |
| Esp | Concurrence, espace libre | aucun concurrent direct trouvé |
| Fit ×2 | Adéquation à ton profil | cœur de tes compétences réelles |
| Fais | Faisabilité non-dev à 10 h/sem | V1 IA + freelance, vente et onboarding courts |
| Auto | Automatisation | self-serve, peu d'opérations |
| ARR ×2 | Plafond d'ARR, revente | ≥ 3 M€ plausible + acquéreurs identifiés |
| Risq | Risques réglementaires, juridiques, employeur | risque faible |

**Pourquoi ces poids.** L'adéquation compte double parce que la niche précédente a échoué sur ce point. Le plafond compte double parce qu'une sortie à 10 M€ demande ~2-4 M€ d'ARR : à cette taille, un SaaS bootstrappé se valorise autour de 4,8× l'ARR ([SaaS Capital](https://www.saas-capital.com/blog-posts/private-saas-company-valuations-multiples/)). **Règle éliminatoire :** une note de 1 en espace libre, en faisabilité ou en risque met la niche hors jeu, quel que soit son total.

Codes : **A** = aéro compétences et capacité, **P** = aéro pièces et supply chain, **B** = B2B vente, facturation et CX.

| Niche | D | € | Esp | Fit | Fais | Auto | ARR | Risq | /50 |
|---|---|---|---|---|---|---|---|---|---|
| P1 Devis pièces aéro | 4 | 3 | 2 | 5 | 3 | 4 | 4 | 4 | **38** |
| B1 Contrat → facture | 4 | 3 | 3 | 5 | 3 | 3 | 4 | 4 | **38** |
| B2 Portail aftersales | 3 | 4 | 3 | 5 | 2 | 2 | 5 | 4 | **38** |
| A1 Matrice autorisations | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | **37** |
| P2 Pré-contrôle certificats | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 3 | 35 |
| B4 Pricing light | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 35 |
| P4 Copilote AOG achat | 5 | 4 | 3 | 4 | 2 | 3 | 3 | 3 | 34 |
| B3 RFQ desk sous-traitants | 3 | 2 | 2 | 4 | 3 | 3 | 3 | 4 | 31 |
| B6 Questionnaires fourn. | 3 | 2 | 3 | 3 | 4 | 5 | 2 | 4 | 31 |
| B7 Voix du client B2B | 2 | 3 | 2 | 4 | 3 | 3 | 3 | 4 | 31 |
| A2 Passeport contractors | 4 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 30 |
| P3 Alertes SUP sur stock | 3 | 2 | 4 | 2 | 4 | 5 | 2 | 4 | 30 |
| P6 Indice prix/délais USM | 2 | 4 | 2 | 3 | 2 | 5 | 3 | 3 | 30 |
| A5 Capture du savoir | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 29 |
| A3 Prépa Part-66 en FR | 3 | 2 | 3 | 2 | 4 | 5 | 2 | 3 | 28 |
| B5 AO public vertical | 3 | 2 | 2 | 2 | 4 | 5 | 2 | 4 | 28 |
| A4 Assistant IA qualité | 3 | 2 | 2 | 2 | 4 | 4 | 2 | 3 | 26 |
| P5 Pièces alternatives | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 26 |
| A6 GPEC, recrutement | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 2 | 23 |
| ✗ B8 Saisie de commandes | 4 | 4 | 1 | 3 | 1 | 2 | 4 | 4 | 30 |
| ✗ A7 Copilote AMM/IPC | 5 | 4 | 1 | 3 | 1 | 3 | 4 | 1 | 29 |
| ✗ B9 Outils de cadrage | 1 | 1 | 1 | 4 | 4 | 5 | 1 | 3 | 25 |
| ✗ A8 Créneaux moteur | 5 | 5 | 1 | 2 | 1 | 1 | 2 | 3 | 24 |

Fit et ARR sont affichés sur 5 et comptés double dans le total. ✗ = hors jeu par la règle éliminatoire.

**Le classement résiste aux poids.** Avec des poids égaux (/40), A1 passe en tête (30), devant P1 et B1 (29), puis B2 (28). Avec la faisabilité aussi comptée double (/55), P1, B1 et A1 sont à égalité (41), devant B2 (40). Le top 4 reste le même dans les trois cas. Un point d'écart entre eux relève du bruit : ce sont les tests qui trancheront, pas la grille.

**Chaque famille a son profil.** La famille B colle le mieux à ton profil (adéquation 4-5 pour B1 à B4 et B7), mais ses marchés sont encombrés partout où l'IA banalise la tâche (saisie de commandes, mémoires d'AO, calcul de devis). La famille P concentre les douleurs les plus fortes (4-5 pour P1, P2 et P4). La famille A a peu de concurrence sur son créneau phare (A1), mais demande une expertise réglementaire que tu n'as pas. Le top 3 prend une niche par famille : tes tests diversifient le risque de marché.

## Cinq fiches : problème, offre, prix, faille, test

### P1 · Agent devis pour vendeurs de pièces aéro européens

**Problème.** Pour se protéger, les compagnies et les MRO stockent et achètent ailleurs : **69 %** ont augmenté leurs stocks de plus de 5 % ([Oliver Wyman 2025](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)). Les prix explosent sur les flottes régionales : la pale d'hélice ATR révisée est passée d'environ 55 k$ à plus de 105 k$ ([Aviation Week](https://aviationweek.com/mro/aircraft-propulsion/atr-strives-improve-parts-reuse-amid-global-shortage)). En hélicoptère, des délais de 3-6 mois sont passés à 6-12 mois, selon un article probablement de 2024 ([Vertical](https://verticalmag.com/features/chain-reaction-the-story-behind-the-helicopter-industrys-supply-chain-squeeze/?amp)). Le vendeur qui répond le premier gagne : Rotabull met en avant un délai moyen de réponse de **6 minutes** ([Rotabull](https://rotabull.com/)).

**Client cible.** Le dirigeant ou le responsable commercial d'un broker, d'un distributeur ou d'un MRO vendeur de 2 à 30 personnes en Europe. Il répond aux RFQ depuis Outlook et Excel, sans ERP intégré. Cette cible est déduite des notes et reste à valider.

**Offre.** Connexion à la boîte mail. Extraction de la référence (PN), de la quantité, de l'état (NE/OH/SV/AR), du certificat exigé et de l'urgence AOG. Rapprochement avec le stock exporté en CSV, brouillon de devis, relances, taux de transformation par client. Interface en français, anglais, espagnol, italien et allemand.

**Prix indicatif.** 150 à 600 €/mois (estim.).

**Concurrents et faille.** Rotabull regroupe les RFQ d'ILS, PartsBase et SkySelect, s'intègre à l'ERP Quantum et compte plus de 10 salariés sans levée trouvée ([Village.ai](https://village.ai/company/rotabull)). ePlane AI automatise les RFQ par email avec l'ERP Pentagon 2000 ([Newswire](https://www.newswire.com/news/pentagon-2000-and-eplane-ai-partner-to-automate-rfq-workflows-for-22614413)). AvSight, bâti sur Salesforce, a levé 20 M$ en 2023 ([Arcadea](https://www.arcadeagroup.com/avsight-announces-dollar20mm-strategic-growth-equity-investment-with-arcadea-group/)). **La faille :** tous visent des vendeurs déjà équipés d'un ERP ou de Salesforce. Les micro-vendeurs européens, multilingues et sans ERP, semblent peu servis (inférence à valider).

**Déclencheur.** Selon Oliver Wyman, la supply chain bridera la production d'avions **au moins jusqu'en 2030**, soit plus de 6 000 appareils non produits ([ARSA/Oliver Wyman](https://arsa.org/wp-content/uploads/2026/03/ARSA-OW-2026FleetMROMarketReport-ExecSum-2026.pdf)). Plus de la moitié des MRO n'attendent pas d'amélioration des délais moteur sous 3 ans ([Oliver Wyman](https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html)). Le rachat d'Unical et d'ecube par Satair, finalisé en mai 2026 (298 M$ de CA cumulé en 2024), montre que l'USM est devenu stratégique ([Cision/AAP](https://www.aap.com.au/aapreleases/cision20260511ae56600/)).

**Hypothèse la plus risquée.** Assez de petits vendeurs européens sans ERP paieront ≥ 150 €/mois plutôt que de passer à Rotabull, à leur ERP ou à un ChatGPT bricolé. Leur nombre est inconnu.

**Premier test (< 2 k€).** Liste 100 petits vendeurs à partir de sources publiques (associations professionnelles, LinkedIn). Ne scrape pas les marketplaces : leurs CGU n'ont pas été vérifiées. Mène 10-12 entretiens. Propose ensuite un pilote « concierge » à 3 vendeurs : ils te transfèrent 30-50 RFQ et leur export de stock, et tu renvoies les brouillons de devis en moins d'une heure, avec un LLM et un outil d'automatisation, sous un accord de traitement RGPD. Termine en demandant un pilote prépayé à 150 €/mois. Budget : ~1-1,5 k€ d'outils et de prospection (estim.).

**Garde-fous.** Traite seulement les RFQ que reçoit le client, c'est-à-dire ses propres données. Ne vise pas les clients de ton employeur.

**Trajectoire ARR (estim.).** 2027 : 3-5 pilotes, ~10-25 k€. 2029 : 25-40 clients, ~0,1-0,2 M€. 2033 : 0,8-1,5 M€. 2036 : 2-3 M€, seulement avec le Royaume-Uni ou les États-Unis et les modules P2, P3 et P6.

### B1 · Contrat de service → facture pour PME de services récurrents

**Problème.** Les PME qui vendent des contrats de maintenance, de la location ou des prestations récurrentes gèrent souvent leur catalogue, leurs devis et leurs révisions de prix dans Excel et Word (inférence). Une PA peut recevoir et émettre les factures, mais elle ne sait pas ce qu'il faut facturer. Les CPQ sont surdimensionnés : Salesforce CPQ coûte 75-150 $ par utilisateur et par mois ([Kugamon](https://www.kugamon.com/compare/pricing/dealhub/)). Aucun outil dédié à la « productisation » des services industriels n'a été trouvé : les PIM restent centrés sur le produit physique ([Catsy](https://catsy.com/blog/pim-software-for-industrial-product/) ; [Quable](https://www.quable.com/en/blog/a-pim-for-service-companies-but-what-for)).

**Client cible.** Le DAF ou le directeur commercial d'une PME de 5 à 100 M€ de CA, dans **un seul vertical** pour la V1. Mon hypothèse : maintenance industrielle ou multitechnique (contrats + interventions + compteurs), ou location de matériel.

**Offre.** Catalogue de services et paliers (bronze, silver, gold, avec un délai d'intervention garanti), grilles de prix et remises, devis et contrat, révision indexée (Syntec, indices INSEE), facturation récurrente ou à l'usage, envoi vers la PA du client par API. Le moteur de facturation peut s'appuyer sur Lago, un outil open source de fondateurs français qui a levé 22 M$ ([Sacra](https://sacra.com/c/lago/)), ce qui réduit le développement.

**Prix indicatif.** 200 à 800 €/mois (estim.).

**Concurrents et faille.** Sellsy (29-49 € par utilisateur et par mois) et Axonaut (~35-97 €/mois) sont des outils généralistes déjà immatriculés comme PA ([Hayot Expertise](https://hayot-expertise.fr/blog/evoliz-vs-sellsy-vs-axonaut-gestion-facturation-tpe-2026)). Pennylane a levé 175 M€ en janvier 2026, à plus de 3,5 Md€ de valorisation ([Maddyness](https://www.maddyness.com/2026/01/20/pennylane-nouvelle-levee-de-fonds-de-175-millions-deuros-pour-la-licorne-francaise/)). La facturation à l'usage, elle, vise surtout le SaaS : Chargebee démarre à 599 $/mois ([CostBench](https://costbench.com/compare/chargebee-vs-stripe-billing/)). **La faille :** personne ne traite le contrat de service industriel de bout en bout pour une PME.

**Déclencheur.** Réception obligatoire depuis le 01/09/2026, émission au 01/09/2027 pour les PME, sans nouveau report annoncé ([Konformy](https://konformy.com/blog/facturation-electronique-2026-qui-est-concerne) ; [Compta-online](https://www.compta-online.com/facturation-electronique-ao5562)). La date d'application des nouvelles amendes reste discutée (2026 ou 2027).

**Hypothèse la plus risquée.** Les PME paieront une couche séparée au lieu d'attendre que leur PA ou leur outil de facturation ajoute les contrats récurrents. Deuxième risque : la fenêtre ferme en septembre 2027, il faut donc une V1 vers mi-2027.

**Premier test (< 2 k€).** Mène 15 entretiens de DAF dans un vertical. Mets en ligne un simulateur en libre-service, « tes contrats sont-ils prêts pour septembre 2027 ? », et mesure les inscriptions. Ce doit être un outil, pas un diagnostic vendu, pour rester hors du conseil. Montre un prototype cliquable catalogue → devis → facture : un outil comme Lovable démarre à ~25 $/mois ([NxCode](https://www.nxcode.io/resources/news/lovable-vs-bolt-new-2026-ai-app-builder-comparison)). Contacte aussi 2-3 PA pour un partenariat API et de distribution. Budget : ~1-1,5 k€, dont ~500 € de publicité (estim.). Abandonne si plus de la moitié répondent « mon outil de facturation le fait déjà ».

**Garde-fous.** Ne deviens jamais PA. Branche-toi sur les PA existantes. Vendre un produit à des PME ne concurrence pas l'intégration de CPQ chez les grands comptes, mais fais-le confirmer par écrit.

**Trajectoire ARR (estim.).** 2027 : 5-10 clients, ~20-50 k€. 2029 : 40-60 clients, ~0,15-0,3 M€. 2033 : 1-1,7 M€. 2036 : 2-4 M€, seulement en ajoutant B2 pour les ETI et un deuxième pays.

### A1 · Matrice d'autorisations pour petits ateliers Part-145 et CAMO

**Problème.** Les personnels de certification doivent suivre une formation continue sur chaque période de 2 ans, facteurs humains compris ([EASA FAQ 19100](https://www.easa.europa.eu/en/faq/19100)). Plus de **40 %** des entreprises MRO voient l'attrition augmenter, et le coût de la main-d'œuvre progresse de **5,5-6 %/an** (+7,4 % en Europe pour la main-d'œuvre moteur) ([Consulting.us](https://www.consulting.us/news/13447/shortages-high-costs-loom-over-growing-aviation-maintenance-sector-oliver-wyman-survey)). Chaque nouvelle arrivée, salariée ou sous-traitée, doit être évaluée avant d'être autorisée.

**Client cible.** Le Quality Manager ou le dirigeant responsable d'un petit organisme Part-145, CAMO ou Part-147 : ateliers composants, stations de ligne, aviation d'affaires, hélicoptères. **79 %** des 5 039 entreprises MRO recensées sont des PME ([ARSA/Oliver Wyman](https://arsa.org/wp-content/uploads/2026/03/ARSA-OW-2026FleetMROMarketReport-ExecSum-2026.pdf)).

**Offre.** Registre des personnels (licences Part-66, qualifications de type), autorisations internes par tâche et par type, échéances (formation continue, facteurs humains, EWIS, CDCCL), évaluation au format GM3 avec preuves, alertes et export prêt pour l'audit. Ensuite : OCR des certificats, puis un contrôle « cette personne peut-elle signer cette tâche aujourd'hui ? ».

**Prix indicatif.** 2 à 4 k€ par an et par site, dans une fourchette de 1 à 6 k€ (estim.).

**Concurrents et faille.** ASA SAM existe depuis 1988 et sert plus de 60 opérateurs ([ASA](https://www.asasoftware.aero/software/sam)). OASES, AMOS, TRAX et Ramco sont des suites complètes et lourdes. eLeaP vise la FAA ([eLeaP](https://www.eleapsoftware.com/14-cfr-part-145-lms/)). Aviatize (29-89 $ par avion et par mois) vise les écoles de pilotage ([Capterra](https://www.capterra.com/p/10036917/Aviatize/)). **La faille :** aucun outil léger, à prix public, pensé d'abord pour l'EASA et disponible en français n'a été trouvé. Un éditeur note que les logiciels stockent les licences sans vérifier l'autorisation tâche par tâche ([OASES](https://www.oases.aero/blog/easa-part-145-software/), éditeur).

**Déclencheur.** La filière française prévoit **20 000 recrutements en 2026** ([GIFAS](https://gifas.fr/news/septembre-2026-aeronautique-et-spatial-une-rentree-placee-sous-le-signe-de-l-emploi)). Les AMC/GM Part-145 ont été amendés deux fois en 2026, et Part-IS s'applique depuis le 22/02/2026 ([EASA](https://www.easa.europa.eu/en/acceptable-means-compliance-and-guidance-material-group/part-145-maintenance-organisation-approvals), résumé de recherche).

**Hypothèse la plus risquée.** Assez de Quality Managers paieront 2-4 k€/an plutôt que de garder Excel. Le nombre d'organismes approuvés en Europe n'a pas été trouvé dans les notes.

**Premier test (< 2 k€).** Compte d'abord les organismes approuvés dans les listes publiques des autorités (France, puis 2-3 pays) : c'est gratuit. Paie un ancien Quality Manager Part-145 1-2 jours (~500-700 €/jour, estim.) pour bâtir un modèle Airtable conforme au GM3. Offre ce modèle en échange d'un entretien et vise 10-15 entretiens. Prévends ensuite le SaaS à 150-300 €/mois.

**Garde-fous.** RGPD sur des données RH, Part-IS pour l'hébergement. L'outil doit être décrit dans le manuel (MOE/CAME) du client, mais n'exige aucune approbation.

**Trajectoire ARR (estim.).** 2027 : 3-5 pilotes, ~10-20 k€. 2029 : 40-60 organismes, ~0,1-0,2 M€. 2033 : 0,75-1,5 M€. 2036 : 2-3 M€, seulement si l'Europe compte 1 000-1 500 cibles et si les modules A2 et A4 font monter le panier. Précédent de sortie : AAR a racheté l'outil de planification Aerostrat **15 M$ plus jusqu'à 5 M$** d'earn-out ([AAR](https://www.aarcorp.com/en/newsroom/press-releases/2025/aar-announces-acquisition-of-maintenance-planning-software-provider-aerostrat-expanding-capabilities-of-trax-subsidiary/)).

### B2 · Portail aftersales pour constructeurs de machines (après 2030)

**Problème.** La marge d'EBIT de l'aftermarket avoisine **25 %**, contre 10 % pour l'équipement neuf, et seuls **4 %** des OEM réussissent à générer du revenu récurrent de services numériques ([Entytle](https://entytle.com/installed-base-revenue-opportunity-missing/), éditeur citant McKinsey et BCG).

**Client cible.** Le directeur service ou aftersales d'un constructeur de machines de 20 à 500 M€ de CA, **hors aéro** pour éviter les clients de ton employeur.

**Offre.** Catalogue de pièces généré par IA à partir des nomenclatures et des vues éclatées, recherche par photo, panier et demande de devis vers l'ERP, base installée, relances de renouvellement de contrats. C'est le programme que tu as déjà mené chez un OEM.

**Prix indicatif.** 500 à 2 000 €/mois, plus des frais de mise en service (estim.).

**Concurrents et faille.** Syncron dépasse 100 k$/an et se déploie en 6-12 mois ([Growmax](https://www.growmax.io/blog/best-spare-parts-management-software), éditeur). Partium a levé 15 M$ ([Techleap](https://finder.techleap.nl/news/feed/partium-raises-15m-in-series-a)). Entytle a été racheté par RapidCanvas le 28/10/2026 ([GlobeNewswire](https://www.globenewswire.com/news-release/2026/10/28/3390266/0/en/rapidcanvas-acquires-entytle-to-bring-ai-driven-execution-to-the-industrial-aftermarket.html)). En bas de gamme, les catalogues coûtent 99 à 200 €/mois ([Slashdot](https://slashdot.org/software/3d-parts-catalog/saas/)). **La faille :** le milieu de marché.

**Déclencheur.** Aucun déclencheur réglementaire. Seule la consolidation du secteur (Entytle) signale l'intérêt des acquéreurs.

**Hypothèse la plus risquée.** Une ETI confie l'onboarding de données de nomenclature sales, sur un cycle de vente de 3 à 9 mois, à une fondatrice seule.

**Premier test (< 1 k€, plutôt en 2028-2029).** Mène 8-10 entretiens de directeurs service d'ETI hors aéro. Montre un catalogue généré par IA à partir d'une vue éclatée publique. Teste-le aussi auprès des clients B1.

**Trajectoire ARR (estim.).** Moins de 0,05 M€ avant 2030. 2033 : 0,7-1,2 M€. 2036 : 1,8-3 M€, avec un panier moyen d'environ 12 k€/an, le plus élevé du classement.

### P2 · Pré-contrôle IA des certificats de pièces à réception

**Problème.** Dans l'affaire AOG Technics, au moins 70 certificats de remise en service falsifiés couvraient environ 50 pièces CFM56 ([Gulf News](https://gulfnews.com/business/aviation/fake-spare-parts-supplied-to-fix-top-selling-jet-engines-1.97845403)). L'EASA a demandé aux opérateurs, MRO et distributeurs de vérifier leurs dossiers et de mettre en quarantaine les pièces douteuses ([EASA](https://www.easa.europa.eu/en/domains/aircraft-products/suspected-unapproved-parts/aircraft-parts-distributed-aog-technics)). L'IA générative s'est montrée efficace pour extraire des informations de documents non structurés ([Oliver Wyman 2025](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)).

**Client cible.** Le Quality Manager ou le responsable magasin d'un Part-145 ou d'une CAMO, ou un distributeur certifié EN 9120/ASA-100.

**Offre.** Le client dépose le PDF ou la photo du Form 1 / 8130-3 avec le bon de commande. L'outil extrait les blocs, contrôle la cohérence (PN, SN, quantité, statut, double libération, numéro d'agrément, dates), compare aux notices SUP, puis produit un score d'anomalie et un dossier d'audit horodaté. C'est un « second regard » : l'humain qualifié valide.

**Prix indicatif.** 200 à 800 €/mois, ou 0,5 à 3 € par document (estim.).

**Concurrents et faille.** Aeroxchange numérise les certificats, mais seulement dans son réseau ([Aeroxchange](https://corp.aeroxchange.com/?p=831)). Bluetail revendique plus de 30 M de documents, surtout en aviation d'affaires ([AIN](https://backend.ainonline.com/aviation-news/business-aviation/2026-08-27/bluetails-ai-platform-tops-30-million-aircraft-records)). ProvenAir travaille la traçabilité « back-to-birth » ([Preqin](https://www.preqin.com/data/profile/asset/provenair-technologies--inc-/1097209), à vérifier). **La faille :** aucun acteur trouvé sur le pré-contrôle du PDF entrant.

**Déclencheur.** L'affaire AOG Technics. S'y ajoute, selon une source secondaire de fiabilité moyenne, une alerte EASA de janvier 2026 sur des pièces détournées ([Airguide](https://hn.jakechampion.name/reader/https://airguide.info/europes-easa-warns-stolen-engine-parts-may-re-enter-supply-chain/)).

**Hypothèse la plus risquée.** Un faux négatif coûte cher. Les clients feront-ils confiance à l'outil, et une RC pro aéro restera-t-elle abordable ?

**Premier test (< 1,5 k€).** Récupère, avec accord, 50 certificats réels anonymisés auprès de 3 organismes, et glisse des anomalies dans 10 d'entre eux. Fais tourner un prototype LLM + règles et mesure ce qu'il détecte et ce qu'il rate. Fais valider les règles par l'ancien Quality Manager du test A1 : un seul conseiller pour deux tests.

**Trajectoire ARR (estim.).** En module de P1 ou de A1 : +20-40 % de panier. Seul : 0,1-0,2 M€ en 2029, 0,5-1 M€ en 2033, 1-3 M€ en 2036 avec la FAA et les États-Unis.

## Écartées ou repoussées : trois raisons reviennent

Trois motifs reviennent. Le premier : des marchés saturés et financés, où l'IA générique banalise la tâche. Le deuxième : des barrières de données ou de responsabilité (données OEM, navigabilité). Le troisième : un plafond ou des budgets trop bas pour viser 2-4 M€ d'ARR.

| Niche (score) | Verdict | Pourquoi |
|---|---|---|
| B4 Pricing light (35) | Module B1/B2 | Trou réel sous Pricefx (2 495 $/module/mois ([TrustRadius](https://www.trustradius.com/compare-products/pricefx))), mais douleur peu documentée |
| P4 Copilote AOG (34) | Plus tard | Intégrations multi-marketplaces, CGU inconnues ; SkySelect a levé 9 M$ ([AviTrader](https://avitrader.com/2026/03/13/skyselect-secures-us9m-to-transform-aviation-parts-procurement)) |
| B3 RFQ desk sous-traitants (31) | Écartée | Paperless Parts, > 800 clients ([Morsa](https://morsa.ai/guides/manufacturing-quoting-software)), et ≥ 5 offres IA françaises dont UsinIA ([UsinIA](https://usinia.fr/chiffrage-ia.html)) |
| B6 Questionnaires fournisseurs (31) | Réserve | Aucune donnée de marché ; plafond bas |
| B7 Voix du client B2B (31) | Module B2 | NPS saturé ; Unwrap à 24 k$/an ([Toolradar](https://toolradar.com/tools/unwrap)) |
| A2 Passeport contractors (30) | Module A1 | StaffNow, né chez Lufthansa Technik, en place ([Aviation Week](https://aviationweek.com/mro/workforce-training/staffing-digitally-mro-work-surges)) ; risque de requalification en travail temporaire |
| P3 Alertes SUP (30) | Aimant à prospects | Données publiques, mais plafond 0,3-1,5 M€ seul (estim.) |
| P6 Indice prix USM (30) | Plus tard | Exige les volumes de P1 ; IATA et Cirium déjà présents |
| A5 Capture du savoir (29) | Écartée | Vente longue, ROI difficile à prouver |
| A3 Prépa Part-66 (28) | Écartée | Plafond < 0,5 M€ en B2C FR (estim.) ; relecture par un licencié obligatoire |
| B5 AO public vertical (28) | Écartée | Plus de 15 outils ([Olra](https://olra.fr/blog/meilleurs-logiciels-reponse-appel-offres-2026)) ; Tenderbolt, rentable, > 200 clients ([The Media Leader](https://fr.themedialeader.com/?p=220572)) |
| A4 Assistant IA qualité (26) | Module A1 | Wingman360 occupe déjà l'espace ([Wingman360](https://wingman360.ai/insights/ai-assistant-for-part-145-and-camo-organisations)) |
| P5 Pièces alternatives (26) | Écartée | Données OEM protégées, enjeu de navigabilité |
| A6 GPEC, recrutement (23) | Écartée | Budgets faibles ; zone de conflit avec le conseil RH |
| ✗ B8 Saisie de commandes | Hors jeu | Canals a levé 35 M$ ([DSG](https://distributionstrategy.com/2026/05/canals-raises-35-million-to-expand-ai-automation-platform-for-wholesale-distributors/)) ; 19 éditeurs ([Y Meadows](https://www.ymeadows.com/en/insights/blog/ai-order-entry-vendors/)) |
| ✗ A7 Copilote AMM/IPC | Hors jeu | Données OEM sous licence, responsabilité du signataire, Zymbly (YC) en place ([YC](https://www.ycombinator.com/launches/PLV-zymbly-the-copilot-for-aircraft-maintenance)) |
| ✗ B9 Outils de cadrage | Hors jeu | WorkBoard a racheté Quantive ([BusinessWire](https://www.businesswire.com/news/home/20250528302450/en)) ; IA générique |
| ✗ A8 Créneaux moteur | Hors jeu | Les ateliers indépendants ne traitent que 15 % des déposes LEAP ([IBA](https://www.iba.aero/resources/articles/engine-mro-rising-demand-limited-capacity/)) |

Trois idées des notes deviennent des fonctions et non des produits : la planification sous contraintes de licences (module de A1), la valorisation « part-out » (sous-produit de P6) et le « CX CoE-in-a-box ». Ce dernier ressemble trop à du conseil, donc à un conflit avec ton employeur : intègre-le à l'onboarding d'un produit. Pour le copilote AMM, deux points pèsent en plus : l'EASA prévoit pour le T2 2027 la NPA qui intégrera ses règles d'IA dans la réglementation de navigabilité ([EASA](https://www.easa.europa.eu/document-library/notices-of-proposed-amendment/npa-2025-07)), et le sujet touche aux services digitaux d'Airbus.

## Synergies : une brique de devis, trois acheteurs, trois suites revendables

**Une même brique sert trois niches.** P1, B1 et B3 reposent sur le même cœur : devis, relances et suivi de la transformation. Si le premier marché déçoit, cette brique peut basculer vers le suivant sans repartir de zéro (inférence). C'est l'argument le plus fort pour commencer par un produit de devis.

**Trois acheteurs dessinent trois suites.** Une suite revendable, c'est-à-dire une porte d'entrée plus 2 à 4 modules vendus au même acheteur, est le moyen le plus plausible de passer d'un plafond de 1-2 M€ à 2-4 M€ d'ARR (estim.).

| Suite | Acheteur | Entrée | Modules | Acquéreurs |
|---|---|---|---|---|
| Vendeurs de pièces | Dir. commercial broker | P1 | P2, P3, P6 | CAMP, Rotabull, ERP pièces |
| Qualité Part-145 | Quality Manager | A1 | P2, A2, A4 | AAR/TRAX, éditeurs MRO |
| Services ETI | DAF, dir. service | B1 | B2, B4, B7 | Visma, TeamSystem, Pennylane |

Plusieurs de ces acquéreurs ont déjà racheté des outils proches. CAMP (groupe Hearst) a racheté ILS en 2019 ([Wikipedia](https://en.wikipedia.org/wiki/Inventory_Locator_Service)) puis un portefeuille de logiciels aviation en 2024 ([AviTrader](https://avitrader.com/2024/03/14/camp-systems-international-to-acquire-portfolio-of-aviation-software-businesses/)). AAR a racheté Aerostrat. Visma a racheté Evoliz (13 000 PME) ([Tech.eu](https://tech.eu/2025/02/05/visma-expands-into-france-with-evoliz-acquisition/)), TeamSystem a racheté Sellsy ([BusinessWire](https://www.businesswire.com/news/home/20250924851671/en/TeamSystem-Strengthens-Its-Presence-in-France-and-Spain-With-the-Acquisition-of-Sellsy-a-Leading-Cloud-Solutions-Specialist-for-SMEs)), et RapidCanvas a racheté Entytle. Rotabull, les ERP pièces et les éditeurs MRO autres qu'AAR restent des acquéreurs plausibles, sans opération documentée dans les notes.

**P2 relie deux suites.** Il intéresse à la fois le Quality Manager (A1) et le distributeur (P1). B1 peut aussi servir de pont : les petits MRO et ateliers aéro français sont des PME qui devront émettre leurs factures en électronique en 2027 (hypothèse de vertical, non vérifiée).

**Une audience peut alimenter chaque produit.** Un récapitulatif hebdomadaire gratuit des notices SUP de l'EASA et de la FAA (P3, données publiques) capterait des Quality Managers et des distributeurs, c'est-à-dire les acheteurs de A1 et P2. Du contenu en anglais sur la pénurie de pièces nourrirait P1. Le simulateur « septembre 2027 » nourrirait B1. Dans les trois cas, l'audience reste un canal, pas un actif revendable en soi.

**Les données augmentent la valeur de revente.** Un indice anonymisé des prix et des délais (P6), tiré des devis traités avec l'accord contractuel des clients, ferait la différence face à IATA et Cirium. Il faudra agréger les données, sans jamais échanger d'informations sensibles entre concurrents, pour respecter le droit de la concurrence.

**Racheter après 2030 : seulement en accélérateur.** Une fois le prêt maison signé et le produit rentable, ta holding peut racheter des actifs voisins. Par exemple un fournisseur de contenus Part-66 (la niche A3 rachetée plutôt que construite), un intégrateur de PA ou d'ERP pour PME dont les clients deviennent ceux de B1, ou un petit éditeur MRO régional. Ces rachats complètent la suite. Ils ne remplacent pas la croissance du produit.

## Conclusion

La grille montre où se trouve ton vrai avantage : **digitaliser une transaction (devis, facture, autorisation) dans un marché sous tension**. L'aéro seul ne suffit pas. Les niches qui vendent du conseil, du contenu ou de l'analyse générique (cadrage, AO, voix du client) chutent, car l'IA générique les banalise. Celles qui s'insèrent dans une transaction ou une obligation réglementaire tiennent. Avec des poids égaux, la niche la plus réglementée et la moins concurrencée (A1) passe en tête : si ton avantage de profil compte moins que prévu, c'est elle qui l'emporte. Ce sont donc les tests qui doivent décider, et B1 doit être testée en premier, car sa fenêtre se ferme en septembre 2027.

Le choix de niche pèse moins que deux décisions déjà prises. La première : construire une **suite**. Seule, chaque niche plafonne entre 1 et 4 M€ d'ARR, souvent sous 2 M€ (estim.). Au gate de mars 2027, choisis la niche dont la suite est la plus profonde et dont les acquéreurs achètent déjà, pas seulement celle qui marche le mieux en test. La seconde : la **bascule à plein temps**. Parmi les SaaS déjà monétisés, 25,1 % atteignent 1 M$ d'ARR en 5 ans ([ChartMogul](https://chartmogul.com/reports/saas-growth-the-odds-of-making-it/)), et les fondateurs à plein temps croissent ~30 % plus vite ([MicroConf](https://microconf.com/founders/0-10k-arr)). La probabilité d'atteindre 10 M€ reste donc faible, de l'ordre de quelques pourcents (estim.). L'issue réaliste en cas de réussite se situe entre 2 et 5 M€.
