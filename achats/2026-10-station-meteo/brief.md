# Brief — Station météo 5 zones

Statut: reco (v2)
Ouvert le: 2026-10-29 (première tentative avec Gemini, août 2026, non aboutie)

## Usage réel
Suivre température et humidité dans 5 zones de l'appartement (salon, cuisine, chambre 1, chambre 2, extérieur), avec un coup d'œil quotidien sur un écran au salon et, si possible, des routines Google Home basées sur ces mesures.

## Ce que j'ai déjà
- Google Home (enceinte(s) / écran à préciser)
- **Home Assistant** (matériel et clé Zigbee/Bluetooth à préciser)
- Wi-Fi

## Budget
- Cible : 120–150 €
- Plafond : 170 €

## Grille (révisée le 2026-10-29 après précisions)
Priorités annoncées : 1) données fiables, 2) connectivité maison, 3) écran = bonus si Google Home répond à la voix.

| Priorité | Critère | Exigence | Comment on vérifie |
|---|---|---|---|
| 🔴 | Fiabilité de mesure | ≈ ± 0,2 à 0,3 °C et ± 2–3 % HR annoncés, puce Sensirion (SHT4x/SHT3x) ou équivalent, cohérence entre capteurs | Fiche fabricant + tests indépendants |
| 🔴 | Fiabilité de transmission | Pas de trous dans les données : liaison robuste (Zigbee maillé, Thread, 868 MHz) sur ~15 m / 2 murs porteurs | Protocole, retours d'utilisateurs HA |
| 🔴 | Zones | 5 : salon, cuisine, chambre 1, chambre 2, extérieur | — |
| 🔴 | Extérieur | Capteur étanche (IP65+) ou abri ventilé, tenue au froid / piles | Fiche + abri |
| 🔴 | Budget | ≤ 150 € (170 € max) tout compris | Panier |
| 🟠 | Home Assistant | Intégration locale native (sans cloud) | Doc HA |
| 🟠 | Google Home | Réponse vocale « quelle température dans la chambre ? » + routines | Doc Google / HA |
| 🟠 | Longévité | Piles standard, autonomie ≥ 1 an, marque pérenne | Fiche, avis |
| 🟢 | Écran salon | Heure, date, prévisions — facultatif si la voix suffit | — |

## Tensions et arbitrage probable
- Réglé : avec Home Assistant, on choisit les meilleurs capteurs et on relie à Google Home ensuite. L'écran couleur devient facultatif.

## Questions ouvertes
- Matériel Home Assistant : as-tu une clé Zigbee ou Thread ? (change le coût de ~20–30 €)
- Google Home est-il déjà relié à Home Assistant ?
