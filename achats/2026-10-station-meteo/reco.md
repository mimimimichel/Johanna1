# Reco — Station météo 5 zones

Date : 2026-10-29

## Verdict
Le pack idéal (écran couleur à prévisions + 5 zones visibles + Google Home + ± 0,5 °C, pour ≤ 170 €) n'existe pas : deux de tes critères éliminatoires se contredisent. Les stations à écran couleur ont des capteurs à ± 1 °C et ne fonctionnent pas avec Google Home ; les capteurs précis et compatibles Google ont des écrans monochromes.

**Reco principale : le pack SwitchBot (≈ 155 €)**. Il est précis (± 0,2 °C), il passe par Google Home via Matter pour les routines, et son écran de salon affiche l'heure, la date et les prévisions. Ce qu'on sacrifie : la couleur, et l'affichage des 5 zones à l'écran (elles sont toutes visibles dans l'appli).

**Si l'écran compte plus que Google Home : Ecowitt HP2560_C (≈ 200–230 €)**. C'est le seul écran couleur qui montre les 5 zones ensemble, mais hors budget, à ± 1 °C et sans Google Home.

## Finalistes
| Critère | A. SwitchBot Matter | B. Ecowitt HP2560_C | C. Ecowitt WS3900 kit |
|---|---|---|---|
| 🔴 5 zones | ✅ | ✅ | ✅ |
| 🔴 Écran couleur avec prévisions | ❌ monochrome (heure, date, prévisions) | ✅ 7" | ✅ 7,5" |
| 🔴 Précision ± 0,5 °C | ✅ ± 0,2 °C | ❌ ± 1 °C | ❌ ± 1 °C |
| 🔴 Budget ≤ 170 € | ✅ 155 € | ❌ ≈ 200–230 € | ✅ ≈ 165–175 € |
| 🟠 5 zones visibles d'un coup | Appli seulement | ✅ page dédiée | ❌ 2 à la fois |
| 🟠 Google Home en routines | ✅ via Matter (à tester) | ❌ | ❌ |
| 🟠 Portée | ⚠️ Bluetooth, à tester | ✅ radio 868 MHz | ✅ radio 868 MHz |

## Option A — SwitchBot via Matter (recommandée)
- **Pour qui** : si la précision et les routines Google Home comptent plus que la couleur.
- **Ce qu'on sacrifie** : un écran couleur. Le Meter Pro affiche heure, date, prévisions, le salon et l'extérieur, en noir et blanc.
- **Prérequis** : un appareil Google servant de hub Matter (Nest Mini, Nest Audio, Nest Hub, Google Home Speaker).
- **Répartition** :
  - Salon : Meter Pro.
  - Extérieur : Outdoor Meter, côté nord, à l'abri de la pluie directe.
  - Cuisine et chambre 1 : un thermo-hygromètre chacune.
  - Chambre 2 : le capteur intégré au câble du Hub 2.
- **Risque n° 1 : portée.** Les thermomètres parlent au Hub 2 en Bluetooth, et deux murs porteurs, c'est limite. Mets le Hub 2 au centre et teste tout dans les 14 jours. Sinon, un deuxième hub à environ 70 € corrige le problème.
- **Risque n° 2 : déclencheur Google non confirmé.** Aucune source ne montre encore un SwitchBot passé par Matter déclenchant une routine Google. À tester tout de suite à réception (voir ci-dessous).
- **Évolution** : un Nest Hub (≈ 105 €, prix à confirmer) ajouterait plus tard un écran couleur avec heure, date et météo.

## Option B — Ecowitt HP2560_C
- **Pour qui** : si voir les 5 zones d'un coup sur un vrai écran couleur est le plus important, et que Google Home est secondaire.
- **Ce qu'on sacrifie** : le budget (≈ + 50 €), Google Home, et la précision (± 1 °C sur la fiche).
- **Affichage** : la page « toutes les zones » est séparée de l'écran principal (qui affiche heure et prévisions). Non vérifié : si cette page reste affichée en permanence.
- **Pack** :
  - Console HP2560_C : 165,99 $.
  - 4 capteurs WN31 : 10,99 $ chacun.
  - Un abri ventilé pour le capteur extérieur : 20 à 35 € (prix non vérifié).

## Écartés
- **La Crosse LW3101** : défilement, ± 1 °C, Google Home non vérifié, ≈ 170–200 €.
- **Bresser Tuya 7006300** : un seul capteur affiché à la fois, capteurs en rupture.
- **Tapo** : pas de prévisions à l'écran, capteur non prévu pour l'extérieur.
- **Netatmo** : plus de 250 €.
- **Aqara** : environ 200 €, déclencheur de température peu fiable.

## Où acheter (option A)
| Article | Qté | Vendeur | Prix |
|---|---|---|---|
| SwitchBot Hub 2 | 1 | eu.switch-bot.com | 79,99 € |
| SwitchBot Meter Pro + Outdoor Meter (lot) | 1 | eu.switch-bot.com | 44,99 € |
| SwitchBot Thermo-hygromètre intérieur/extérieur (lot de 2) | 1 | eu.switch-bot.com | 29,99 € |
| Option : prise Tapo P110 (pour un déshumidificateur) | 1 | fr.store.tapo.com | 10,99 € |

Total : **154,97 €** (165,96 € avec la prise). Frais de port à vérifier au panier.

Prix lus le 2026-10-29. Je n'ai pas pu vérifier Amazon.fr, Boulanger et Fnac (sites bloqués pour l'outil).

**Acheter maintenant ou attendre ?** Le Black Friday a lieu le 27 novembre 2026, dans 4 semaines. Sauf urgence, attends et compare la boutique SwitchBot et Amazon.fr (vendu et expédié par Amazon, retour sous 30 jours), avec l'historique de prix sur Keepa.

## À la réception (pendant le délai de retour)
- [ ] Laisse les 5 capteurs côte à côte 24 h et vérifie qu'ils restent à moins de 0,5 °C les uns des autres.
- [ ] Ajoute le Hub 2 à Google Home **via Matter** (pas via le compte SwitchBot), et vérifie que les 5 thermomètres apparaissent.
- [ ] Crée une routine test « humidité chambre > 65 % → notification » et vérifie qu'elle se déclenche.
- [ ] Mets chaque capteur à sa place finale et vérifie pendant 48 h que les mesures remontent sans trou.
- [ ] Si la portée ou la routine échoue : retourne le pack.
