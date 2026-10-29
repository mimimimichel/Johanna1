# Opportunités logicielles B2B « funnel de vente, quote-to-cash, CX et cadrage », hors aéro ou adjacentes (état au 29/10/2026)

Contexte : Johanna est consulting manager produit/innovation salariée d'un grand cabinet de conseil IT, à Toulouse. Elle n'est pas développeuse. Elle dispose d'environ 10 h/semaine et de 6 à 25 k€ pour une V1 construite avec des outils de code IA et des freelances. Cible : 1 à 4 M€ d'ARR, puis une revente d'ici 2036. L'activité doit rester 100 % légale FR/UE. Elle peut vendre un logiciel, mais pas du conseil.

Conventions :
- « $ » désigne des dollars US non convertis.
- « Éditeur » signale une source écrite par un vendeur du secteur, donc biaisée.
- « Secondaire » désigne un agrégateur ou un blog qui reprend une autre source.
- Les « calc » sont mes propres calculs.

Les données antérieures à 2025 sont signalées. Les chiffres de prix viennent surtout de comparateurs ou d'éditeurs ; ils doivent être vérifiés auprès des éditeurs avant tout business plan.

---

## Q1. Réponse aux RFQ et devis industriels (CPQ-lite pour l'usinage et la sous-traitance, devis à partir de plans reçus par e-mail)

### Takeaway
Le besoin est réel et bien documenté : chiffrer une pièce à la main prend de 15 minutes à 2 heures, et un assemblage complexe jusqu'à 4 jours. Le marché est déjà occupé.
- Aux États-Unis : Paperless Parts (45,5 M$ levés, plus de 800 industriels clients) et une dizaine d'outils IA lancés en 2025-2026.
- En France, au moins 5 offres IA d'éditeurs francophones existent (COTIA/UsinIA, UsiQuoteIA, Solanys, Fabera, Evolia), en plus des outils historiques (Cetim TechniQuote, La Machine aux Devis).

Il reste une place pour un outil centré sur la boîte mail : l'e-mail de RFQ devient un devis, avec relances et suivi du taux de transformation. La partie « funnel » y est plus importante que la partie « calcul de gamme ». C'est aussi la plus proche du profil de Johanna.

