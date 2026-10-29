# Recherche — Station météo 5 zones

Date : 2026-10-29. Prix lus sur les boutiques officielles ce jour, sauf mention contraire.
Note : la boutique Ecowitt affiche ses prix en dollars, même sur les pages UE ; les conversions en euros sont approximatives.

## Constat principal
Rien sur le marché à ≤ 170 € ne réunit les quatre conditions : écran couleur avec prévisions, 5 zones affichées en même temps, Google Home en routines, précision ± 0,5 °C.

Deux critères 🔴 se contredisent :
- **Précision ± 0,5 °C** : les capteurs des stations météo (Ecowitt WN31, La Crosse, Bresser, TFA) sont annoncés à **± 1 °C**. Seuls les capteurs domotiques (SwitchBot ± 0,2 °C, Tapo ± 0,3 °C, Aqara ± 0,2 °C) tiennent la cible.
- **Écran couleur avec prévisions** : seules les stations météo l'ont. Les écrans domotiques sont monochromes.

## Google Home : ce qui marche vraiment
- Depuis février 2026, l'éditeur de routines accepte **l'humidité** comme déclencheur et comme condition, et **la température** comme déclencheur. Dans l'éditeur de scripts (home.google.com), les deux sont acceptées comme déclencheur et comme condition. Sources : support.google.com/googlehome/answer/15684394, developers.home.google.com/automations/schema.
- Cela ne marche bien qu'avec des capteurs **Matter** (connexion locale), qui nécessitent un appareil Google servant de hub : Nest Mini, Nest Audio, Nest Hub, Google Home Speaker ou Google TV Streamer.
- Les capteurs reliés par compte cloud (SwitchBot, Tuya, Tapo) n'apparaissent pas, ou mal, comme déclencheurs.
- **Ecowitt** : aucune intégration Google Home, ni par Matter ni par IFTTT. La seule voie est Home Assistant (matériel en plus, configuration lourde).
- **SwitchBot** : le Hub 2 et le Hub 3 transmettent leurs thermomètres à Google Home via Matter. Aucune source ne montre encore une routine Google déclenchée par un SwitchBot passé par Matter : **à tester pendant le délai de retour**.

