# Reco v3 — Robot aspirateur laveur : poils de chien d'abord

Date : 2026-10-31. Critère n° 1 : poils de chien et cheveux longs et frisés. Le prix est affiché, mais il n'élimine aucun modèle. Hauteur sous le lit : ≈ 10 cm, à mesurer.
Colonne domotique vérifiée le 2026-10-31. HA = Home Assistant ; « communautaire » = extension HACS non officielle.

## Verdict
1. **Le meilleur tout court : Dreame X50 Ultra Complete, ≈ 699 €.**
   - Poils de chien ramassés : 98 %. Cheveux enroulés : 0 % (Vacuum Wars).
   - Au test allemand de smarthomeassistent, aucun cheveu enroulé, ni sur la brosse ni sur la brosse latérale.
   - Il passe à **8,9 cm** grâce à son laser rétractable.
   - Il existe aussi en **reconditionné B3 chez Cdiscount, à 349–399 €**.
2. **Le meilleur rapport qualité/prix : Dreame L40s Pro Ultra, 459 €** (une des offres de tes captures).
   - Même double brosse que le X50. Sur tapis, test smarthomeassistent : « tous les cheveux ont disparu ».
   - ⚠️ Il mesure **10,4 cm** : il ne convient que si ton lit dégage au moins 10,5 cm.
3. **Le moins cher sous 10 cm : Ecovacs T50 Pro Omni Gen3, 299–399 €.**
   - Il mesure 8,1 cm, mais aucun test de la Gen3 elle-même n'existe.
   - Son bac de 260 ml est petit, et sur un modèle proche la brosse latérale accroche beaucoup de cheveux.

## Classement des poils (toutes les offres + les meilleurs du marché)
| # | Modèle | Prix | Hauteur | Brosse | Résultats poils (tests indépendants) | Domotique (provisoire) | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Dreame X50 Ultra Complete | ≈ 699 € (reconditionné 349–399 €) | **8,9 cm** | double brosse DuoBrush | 98 % ramassés, 0 % enroulés ; smarthomeassistent : aucun enroulement. Rtings : laisse des poils incrustés dans les tapis | HA communautaire complet ; **Matter 1.4** ; Google ✅ | ✅ Meilleur |
| 2 | Dreame Matrix10 Ultra | 650–749 € | 8,9 cm | DuoBrush | 92 % ramassés, 0 % enroulés ; nul sur les tapis à poils longs | HA communautaire ; Google ✅ | 🟡 Plus cher que le X50 |
| 3 | **Dreame L40s Pro Ultra** (Dealabs) | **459 €** | 10,4 cm | DuoBrush | Tapis 10/10, sol stratifié 8,9/10 ; 91 % / 0 % sur le modèle frère | HA communautaire complet ; Matter ? ; Google ✅ | ✅ Meilleur rapport qualité/prix, si la hauteur passe |
| 4 | Dreame Matrix10 Pro (Dealabs) | 569 € | 10,4 cm | DuoBrush | Données du Matrix10 Ultra, son modèle frère | HA communautaire ; Matter annoncé ; Google ✅ | 🟡 Bon sur les poils, mais 110 € de plus que le L40s |
| 5 | Roborock Saros 10R | 699–799 € | 8 cm | rouleau DuoDivide | 92 % / 0 % ; Rtings « décevant » sur les tapis ; bac de 270 ml | **HA officiel** ; Matter ✅ ; Google ✅ | 🟡 Bac trop petit pour un gros chien |
| 6 | Ecovacs T50 Pro Omni Gen3 | 299–399 € | **8,1 cm** | ZeroTangle 3.0 | Modèle frère : 86 % / 0 %, mais beaucoup de cheveux sur la brosse latérale ; bac de 260 ml | HA officiel depuis 2026.10.2, pièces/carte non garanties ; Google ✅ | 🟡 Option budget |
| 7 | DJI Romo P (Dealabs) | ≈ 697 € | 9,8 cm | 2 rouleaux fournis | Pas d'enroulement (Nextpit), pas de chiffres | ❌ pas de HA ; Matter non confirmé | 🟡 Cher pour ce qui est prouvé |
| 8 | Dreame L40 Ultra AE | ≈ 359 € (rupture) | 9,7 cm | TriCut | 81 % / 0 % (modèle frère, avec la brosse TriCut) | HA communautaire ; pas de Matter ; Google ✅ | 🟡 Moyen |
| 9 | Dreame L50 Ultra AE (Dealabs) | 429–459 € | 9,7 cm | TriCut 3.0 | « beaucoup de cheveux emmêlés » ; tapis à poils longs 2,1/10 | HA communautaire ; Matter ✅ ; Google ✅ | ❌ Mauvais sur les poils |
| 10 | Dreame L40 Ultra A (Dealabs) | 349 € | 9,7 cm | TriCut | Modèle frère : cheveux enroulés autour des embouts de la brosse | HA communautaire ; Google ✅ | ❌ |
| 11 | Roborock Qrevo S Pro (Dealabs) | ≈ 380 € | 9,7 cm | caoutchouc | Résultat « satisfaisant » sur les poils ; en laisse sur les tapis | **HA officiel** (en partie local) ; pas de Matter ; Google ✅ | ❌ Pour les poils |
| 12 | Dreame L10s Ultra Gen 3 (Dealabs, expiré) | 379 € | 9,7 cm | caoutchouc simple | Enroule des cheveux par endroits | HA communautaire ; Google ✅ | ❌ |

