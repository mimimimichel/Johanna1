# Pénurie de pièces aéro (aftermarket) et supply chain : niches logiciel / agent IA / data pour Johanna (état au 29/10/2026)

Contexte rappelé : Johanna est consulting manager produit/innovation à Toulouse et n'est pas développeuse. Elle a 10 h/semaine et 6 à 25 k€ pour une V1. Son objectif est un produit vendu (pas du conseil) visant 1 à 4 M€ d'ARR, revendable d'ici 2036, 100 % légal en France et dans l'UE.

Conventions :
- $ = dollars US, sans conversion. Md = milliard.
- « Secondaire » = blog, agrégateur ou site d'un éditeur concurrent (ex. ePlaneAI republie beaucoup de news), pas la source primaire.
- « Inférence » = mon raisonnement, non sourcé.
- Les chiffres d'avant 2025 sont signalés.
- cfnews.net n'a pas été utilisé.

## Q1. Quelles données dures 2024-2026 sur la crise des pièces aftermarket (coûts AOG, délais, USM, moteurs, impact compagnies/MRO) ?

### Takeaway
La crise est documentée par des sources primaires solides (IATA, Oliver Wyman) :
- Elle coûte plus de 11 Md$ aux compagnies en 2025.
- Pour la 2e année, les pénuries de matière sont le disrupteur n°1 cité par les dirigeants MRO.
- Les délais de remise en état (TAT) se dégradent sur presque toutes les familles de pièces, et un TAT moteur narrowbody dépasse 180-200 jours.
- La réponse dominante reste de stocker davantage, avec un recours accru aux USM, PMA, brokers et distributeurs, ce qui multiplie les transactions, les devis et les certificats à traiter.

Le marché USM pèse environ 8-9 Md$ selon la plupart des cabinets, avec une croissance de 3-6 %/an, mais les estimations divergent fortement.

