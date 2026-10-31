# Brief — Aspirateur laveur

Statut: recherche v2 (cadrage reçu)
Ouvert le: 2026-10-31
Contexte : promos repérées sur Dealabs avant le Black Friday (27/11/2026). L'utilisatrice envoie des captures ; on rend un go / no go sur chaque offre.

## Usage réel
Robot aspirateur laveur avec station pour un appartement de 70–100 m², surtout des sols durs. Foyer avec un **chien à poils longs et sous-poil dense** (grosse mue chaque année) et une personne aux **cheveux très longs et très frisés**. Le robot doit passer sous un lit d'environ **10 cm** de dégagement.

## Salissures humides (automne/hiver)
- Traces de pattes mouillées et boueuses dans la cuisine et l'entrée.
- Feuilles mouillées ramenées par le chien.
- Eau projetée autour de la gamelle, croquettes imbibées d'eau.
→ Un robot gère mal les débris mouillés. Piste étudiée : un **balai aspirateur laveur** (aspiration eau + débris) en complément, ou un robot à rouleau laveur.

## Ce que j'ai déjà
- Google Home + Home Assistant (intégration locale = bonus pour un robot)

## Budget
- Cible : ≤ 400 € livré
- Plafond : 400 €

## Grille (validée le 2026-10-31)
| Priorité | Critère | Exigence | Comment on vérifie |
|---|---|---|---|
| 🔴 | Type | Robot laveur avec station OU balai aspirateur laveur | Réponse utilisatrice |
| 🔴 | Lavage réel | Serpillières rotatives ou rouleau auto-nettoyé, eau propre/sale séparées | Fiche + tests indépendants |
| 🔴 | Budget | ≤ 400 €, vendeur sûr | Panier |
| 🔴 | Poils et cheveux | Brosse principale et brosses latérales qui n'emmêlent pas les cheveux longs et frisés ; bonne aspiration des poils de chien | Tests d'enroulement (Vacuum Wars, Rtings) |
| 🔴 | Hauteur | ≤ 10 cm (passe sous le lit) | Fiche technique |
| 🟠 | Évitement des déjections du chien | Caméra IA de préférence | Tests |
| 🟠 | Entretien | Station : vidage auto, lavage/séchage à l'air chaud des serpillières | Fiche |
| 🟠 | Fiabilité / SAV | Marque avec SAV en France, pièces détachées vendues | Site marque, avis |
| 🟠 | Bruit | dB en usage | Tests |
| 🟢 | Home Assistant | Intégration locale | Doc HA |
| 🟢 | Google Home | Lancer le nettoyage à la voix | Fiche |

## Promo
- Vérifier pour chaque offre : prix barré réel (historique de prix), prix ailleurs (comparateur), modèle de l'année vs ancien modèle renommé.

## Questions ouvertes
Voir la conversation du 2026-10-31.

## Offres Dealabs à évaluer (captures du 2026-10-31)
| Modèle | Prix | Prix barré | Vendeur | Posté |
|---|---|---|---|---|
| Dreame L40s Pro Ultra | 459 € | 599 € | Amazon | ~30/10 |
| Dreame Matrix10 Pro | 569 € | 886 € | Amazon | ~30/10 |
| Dreame L50 Ultra AE | 459 € | 524,83 € | Dreame | ~27/10 |
| Dreame L10s Pro Gen 3 | 199 € | 299 € | Dreame | ~25/10 |
| Dreame L40 Ultra A | 349 € | 437,66 € | Amazon | ~24/10 |
| Roborock Qrevo S Pro | 379,99 € | 599,99 € | Amazon (vendeur tiers) | ~10/10 |
| Dreame L10s Ultra Gen 3 Kit-A | 379 € | 493,36 € | Amazon | expiré |
| DJI Romo P | 671,43 € + 26,13 € | — | Amazon.de | expiré |

## Synthèse recherche (2026-10-31)
Détail et sources dans les rapports de recherche résumés dans `reco.md`. Points clés :
- Le Black Friday de Dreame a déjà commencé (vers le 28–30/10).
- L40s Pro Ultra : plus bas 447,91 € (vendeur tiers, sept.), 474 € au Prime Day d'octobre, 429 € annoncé par Dreame. Sources : NeozOne, Labo Maison, Clubic.
- L50 Ultra AE : 419,99 € chez Darty en octobre, 429 € chez Cdiscount (Bonne-Promo).
- Qrevo S Pro : 349 € chez Darty sur Rakuten et 379,99 € sur le site Roborock en octobre ; intégration officielle dans Home Assistant (home-assistant.io/integrations/roborock).
- Matrix10 Pro : 569 € = plus bas pour un neuf ; intégration Home Assistant communautaire cassée depuis HA 2026.9.
- Service après-vente : Roborock mieux réputé que Dreame en France (sources faibles).