### Cited Findings
**Prix et acteurs (guide Morsa du 26/10/2026, éditeur, prix relevés le 25/10/2026)** — [Morsa](https://morsa.ai/guides/manufacturing-quoting-software)
- **Paperless Parts** : prix sur devis ; Software Finder estime environ 1 500 $/mois pour démarrer ; plus de 800 industriels clients ; « jusqu'à 2 h à la main par composant contre 15 min », « un assemblage complexe jusqu'à quatre jours ».
- **Tempus Tools** (découpe laser) : 75, 225 ou 375 $ par utilisateur et par mois en annuel (100, 300 ou 500 $ en mensuel).
- **DigiFabster** (devis instantané en ligne) : à partir de 415 ou 840 $/mois en annuel, plus des frais de paiement.
- **Customiser** : 0,10 $ par crédit en paiement à l'usage. Il lit les plans 2D et les spécifications et construit la nomenclature.
- **Mavlon** : facturé selon le volume annuel d'appels d'offres, sans licence par siège. Il lit les dossiers d'appel d'offres, y compris les plans scannés et les fils d'e-mails.
- **Kwantflow** : gratuit et open source (GPL-3.0).
- **Toolpath** : gratuit au démarrage.
- **SOLIDWORKS Costing** : 3 456 à 4 716 $/an par siège selon un revendeur.
- **Morsa** lui-même : un pilote d'abord, puis une part de la valeur créée, sans licences par siège.
- **SecturaFAB** : un devis d'assemblage complexe passe « d'une journée ou plus à environ une demi-heure ».

**Paperless Parts**
- 45,5 M$ levés au total — [LeadIQ](https://leadiq.com/c/paperless-parts/5a1dc48f2300005a00c6c755) (secondaire).
- Série B de 30 M$ menée par OpenView en septembre 2021 — [YesPress](https://yespress.io/paperless-parts) (secondaire).
- Environ 139 salariés, fondée en 2017 — [PitchBook](https://pitchbook.com/profiles/company/181087-30).
- Chiffres déclarés par l'entreprise, non vérifiés : plus de 86 % de croissance annuelle des nouvelles réservations d'ARR au T1, et une fonction de finalisation de devis lancée en août 2026 — [YesPress](https://yespress.io/paperless-parts).
- Partenariat avec Tighitco (sous-traitant aéro) en juillet 2026 — [LeadIQ](https://leadiq.com/c/paperless-parts/5a1dc48f2300005a00c6c755).

**Autres concurrents nommés**
- DigiFabster, Machine Research, Costimator, ProShop, Fulcrum, JobBOSS et aPriori — [YesPress](https://yespress.io/paperless-parts).
- K+G Ai ERP, qui intègre le devis IA à un ERP — [K+G](https://kgindustrialgroup.com/platform/alternatives/paperless-parts/).
- CloudNC — [LeadIQ](https://leadiq.com/c/paperless-parts/5a1dc48f2300005a00c6c755).

**Acteurs français**
- **COTIA (UsinIA)** : propose gamme, temps et prix à partir du plan. Hébergé en France, il s'appuie sur Claude d'Anthropic et se présente comme une « aide à la décision » à valider par un humain — [UsinIA](https://usinia.fr/chiffrage-ia.html).
- **UsiQuoteIA** : analyse des fichiers STEP et PDF, gammes générées par IA, export vers l'ERP, devis en plusieurs quantités en « moins de 2 min » — [UsiQuoteIA](https://usiquoteia.com/).
- **Solanys** : recherche de pièces similaires dans l'historique des devis — [Solanys](https://solanys.ai/fr/secteurs/usinage/).
- **Fabera** : start-up lyonnaise, développée avec le laboratoire Insavalor (article d'environ 2 ans) — [innovations.fr](https://innovations.fr/lia-au-service-du-chiffrage-des-devis-industriels/).
- **Evolia Stratégie** : lecture de plans, devis et planification — [Evolia](https://www.evoliastrategie.com/secteurs/mecanique-precision).
- **Cetim TechniQuote** : logiciel de référence pour l'usinage et la mécano-soudure ; la version 2023 ajoute un module FAO — [Cetim](https://www.cetim.fr/logiciels/cetim-techniquote/).
- **La Machine aux Devis (Progilab)** : usinage et tôlerie — [Progilab](https://www.progilab.fr/).
- **Coekipia (cas SC Meca)** : la valeur vient de la structuration des données existantes (centres de frais, taux horaires, phases standard) — [Coekipia](https://coekipia.fr/cas-clients/sc-meca-chiffrage-usinage).

**Taille de marché France** (aucun chiffre consolidé et fiable)
- Xerfi chiffre les facturations de la mécanique industrielle à 8,4 Md€ en 2023 — [Xerfi](https://www.xerfi.com/presentationetude/La-mecanique-industrielle_23MET03).
- Une page d'événement avance 260 000 entreprises sous-traitantes, dont 4/5 de PME. Ce chiffre est peu fiable et son périmètre est inconnu — [Luma/FFI](https://luma.com/ffi-znfi).

### Inferences
- Le calcul de prix à partir de la géométrie se banalise vite : des outils gratuits ou open source existent, et des acteurs français s'appuient directement sur des LLM du marché. Une V1 fondée sur ce calcul serait peu défendable.
- L'angle défendable est plutôt le « RFQ desk » :
  - capter les RFQ dans Outlook ;
  - extraire plans et quantités ;
  - retrouver des pièces similaires dans l'historique ;
  - produire un devis brouillon dans le modèle du client ;
  - relancer automatiquement ;
  - suivre le taux de transformation par client et par donneur d'ordre.

  C'est exactement le métier de digitalisation du funnel de vente B2B.
- Prix cible plausible : 150 à 500 €/mois par site (calc : 300 clients × 300 €/mois ≈ 1,1 M€ d'ARR).
- Points faibles : un plafond d'ARR modéré en France seule et une forte attente d'intégration ERP (Sylob, Clipper, Divalto, etc.).
- Il faut un ou deux freelances solides en extraction de PDF et de plans.
- La proximité avec l'écosystème aéro toulousain est un atout pour trouver des clients pilotes, mais il faut vérifier la clause de non-concurrence et d'exclusivité du contrat de travail.

### Gaps
- Aucun chiffre fiable sur le nombre d'ateliers d'usinage ou de sous-traitants en France (il faudrait l'INSEE Ésane, NAF 25.62A/B).
- Pas de levée ni d'ARR connus pour les acteurs français (UsinIA, UsiQuoteIA, Solanys, Fabera).
- Pas de taux de transformation devis → commande sourcé pour la sous-traitance française.

---

## Q2. IA pour les appels d'offres publics et privés en France (veille et rédaction de mémoires techniques)

### Takeaway
Le marché sous-jacent est très grand :
- 223 383 marchés recensés en 2024 pour 233,3 Md€ ;
- les PME remportent 60 % des marchés en nombre ;
- 8 825 acheteurs ont notifié au moins un marché entre janvier et juillet 2026.

Mais la catégorie « IA pour les AO » est déjà encombrée : plus de 15 outils, des prix d'entrée de 30 à 150 €/mois, et un leader français autofinancé et rentable, Tenderbolt. Une entrée généraliste n'est plus raisonnable. Il reste deux options :
- se spécialiser sur une famille d'achats, avec une bibliothèque de contenus métier et des modèles de mémoire propres ;
- viser les AO privés et les questionnaires fournisseurs, moins couverts.

### Cited Findings
**Volumes du marché public**
- Recensement 2024, publié en mars 2026 :
  - 223 383 marchés pour 233,3 Md€ (contre 243 731 marchés en 2023) ;
  - les collectivités passent plus de 159 000 marchés pour 100,7 Md€ ;
  - PME : 60 % des marchés en nombre et 25 % en valeur ;
  - seuil de recensement abaissé à 40 000 € HT, ce qui casse la comparabilité avec les années précédentes ;
  - start-up : 1,4 % des marchés (3 138).

  Sources : [La Gazette des communes](https://www.lagazettedescommunes.com/1029534/marches-publics-les-chiffres-cles-de-2024-viennent-detre-publies/) ; [Le Moniteur](https://www.lemoniteur.fr/reglementation/commande-publique-bercy-publie-enfin-les-chiffres-pour-2024.M2H5HDSYPVHYTFZPNQU2P46XEA.html).
- Baromètre DECP sur janvier-juillet 2026 (édition du 7/9/2026) — [Trinta](https://trinta.ai/barometre) :
  - 104 329 marchés après dédoublonnage, dont 47 282 en procédure adaptée et 30 376 en appel d'offres ouvert ;
  - 8 825 acheteurs ;
  - médiane de 3 offres par marché, moyenne de 6,3 ;
  - 18,7 % de marchés à offre unique ;
  - 40 % des marchés reçoivent 2 offres ou moins ;
  - travaux de construction (CPV 45) : 33 221 marchés ;
  - architecture et ingénierie (CPV 71) : 7 382 ;
  - services aux entreprises (CPV 79) : 4 108.
- La médiane d'offres par famille d'achats varie de 2 (numérique, transport) à 4 (études, second œuvre) — [Dossiers Gagnants](https://dossiersgagnants.fr/barometre-marches-publics.html).

**Acteurs et prix** (comparatif publié par l'éditeur Olra, donc biaisé) — [Olra](https://olra.fr/blog/meilleurs-logiciels-reponse-appel-offres-2026)

| Outil | Positionnement | Prix |
|---|---|---|
| France Marchés | Veille | 30 à 50 €/mois |
| EDAO | BTP | 80 à 120 €/mois |
| Tenderbolt | Analyse du DCE et rédaction | environ 99 €/mois au départ, équipes sur devis |
| Olra | Audit du DCE et mémoire ; cible 1 à 50 salariés répondant à 5-30 AO/an | 79 € HT (Essentiel) ou 149 € HT (Pro) par mois, 30 € HT le dossier |
| Klekoon | Accès candidat de base | gratuit |
| Vecteur Plus, DoubleTrade, AO Conquête, Wanao, Spigao | Divers | sur devis |
| Sage e-Appel d'Offre | Intégré à Sage | lié à la licence Sage |

Le même comparatif suggère un budget de 100 à 250 €/mois pour 10 à 30 AO par an, et de 250 à 600 €/mois au-delà de 30.

**Tenderbolt** (article du 14/10/2026) — [The Media Leader FR](https://fr.themedialeader.com/?p=220572)
- Lancé en juillet 2024, rentable en moins de 2 ans.
- Plus de 100 % de croissance annuelle et plus de 200 clients dans 10 pays.
- 17 personnes, croissance financée surtout par ses revenus.
- Premier jet en 30 minutes contre 3 jours, et 70 % de temps gagné par AO (chiffres de l'entreprise).
- Secteurs : BTP, facility management, énergie, édition de logiciels, santé, assurance.
- Une autre source parle de 13 salariés et d'une fondation en 2024 — [Latka](https://getlatka.com/companies/tenderbolt.ai/competitors).

**Autres acteurs**
- **Tengo** : IA pour détecter les AO et produire l'offre ; 3,22 M$ levés le 24/06/2024 — [CB Insights](https://www.cbinsights.com/company/tengo-2/alternatives-competitors). Brainial (Pays-Bas) est cité comme concurrent.
- **Vecteur Plus** (groupe Infopro Digital, ex-Groupe Moniteur) revendique plus de 6 000 clients et 20 000 utilisateurs. Le chiffre vient d'un comparatif concurrent — [Jorpex](https://jorpex.com/fr/compare/vecteur-plus-alternative/).
- **Encombrement observé en une seule recherche** : [Remporte](https://remporte.fr/), [TenderCrunch](https://tendercrunch.com/logiciel-reponse-appels-offres), [Maître AO](https://www.maitre-ao.fr/fr/guide/ia-appel-offre), [Codito BTP](https://www.codito-btp.com/blog/ia-appel-offres-btp-methode-complete-2026), [SparkyFlow](https://sparkyflow.com/article/solution/ia-reponse-appels-offres-guide/), [Bryte](https://bryte-solutions.com/ressources/ia-gestion-appels-offres), [Koino](https://www.koino.fr/articles/ia-appels-offres-publics-repondre-2026), [Tensoria](https://tensoria.fr/blog/reponse-appels-offres-ia-roi-heures-gagnees-2026), [marchespublics.ai](https://marchespublics.ai/barometre). TenderCrunch et Propizi sont aussi cités comme concurrents de Tenderbolt — [Apistemic](https://markets.apistemic.com/companies/tenderbolt-ai-qjpmzg).
- **Gains de temps annoncés** par des pages d'éditeurs, non audités :
  - un mémoire de 8-12 h passe à 2-3 h, ou de 20 h à 3-4 h ;
  - le résultat reste un premier jet à relire, sinon il est « reconnaissable » par la commission.

  Sources : [Tensoria](https://tensoria.fr/blog/reponse-appels-offres-ia-roi-heures-gagnees-2026) ; [Maître AO](https://www.maitre-ao.fr/fr/guide/ia-appel-offre).
- **RFP privés (côté vendeur)** : AutoRFP.ai revendique une rentabilité autofinancée — [rfp.wiki](https://www.rfp.wiki/vendors/autorfp-ai). Loopio et Responsive dominent le haut de gamme.

### Inferences
- La rédaction IA de mémoires génériques devient une fonctionnalité. ChatGPT ou Claude avec le DCE en pièce jointe en couvrent déjà une partie, et Tenderbolt, Tengo et Olra ont pris de l'avance.
- Plafond pour un nouvel entrant généraliste (calc) : 1 000 clients × 120 €/mois ≈ 1,4 M€ d'ARR, avec un coût d'acquisition élevé face à plus de 15 concurrents.
- Niches encore plausibles :
  1. **Une famille d'achats précise** où la valeur vient de contenus métier : modèles de mémoire, références, moyens, certifications, méthodologies. Exemples : propreté et multiservices, maintenance CVC, ingénierie et bureaux d'études (CPV 71 : 7 382 marchés sur 7 mois).
  2. **Côté AO privés et industriels** : réponses aux consultations de grands donneurs d'ordre (questionnaires fournisseurs, RFI, qualification). C'est un sujet adjacent à l'aéro, où Johanna connaît le côté acheteur.
  3. **« Go/No-Go et pilotage du portefeuille d'AO »** : décider où répondre, suivre le taux de succès, prioriser. Cela relève du cadrage et de la priorisation, sa compétence clé.
- Risque employeur : les cabinets de conseil répondent eux-mêmes à des AO et vendent parfois de l'accompagnement à la réponse. Un SaaS est en principe autorisé, mais il faut éviter de cibler le secteur « conseil IT ».

### Gaps
- Pas de chiffre sourcé du nombre d'entreprises distinctes qui répondent ou remportent des marchés en France (ni le recensement, ni Trinta ne le donnent ; le PDF de la DAJ renvoyait une erreur 403).
- Pas d'ARR ni de prix publics pour Tengo, Vecteur Plus ou DoubleTrade.
- Je n'ai pas trouvé trace de « Tenderz », « Brainyz », « Lexito » ou « AppelOffres.ai » ; ces noms sont peut-être inexacts.
- Volume des AO privés en France : aucune donnée.

---

## Q3. Digitalisation de la vente de services pour les industriels (portails pièces et aftersales, renouvellement de contrats, intelligence de base installée) pour les ETI

### Takeaway
Le marché est validé et l'économie est forte :
- la marge d'EBIT de l'aftermarket est d'environ 25 %, contre 10 % pour la vente d'équipements neufs (McKinsey cité par Entytle) ;
- seuls 4 % des OEM réussissent à générer du revenu récurrent de services numériques (BCG 2025 cité par Entytle).

L'offre est polarisée :
- côté grands comptes : Syncron (plus de 100 k$/an et 6 à 12 mois de déploiement), Partium (15 M$ de série A), Entytle (racheté par RapidCanvas le 28/10/2026) ;
- côté petits budgets : catalogues à 99-200 €/mois (PartGrid, Interactive Spares, Components Engine) ou plateformes de commerce à 199 $/mois (Growmax).

Le milieu n'est pas servi : un « portail aftersales clé en main » pour constructeurs de machines de 20 à 500 M€ de CA, qui couvre catalogue de pièces, demandes de devis, contrats de service et relances de renouvellement. C'est presque exactement le programme qu'a mené Johanna chez un OEM aéro.

### Cited Findings
- **Entytle** (« Installed Base Intelligence », plateforme Insyghts pour constructeurs de machines) est racheté par RapidCanvas ; l'équipe, les clients et la plateforme rejoignent l'acquéreur. Communiqué du 28/10/2026 — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/10/28/3390266/0/en/rapidcanvas-acquires-entytle-to-bring-ai-driven-execution-to-the-industrial-aftermarket.html) (page non lue en entier, erreur 403 ; faits tirés de l'extrait de recherche).
- Marge d'EBIT aftermarket d'environ 25 % contre 10 % pour l'équipement neuf (McKinsey) ; 4 % des OEM réussissent le revenu récurrent numérique lié à la base installée (BCG 2025). Source éditeur — [Entytle](https://entytle.com/installed-base-revenue-opportunity-missing/).
- **Partium** (recherche de pièces par IA à partir d'une photo, d'un code-barres ou de texte) :
  - série A de 15 M$ en septembre 2024 — [Techleap](https://finder.techleap.nl/news/feed/partium-raises-15m-in-series-a) ;
  - clients surtout dans l'énergie, la production et la mine ;
  - plus de 10 000 techniciens de la Deutsche Bahn équipés — [Railmarket](https://railmarket.com/news/technology-innovation/15805-rail-traction-company-tests-euro9000-on-brenner-corridor-after-italy-approval).
- **Prix d'entrée** — [Slashdot](https://slashdot.org/software/3d-parts-catalog/saas/) ; [Growmax](https://www.growmax.io/blog/best-spare-parts-management-software) (éditeur) :
  - PartGrid environ 99 €/mois ;
  - Interactive Spares 99 €/mois ;
  - Components Engine 200 €/mois ;
  - Growmax à partir de 199 $/mois, déployé en 2 à 4 semaines ;
  - Documoto : catalogue sans fonction de commande, prix sur devis ;
  - Syncron : « Enterprise pricing (100 K$+/an) », 6 à 12 mois de déploiement.
- Syncron propose aussi un module de tarification des pièces de service — [Syncron](https://www.syncron.com/solutions/parts-pricing).

### Inferences
- **Produit cible** : un « Aftersales Portal-as-a-Service » pour ETI industrielles, constructeurs de machines spéciales, équipementiers ou fabricants de matériel médical ou agricole. Il comprendrait :
  - un catalogue de pièces généré par IA à partir des nomenclatures, PDF et vues éclatées ;
  - la recherche par photo ;
  - un panier et une demande de devis vers l'ERP ;
  - une base installée minimale (numéros de série × clients) ;
  - des alertes de renouvellement de contrats et de propositions de maintenance préventive.
- Prix plausible : 500 à 2 000 €/mois plus des frais de mise en service (calc : 150 clients × 1 000 €/mois ≈ 1,8 M€ d'ARR). Le marché UE est accessible en anglais et en allemand.
- **Atout de Johanna** : ce qu'elle a mené chez l'OEM (800 k€/an d'économies, pilotes avec des compagnies aériennes) sert directement de cas client et de modèle de business case dans la vente.
- **Risques** :
  - intégration ERP et qualité des données (nomenclatures sales), qui demandent de l'onboarding ;
  - cycle de vente de 3 à 9 mois pour une ETI ;
  - en aéro, les OEM ont des outils internes et l'employeur y a des clients. Mieux vaut viser les machines industrielles non aéro.
- **Défensibilité vs IA générique** : bonne. La valeur vient des données intégrées (base installée, prix, stocks) et du workflow transactionnel, que ChatGPT ne fournit pas.

### Gaps
- Prix réels et nombre de clients de Partium et Documoto non trouvés.
- Nombre d'ETI de la mécanique et des machines en France non chiffré (il faudrait l'INSEE ou la FIM).
- Montant du rachat d'Entytle non publié.
- Pas de données sur les outils de renouvellement de contrats de service pour les ETI (ServiceSource et autres non recherchés).

---

## Q4. Assistant de vente IA pour distributeurs B2B de niche et portail client as-a-service

### Takeaway
Lire automatiquement les commandes et demandes de devis reçues par e-mail ou PDF, puis les saisir dans l'ERP, est devenu l'un des créneaux les plus financés de 2026 :
- Canals : 35 M$ de série A en mai 2026, plus de 100 distributeurs ;
- Mercura : 1,8 M€ en seed en janvier 2026 ;
- Proton.ai : lancement d'un produit en juillet 2026 ;
- un comparatif recense 19 éditeurs.

En France, au moins 4 acteurs existent déjà (Order1, Vistaflow, Kimayo, evolio). Le créneau est attractif mais encombré. Une entrée n'a de sens que verticale (un ERP précis × un type de négoce).

### Cited Findings
- **Canals** (Miami) : série A de 35 M$ menée par Base10, annoncée le 28/05/2026 ; plus de 100 distributeurs (DSG, Locke Supply, The Kendall Group). Produit parti de la saisie de commandes et étendu à la vente, au service client, à la comptabilité, aux achats et à la réception — [Distribution Strategy Group](https://distributionstrategy.com/2026/05/canals-raises-35-million-to-expand-ai-automation-platform-for-wholesale-distributors/) ; [MDM](https://www.mdm.com/news/breaking-news-in-wholesale-distribution/canals-raises-35m-series-a-to-expand-ai-workflow-tools-for-distributors/).
- **Proton.ai** lance une plateforme d'automatisation de la saisie des commandes et devis pour distributeurs en juillet 2026 — [Distribution Strategy Group](https://distributionstrategy.com/2026/07/proton-ai-launches-ai-platform-to-automate-order-and-quote-entry-for-distributors/).
- **Mercura** (Munich, YC) : seed de plus de 1,8 M€ (TQ Ventures, SignalFire, YC), annoncé le 07/01/2026 ; devis et commandes pour le négoce CVC, électricité et plomberie, avec synchronisation ERP — [Munich Startup](https://www.munich-startup.de/en/news/mercura-secures-e1-8-million).
- Un comparatif recense 19 éditeurs d'« AI order entry » en 2026 — [Y Meadows](https://www.ymeadows.com/en/insights/blog/ai-order-entry-vendors/).
- Merlin cible le devis catalogue des distributeurs — [Merlin](https://merlin.work/compare/merlin-vs-paperless-parts).
- **Acteurs français** :
  - Order1 (OrderScan lit les bons de commande PDF, mail ou marketplace) — [Order1](https://www.order1.ai/) ;
  - Vistaflow (agent entre la boîte mail et l'ERP Divalto, « jusqu'à 80 % » de temps gagné selon l'éditeur ; cible aussi la distribution d'EPI) — [Vistaflow](https://www.vistaflow.ai/blog/ia-divalto) ;
  - Kimayo (e-mail, PDF, EDI, Excel ; correction des codes articles) — [Kimayo](https://kimayo.com/saisie-automatique-commandes-ia/) ;
  - evolio.ai — [evolio](https://evolio.ai/).
- **Portails de commerce B2B** : WizCommerce et d'autres éditeurs présentent l'IA comme un levier pour le commerce de gros — [WizCommerce](https://wizcommerce.com/blog/ai-in-b2b-ecommerce-use-cases/).

### Inferences
- La saisie de commandes devient vite une commodité : les frais d'intégration ERP dominent et le support est lourd. C'est peu compatible avec 10 h/semaine.
- Un angle plus proche du « funnel » reste peu couvert pour les distributeurs français : le **suivi des devis non transformés**, qui comprend :
  - la relance automatique ;
  - un score de probabilité de transformation ;
  - des alertes de clients dormants ou de perte de part de portefeuille, à partir de l'historique de l'ERP.

  Prix possible : 300 à 1 000 €/mois. C'est une brique de « sales intelligence » sans saisie, donc plus légère à intégrer (lecture seule de l'ERP).
- Le portail client as-a-service généraliste est en concurrence avec les plateformes e-commerce B2B (Sana, Oro, etc., non recherchées). Pas recommandé comme produit autonome.

### Gaps
- Prix des acteurs français non publiés.
- Nombre de distributeurs B2B en France par segment non chiffré.
- Didero (série A de 30 M$ citée dans un résumé de recherche) non vérifié dans une source primaire.

---

## Q5. Quote-to-cash pour PME et ETI : catalogue d'offres et « PIM pour services », CPQ, facturation récurrente ou à l'usage, et réforme de la facturation électronique (ajout de périmètre)

### Takeaway
Le marché est très capitalistique et se consolide vite :
- Stripe a racheté Metronome (environ 1 Md$, janvier 2026), Adyen a racheté Orb (environ 335 M$, vers juillet 2026), Salesforce a racheté m3ter (juillet 2026) ;
- DealHub a racheté Subskribe (novembre 2025) ;
- TeamSystem a racheté Sellsy (septembre 2025) ;
- Pennylane est valorisé plus de 3,5 Md€ (janvier 2026).

La réforme française de facturation électronique déclenche la demande : réception obligatoire depuis le 01/09/2026, émission obligatoire pour les PME et TPE au 01/09/2027, amendes portées à 50 € par facture. Mais elle profite surtout aux plateformes agréées, au nombre de 163 ou plus.

Le trou du marché est en amont de la facture, sur deux points :
1. définir et tarifer les offres de services, c'est-à-dire un catalogue de services : aucun outil dédié trouvé ;
2. passer du contrat de service récurrent (maintenance, location, abonnement, usage) à une facture conforme. Les CPQ coûtent 60 à 150 $ par utilisateur et par mois, avec une médiane de 44 k$/an chez DealHub, ce qui est surdimensionné pour une PME industrielle.

### Cited Findings
**Réforme de la facturation électronique**
- Réception obligatoire pour toutes les entreprises depuis le 01/09/2026. Émission et e-reporting au 01/09/2027 pour les PME et micro-entreprises — [Konformy](https://konformy.com/blog/facturation-electronique-2026-qui-est-concerne) ; [ma-facture-electronique.org](https://ma-facture-electronique.org/reforme-2026/echeance-septembre-2026/).
- Pas de nouveau report — [Compta-online](https://www.compta-online.com/facturation-electronique-ao5562) ; [Why](https://www.why.eu/facture-electronique-nouveau-report-pour-les-pme/).
- **Nombre de plateformes agréées (PA, ex-PDP)** :
  - 163 sur les listes officielles (149 définitives et 14 sous réserve), selon le registre DGFiP au 03/09/2026 rapporté par l'éditeur Why — [Why](https://www.why.eu/facture-electronique/) ;
  - environ 140, dont 52 qui visent l'émission dès septembre 2026 — [Compta-online](https://www.compta-online.com/facturation-electronique-ao5562) ;
  - plus de 100 — [Libeo](https://libeo.io/blog/plateforme-de-facturation-electronique).
- Why affirme que plus de 20 % des flux ont été rejetés au démarrage, d'après un « bilan AIFE/DGFiP du 03/09 ». Ce chiffre n'est pas confirmé par une source officielle — [Why](https://www.why.eu/facture-electronique/).
- **Sanctions** : la loi n° 2026-103 du 19/02/2026 (loi de finances pour 2026) porte l'amende de 15 € à 50 € par facture non électronique, et selon certaines sources de 250 € à 500 € par manquement à l'e-reporting. Le plafond reste de 15 000 €/an. La date d'application est discutée (2026 ou 2027) — [CAPEB](https://www.capeb.fr/actualites/des-sanctions-plus-severes-en-cas-de-non-respect-de-la-facturation-electronique-vesr0i) ; [ecosio](https://ecosio.com/fr/blog/amende-facturation-electronique/) ; [Portail auto-entrepreneur](https://www.portail-autoentrepreneur.fr/academie/gestion-auto-entreprise/facturation/sanctions-facturation-electronique).

**Acteurs PME en France**
- **Pennylane** :
  - 75 M€ levés en avril 2025 pour accélérer avant la réforme — [Maddyness](https://www.maddyness.com/2025/04/07/pennylane-leve-75-millions-deuros-a-lapproche-de-la-reforme-de-la-facturation-electronique/) ;
  - 175 M€ levés en janvier 2026 (TCV, Blackstone), valorisation de plus de 3,5 Md€ — [Maddyness](https://www.maddyness.com/2026/01/20/pennylane-nouvelle-levee-de-fonds-de-175-millions-deuros-pour-la-licorne-francaise/) ;
  - 115 M€ d'ARR en 2025, selon Maddyness cité dans un résumé de recherche (non relu en direct) ;
  - immatriculation définitive comme PA en décembre 2025 — [ma-facture-electronique.org](https://ma-facture-electronique.org/?p=1417).
- **Sellsy** (« lead-to-cash » pour PME) racheté par l'italien TeamSystem (Hellman & Friedman) à PSG, le 24/09/2025 — [BusinessWire](https://www.businesswire.com/news/home/20250924851671/en/TeamSystem-Strengthens-Its-Presence-in-France-and-Spain-With-the-Acquisition-of-Sellsy-a-Leading-Cloud-Solutions-Specialist-for-SMEs).
- **Prix publics, très variables selon les sources** — [Hayot Expertise](https://hayot-expertise.fr/blog/evoliz-vs-sellsy-vs-axonaut-gestion-facturation-tpe-2026) ; [comparatif-facture-electronique.fr](https://www.comparatif-facture-electronique.fr/sellsy-vs-axonaut/) :
  - Sellsy : 29 à 49 € HT par utilisateur et par mois ;
  - Axonaut : environ 35 à 97 €/mois ;
  - les deux sont des PA immatriculées (Sellsy le 24/12/2025, Axonaut le 08/01/2026).
- **Visma** a racheté Evoliz (février 2025 ; plus de 13 000 PME françaises ; certifié NF203) — [Tech.eu](https://tech.eu/2025/02/05/visma-expands-into-france-with-evoliz-acquisition/). Visma avait déjà acquis Chaintrust (2024), Teledec (2024) et Inqom (2022) — [Techzine](https://www.techzine.eu/news/applications/115514/visma-strengthens-presence-in-france-through-acquisition-of-chaintrust).

**CPQ**
- **DealHub** :
  - pas de prix public ; offres Growth et Scale ; facturation et reconnaissance du revenu seulement dans Scale ;
  - rachat de Subskribe en novembre 2025, plateforme de facturation pas encore intégrée — [Kugamon](https://www.kugamon.com/compare/vendors/dealhub/) (concurrent) ;
  - contrat médian de 44 400 $/an sur 145 achats — [Vendr](https://www.vendr.com/marketplace/dealhub) ;
  - 60 à 150 $ par utilisateur et par mois selon les estimations — [Kugamon](https://www.kugamon.com/compare/pricing/dealhub/).
- **Salesforce** : CPQ à 75-150 $ et Revenue Cloud à 150-200 $ par utilisateur et par mois — [Kugamon](https://www.kugamon.com/compare/pricing/dealhub/).
- **Cacheflow** : aucune donnée trouvée.

**Facturation par abonnement et à l'usage**
- Stripe a finalisé le rachat de Metronome le 14/01/2026 (environ 1 Md$) ; Adyen a racheté Orb (environ 335 M$, clôture vers le 01/07/2026) ; Salesforce a racheté m3ter (clôture le 01/07/2026). Source éditeur — [UsageBox](https://usagebox.com/articles/independent-usage-based-billing-after-acquisitions-2026) ; voir aussi [Lago](https://getlago.com/blog/lago-vs-metronome).
- **Lago** (open source AGPL, fondateurs français) : 22 M$ levés (seed de 7 M$ SignalFire, série A de 15 M$ FirstMark, 2024) — [Sacra](https://sacra.com/c/lago/).
- **Prix** — [CostBench](https://costbench.com/compare/chargebee-vs-stripe-billing/) ; [CostBench](https://costbench.com/software/subscription-billing/) :
  - Chargebee Performance à partir de 599 $/mois ;
  - Stripe Billing environ 0,7 % du volume facturé en paiement à l'usage ;
  - Zuora estimé à plus de 75 k$/an ;
  - Maxio et Zuora conseillés au-delà de 10 M$ et 50 M$ d'ARR.

**Catalogue d'offres et « PIM pour services »**
- Quable (PIM français) défend l'usage d'un PIM pour les offres de services : variantes, multilingue, déclinaisons par marché. Source éditeur — [Quable](https://www.quable.com/en/blog/a-pim-for-service-companies-but-what-for).
- Aucun outil dédié à la « productisation » des services industriels (référence de service, paliers, grilles de prix) n'a été trouvé. Les PIM industriels (Catsy, inRiver, Quable) restent centrés sur le produit physique — [Catsy](https://catsy.com/blog/pim-software-for-industrial-product/) ; [inRiver](https://www.inriver.com/solution/industrial-manufacturing/page/21/).

### Inferences
- **Ne pas devenir PA ni facturier généraliste** : il y a plus de 160 plateformes et des acteurs financés à des centaines de millions (Pennylane, Visma, TeamSystem).
- **Se brancher sur les PA via API** et vendre la couche manquante : le passage du contrat de service à une facture conforme pour les PME et ETI industrielles et de services. Cette couche couvre :
  - le catalogue de services et les paliers (bronze, silver, gold, avec un temps d'intervention garanti) ;
  - les grilles de prix et les remises ;
  - la génération de devis et de contrats ;
  - la révision de prix indexée (Syntec, indices INSEE) ;
  - la facturation récurrente ou à l'usage (heures, interventions, compteurs machine), poussée vers la PA du client.

  C'est l'expertise d'Epic Owner « vente de services » de Johanna.
- **Déclencheur commercial** : l'obligation d'émettre en septembre 2027 (avec 50 € d'amende par facture) pousse les PME à revoir tout le cycle devis-facture entre septembre 2026 et septembre 2027. Il faut une V1 au premier semestre 2027 pour attraper cette fenêtre.
- **Prix plausible** : 200 à 800 €/mois par entreprise (calc : 300 clients × 400 €/mois ≈ 1,4 M€ d'ARR).
- **Risques** :
  - Sellsy, Axonaut et Pennylane peuvent ajouter des fonctions de contrat récurrent ;
  - il faut une vraie spécialisation métier (maintenance industrielle, location de matériel, prestations récurrentes) ;
  - les cabinets de conseil intègrent Salesforce CPQ, mais vendre un produit à des PME ne concurrence pas l'offre d'intégration grands comptes. Il faut tout de même le vérifier avec l'employeur.

### Gaps
- Pas de statistique sur la part des PME prêtes pour 2027.
- Pas de chiffre sur le nombre d'entreprises françaises qui facturent des contrats de maintenance ou de service récurrents.
- Prix de Cacheflow et de Subskribe introuvables.
- La date d'application exacte des nouvelles amendes reste à vérifier dans l'article 1737 du CGI (Légifrance).
- La page officielle economie.gouv.fr et le guide PDF de la DGFiP n'ont pas pu être lus (erreur 403 ou PDF non extractible).

---

## Q6. Opportunités produit CX pour PME et ETI B2B (voix du client, parcours client, maturité et CoE CX, health score, analyse des tickets) (ajout de périmètre)

### Takeaway
Le CX est un marché très encombré en haut (Qualtrics, Medallia, Gainsight, Planhat) comme en bas, avec des dizaines d'outils de sondage NPS. Deux signaux 2026 ouvrent pourtant une fenêtre :
1. Qualtrics a fermé Delighted le 30/06/2026 et oriente les clients vers des suites entreprise. Selon des concurrents, ces suites coûtent 25 à 100 k$/an ou plus, ce qui laisse des PME orphelines.
2. L'analyse de feedback par IA (Unwrap, Enterpret) reste chère (environ 24 k$/an ou plus) et pensée pour le logiciel B2C ou le SaaS.

Gap identifié : un outil de voix du client B2B relationnelle pour les industriels et les entreprises de services. Il rapprocherait enquêtes, tickets SAV et historique de devis pour sortir des signaux de churn et d'upsell par compte. Il pourrait inclure un « CX CoE-in-a-box » (diagnostic de maturité et modèles de programme).

### Cited Findings
- **Delighted** :
  - fin des renouvellements annuels le 01/07/2025 ;
  - arrêt le 30/06/2026 (une version de la FAQ dit le 01/07/2026) ;
  - migration proposée vers « Qualtrics XM for Customer Experience ».

  Source : [Delighted FAQ](https://help.delighted.com/article/840-delighted-sunset-faq).
- Selon un concurrent, Qualtrics demande 25 000 à 100 000 $/an ou plus et 3 à 6 mois d'implémentation. Source éditeur — [Simplesat](https://www.simplesat.io/blog/delighted-is-shutting-down-dont-follow-their-migration-advice). Les concurrents se battent pour récupérer la base Delighted : [Zonka](https://www.zonkafeedback.com/blog/delighted-is-sunsetting-switch-to-zonka-feedback), [SurveySparrow](https://surveysparrow.com/blog/how-to-migrate-from-delighted), [Usercall](https://www.usercall.co/post/delighted-alternatives-shutdown-2026).
- **Unwrap** :
  - série A de 12 M$ menée par Scale — [Scale VP](https://www.scalevp.com/press/unwrap-ai-receives--12-million-in-series-a-funding) ;
  - prix selon le volume de feedback ; offre Enterprise listée à 24 000 $/an — [Toolradar](https://toolradar.com/tools/unwrap).
- **Enterpret** : prix sur devis, pas d'offre gratuite — [Toolradar](https://toolradar.com/compare/enterpret-vs-unwrap).
- **Planhat** (Stockholm) :
  - autofinancé pendant 7 ans, puis série A de 50 M$ en avril 2022 — [Planhat](https://www.planhat.com/press/next-generation-customer-platform-planhat-raises-50m-series-a) ;
  - nommé leader du Magic Quadrant Gartner Customer Success en novembre 2025, d'après un résumé de recherche.
- **Gainsight** (Vista, valorisation d'environ 1,1 Md$ en 2020) a racheté Skilljar en avril 2025 — [Kirkland](https://www.kirkland.com/news/press-release/2025/04/kirkland-advises-vista-backed-gainsight-on-acquisition-of-skilljar) — puis Staircase AI — [StartupHub](https://startuphub.ai/news/staircase-ai-acquired-by-gainsight-to-extend-leadership-in-human-first-ai).
- **Parcours et recherche client** :
  - UXPressia : gratuit, Pro à 36 $ et Business à 95 $ par utilisateur et par mois, Enterprise sur devis — [Capterra UK](https://www.capterra.co.uk/software/172668/uxpressia) ;
  - Smaply : 4 offres, prix non trouvés — [Capterra](https://www.capterra.com/p/177161/Smaply/pricing/) ;
  - Dovetail : Professional à 29 $ par utilisateur et par mois selon Capterra, dépense moyenne de 2 531 $/an pour une PME selon SpendHound — [SpendHound](https://www.spendhound.com/marketplace/dovetail-pricing).
- **Skeepers** (Marseille, avis clients et UGC, détenu par PSG) : 60 M€ de CA et 450 salariés en 2023, 9 start-up rachetées (Avis Vérifiés, MyFeelBack, etc.), objectif de 100 M€ — [Maddyness, 2023](https://www.maddyness.com/2023/11/08/skeepers-ou-comment-acquerir-9-startups-pour-creer-un-leader-europeen/). Orienté B2C et e-commerce.
- **Satismeter et Medallia** : pas de données recueillies.

### Inferences
- **À éviter** : un outil de sondage NPS de plus, la cartographie de parcours (UXPressia et Smaply couvrent le besoin à moins de 100 $ par utilisateur et par mois), un CSM généraliste (Gainsight, Planhat) et l'analyse de feedback SaaS (Unwrap, Enterpret).
- **Angle crédible** : « B2B Account Voice » pour industriels et sociétés de services de 20 à 500 M€ de CA. Il comprendrait :
  - des enquêtes relationnelles par compte, pas seulement transactionnelles ;
  - l'analyse IA des tickets SAV, des e-mails et des comptes rendus d'intervention ;
  - un health score par compte croisé avec la base installée et les contrats (lien avec Q3 et Q5) ;
  - des alertes d'upsell et de renouvellement à risque.
- Ce produit se combine naturellement avec le portail aftersales (Q3) comme module, plutôt que comme produit séparé.
- Le « CX CoE-in-a-box » (diagnostic de maturité, modèles de gouvernance, rituels) est vendable, mais ressemble beaucoup à du conseil : **risque de conflit avec l'employeur**. Mieux vaut l'intégrer au produit comme parcours d'onboarding qu'en faire une offre séparée.
- Prix plausible : 300 à 1 500 €/mois. La défensibilité vient de l'intégration des données internes (SAV, ERP), pas de l'analyse de texte, devenue une commodité.

### Gaps
- Nombre et profil des anciens clients Delighted en Europe : inconnus.
- Prix de Satismeter, Medallia, Gainsight et Planhat non trouvés.
- Pas de données sur l'adoption des programmes de voix du client dans les ETI industrielles françaises.

---

## Q7. Outils de cadrage produit et projet (business case, suivi de valeur, gestion de portefeuille pour PME et secteur public, OKR) : évaluation honnête de la saturation

### Takeaway
Ces marchés sont saturés et en consolidation :
- les OKR se concentrent (WorkBoard a racheté Quantive en mai 2025, Microsoft a fermé Viva Goals fin 2025) ;
- les outils de gestion de portefeuille (Planview, Sciforma, Triskell à partir d'environ 15 €, Planisware) couvrent déjà les PME ;
- Copilot et ChatGPT génèrent un business case ou un brief produit en quelques minutes.

C'est le domaine de compétence principal de Johanna, mais c'est la moins bonne base pour un produit autonome. À utiliser plutôt comme fonctionnalité différenciante, par exemple un business case automatique dans le portail aftersales ou l'outil Go/No-Go d'AO.

### Cited Findings
- WorkBoard a racheté Quantive en mai 2025, en citant ses partenariats de co-vente avec Workday et Microsoft — [BusinessWire](https://www.businesswire.com/news/home/20250528302450/en).
- Viva Goals (Microsoft) fermé le 31/12/2025, d'après un suivi des fermetures tenu par un éditeur d'OKR — [Tability](https://www.tability.io/compare/shutdowns).
- Le marché est décrit à la fois comme « fragmenté » et « consolidé » selon les cabinets d'étude — [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/okr-and-goal-management-software-market).
- Article ancien : « Why is everyone making OKR software? » — [TechCrunch](https://techcrunch.com/?p=1935428).
- Gestion de portefeuille : Triskell « à partir de 15 € » et Planview ProjectAdvantage « 760 $ » sur Capterra France, sans unité précisée — [Capterra FR](https://www.capterra.fr/compare/18756/146070/Planview-ProjectAdvantage/vs/triskell-ppm). Triskell revendique l'absence d'engagement long, contre des contrats pluriannuels chez Planview (source éditeur) — [Triskell](https://triskellsoftware.com/compare/planview-vs-triskell/).

### Inferences
- Faible pouvoir de prix, forte substitution par l'IA générique et par les suites (Microsoft, Atlassian, monday).
- Le « value management » de vente (calculateurs de ROI) existe chez les éditeurs spécialisés (non recherchés).
- Une niche plausible mais peu documentée : la mesure de la valeur des projets numériques publics. L'outil de l'État existe mais il est rudimentaire. Je n'ai pas de données ; c'est à traiter comme une hypothèse.
- Verdict : ne pas en faire le produit principal.

### Gaps
- Pas de recherche sur les outils de chiffrage de valeur ou de ROI de vente (Cuvama, Mediafly, etc.) ni sur la méthode de valeur des projets numériques de l'État et son outillage.
- Pas de prix fiables pour Sciforma ou Planview.

---

## Q8. Autres niches à forte douleur où un profil « funnel et cadrage » a un avantage

### Takeaway
Le pricing B2B pour les entreprises de moins de 50 M€ de CA est mal servi : Pricefx démarre à environ 2 495 $ par module et par mois, avec un coût total estimé de 100 à 200 k$ la première année. Un outil « pricing light » pour PME industrielles et distributeurs est donc une niche plausible, mais peu documentée. Elle couvrirait les grilles tarifaires, les hausses annuelles, les fuites de marge et les remises hors politique.

### Cited Findings
- Pricefx : à partir de 2 495 $ par module et par mois — [TrustRadius](https://www.trustradius.com/compare-products/pricefx). Déploiement de taille moyenne estimé à environ 100 k$/an de SaaS plus 100 k$ d'implémentation, et le pricing dédié « pas rentable sous ~50 M$ de CA ». Source non vérifiée — [DataToolIndex](https://datatoolindex.pages.dev/use-cases/best-pricing-analytics-software-b2b-industrial/).
- Pricefx s'adresse au mid-market et aux grands comptes (distribution, biens de consommation, industrie) — [Capterra](https://www.capterra.com/p/146889/Price-f-x/). Zilliant a des coûts comparables. Pricemoov (FR) et Competera apparaissent, sans prix — [Capterra AE](https://www.capterra.ae/compare/146889/180198/price-f-x/vs/pricemoov).
- Syncron vend un module de tarification des pièces de service aux OEM — [Syncron](https://www.syncron.com/solutions/parts-pricing).

### Inferences
- Un « pricing des pièces de rechange et des services pour ETI industrielles » combine Q3 et Q8. L'aftermarket offre les marges les plus élevées (Q3), et ces entreprises ne peuvent pas se payer Syncron ou Pricefx.
- Tarif plausible : 500 à 1 500 €/mois. Les données (historique de ventes de l'ERP) restent dans la logique d'une connexion en lecture seule.
- La conformité « régulée » (KYC/KYB pour l'onboarding client) n'a pas été recherchée. Elle semble a priori saturée (fintechs financées) et réglementairement lourde.

### Gaps
- Pas de données sur les prix ou les clients de Pricemoov ni sur d'éventuels outils de pricing pour PME en France.
- Pas de données sur la fuite de marge typique des PME industrielles.

---

## Q9. Exemples documentés de petites équipes ou de fondateurs solo atteignant 1 M+ d'ARR (ou une sortie) en IA ou SaaS B2B vertical, 2024-2026

### Takeaway
Les exemples vérifiables existent mais sont rares. Le cas le plus pertinent est Tenderbolt, une IA d'AO française : lancé en juillet 2024, rentable en moins de 2 ans, plus de 200 clients, environ 17 personnes, autofinancé en grande partie. Le cas d'une sortie solo est Base44 : un fondateur seul, sans financement externe, racheté environ 80 M$ par Wix en 6 mois, mais dans un segment horizontal. Les listes « solo à 1 M$ ARR » circulant en ligne sont surtout non vérifiables.

### Cited Findings
- **Tenderbolt** : voir Q2 — [The Media Leader FR](https://fr.themedialeader.com/?p=220572).
- **Base44** — [Globes](https://en.globes.co.il/en/article-1001513267) ; [DesignRush](https://news.designrush.com/wix-buys-ai-startup-base44-for-80m-six-month-sprint-deal) ; [Wandb](https://wandb.ai/byyoung3/ml-news/reports/Wix-Acquires-Israeli-AI-Startup-Base44-for-80-Million--VmlldzoxMzI5MTMzNw) :
  - fondé par Maor Shlomo, autofinancé ;
  - racheté par Wix pour environ 80 M$ cash plus des compléments de prix jusqu'en 2029 (juin 2025) ;
  - 6 à 8 salariés selon les sources ;
  - plus de 1 300 clients payants selon une source.
- **Planhat** (SaaS B2B de customer success) : 7 ans d'autofinancement avant une série A de 50 M$ — [Silicon Canals](https://siliconcanals.com/?p=7556).
- **AutoRFP.ai** revendique une rentabilité autofinancée, sans chiffre publié — [rfp.wiki](https://www.rfp.wiki/vendors/autorfp-ai).
- **BuiltWith** (données B2B, 1 personne) aurait 14 M$/an de revenus selon un article promotionnel non sourcé (22/02/2026) — [Vin Patel](https://vinpatel.com/insights/solo-founder-revenue-atlas/).
- Les guides en ligne avancent des prix de 100 à 500 $ par utilisateur et par mois pour les agents IA verticaux et une marge brute de 70 à 85 % en micro-SaaS vertical. Ce sont des listes SEO non vérifiées — [Growtoria](https://growtoria.com/vertical-micro-saas-ai-business-guide/) ; [Jagadish](https://jagadishwrites.com/blog/ai-business-ideas-that-can-reach-1m-arr-2026-playbook-for-solo-founders).

### Inferences
- Le modèle Tenderbolt est la référence la plus proche :
  - une niche B2B française avec un process documentaire lourd ;
  - un prix d'environ 100 € par mois ou plus ;
  - de l'autofinancement ;
  - mais 17 personnes à plein temps, donc bien plus que 10 h/semaine.

  Pour Johanna, 1 M€ d'ARR suppose de passer à plein temps ou de recruter un associé opérationnel vers 200-300 k€ d'ARR.

### Gaps
- ARR exact de Tenderbolt non publié.
- Aucun cas vérifié d'un fondateur solo à temps partiel dépassant 1 M€ d'ARR en SaaS B2B vertical français.

---

## Q10. Acquéreurs français et européens actifs sur ces segments (pour une sortie d'ici 2036)

### Takeaway
Les acheteurs stratégiques sont nombreux et actifs en 2025-2026 sur la PME française (Visma, TeamSystem, Infopro Digital, Skeepers/PSG), le quote-to-cash (Stripe, Adyen, Salesforce, DealHub), l'aftermarket industriel (RapidCanvas) et le CX (Gainsight, WorkBoard). Une sortie à 1-4 M€ d'ARR vers un éditeur PME européen (multiple non documenté ici) est un scénario réaliste si le produit s'intègre à leur pile : ERP PME, facturation, veille AO.

### Cited Findings

| Acquéreur | Opérations | Sources |
|---|---|---|
| Visma | Evoliz (2025, 13 000 PME), Chaintrust (2024), Teledec (2024), Inqom (2022) | [Tech.eu](https://tech.eu/2025/02/05/visma-expands-into-france-with-evoliz-acquisition/) ; [Techzine](https://www.techzine.eu/news/applications/115514/visma-strengthens-presence-in-france-through-acquisition-of-chaintrust) ; [Cision](https://publish.ne.cision.com/Release/ViewReleaseHtml/265CAA7C85DA8923) |
| TeamSystem (IT) | Sellsy (09/2025), après Clémentine | [BusinessWire](https://www.businesswire.com/news/home/20250924851671/en/TeamSystem-Strengthens-Its-Presence-in-France-and-Spain-With-the-Acquisition-of-Sellsy-a-Leading-Cloud-Solutions-Specialist-for-SMEs) ; [Le Journal des Entreprises](https://www.lejournaldesentreprises.com/breve/lediteur-rochelais-sellsy-passe-sous-pavillon-italien-2127020) |
| Infopro Digital | Groupe Moniteur et Vecteur Plus (veille AO) ; Companeo (marketplace B2B) | [Le Monde Informatique](https://www.lemondeinformatique.fr/actualites/lire-comm-back-passe-entre-les-mains-de-vecteur-plus-23551.html) (ancien) ; [FrenchWeb](https://www.frenchweb.fr/infopro-digital-soffre-companeo-pour-devenir-un-acteur-majeur-des-marketplaces-b2b-en-europe/313178) |
| RapidCanvas | Entytle (10/2026, base installée aftermarket) | [GlobeNewswire](https://www.globenewswire.com/news-release/2026/10/28/3390266/0/en/rapidcanvas-acquires-entytle-to-bring-ai-driven-execution-to-the-industrial-aftermarket.html) |
| Stripe / Adyen / Salesforce | Metronome (01/2026) / Orb (07/2026) / m3ter (07/2026) | [UsageBox](https://usagebox.com/articles/independent-usage-based-billing-after-acquisitions-2026) |
| DealHub | Subskribe (11/2025) | [Kugamon](https://www.kugamon.com/compare/vendors/dealhub/) |
| Gainsight (Vista) | Skilljar (04/2025), Staircase AI, UpdateAI | [Kirkland](https://www.kirkland.com/news/press-release/2025/04/kirkland-advises-vista-backed-gainsight-on-acquisition-of-skilljar) ; [StartupHub](https://startuphub.ai/news/staircase-ai-acquired-by-gainsight-to-extend-leadership-in-human-first-ai) |
| WorkBoard | Quantive (05/2025) | [BusinessWire](https://www.businesswire.com/news/home/20250528302450/en) |
| Skeepers (PSG) | 9 rachats de start-up FR en CX et avis clients | [Maddyness, 2023](https://www.maddyness.com/2023/11/08/skeepers-ou-comment-acquerir-9-startups-pour-creer-un-leader-europeen/) |
| Wix | Base44 (06/2025) | [Globes](https://en.globes.co.il/en/article-1001513267) |

### Inferences
- Pour un outil AO : Infopro Digital (Vecteur Plus) et les éditeurs d'ERP BTP ou PME sont des acheteurs naturels.
- Pour le quote-to-cash et les services : Visma, TeamSystem, Pennylane et les éditeurs d'ERP industriels.
- Pour l'aftersales : les éditeurs d'ERP et de gestion d'interventions, ou des acteurs comme RapidCanvas.

### Gaps
- Cegid, Septeo, Docaposte, Sage, Lefebvre Dalloz, Divalto et Sylob non recherchés.
- Les multiples de valorisation des rachats de petits SaaS français ne sont pas documentés ici.
- (Les sources cfnews ont été volontairement exclues.)

---

## Q11. Shortlist : 6 à 10 opportunités produit étroites, évaluées pour Johanna

### Takeaway
Les meilleurs paris combinent :
- son expertise de vente de services et de funnel B2B ;
- un déclencheur daté (réforme de la facture électronique de 2027, sortie de Delighted) ;
- des données intégrées (ERP, base installée), qui protègent de ChatGPT et Copilot.

Classement :
1. un **quote-to-cash pour contrats de services récurrents des PME et ETI industrielles** (catalogue de services, devis, indexation, facturation vers la PA) ;
2. un **portail aftersales clé en main pour constructeurs de machines de taille ETI** ;
3. un **« RFQ desk » de suivi des devis pour sous-traitants et distributeurs**.

Les outils d'AO et la voix du client B2B sont viables seulement en version très verticale. Les outils de cadrage (OKR, gestion de portefeuille) et la saisie de commandes généraliste sont déconseillés.

### Cited Findings
- Les données d'appui sont citées en Q1 à Q10 :
  - déclencheur facture électronique et amendes ([Konformy](https://konformy.com/blog/facturation-electronique-2026-qui-est-concerne), [CAPEB](https://www.capeb.fr/actualites/des-sanctions-plus-severes-en-cas-de-non-respect-de-la-facturation-electronique-vesr0i)) ;
  - prix des CPQ ([Vendr](https://www.vendr.com/marketplace/dealhub)) ;
  - aftermarket ([Entytle](https://entytle.com/installed-base-revenue-opportunity-missing/), [Growmax](https://www.growmax.io/blog/best-spare-parts-management-software)) ;
  - devis industriels ([Morsa](https://morsa.ai/guides/manufacturing-quoting-software)) ;
  - AO ([Olra](https://olra.fr/blog/meilleurs-logiciels-reponse-appel-offres-2026), [Trinta](https://trinta.ai/barometre), [The Media Leader](https://fr.themedialeader.com/?p=220572)) ;
  - CX ([Delighted](https://help.delighted.com/article/840-delighted-sunset-faq)) ;
  - pricing ([TrustRadius](https://www.trustradius.com/compare-products/pricefx)).

### Inferences
Grille : ★ = faible, ★★★ = fort. Plafonds d'ARR calculés à l'ordre de grandeur et non validés.

| # | Opportunité étroite | Douleur | Acheteur et budget | Prix plausible | Concurrence et trou | Faisable sans dev (IA + freelances) | Automatisable (peu d'ops) | Plafond d'ARR | Défense vs IA générique et gros éditeurs |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Contrat de service → facture** pour PME et ETI de maintenance, location ou prestations récurrentes : catalogue de services, devis, révision indexée, facturation à l'usage, envoi vers la PA | ★★★ (échéance 09/2027, 50 € d'amende par facture) | DAF et direction commerciale de PME de 5 à 100 M€ | 200 à 800 €/mois | Sellsy, Axonaut, Pennylane sont généralistes ; CPQ trop chers (médiane DealHub 44 k$) ; pas d'outil catalogue de services | ★★ (API des PA, moteur de facturation existant comme Lago, modèles métier) | ★★ (onboarding de contrats, puis récurrent) | 1 à 3 M€ (FR, puis BE/IT/ES avec leurs propres réformes) | ★★ (données contractuelles et intégrations ; risque d'ajout de fonctions par les éditeurs PME) |
| 2 | **Portail aftersales clé en main** pour constructeurs de machines ETI : catalogue IA depuis les nomenclatures, recherche par photo, devis et commande, base installée, relances de contrats | ★★★ (marge aftermarket ~25 % contre ~10 % ; seuls 4 % des OEM réussissent le récurrent) | Directions service et aftersales d'ETI de 20 à 500 M€ | 500 à 2 000 €/mois plus mise en service | Syncron et Partium visent les grands comptes ; PartGrid et Growmax sont basiques ; Entytle racheté | ★★ (freelances intégration ERP) | ★ à ★★ (qualité des données à l'onboarding) | 1,5 à 4 M€ (UE) | ★★★ (données et workflow transactionnel) |
| 3 | **RFQ desk** pour sous-traitants mécaniques et distributeurs techniques : captation des RFQ dans la boîte mail, brouillon de devis, relances, transformation par client | ★★ à ★★★ (15 min à 2 h par pièce ; devis non suivis) | Dirigeants et ADV de PME de 10 à 200 salariés | 150 à 500 €/mois | Paperless Parts (US, environ 1 500 $/mois) ; 5 acteurs IA FR centrés sur le calcul, pas sur le funnel | ★★ | ★★ | 0,7 à 1,5 M€ en FR | ★★ (historique de devis ; le calcul pur se banalise) |
| 4 | **Pricing light des pièces et services** pour ETI industrielles et distributeurs : hausses annuelles, fuites de marge, remises | ★★ | DAF et direction commerciale d'entreprises de 20 à 200 M€ | 500 à 1 500 €/mois | Pricefx et Zilliant à 100 k$ ou plus ; trou sous 50 M$ de CA | ★★ (lecture de l'ERP plus analytique) | ★★★ | 1 à 2 M€ | ★★ |
| 5 | **Copilote AO vertical** (ex. propreté et multiservices, maintenance CVC, ou bureaux d'études CPV 71), avec bibliothèque métier et Go/No-Go | ★★ (médiane de 3 offres, PME à 60 % des marchés) | Dirigeants de PME de 10 à 250 salariés | 100 à 300 €/mois | Plus de 15 outils généralistes (Tenderbolt, Tengo, Olra…) ; trou dans les contenus métier | ★★★ | ★★★ | 0,5 à 1,5 M€ | ★ (le LLM générique avec le DCE en pièce jointe couvre une partie) |
| 6 | **Réponse aux consultations et questionnaires fournisseurs privés** (RFI, qualification, RSE, sécurité) pour sous-traitants industriels | ★★ | Directions commerciales et qualité de PME sous-traitantes | 150 à 400 €/mois | Loopio et Responsive sont chers et orientés SaaS ; peu d'acteurs côté industrie | ★★★ | ★★★ | 0,5 à 1,5 M€ | ★ à ★★ |
| 7 | **Voix du client B2B par compte** pour industriels et sociétés de services (tickets SAV, enquêtes, health score), en module du n° 2 | ★★ (sortie de Delighted ; Qualtrics à 25 k$ ou plus) | Directions service client et CX d'ETI | 300 à 1 500 €/mois | Unwrap à 24 k$/an, Enterpret orientés SaaS ; outils NPS encombrés | ★★ | ★★ | 0,5 à 2 M€ | ★★ (si croisé avec les données SAV et ERP) |
| 8 | **Suivi des devis et relances pour distributeurs** (sans saisie de commande), en lecture seule de l'ERP | ★★ | Directions commerciales de négoces de 10 à 200 M€ | 300 à 1 000 €/mois | Canals, Mercura, Order1, Vistaflow se concentrent sur la saisie | ★★ | ★★ | 0,5 à 1,5 M€ | ★★ |
| ✗ | Saisie de commandes généraliste | ★★★ | Distributeurs | 300 à 2 000 €/mois | Saturé et financé (Canals 35 M$, plus de 19 éditeurs) | ★ | ★ | Élevé, mais hors de portée | ★ |
| ✗ | Outils de cadrage (OKR, gestion de portefeuille, business case) | ★ | PME et secteur public | 10 à 30 € par utilisateur | Consolidation (Quantive, Viva Goals), suites Microsoft et Atlassian | ★★★ | ★★★ | Faible | ★ |

**Lecture pour Johanna**
- Les n° 1 et 2 utilisent directement son expérience d'Epic Owner (digitalisation de la vente de services : catalogue, devis, contrats, portail client, business case à 800 k€/an).
- Les n° 2, 7 et 4 peuvent former une suite « revenu de services des ETI industrielles » : portail, puis pricing, puis voix du client. Ce récit d'acquisition parle à des éditeurs d'ERP et de gestion d'interventions.
- Le n° 1 dispose d'un calendrier commercial forcé (09/2026 → 09/2027).
- **Contrainte de temps** : avec 10 h/semaine et 6 à 25 k€, viser un seul cas d'usage et un seul ERP ou une seule PA pour la V1. Prévoir 3 à 5 clients pilotes payants avant d'élargir.
- **Contrainte employeur** : éviter les segments où son cabinet vend de l'intégration (Salesforce CPQ grands comptes, aéro grands OEM). Vérifier par écrit les clauses d'exclusivité et de non-concurrence. Ne pas vendre de « CoE CX » ni de « bid management » sous forme de prestation.

### Gaps
- Aucune des estimations de prix et de plafond d'ARR n'a été validée par des entretiens clients. Il faudrait 15 à 20 entretiens de découverte par piste avant de choisir.
- Pas de données sur les cycles de vente réels des ETI industrielles pour ce type de SaaS.
- Les intégrations ERP (Divalto, Sylob, Sage X3, Cegid) et les API des PA n'ont pas été évaluées techniquement.