### Cited Findings
**Coût global pour les compagnies (IATA × Oliver Wyman, octobre 2025)**
- Le rapport IATA/Oliver Wyman *Reviving the Commercial Aircraft Supply Chain* (oct. 2025) estime le surcoût des problèmes de supply chain pour les compagnies à plus de 11 Md$ en 2025 (AVweb donne 11,3 Md$). Il se décompose ainsi :
  - environ 4,2 Md$ de surconsommation de carburant (avions anciens maintenus en service) ;
  - environ 3,1 Md$ de maintenance supplémentaire ;
  - environ 2,6 Md$ de location de moteurs ;
  - environ 1,4 Md$ de stock de pièces supplémentaire.
  — [AVweb](https://avweb.com/aviation-news/airline-supply-chain-to-add-11-billion/) ; [TravelMole](https://www.travelmole.com/news/supply-chain-challenges-burden-airlines)
- Ce même rapport recommande une meilleure visibilité de bout en bout de la supply chain, plus de maintenance prédictive, des pools de pièces partagés, davantage de capacité de réparation et l'usage de pièces alternatives (PMA, USM) — [AVweb](https://avweb.com/aviation-news/airline-supply-chain-to-add-11-billion/)

**Enquête MRO Oliver Wyman 2026 (publiée avril 2026, plus de 150 répondants, ~70 % hors Amérique du Nord)**
- Le marché MRO mondial a dépassé 136 Md$ en 2025 (+8 % vs 2024). La prévision est d'environ 193 Md$, à horizon « fin de décennie » sur la page article et « 2036 » sur une page liée, une incohérence à signaler. Le moteur représente plus de la moitié de la dépense MRO — [Oliver Wyman, avr. 2026](https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html)
- Pénuries de matière et de main-d'œuvre et maîtrise des coûts restent les disrupteurs n°1. Géopolitique et tarifs douaniers entrent en 2e position. L'adoption de l'IA générative est 5e — [Oliver Wyman, avr. 2026](https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html)
- En 2025, l'inflation du coût matière a dépassé les attentes de 100 à 200 points de base selon les segments. Environ 90 % des répondants subissent un impact des tarifs douaniers, surtout sur les achats de composants, les réparations et les révisions moteur — [Oliver Wyman, avr. 2026](https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html)
- Sur les moteurs :
  - le TAT moteur narrowbody atteint régulièrement 180-200 jours ou plus chez beaucoup d'opérateurs ;
  - plus de la moitié des répondants n'attendent pas d'amélioration dans les 3 ans, voire jamais ;
  - deux tiers disent que le coût des visites atelier des moteurs de nouvelle génération dépasse leurs attentes d'au moins 21 %, et un quart d'au moins 50 %.
  — [Oliver Wyman, avr. 2026](https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html)
- L'inflation des taux de main-d'œuvre s'est installée à 5,5-6,0 %/an, contre environ 3 % avant la pandémie — [Oliver Wyman, avr. 2026](https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html)
- Sur l'IA : 58 % des répondants sont au stade « expérimental », comme l'an dernier. Deux tiers jugent la valeur obtenue conforme ou supérieure aux attentes. La moitié prévoit d'investir dans l'IA sur 5 ans, mais seulement un tiers dans l'infrastructure IT — [Oliver Wyman, avr. 2026](https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html)

**Enquête MRO Oliver Wyman 2025 (PDF primaire, 172 répondants)**
- Le marché MRO était de 114 Md$ en 2024 (+7,2 % vs pic 2019, en dollars constants), avec 120 Md$ prévus pour 2025 et 156 Md$ en 2035 (+2,7 %/an) — [Oliver Wyman MRO Survey 2025 (PDF hébergé par AAR)](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)
  - ⚠️ Écart avec les « 136 Md$ en 2025 » de l'édition 2026 : probable changement de périmètre ou de méthode, non expliqué dans la page consultée.
- « Pénuries de matière » est entré dans le questionnaire en 2025 et s'est classé disrupteur n°1, cité par plus des deux tiers des répondants. Plus de la moitié pensent que les problèmes de supply chain dureront encore au moins 18 mois, et 14 % les jugent permanents — [OW 2025 PDF](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)
- Pour retrouver confiance, deux tiers ou plus des répondants demandent trois choses : performance fournisseur plus régulière (moins de volatilité des délais), meilleure disponibilité des stocks et délais réduits — [OW 2025 PDF](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)
- Inflation matière 2024 : 6,5 % attendus, 7,7 % constatés (8,3 % l'année précédente), 6,3 % projetés pour 2025 — [OW 2025 PDF](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)
- Part des répondants voyant le TAT se dégrader sur l'année : moteurs/APU 75 %, intérieurs 61 %, avionique 60 %, trains 60 %, structures 58 %, hydraulique/pneumatique 50 %, visites cellule 49 %, roues/freins 43 %. La disponibilité des pièces détachées (« piece part availability ») est la 1re cause citée, devant le manque de capacité de réparation et de compétences — [OW 2025 PDF](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)
- Leviers cités : PMA, pièces produites par l'opérateur (OOPP), achat de moteurs ou d'avions entiers, et « recours accru aux brokers et distributeurs ». La réponse dominante reste toutefois le stock : 69 % ont augmenté leurs stocks de plus de 5 %, certains de plus de 15 %. Plus de la moitié prévoient de ne réduire leurs stocks que légèrement quand la situation se normalisera — [OW 2025 PDF](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)
- L'IA progresse :
  - adoption passée de 58 % à 64 % ;
  - 58 % voient la valeur attendue réalisée ou dépassée, contre 20 % l'année précédente ;
  - l'IA générative s'avère efficace pour parser et catégoriser des données et extraire des informations de documents non structurés (CMM, service bulletins) ;
  - 52 % des MRO/OEM appliquent l'IA aux prévisions de matière/stock, contre 38 % des opérateurs.
  — [OW 2025 PDF](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)

**Moteurs (IATA × Emerton, 24 juin 2026)**
- Les avions à moteurs Pratt & Whitney GTF cloués au sol ont culminé à 648 en mars 2025, soit 28 % de la flotte GTF, en attente de visite atelier, de moteur de rechange ou de pièces — [IATA, communiqué 24/06/2026](https://www.iata.org/en/pressroom/2026-releases/06-24-urgent-action-needed-to-ease-engine-mro-bottlenecks/)
- Visites atelier LEAP : environ 600-800 en 2025, plus de 5 000/an à l'horizon 2040. GTF : environ 1 000 en 2025, plus de 2 000 ensuite — [IATA](https://www.iata.org/en/pressroom/2026-releases/06-24-urgent-action-needed-to-ease-engine-mro-bottlenecks/)
- Recommandations IATA :
  - accélérer l'approbation des réparations (moins de rebut) ;
  - étendre la production sous licence ;
  - récupérer davantage d'USM issues des démontages (teardowns) de moteurs ;
  - garantir un accès équitable au MRO ;
  - négocier des catalogues de pièces à prix prévisibles.
  L'accord IATA-CFM a été renouvelé en janvier 2026 — [IATA](https://www.iata.org/en/pressroom/2026-releases/06-24-urgent-action-needed-to-ease-engine-mro-bottlenecks/)
- Un site secondaire, non daté et peu fiable, évoque 835 avions GTF stockés, soit environ un tiers de la flotte — [Aeroxplorer](https://aeroxplorer.com/articles/gtf-storage-crisis-deepens-835-aircraft-grounded-as-pratt-whitney-recalls-surge-postmidyear)

**Coût d'un AOG**
- Selon une estimation de Boeing reprise par Wikipédia (date non précisée), un AOG de 1-2 h coûte 10 000 à 20 000 $, et jusqu'à 150 000 $/h selon l'avion et la route — [Wikipedia, Aircraft on ground](https://en.wikipedia.org/wiki/Aircraft_on_ground)
- Les fourchettes « 10 k$/h narrowbody, 150 k$/h widebody » viennent de blogs d'éditeurs qui se citent entre eux (secondaire). Aucun benchmark primaire 2025 n'a été trouvé — [Aircargoweek](https://aircargoweek.com/the-real-cost-of-aog/) ; [Proponent](https://www.proponent.com/?p=40475)

**Délais et prix : régional, hélicoptère**
- ATR :
  - le prix d'une pale d'hélice ATR révisée est passé d'environ 55 000 $ à plus de 105 000 $ (article Aviation Week, date non visible) — [Aviation Week](https://aviationweek.com/mro/aircraft-propulsion/atr-strives-improve-parts-reuse-amid-global-shortage)
  - ATR a livré 32 avions en 2025 (3 de moins qu'en 2024), pour un carnet de 160 — [FlightGlobal](https://www.flightglobal.com/aerospace/atr-misses-2025-delivery-target-despite-strong-order-intake/166356.article)
  - ATR dit avoir ramené ses pénuries de pièces à environ un tiers du niveau de début 2025 — [Aviation24](https://www.aviation24.be/manufacturers/atr/atr-reports-strong-2025-demand-prepares-2026-production-ramp-up/amp/)
- Hélicoptères :
  - des pièces habituellement à 3-6 mois sont passées à 6-12 mois, et les pièces critiques liées aux pièces de fonderie à 12-18 mois (article Vertical, probablement 2024) — [Vertical Magazine](https://verticalmag.com/features/chain-reaction-the-story-behind-the-helicopter-industrys-supply-chain-squeeze/?amp)
  - en janvier 2024, les opérateurs Robinson devaient compter 24 mois pour les nouvelles commandes de moteurs et cylindres Lycoming (pré-2025) — [HeliHub](https://www.helihub.com/2024/01/23/rotorcorp-warns-robinson-operators-of-lycoming-backlog-implications/)
  - en janvier 2026, le rapport Rotortrade sur 2025 relève une forte demande, de longs délais OEM et des stocks limités — [AIN, 30/01/2026](https://backend.ainonline.com/aviation-news/business-aviation/2026-01-30/rotortrade-report-flags-strong-demand-tight-supply)

**USM, PMA et marché des pièces**
- Les estimations du marché USM « air transport » divergent :
  - Fortune Business Insights : 8,55 Md$ en 2025, 12,93 Md$ en 2034 (TCAC 4,7 %), Amérique du Nord 34,85 % — [Fortune BI](https://www.fortunebusinessinsights.com/air-transport-usm-market-109639)
  - Market Glass : 8,4 Md$ en 2025, 11,3 Md$ en 2032 — [Research and Markets](https://www.researchandmarkets.com/reports/5140944/air-transport-usm-global-strategic-business)
  - Stratview : 8,8 Md$ en 2024, 9,0 Md$ en 2025, TCAC 2,6 % — [Stratview](https://www.stratviewresearch.com/2739/air-transport-USM-market.html)
  - Verified Market Research : 5,08 Md$ en 2025 — [VMR](https://www.verifiedmarketresearch.com/product/air-transport-usm-market/)
  - TechSci : 2,93 Md$ — [TechSci](https://techsciresearch.com/report/air-transport-usm-market/22325.html)
  - Cabinets de « market research » génériques, à méthodologie opaque.
- Marché total des pièces aftermarket : 54,4 Md$ en 2025, 93,5 Md$ en 2032 (Fortune BI). Les PMA seraient la catégorie la plus dynamique (TCAC 11,2 % sur 2025-2034, selon GMI) — [Fortune BI](https://www.fortunebusinessinsights.com/segmentation/aircraft-aftermarket-parts-market-105451) ; [GMI](https://www.gminsights.com/ja/industry-analysis/aircraft-aftermarket-parts-market)
- Le spécialiste USM devient un actif stratégique pour les OEM :
  - Satair (Airbus) a finalisé en mai 2026 le rachat d'Unical Aviation et d'ecube (démontage et stockage d'avions), annoncé en novembre 2025, montant non divulgué.
  - Unical et ecube réunis : 298 M$ de CA en 2024, 413 salariés, 7 sites.
  — [Communiqué Satair via AAP/Cision](https://www.aap.com.au/aapreleases/cision20260511ae56600/)
- TransDigm a racheté Jet Parts Engineering (PMA) et Victor Sierra pour environ 2,2 Md$ en 2026 (source secondaire) — [Panabee](https://www.panabee.com/news/transdigm-to-acquire-two-aerospace-aftermarket-leaders-for-2-2-billion)
- Selon AeroDynamic Advisory, la dépense MRO annuelle a augmenté de 40 % depuis 2019 pour soutenir 10 % de capacité mondiale en plus. Ce chiffre vient d'un extrait indexé d'un article payant, non vérifié dans le texte complet — [Aviation Week, 22/01/2026](https://aviationweek.com/mro/supply-chain/early-2026-outlook-shows-mro-market-momentum-increasing)

**Pièces non approuvées et traçabilité (risque documentaire)**
- Affaire AOG Technics (2023) :
  - au moins 70 certificats de remise en service (ARC) falsifiés couvrant environ 50 pièces CFM56 (737NG/A320ceo), avec aussi des pièces CF6 concernées ;
  - CFM a ensuite parlé de 126 moteurs touchés ;
  - l'EASA a demandé aux opérateurs, MRO et distributeurs de vérifier leurs dossiers et de mettre en quarantaine les pièces dont l'authenticité du certificat ne peut être vérifiée.
  — [Gulf News](https://gulfnews.com/business/aviation/fake-spare-parts-supplied-to-fix-top-selling-jet-engines-1.97845403) ; [FlightGlobal](https://www.flightglobal.com/safety/cfm-scrutinises-data-from-suspect-distributor-in-hunt-for-unapproved-engine-parts/155256.article) ; [EASA – AOG Technics](https://www.easa.europa.eu/en/domains/aircraft-products/suspected-unapproved-parts/aircraft-parts-distributed-aog-technics)
- Fin janvier 2026, un lot de pièces moteur destiné à la destruction aurait été détourné par un tiers se faisant passer pour le prestataire de destruction. L'EASA aurait appelé compagnies, MRO et distributeurs à vérifier leurs stocks contre les numéros de série publiés. Source secondaire relayée par un miroir, fiabilité moyenne — [Airguide (miroir)](https://hn.jakechampion.name/reader/https://airguide.info/europes-easa-warns-stolen-engine-parts-may-re-enter-supply-chain/)
- Titre d'un article de décembre 2024 : « plus de 7 700 pièces suspectes, l'EASA face à un défi pour réguler la supply chain » (secondaire, contenu non lu) — [SAS Sofia](https://sassofia.com/blog/with-over-7700-suspect-parts-easa-faces-uphill-battle-to-regulate-the-aviation-supply-chain/)

### Inferences
- La douleur est structurelle, pas conjoncturelle :
  - 14 % jugent le changement permanent et plus de la moitié attendent au moins 18 mois de plus (2025) ;
  - en 2026, plus de la moitié n'attendent pas d'amélioration des TAT moteur avant 3 ans ;
  - les visites atelier LEAP vont être multipliées par plus de 6 d'ici 2040.
  Un produit lancé en 2027 adresserait donc une douleur qui durera vraisemblablement jusqu'en 2030 et au-delà.
- Les leviers que l'industrie active ont un point commun : stock, USM, PMA, brokers/distributeurs, pools. Ils augmentent le nombre de transactions entre petits acteurs, donc le volume de RFQ, de devis, de certificats et de vérifications de traçabilité. C'est précisément la zone où un agent IA « back-office » a de la valeur.
- L'IA générative a fait ses preuves sur l'extraction de documents non structurés (OW 2025). Cela valide techniquement les cas d'usage « lire un email RFQ » et « lire un Form 1 / 8130-3 ».

### Gaps
- Pas trouvé de chiffre primaire 2025-2026 sur les délais moyens par famille de pièces. Le « 20-40 semaines au lieu de 4-6 » circule via un blog de distributeur (Safe Fly Aviation), non vérifié.
- Le rapport complet IATA/Oliver Wyman d'octobre 2025 n'a pas été lu (seulement sa couverture presse). Le PDF IATA/Emerton de juin 2026 non plus.
- Aucune prévision USM d'AeroDynamic Advisory, d'ICF ou d'Aviation Week (sources payantes) n'a été trouvée. Les tailles de marché USM ci-dessus viennent de cabinets génériques peu fiables.
- Pas de benchmark AOG primaire récent par type d'avion, ni de données sur les AOG des opérateurs régionaux ou d'aviation d'affaires.

## Q2. Parmi les petits et moyens acheteurs, qui souffre le plus et achèterait un outil léger ?

### Takeaway
Quatre segments de petits et moyens acheteurs ressortent :
- les opérateurs régionaux (ATR, Dash 8), avec des prix de pièces qui doublent et des immobilisations longues ;
- les opérateurs hélicoptère, avec des délais de 6-18 mois et des moteurs à 24 mois en 2024 ;
- l'aviation d'affaires ;
- les petits brokers/distributeurs et MRO indépendants, désormais un « levier » officiel de l'industrie, qui traitent un volume croissant de RFQ et de certificats avec peu de personnel.

Les grandes compagnies ont déjà SkySelect, des ERP et des équipes IA internes. Les petits acteurs n'ont ni l'un ni l'autre.

### Cited Findings
- **Opérateurs régionaux et turbopropulseurs :**
  - pales d'hélice ATR révisées passées de 55 k$ à plus de 105 k$ — [Aviation Week](https://aviationweek.com/mro/aircraft-propulsion/atr-strives-improve-parts-reuse-amid-global-shortage)
  - Aurigny (Guernesey) a vu la disponibilité de sa flotte ATR affectée par une longue attente de pièces neuves, dont un train avant (date non visible) — [Island FM](https://islandfm.com/news/guernsey/atr-working-to-restore-aurignys-fleet-capacity)
  - en Afrique, les AOG sont de plus en plus attribués à une pénurie chronique de pièces — [Aviation Week](https://aviationweek.com/mro/supply-chain/closing-gap-africas-spare-parts-crunch)
  - en 2024 en Inde, ATR qualifiait des fournisseurs alternatifs pour les pièces simples urgentes et cannibalisait des avions (résumé de recherche, pré-2025) — [Aviation Week, page ATR 42](https://aviationweek.com/term/atr-42)
- **Hélicoptères :**
  - délais de 6-12 mois, et 12-18 mois pour les pièces de fonderie critiques ;
  - les opérateurs augmentent leurs stocks autant que possible, certains testent des PMA pour la première fois.
  — [Vertical](https://verticalmag.com/features/chain-reaction-the-story-behind-the-helicopter-industrys-supply-chain-squeeze/?amp)
  - En 2025-2026, demande forte, longs délais OEM et stocks limités — [AIN 01/2026](https://backend.ainonline.com/aviation-news/business-aviation/2026-01-30/rotortrade-report-flags-strong-demand-tight-supply)
  - En septembre 2025, Locatory notait que longs délais et goulots de production OEM poussent MRO et opérateurs vers le marché secondaire — [Locatory](https://www.locatory.com/?p=6603)
- **Opérateurs en général :** environ un tiers des opérateurs ont vu les taux de main-d'œuvre de maintenance augmenter de 10 % ou plus sur certains segments (2025) — [OW 2025 PDF](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)
- **Brokers et distributeurs :**
  - Oliver Wyman cite explicitement le « recours accru aux brokers et distributeurs » comme levier face à la supply chain — [OW 2025 PDF](https://www.aarcorp.com/globalassets/6.-careers/students/reports/mro-survey-2025.pdf)
  - Ils sont aussi en première ligne du risque documentaire : l'EASA leur a demandé de vérifier leurs dossiers pour toute pièce venant directement ou indirectement d'AOG Technics — [EASA](https://www.easa.europa.eu/en/domains/aircraft-products/suspected-unapproved-parts/aircraft-parts-distributed-aog-technics)
- **Les gros acteurs USM construisent leur IA en interne (Aviation Week, 21/10/2026) :**
  - AJW avec son système de stock « Apollo » (modélisation probabiliste) ;
  - GA Telesis avec une cellule data/IA pour le pricing, l'achat, la réparation et le positionnement du stock depuis 2022 ;
  - APOC rappelle que le jugement humain reste nécessaire sur l'état des pièces et leur traçabilité.
  — [Aviation Week](https://aviationweek.com/mro/emerging-technologies/mro-memo-part-ificial-intelligence-ai-comes-usm-trading)
- **Aviation d'affaires :**
  - Bluetail (records IA) cible l'aviation d'affaires, des propriétaires individuels aux grands opérateurs, avec des directeurs de maintenance et des équipes conformité comme utilisateurs — [AIN, 27/08/2026](https://backend.ainonline.com/aviation-news/business-aviation/2026-08-27/bluetails-ai-platform-tops-30-million-aircraft-records)
  - Aviaa est une centrale d'achat (GPO) pour l'aviation privée (pièces, services, carburant), avec une extension européenne via Convolus, Munich (2019, pré-2025) — [AIN](https://ainonline.com/aviation-news/business-aviation/2019-01-28/aviaa-expands-european-footprint-convolus-merger)

### Inferences
- **Meilleur ratio douleur / capacité à payer / absence d'outil :**
  1. petits brokers/distributeurs et traders USM (2-30 personnes), côté vente : RFQ, devis, certificats ;
  2. petits MRO Part-145 et CAMO indépendants (contrôle à réception, traçabilité) ;
  3. opérateurs hélicoptère et régionaux de moins de 30 appareils, côté achat AOG.
- Les compagnies majeures sont déjà servies (SkySelect, ERP AMOS/TRAX, équipes internes) et ont des cycles de vente longs. À éviter pour une solo-founder à 10 h/semaine.
- **Drones et UAM :** volumes de pièces trop faibles et réglementation en mouvement. Pas de douleur « pièces » documentée trouvée ; segment à écarter pour ce sujet.
- **Proximité de Toulouse :** l'écosystème ATR / turbopropulseurs régionaux et hélicoptères (Airbus Helicopters à Marignane, Safran HE à Bordes) est un terrain naturel pour des entretiens clients en français.
  - ⚠️ Vérifier le contrat de travail : clause d'exclusivité, obligation de loyauté, conflits avec les clients de l'employeur (Airbus/Satair probablement clients).

### Gaps
- Pas de décompte fiable du nombre de brokers/distributeurs européens (ASA, EASA, AFRA), ni du nombre de Part-145 en Europe. EASA publie des listes par État membre, non agrégées dans les résultats — [EASA (doc. roadshow, 2005)](https://www.easa.europa.eu/en/downloads/13853/en)
- Pas de données sur le budget logiciel type d'un petit broker ou d'un petit MRO.
- Pas de données spécifiques 2025-2026 sur les pénuries de pièces en aviation d'affaires à voilure fixe.

## Q3. Quels logiciels et marketplaces existent (ILS, PartsBase, Aeroxchange, Locatory, AvSight, SkySelect, ePlaneAI, Rotabull, Satair…), et où sont les trous ?

### Takeaway
Le marché est structuré en couches :
- des annuaires et marketplaces historiques (ILS/CAMP, PartsBase, Locatory, Aeroxchange) qui génèrent les RFQ ;
- des couches d'achat IA pour compagnies (SkySelect) ;
- des outils de vente pour fournisseurs (Rotabull, ePlane AI, AvSight sur Salesforce) ;
- des ERP de distributeurs (Quantum, Pentagon 2000) ;
- des outils de records IA, surtout en aviation d'affaires aux États-Unis (Bluetail) ;
- des modèles de valorisation pour gros acteurs (Cirium, IATA).

Trous visibles :
- un outil européen simple et multilingue pour les très petits vendeurs et acheteurs ;
- la vérification automatisée des certificats Form 1 / 8130-3 et des dossiers de traçabilité au contrôle à réception ;
- des alertes SUP/conformité poussées sur l'inventaire ;
- un outil d'aide à la décision « réparer / échanger / USM / PMA » pour les petites flottes.

### Cited Findings
**Marketplaces et annuaires (côté génération de RFQ)**
- ILS (Inventory Locator Service) a été racheté à Boeing par CAMP Systems (groupe Hearst) en 2019 — [Wikipedia ILS](https://en.wikipedia.org/wiki/Inventory_Locator_Service)
- CAMP a racheté un portefeuille de logiciels aviation à World Kinect en mars 2024 et se présente comme exploitant la plus grande marketplace digitale de pièces et services — [AviTrader](https://avitrader.com/2024/03/14/camp-systems-international-to-acquire-portfolio-of-aviation-software-businesses/)
- PartsBase a racheté PMA Parts Finder en 2010 (pré-2025). Ses prix ne sont pas publics — [AIN 2010](https://backend.ainonline.com/aviation-news/business-aviation/2010-07-28/partsbase-acquires-pma-parts-finder) ; [G2](https://www.g2.com/products/partsbase/pricing)
- Locatory : une page promotionnelle affiche un plan « Pro » à 3 900 $ et un plan « Premium » à 6 700 $ (périodicité non précisée, domaine « promo-test », à confirmer) — [Locatory](https://promo-test.locatory.com)
- Aeroxchange propose « eARC », un enregistrement numérique sécurisé et vérifiable des certificats FAA 8130-3 et EASA Form 1 — [Aeroxchange](https://corp.aeroxchange.com/?p=831)
- Marubeni a finalisé vers avril 2026 le rachat de DASI (distributeur américain) et prévoit d'investir dans sa marketplace en ligne (source secondaire) — [blog repost](https://dcnewsroom.blogspot.com/2026/04/japan-conglomerate-completes.html?m=0)

**Couche achat IA (compagnies)**
- SkySelect, d'origine estonienne, a levé 9 M$ en mars 2026 :
  - tour co-mené par Verb Ventures et RockCreek, avec SmartCap Green Fund (UE), Bain Capital Ventures et Lux Capital ;
  - plus de 6 Md$ de transactions depuis le lancement, dont 1,3 Md$ en 2025 ;
  - clients : JetBlue, Sun Country, ATSG, Widerøe, Vueling ;
  - algorithmes spécialisés de matching demande/fournisseurs sur des milliers de vendeurs, intégration ERP.
  — [AviTrader, 13/03/2026](https://avitrader.com/2026/03/13/skyselect-secures-us9m-to-transform-aviation-parts-procurement)
- SkySelect et Rotabull sont intégrés depuis 2023 : le fournisseur est sollicité automatiquement pour les pièces en stock — [SkySelect](https://skyselect.com/insights/skyselect-partners-with-rotabull-to-automate-aircraft)

**Couche vente pour fournisseurs, brokers et MRO**
- Rotabull :
  - boîte de réception unifiée des RFQ venant d'ILS, PartsBase, SkySelect et Stockmarket ; intégration Quantum ; « Vendor Quotes » ; « Intelligence » (données par pièce) ; app mobile ;
  - revendique plus de 10 M de lignes de stock vérifiées publiées par jour, des vendeurs utilisant Rotabull chez qui 94 % des compagnies mondiales ont acheté, et 6 minutes de temps moyen de réponse aux RFQ ;
  - clients affichés : AAR, AvAir, Chromalloy, Magnetic MRO.
  — [Rotabull](https://rotabull.com/)
  - Fondé en 2017, plus de 10 salariés, aucune levée trouvée — [Village.ai](https://village.ai/company/rotabull)
- ePlane AI :
  - « Email AI » d'automatisation des RFQ ;
  - partenariat avec l'ERP Pentagon 2000 (juillet 2025) : extraction des références, quantités et urgences depuis les emails RFQ vers l'ERP, en bêta avec rollout prévu au T3 2025, statut actuel non vérifié.
  — [Newswire](https://www.newswire.com/news/pentagon-2000-and-eplane-ai-partner-to-automate-rfq-workflows-for-22614413)
- AvSight : plateforme cloud sur Salesforce (stock, devis, réparations, commandes, finance) ; levée de 20 M$ en growth equity auprès d'Arcadea Group (janvier 2023, pré-2025) — [Arcadea](https://www.arcadeagroup.com/avsight-announces-dollar20mm-strategic-growth-equity-investment-with-arcadea-group/)

**Records, traçabilité, IA documentaire**
- Bluetail :
  - plus de 30 M de documents avion numérisés (août 2026) ;
  - lancement en 2026 de « Ask Bluetail », « Autonomous Logbooks », « Lifecycle Timeline » et « Compliance Check » ;
  - cible : aviation d'affaires.
  — [AIN](https://backend.ainonline.com/aviation-news/business-aviation/2026-08-27/bluetails-ai-platform-tops-30-million-aircraft-records)
  - Série A de 2,1 M$ (date non confirmée dans les résultats) — [AviationPros](https://www.aviationpros.com/aircraft-maintenance-technology/mros-repair-shops/maintenance-it/press-release/21236540/bluetail-bluetail-raises-21m-series-a-to-solve-paper-to-digital-pains-of-modern-aircraft-records-management)
- ProvenAir Technologies (Chicago) : automatisation et IA pour établir la traçabilité « back-to-birth » des composants d'avions commerciaux ; 487 500 $ levés en août 2026 (profil Preqin, à vérifier) — [Preqin](https://www.preqin.com/data/profile/asset/provenair-technologies--inc-/1097209)
- Soji AI s'est associé à Active Partners en mai 2026 pour appliquer l'IA aux records MRO (source secondaire) — [ePlaneAI news](https://www.eplaneai.com/ar/news/soji-ai-and-active-partners-explore-ai-applications-for-mro-records)
- Aucune startup ni aucune guidance réglementaire spécifiquement dédiée à la vérification IA des Form 1 / 8130-3 n'a été trouvée lors de la recherche — [résultats autour d'Aviatize](https://www.aviatize.com/glossary/form-1-and-8130-3)

**Valorisation part-out et USM**
- Cirium « Part Out Value Model » : valeur de démontage des principaux types d'avions et moteurs, et projection des retraits sur 10 ans — [Cirium](https://cirium.com/solutions/part-out-value-model)
- IATA « MRO SmartHub Evaluator » et « MRO Insights » : valorisation neutre des pièces de rechange, score de risque basé sur le taux de rebut historique — [IATA MRO Insights](https://www.iata.org/en/services/data/mro-insights/) ; [SmartHub Evaluator](https://mrosmarthub.iata.org/info/modules/evaluator/evaluator.html)
- AerSale publie ses démontages à venir (avions, moteurs) avec disponibilité USM — [AerSale](https://www.aersale.com/products-services/parts-sales/upcoming-teardowns)

**Autres mouvements**
- Aero NextGen a racheté Digital Flight (matchmaking tech MRO) — [Aviation Week](https://aviationweek.com/mro/emerging-technologies/aero-nextgen-acquisition-seeks-streamline-mro-tech-matchmaking)
- Trade:Aero (marketplace européenne d'aviation générale) cherchait un seed de 500-750 k€ — [Trade:Aero](https://trade.aero/company/investors/)

### Inferences
**Trous identifiés (inférence)**
- **(a) Européens « micro » :** Rotabull, ePlane AI et AvSight sont américains, israélo-chypriotes ou US-centrés, et ciblent des fournisseurs déjà équipés d'un ERP (Quantum, Pentagon 2000, Salesforce).
  - Les très petits brokers et MRO européens travaillant sur Outlook + Excel, en français, espagnol, italien ou allemand, semblent peu adressés.
  - À valider par entretiens.
- **(b) Vérification documentaire au contrôle à réception :** Aeroxchange numérise les certificats, mais seulement si l'émetteur est dans son réseau. Bluetail et ProvenAir travaillent sur les records et la traçabilité. Aucun outil simple « dépose le PDF du Form 1 + le bon de commande → check-list d'anomalies » pour un petit Part-145 n'a été trouvé.
- **(c) Alertes SUP et conformité poussées :** les notices SUP EASA/FAA existent mais sont dispersées. Aucun service « alerte quand un PN/SN de mon stock apparaît dans une notice » n'a été trouvé.
- **(d) Aide à la décision pour petites flottes :** réparer / échanger / acheter USM / PMA, intégrant TAT et coût AOG. Les outils de valorisation existants (Cirium, IATA) visent lessors, grands MRO et compagnies.
- **Risque concurrentiel :** les marketplaces (ILS/CAMP, PartsBase) contrôlent le flux de RFQ et peuvent intégrer de l'IA. Un nouvel entrant doit se brancher dessus (intégration email ou export), pas les remplacer.

### Gaps
- Prix publics de Rotabull, SkySelect, ePlane AI, AvSight, ILS et PartsBase : non trouvés (tous « sur demande »).
- Nombre d'abonnés et CA d'ILS et PartsBase non trouvés.
- Aeroxchange (propriété, prix, adoption d'eARC) non approfondi.
- Satair « Skywise marketplace » et Boeing Global Services (offre digitale pièces) non couverts par mes recherches.
- Conditions d'API et d'export d'ILS, PartsBase et Locatory pour un outil tiers non vérifiées : risque de CGU interdisant le scraping.

## Q4. Quels exemples de petites équipes ou startups ayant construit du revenu, levé des fonds ou été rachetées ?

### Takeaway
Les références les plus proches du modèle de Johanna (logiciel de niche, petite équipe) sont :
- Rotabull, fondé en 2017, plus de 10 salariés, aucune levée publique, adopté par AAR, Chromalloy et Magnetic MRO ;
- SkySelect, 9 M$ levés en mars 2026, 1,3 Md$ de transactions en 2025 ;
- Bluetail, levées modestes et 30 M de documents ;
- AvSight, 20 M$ en growth equity ;
- Aerostrat, logiciel de planification racheté 15 M$ (+5 M$ d'earn-out) par AAR.

Les sorties existent : acquéreurs = AAR, CAMP/Hearst, Satair/Airbus, TransDigm, Marubeni, fonds PE. Mais les multiples ne sont pas publiés.

### Cited Findings
- **SkySelect :** 9 M$ en mars 2026 (Verb Ventures, RockCreek, SmartCap, Bain Capital Ventures, Lux), plus de 6 Md$ de transactions cumulées, 1,3 Md$ en 2025 — [AviTrader](https://avitrader.com/2026/03/13/skyselect-secures-us9m-to-transform-aviation-parts-procurement). Aucun rachat de SkySelect n'a été trouvé, contrairement à l'hypothèse de la question.
- **ePlane / ePlane AI :**
  - série A de 9 M$ en mars 2020 menée par Marubeni — [TechCrunch](https://techcrunch.com/2020/03/24/eplane)
  - CB Insights compte 10 M$ en 3 tours — [CB Insights](https://www.cbinsights.com/company/eplane/financials)
  - Caplight mentionne une « Series C » en février 2026 et 20 M$ au total, sans montant, non corroboré — [Caplight](https://www.caplight.com/company/eplaneai)
  - L'identité du CEO diffère selon les sources.
- **AvSight :** 20 M$ en growth equity d'Arcadea Group (janvier 2023), sur Salesforce — [Arcadea](https://www.arcadeagroup.com/avsight-announces-dollar20mm-strategic-growth-equity-investment-with-arcadea-group/) ; [MRO Global](https://www.mroglobal-online.com/mro-software-business-avsight-in-equity-deal-with-arcadea/)
- **Rotabull :** fondé en 2017, plus de 10 salariés, aucune levée trouvée — [Village.ai](https://village.ai/company/rotabull)
  - Un communiqué titre « croissance significative 4 années consécutives » (contenu non récupéré) — [Newsfile](https://www.newsfilecorp.com/release/162145/Rotabull-The-Leading-Sales-Platform-for-the-Aviation-Aftermarket-Shows-Significant-Growth-Four-Consecutive-Years)
- **AAR / Aerostrat :** AAR a racheté Aerostrat (logiciel de planification de maintenance) pour 15 M$ plus jusqu'à 5 M$ d'earn-out, intégré à sa filiale Trax (fin 2025) — [Barchart / communiqué AAR](https://www.barchart.com/story/news/34073432/aar-announces-acquisition-of-maintenance-planning-software-provider-aerostrat-expanding-capabilities-of-trax-subsidiary)
- **Bluetail :** série A de 2,1 M$ (date non confirmée) et 30 M de documents en août 2026 — [AviationPros](https://www.aviationpros.com/aircraft-maintenance-technology/mros-repair-shops/maintenance-it/press-release/21236540/bluetail-bluetail-raises-21m-series-a-to-solve-paper-to-digital-pains-of-modern-aircraft-records-management) ; [AIN](https://backend.ainonline.com/aviation-news/business-aviation/2026-08-27/bluetails-ai-platform-tops-30-million-aircraft-records)
- **ProvenAir :** 487,5 k$ en août 2026 (Preqin) — [Preqin](https://www.preqin.com/data/profile/asset/provenair-technologies--inc-/1097209)
- **CAMP Systems (Hearst) :** rachat d'ILS à Boeing (2019) puis de logiciels de World Kinect (2024). C'est un consolidateur actif — [Wikipedia](https://en.wikipedia.org/wiki/Inventory_Locator_Service) ; [AviTrader](https://avitrader.com/2024/03/14/camp-systems-international-to-acquire-portfolio-of-aviation-software-businesses/)
- **Satair :** rachat d'Unical et ecube (USM, 298 M$ de CA 2024), finalisé en mai 2026 — [Cision/AAP](https://www.aap.com.au/aapreleases/cision20260511ae56600/)
- **Aviaa :** rachat de Convolus (centrale d'achat européenne) en 2019, montant non divulgué — [AviTrader](https://avitrader.com/2019/01/28/aviaa-to-acquire-convolus)

### Inferences
- **Acquéreurs naturels d'un petit SaaS de niche en 2030-2036 :**
  - consolidateurs logiciels aviation : CAMP/Hearst, AAR/Trax, Veryon, éditeurs d'ERP (Quantum, Pentagon 2000) ;
  - marketplaces (ILS, PartsBase, Locatory/Avia Solutions Group) ;
  - SkySelect, Rotabull ;
  - distributeurs adossés à des OEM ou à du PE (Satair, Marubeni/DASI).
  L'exemple Aerostrat (15-20 M$) montre qu'un logiciel de niche peut se vendre à ce niveau. Son ARR n'est pas publié, donc impossible d'en déduire un multiple.
- Le fait que Rotabull existe depuis 2017 avec plus de 10 salariés, sans levée publique, suggère qu'un SaaS vertical « vente de pièces » peut être autofinancé. C'est cohérent avec le budget de Johanna, mais Rotabull a été fondé par des équipes techniques.

### Gaps
- Aucun ARR public n'a été trouvé pour Rotabull, SkySelect, ePlane AI, AvSight ou Bluetail.
- Le rachat de SkySelect n'a pas été trouvé, sans doute inexistant à la date de recherche.
- Les multiples de valorisation des deals logiciels aviation ne sont pas publics.
- Veryon, Traxxall et Aviaa n'ont pas été approfondis.

## Q5. Que peut-on vendre comme produit étroit et automatisable à faible exposition réglementaire, et que faut-il certifier ? Évaluation de 5 à 10 opportunités

### Takeaway
Un logiciel qui aide à acheter, vendre, trier, alerter ou pré-contrôler ne requiert pas d'agrément EASA en soi, tant que ce n'est pas Johanna qui émet des certificats ou libère des pièces. La responsabilité de l'acceptation d'une pièce reste à l'organisme agréé client (Part-145/CAMO). La production d'un Form 1, elle, relève d'un organisme agréé Part-21G ou Part-145.

Le risque principal n'est donc pas la certification mais la responsabilité contractuelle (un faux négatif sur un faux certificat) et l'accès aux données (CGU des marketplaces, propriété intellectuelle des données OEM). Les meilleures pistes :
1. agent RFQ/devis pour petits vendeurs européens ;
2. pré-contrôle IA des certificats et de la traçabilité ;
3. veille et alertes SUP sur l'inventaire ;
4. copilote AOG côté achat pour petites flottes.

### Cited Findings
- Le Form 1 EASA (Authorised Release Certificate) est l'équivalent du FAA 8130-3. Ces certificats de navigabilité n'impliquent pas automatiquement l'approbation de la pièce pour un usage donné. Un 8130-3 à double libération (bloc 12) serait accepté comme équivalent dans le périmètre de l'accord UE-US (source secondaire, à vérifier) — [Aviatize](https://www.aviatize.com/glossary/form-1-and-8130-3) ; [Aviation Souk](https://www.aviationsouk.com/knowledge/easa-and-faa-certification-forms-types-usage-and-issuance/)
- Le système de déclaration obligatoire des pièces suspectes (SUP) repose sur l'article 4(4) du règlement (UE) 376/2014. L'EASA publie les notices SUP — [EASA SUP background](https://easa.europa.eu/en/domains/aircraft-products/suspected-unapproved-parts/background)
- Aeroxchange démontre l'existence d'un marché de la vérifiabilité numérique des Form 1 / 8130-3 (eARC) — [Aeroxchange](https://corp.aeroxchange.com/?p=831)
- AI Act : le règlement de base EASA 2018/1139 figure à l'annexe I, section B. L'article 108 de l'AI Act modifie 2018/1139 pour que les actes délégués et d'exécution EASA sur l'IA « composant de sécurité » tiennent compte des exigences « haut risque » — [rgpd.com – art. 108](https://rgpd.com/ai-act/chapter-13-final-provisions/article-108-amendments-to-regulation-eu-2018-1139)
  - Un « Digital Omnibus » (règlement (UE) 2026/1744 selon une source) ajouterait un renvoi similaire à l'article 27 de 2018/1139, non vérifié — [euaiact.com](https://www.euaiact.com/digital-omnibus-ai/sectoral-amendments)
- L'EASA travaille surtout sur la certification de systèmes embarquant de l'IA (feuille de route IA), pas sur l'usage de l'IA pour vérifier des documents de libération — [Aviation Week](https://ngstage.aviationweek.com/air-transport/easa-releases-roadmap-artificial-intelligence-use)
- Les acteurs USM rappellent que le jugement humain reste indispensable sur l'état et la traçabilité des pièces — [Aviation Week, 21/10/2026](https://aviationweek.com/mro/emerging-technologies/mro-memo-part-ificial-intelligence-ai-comes-usm-trading)
- Pas d'outil IA spécialisé Form 1 / 8130-3 trouvé (cf. Q3) — [résultats Aviatize/Aeroxchange](https://www.aviatize.com/glossary/form-1-and-8130-3)

### Inferences
**Cadre réglementaire (inférence, à faire valider par un juriste ou un ex-responsable qualité Part-145)**
- Ce que je retiens de Part-145 (145.A.42 « Components ») : l'organisme agréé doit classer les composants et s'assurer qu'ils sont accompagnés d'un Form 1 ou équivalent avant installation. L'outil de Johanna serait un moyen au service de cette procédure, pas un substitut. Il ne nécessite pas d'agrément, mais le client doit l'intégrer dans son MOE ou ses procédures.
  - À vérifier dans les Easy Access Rules Part-145 / Part-CAMO / Part-21 (non consultées ici).
- AI Act : un outil de back-office (devis, tri d'emails, pré-contrôle documentaire) n'est vraisemblablement pas un « composant de sécurité » d'un produit aéronautique. Les obligations de l'article 2(2) pour l'annexe I section B ne s'appliqueraient pas directement. Rester sur des obligations de transparence et RGPD.
  - Connaissance propre à vérifier au Journal officiel.
- **Positionnement à tenir :** « aide à la décision, l'humain qualifié valide » ; journalisation complète ; limitation de responsabilité contractuelle ; assurance RC pro adaptée à l'aéronautique.
  - Ne jamais émettre, modifier ou « valider » un certificat.
  - Ne jamais devenir distributeur de pièces : cela ferait entrer dans EN 9120/ASA-100 et dans le risque produit.

**Les 8 opportunités (toutes = inférences construites sur les findings ci-dessus)**

Les fourchettes d'ARR sont des ordres de grandeur, avec des hypothèses explicites. Le nombre de clients potentiels est une lacune non sourcée.

**1. Agent RFQ → devis pour petits brokers, distributeurs et MRO européens (« Rotabull light » multilingue, sans ERP)**
- Douleur :
  - flux croissant de RFQ (brokers et distributeurs = levier officiel, OW 2025) ;
  - le temps de réponse est l'arme commerciale (Rotabull vante 6 min) ;
  - les petits n'ont pas d'ERP intégré.
- Produit : connexion à Outlook/Gmail et aux exports ILS/PartsBase/Locatory. Extraction PN, quantité, condition (NE/OH/SV/AR), certificat exigé et urgence AOG. Rapprochement avec le stock (CSV/Excel). Brouillon de devis et relances. Tableau des taux de conversion.
- Qui paie : dirigeant d'un broker de 2-20 personnes. Willingness to pay estimée entre 150 et 600 €/mois. Repère : Locatory facture 3 900-6 700 $ par plan.
- Concurrence : Rotabull, ePlane AI Email AI, AvSight, modules ERP (Pentagon 2000). Différenciation : UE, multilingue, pas d'ERP requis, prix d'entrée bas, onboarding en 1 jour.
- Faisabilité pour une non-développeuse : moyenne. LLM d'extraction + intégration email + base simple, réalisables avec des outils IA de code et un freelance. Point dur : fiabilité des intégrations email et des formats de stock.
- Automatisation : élevée (self-serve, onboarding guidé).
- Réglementation : faible (activité commerciale). RGPD sur les emails.
- Plafond ARR : 300-700 clients × 3-6 k€ ≈ 1-4 M€, si le marché européen et anglophone de petits vendeurs est assez large (non vérifié).

**2. Pré-contrôle IA des certificats et dossiers de traçabilité au contrôle à réception (Form 1 / 8130-3 / CoC / back-to-birth)**
- Douleur : AOG Technics (≥ 70 ARC falsifiés, 126 moteurs), alertes EASA 2026, contrôle à réception manuel dans les petits Part-145, distributeurs et CAMO.
- Produit :
  - dépôt du PDF ou de la photo du certificat + du bon de commande ;
  - extraction des blocs ;
  - contrôles de cohérence : PN, SN, quantité, statut, bloc 12 double libération, n° d'agrément de l'émetteur vs listes publiques, dates ;
  - comparaison avec les notices SUP ;
  - score d'anomalie et dossier d'audit horodaté.
- Qui paie : responsable qualité ou magasin d'un Part-145/CAMO, distributeur certifié EN 9120/ASA-100. Facturation par document (0,5-3 €) ou abonnement 200-800 €/mois (estimation).
- Concurrence : Aeroxchange eARC (numérique natif, réseau fermé), Bluetail Compliance Check (records, US/bizav), ProvenAir (BtB). Aucun acteur trouvé sur « pré-contrôle du PDF entrant ».
- Faisabilité : moyenne. Extraction documentaire mature (OW 2025). Le savoir-faire métier (règles de contrôle) est la valeur : Johanna peut le formaliser avec un ex-responsable qualité freelance.
- Automatisation : élevée.
- Réglementation : modérée. Pas d'agrément, mais une responsabilité en cas de faux négatif. Positionner comme « second regard », et faire écrire la procédure par le client.
- Plafond ARR : 1-3 M€ sur l'UE + UK, davantage avec une extension US/FAA.

**3. Flux d'alertes SUP / conformité fournisseur appliqué à l'inventaire (data feed)**
- Produit :
  - agrégation automatique des notices SUP EASA/FAA, alertes de vol ou détournement, suspensions/retraits d'agréments, AD pertinentes ;
  - rapprochement quotidien avec le stock ou les achats du client (PN/SN, fournisseurs) ;
  - alerte email/Slack.
- Douleur : l'EASA demande aux distributeurs et MRO de vérifier leurs stocks à chaque alerte, aujourd'hui manuellement.
- Prix : 50-300 €/mois (estimation). Très automatisable, réglementation faible (données publiques).
- Plafond : 0,3-1,5 M€ seul. Plutôt un produit d'entrée (« wedge ») ou un module de l'option 2.
- Faisabilité : élevée (scraping de sources publiques + matching).

**4. Copilote AOG côté achat pour petites flottes (hélicoptère, régional, aviation d'affaires, CAMO indépendants)**
- Produit :
  - à partir d'un PN, recherche multi-sources (via les comptes du client sur les marketplaces, sans scraping illicite) ;
  - envoi groupé de RFQ aux brokers ;
  - comparatif normalisé : prix, condition, certificat, TAT, échange vs achat ;
  - pré-contrôle des certificats (option 2) ;
  - historique des prix.
- Douleur : délais de 6-18 mois et prix ×2 (pales ATR), AOG chiffré jusqu'à 150 k$/h (Boeing). Les petites flottes n'ont pas de SkySelect.
- Qui paie : responsable logistique ou directeur de maintenance d'un opérateur de 5-50 appareils. 300-1 000 €/mois (estimation).
- Concurrence : SkySelect (compagnies), Aviaa (centrale d'achat bizav), brokers eux-mêmes.
- Faisabilité : moyenne-basse, car il faut une intégration avec plusieurs marketplaces dont les CGU et API sont inconnues.
- Plafond : 1-2 M€.

**5. Moteur « pièces alternatives » : interchangeabilité, PMA, obsolescence pour flottes vieillissantes**
- Douleur : IATA et Oliver Wyman poussent PMA/USM et la production sous licence. Les opérateurs hélicoptère testent les PMA pour la première fois. Les PMA sont la catégorie la plus dynamique (TCAC 11,2 %, GMI).
- Produit : recherche d'alternatives (PMA approuvées, superseded PN), alertes d'obsolescence.
- Données :
  - les listes PMA de la FAA sont publiques, à vérifier ;
  - les IPC et données OEM sont protégées (propriété intellectuelle, contrats) et constituent un frein majeur ;
  - l'acceptation des PMA FAA sous EASA est encadrée par l'accord UE-US, à vérifier.
- Réglementation : modérée. Le choix d'une alternative engage la navigabilité ; l'outil ne fait que lister.
- Faisabilité : basse-moyenne (données). Plafond 0,5-2 M€.

**6. Indice prix / délais USM et pièces (data product construit sur les données des options 1 et 4)**
- Produit : indices anonymisés et agrégés de prix et délais par PN ou famille, issus des devis traités, avec accord contractuel des clients. Vendu aux MRO, lessors et traders.
- Concurrence : IATA MRO SmartHub / MRO Insights, Cirium, plateformes internes d'AJW et GA Telesis.
- Faisabilité : seulement après traction des options 1 et 4 (effet réseau des données). Réglementation faible, avec une vigilance sur le droit de la concurrence : pas d'échange d'informations sensibles entre concurrents, il faut agréger.
- Plafond : additionnel de 0,5-1,5 M€. Fort levier de valorisation à la revente.

**7. Aide à la décision « réparer / échanger / USM / neuf » pour les CAMO de petites flottes**
- Produit : pour chaque dépose, comparaison coût total (prix, TAT, coût d'immobilisation, garantie, risque de rebut) à partir des devis reçus.
- Douleur : TAT dégradés sur 43-75 % des familles (OW 2025), coût des visites atelier au-dessus des attentes.
- Faisabilité : moyenne (surtout logique métier + tableur augmenté). Risque : dépend de la qualité des devis.
- Plafond : 0,5-1,5 M€. Plutôt un module de l'option 4.

**8. Valorisation « part-out » light pour petits lessors, brokers et opérateurs hélicoptère**
- Douleur : USM devenu stratégique (Satair/Unical), IATA demande plus d'USM issues de démontages.
- Concurrence lourde : Cirium Part Out Value Model, IATA Evaluator, données propriétaires des gros traders.
- Faisabilité : basse. Il faut des historiques de prix que Johanna n'a pas.
- À considérer seulement comme sous-produit de l'option 6.

**Classement préliminaire (inférence)**
- **1. Pré-contrôle documentaire (2) + alertes SUP (3) :**
  - douleur réglementaire et réputationnelle forte (AOG Technics) ;
  - pas d'acteur direct trouvé ;
  - valeur métier formalisable par Johanna ;
  - très automatisable ;
  - vendable en Europe en français ;
  - point dur = responsabilité.
- **2. Agent RFQ/devis UE (1) :** marché prouvé (Rotabull, ePlane AI) donc concurrence réelle, mais un créneau européen sans ERP est plausible.
- **3. Copilote AOG petites flottes (4) :** forte douleur mais dépendance aux marketplaces.
- **Ensuite :** options 5, 6 et 7 comme extensions, et 8 à éviter en V1.

**Ce qui n'est pas compatible avec les contraintes de Johanna**
- Devenir broker ou distributeur de pièces (stock, EN 9120, risque produit).
- Émettre ou modifier des certificats.
- Logiciel embarqué ou de maintenance prédictive certifiable.
- Ventes « grands comptes » à cycle de 12-18 mois (compagnies majeures, OEM).

### Gaps
- Texte exact des exigences Part-145 (145.A.42), Part-CAMO et Part-21 (21.A.163, issuance du Form 1) non consulté. À vérifier dans les EASA Easy Access Rules.
- Aucune guidance EASA ou FAA trouvée sur l'usage d'outils IA pour l'acceptation des pièces ou la vérification des certificats.
- Statut du « Digital Omnibus » (règlement 2026/1744) et application précise de l'AI Act aux outils de back-office aéronautiques non vérifiés.
- CGU et API d'ILS, PartsBase, Locatory et SkySelect pour des intégrations tierces non vérifiées : conditionne les options 1, 4 et 6.
- Statut des données FAA PMA (export public) et accès aux IPC OEM non vérifiés : conditionne l'option 5.
- Pas de données sur le nombre de petits brokers, MRO et CAMO en UE/UK, ni sur leur budget logiciel. Les plafonds d'ARR ci-dessus restent des hypothèses à valider par 15-20 entretiens clients.