## Stations tout-en-un vérifiées dans leurs manuels
| Modèle | Zones max | Zones à l'écran en même temps | Prévisions | Wi-Fi / Google | Précision capteurs | Pack 5 zones |
|---|---|---|---|---|---|---|
| Ecowitt HP2560_C (TFT 7") | 1 + 8 | **Toutes**, sur une 2ᵉ page sans prévisions ni heure | Icônes (baromètre) | Wi-Fi, appli gratuite / pas Google | ± 1 °C | ≈ 200–230 € |
| Ecowitt WS3900 en kit + 3 WN31 | 1 + 8 | 2 (salon + une zone qui défile) | Icônes (baromètre) | Wi-Fi, appli gratuite / pas Google | ± 1 °C | ≈ 165–175 € |
| La Crosse LW3101 | 2 + 4 | 3 (défilement toutes les 6 s) | Icônes AccuWeather | Wi-Fi, appli / Google non vérifié | ± 1 °C | ≈ 170–200 € |
| Bresser Tuya 7006300 | 1 + 7 | 1 (défilement toutes les 4 s) | Tendance | Tuya | ± 1 °C | ≈ 135–140 €, capteurs en rupture |
| Bresser couleur 3 capteurs | 1 + 3 | 4 | Graphique | Aucun | ± 1 °C | Une zone manque |
| TFA VIEW BREEZE | 1 + 4 | Défilement (bouton EXTRA) | Internet | Wi-Fi / pas Google | ± 1 °C | Non chiffré |

Manuels : HP2560 (oss.ecowitt.net, p. 44), WS3900/WS3910 (§3.5.1), WN1980 (§5.6.1), LW3101 (lacrossetechnology.fr).

## Combinaisons domotiques
| Pack | Contenu | Prix | Écran salon | Google routines | Précision |
|---|---|---|---|---|---|
| A | SwitchBot Hub 2 + Meter Pro + Outdoor Meter + 2 thermo-hygromètres | 154,97 € | Monochrome : heure, date, prévisions, salon + extérieur | Via Matter (à tester) | ± 0,2 °C |
| B | SwitchBot Hub 3 + 4 thermo-hygromètres | 189,98 € | Monochrome : prévisions 24 h, environ 2 capteurs | Via Matter (à tester) | ± 0,2 °C |
| C | Tapo H100 + T315 + 4 T310 | 128,93 € | Petit écran à encre électronique, pièce seule, sans prévisions | Cloud aléatoire ; Matter en bêta | ± 0,3 °C, pas prévu pour l'extérieur |

## Affirmations de Gemini
- « Le WN1980 affiche un seul capteur distant à la fois » : **vrai**.
- « Le WN1980 coûte ~50 € » : **faux**, 68,99 $ pour la console seule.
- « Aucun écran à icônes n'affiche 5 zones » : **non contredit**. Ecowitt affiche toutes les zones, mais sur un écran TFT et sur une page séparée.
- « Bresser 7009999 = station 8 canaux » : **faux**. C'est un capteur 7 canaux, pas une station.
- « Ecowitt + IFTTT ou Google Home pour les routines » : **faux**. Pas d'intégration, et IFTTT ne peut pas déclencher une routine Google Home.
- « Capteurs Ecowitt ± 0,5 °C (Sensirion) » : **faux sur la fiche**. Les WN31 sont annoncés à ± 1 °C.
- « Le Hub 2 de SwitchBot n'affiche aucune prévision » : vrai pour le Hub 2. En revanche, le **Meter Pro** et le **Hub 3** affichent des prévisions.

## Écartés
- **Netatmo** : 250 à 370 € pour 5 zones, sans console.
- **Aqara W100 ×5** : environ 200 €, et le déclencheur de température dans Google Home n'est pas fiable.
- **Tuya génériques** : déjà rejetés par toi, sans déclencheur dans Google Home.
- **Bresser 100 % radio** : aucune connectivité.

---

# v2 — Recherche après précisions (fiabilité d'abord, Home Assistant présent)

## Capteurs classés par fiabilité des données
| # | Capteur | Puce | Précision annoncée | Preuve indépendante | Liaison | Prix |
|---|---|---|---|---|---|---|
| 1 | Sonoff SNZB-02P | SHT40 (démontage) | ± 0,2 °C / ± 2 % | Meilleur sur 12 capteurs (smarthomescene.com, août 2026) | Zigbee | 17,24 € ; 30,50 € les 2 |
| 1b | Sonoff SNZB-02B | Sensirion (modèle non précisé) | ± 0,2 / ± 2 | Top 5, « meilleur à piles AAA » | Zigbee | 36,62 € les 4 |
| 2 | Sonoff SNZB-02WD (IP65) | SHT40 | ± 0,2 / ± 2, jusqu'à −20 °C | Proche d'un SwitchBot Meter Pro (techtest.org) | Zigbee | 20,30 € |
| 3 | Aqara T1 / WSDCGQ11LM | SHT30 | ± 0,3 / ± 3 | Top 5, mais décrochages signalés | Zigbee | ≈ 22 € |
| 5 | IKEA TIMMERFLOTTE | SHT4x (non confirmé) | non publiée | Humidité qui varie entre unités | Thread | 7,99 € |
| 7 | Ecowitt WN31 | ? | ± 1 / ± 5 | Humidité décalée de 5 à 15 % selon des utilisateurs | 868 MHz | — |

À éviter : Sonoff SNZB-02 (sans « P », environ 10 % d'humidité de trop), Tuya génériques (TH01, ZTH02…), Thirdreality (trous jusqu'à 6 h).

## Home Assistant → Google Home
- **Intégration Google Assistant manuelle** : gratuite, fonctionne encore en 2026. Il faut un accès HTTPS avec nom de domaine et une console développeur Google. Difficulté moyenne à élevée. Source : home-assistant.io/integrations/google_assistant
- **Home Assistant Cloud** : ≈ 7,50 €/mois ou 75 €/an (prix en euros selon une source secondaire), essai de 31 jours. Renommé « Home Assistant Link » en décembre 2026.
- **Ponts Matter communautaires** : gratuits et locaux (fork RiDDiX de Home Assistant Matter Hub, Matterbridge). L'original a été abandonné en janvier 2026, c'est le risque de ce choix.
- **Réponse vocale** : historiquement, la question sur la température ou l'humidité d'une pièce marche. Aucune confirmation sous Gemini for Home en français.
- **Routines Google** : les déclencheurs d'humidité sont corrects, ceux de température instables. Faire les automatisations dans Home Assistant.
- **Écran** : tablette + Fully Kiosk + Météo-France. Le Nest Hub revient à l'accueil au bout d'environ 10 minutes.