À retenir : chez Dreame, ce qui fait la différence sur les poils, c'est la **double brosse DuoBrush** (X50, Matrix10, L40s Pro Ultra), pas la brosse TriCut (L50 AE, L40 A, L40 AE).

## Domotique : ce qu'il faut savoir
- **Google Home** : tous les modèles du tableau, sauf le DJI, se lancent à la voix (« Ok Google, lance l'aspirateur » ou « nettoie la cuisine ») et dans les routines, par exemple au départ de tout le monde.
- **Home Assistant** :
  - **Roborock** : intégration officielle, en partie locale. C'est la plus simple et la plus fiable.
  - **Dreame** : extension communautaire (HACS, développeur Tasshack). C'est la plus complète (carte, pièces, station, consommables), mais elle repose sur un seul développeur : elle a cassé avec HA 2026.9, puis a été réparée le 30/09 (version 2.0.2).
  - **Ecovacs** : intégration officielle, mais les nouveaux modèles arrivent avec des mois de retard et souvent incomplets.
  - **DJI** : rien.
- **Matter** : c'est une solution de secours locale, qui marche même si l'extension tombe. Elle permet le lancement, l'arrêt, le mode et le choix des pièces dans HA, mais sans carte ni station. Modèles concernés : **X50 Ultra** (Matter 1.4), L50 Ultra AE et Saros 10R.
- **T50 Pro Omni Gen3** :
  - il faut HA en version **2026.10.2** au minimum ;
  - vérifie le code de l'appareil dans HA : `npwtuz` ou `jjg8ne` sont reconnus, **la version « Care Kit » (`be9ucr`) ne l'est pas** ;
  - lancement, arrêt, retour à la base, aspiration, débit d'eau et consommables : OK ;
  - nettoyage par pièce et carte : pas garantis (bugs ouverts sur des modèles proches).

## Balai aspirateur laveur pour les dégâts mouillés (option)
- **Tineco Floor One Stretch S6**, ≤ 200 €, ou **Roborock F25 XT**, ≈ 260 €.
- Il gère bien les pattes boueuses, l'eau de la gamelle et les croquettes trempées.
- Les feuilles entières restent à ramasser à la main.

## Où acheter
- Boulanger, Fnac, Darty, la boutique de la marque, ou Amazon vendu par Amazon. Jamais un vendeur tiers.
- Le reconditionné Cdiscount B3 ne vaut le coup que si le vendeur donne une garantie claire, de 12 mois minimum.

## Incertitudes
- Aucun test ne mesure le sous-poil dense d'un chien à poils longs ; le test « poils d'animaux » de Vacuum Wars est ce qui s'en rapproche le plus.
- Les prix du X50, du Matrix10 Ultra et du Saros 10R viennent d'annonces non datées ou expirées ; ils sont à vérifier le jour de l'achat.
- Tous les bacs des robots font entre 260 et 310 ml : en période de mue, il faudra les vider souvent, quel que soit le modèle.
