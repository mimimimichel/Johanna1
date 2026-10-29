# Reco v2 — Capteurs 5 zones (fiabilité d'abord, Home Assistant)

Date : 2026-10-29. Remplace la v1 (SwitchBot / Ecowitt), devenue caduque une fois Home Assistant connu et les priorités précisées.

## Verdict
Prends **5 capteurs Zigbee Sonoff à puce Sensirion SHT40** (4 × SNZB-02P à l'intérieur, 1 × SNZB-02WD étanche à l'extérieur, sous abri), intégrés **en local dans Home Assistant**.
- Coût : **≈ 133 €** avec une clé Zigbee, **≈ 153 €** avec l'abri extérieur.
- Si tu as déjà une clé Zigbee : **≈ 97 €**, ou **≈ 117 €** avec l'abri.

Google Home reçoit les mesures depuis Home Assistant, pour répondre à la voix. Les automatisations se font dans Home Assistant, plus fiable que les routines Google. L'écran devient une option à ajouter plus tard.

## Pourquoi ce choix
- **Précision** : puce Sensirion SHT40, ± 0,2 °C et ± 2 % d'humidité annoncés, confirmés par une ouverture du boîtier.
- **Test indépendant** : « meilleur capteur » d'un test de 12 capteurs Zigbee sur 10 jours, face à une référence calibrée (SmartHomeScene, août 2026). Deux capteurs Sonoff côte à côte restent à 0,1–0,2 °C l'un de l'autre.
- **Pas de trous dans les données** : le Zigbee forme un réseau maillé. Une prise Zigbee branchée entre les pièces éloignées relaie le signal à travers les murs porteurs.
- **Local** : intégration native dans Home Assistant (ZHA ou Zigbee2MQTT), sans cloud ni compte Sonoff.
- **Autonomie** : pile CR2477, jusqu'à 4 ans annoncés (2 ans pour le modèle extérieur).

## Finalistes
| | A. Sonoff SHT40 (reco) | B. Sonoff éco (piles AAA) | C. IKEA TIMMERFLOTTE (Thread) |
|---|---|---|---|
| Puce | SHT40 confirmée | « Sensirion », modèle non précisé | SHT4x, non confirmé |
| Preuve indépendante | Meilleur du test | Top 5 du test | Humidité qui varie entre unités |
| Liaison | Zigbee maillé | Zigbee maillé | Thread, retours mitigés dans HA |
| Extérieur | SNZB-02WD étanche IP65 | idem | Pas de modèle extérieur |
| Pack avec clé + abri | ≈ 153 € | ≈ 118 € | ≈ 100 € (montage mixte compliqué) |

Écartés :
- **Ecowitt** : ± 1 °C et ± 5 % d'humidité annoncés.
- **Shelly H&T** : Wi-Fi, ≈ 38 € pièce.
- **Aqara** : puce plus ancienne (SHT30), décrochages signalés.
- **Xiaomi** : qualité variable selon la version reçue.
- **Tuya génériques** : écarts mesurés jusqu'à 0,8 °C.
- **Eve Weather** : ≈ 70 €, autonomie faible.
- **Sonoff SNZB-02** (sans « P ») : lit environ 10 % d'humidité de trop.

## Panier (option A)
| Article | Qté | Vendeur | Prix |
|---|---|---|---|
| Sonoff SNZB-02P, lot de 2 | 2 | sonoff.tech (boutique UE) | 61,00 € |
| Sonoff SNZB-02WD (extérieur, IP65) | 1 | sonoff.tech | 20,30 € |
| Clé Zigbee Sonoff Dongle Plus MG24 — **seulement si tu n'en as pas** | 1 | sonoff.tech | 36,62 € |
| Prise Zigbee Sonoff iPlug S60ZBTPF (relais du réseau) | 1 | sonoff.tech | 15,20 € |
| Abri TFA Dostmann 98.1114.02 | 1 | Amazon.fr | ≈ 20–25 € |

**Total : ≈ 153 €** livré. La livraison est gratuite dès 59 € depuis l'entrepôt allemand, sous 3 à 6 jours. Prix lus le 2026-10-29 ; celui de l'abri vient d'Amazon et sa date n'a pas pu être vérifiée.

- **Variante clé** : la Home Assistant Connect ZBT-2 (≈ 45 €, Domadoo) remplace la clé Sonoff ; total ≈ 161 €.
- **Abri** : ses dimensions intérieures font 10,2 × 9,5 × 17,5 cm, mais celles du SNZB-02WD n'ont pas été vérifiées. Contrôle qu'il rentre. Un endroit toujours à l'ombre, au nord, peut suffire sans abri.
- **Quand acheter** : le Black Friday a lieu le 27 novembre. Ces prix sont déjà bas, donc tu peux acheter maintenant si c'est utile.

## Relier à Google Home
1. Expose dans Home Assistant les 10 mesures (température et humidité par pièce) avec le bon type : température ou humidité.
2. Teste avec **l'essai gratuit de 31 jours de Home Assistant Cloud**, qui s'active en 2 clics. Ensuite, deux choix :
   - garder l'abonnement : ≈ 75 €/an (selon une source secondaire, à confirmer au paiement). Il sera renommé « Home Assistant Link » en décembre ;
   - passer à une solution **gratuite** : l'intégration Google Assistant manuelle (environ 1 à 2 h de configuration, nécessite un accès HTTPS) ou un pont Matter communautaire (Matterbridge, ou le fork RiDDiX de Home Assistant Matter Hub).
3. Range chaque capteur dans la bonne pièce dans Google Home. Teste ensuite « Ok Google, quelle est la température dans la chambre ? ».
4. **Point incertain** : aucune source ne confirme que Gemini for Home répond en français pour un capteur seul. Plan B : un script Home Assistant qui annonce les valeurs sur l'enceinte Google, lancé par une routine Google (« Ok Google, températures maison »).
5. Les automatisations (seuil d'humidité, alertes) se font dans Home Assistant : les déclencheurs de température de Google restent instables.

## Écran (option, plus tard)
- **Meilleure option** : une tablette Android à ≈ 100 € (ou d'occasion) avec Fully Kiosk (8,90 €). Le tableau de bord Home Assistant afficherait heure, date, prévisions Météo-France (intégration gratuite) et les 5 zones en même temps.
- **À éviter comme écran permanent** : le Nest Hub (99,99 €), qui revient à son écran d'accueil au bout d'environ 10 minutes.

## À la réception
- [ ] Mets les 5 capteurs côte à côte pendant 24 h, puis règle les décalages dans Home Assistant. Vise moins de 0,3 °C et moins de 3 % d'humidité d'écart.
- [ ] Branche la clé Zigbee au centre de l'appartement, sur une rallonge USB, loin du routeur Wi-Fi. Branche la prise relais entre le salon et les chambres.
- [ ] Mets les capteurs en place et vérifie pendant 48 h qu'aucune mesure ne manque dans l'historique.
- [ ] Teste la question vocale à Google pendant l'essai de Home Assistant Cloud.
