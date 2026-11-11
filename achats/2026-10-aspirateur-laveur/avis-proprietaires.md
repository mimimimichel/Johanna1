# Avis de propriétaires (pas de testeurs) : relevé du 12/11/2026

But : vérifier ce que disent les **gens qui ont le robot chez eux**, sur les points qui comptent pour nous : chien à poils longs qui perd beaucoup, cheveux très longs et bouclés, tapis, traces de pattes mouillées.

**Légende** (la même que `sources-neutres.md`)
- **(P)** : page lue directement par l'outil.
- **(E)** : texte vu seulement dans l'extrait ou le résumé du moteur de recherche, page non chargée. ⚠️ Le résumé peut se tromper de modèle ou d'auteur. À reconfirmer avant de s'appuyer dessus.
- **Nb** : nombre de propriétaires **distincts** qui décrivent le problème eux-mêmes. Un « je pense que… » ou un « j'ai lu que… » ne compte pas.
- 🧪 : test d'un membre de forum avec **appareil fourni par la marque**. Ce n'est pas un propriétaire, donc non compté.

---

## En bref

1. **Très peu de retours de propriétaires sont accessibles.** Chaque robot n'en compte qu'entre 0 et 6. Aucun chiffre ci-dessous n'est une statistique : ce sont des signaux.
2. **Roborock Saros 10R** : c'est le plus documenté et le plus rassurant sur les **poils**. 3 propriétaires, dont un foyer « cheveux longs + chien qui perd beaucoup », disent ne pas avoir de cheveux enroulés. Le point faible qui revient, ce sont les **serpillières qui manquent d'eau**. Au moins 3 propriétaires, et des robots échangés par Roborock.
3. **Dreame Matrix10 Ultra** : c'est lui qui a **le plus de pannes mécaniques signalées**. Mécanisme d'échange des serpillières, panne au bout de 6 mois, SAV Dreame lent.
4. **MOVA V70 Ultra** : les propriétaires parlent de problèmes de **serpillières**. Le robot ne les reprend pas à la station, la serpillière sur bras se détache, les serpillières sont peu mouillées. S'y ajoutent des **bugs après mise à jour**. Aucun retour sur les poils de chien.
5. **Dreame X50 Ultra** : peu de retours sur les poils. Ce qui revient : **navigation** (coins oubliés) et **petites pannes** (brosse latérale, pompe).

---

## Ce qui a été bloqué ou sauté (sans contournement)

| Site | Résultat |
|---|---|
| Dealabs, commentaires | La page se charge (P), mais **sans les commentaires**, qui s'affichent par script. Seuls les extraits du moteur ont été utilisés (E). Une lecture du HTML brut a été refusée comme contournement anti-robot, donc abandonnée. |
| Reddit | Refusé à l'outil, en lecture comme en recherche. Les agrégateurs : RedditRecs est fermé et les miroirs n'ont pas été utilisés. |
| roboter-forum.com (DE) | Erreur 403 à la lecture. Seuls les extraits du moteur ont été utilisés (E). |
| commentcamarche.net, 60millions-mag.com | Refusés au robot de recherche. |
| forum.quechoisir.org, hacf.fr | Rien sur nos modèles. Sur hacf, un seul fil Dreame L20. |
| forum.hardware.fr (HFR) « Du Robot domestique [Topic Unik] » | **Lu (P)**, pages 511 à 513 (oct.–nov. 2026). Mais les propriétaires y parlent surtout de l'Ecovacs T80S, aucun de nos 6 robots prioritaires. |
| mydealz, computerbase | Lus ou vus. Que des questions, pas de propriétaires de nos modèles. |
| GitHub (intégrations Home Assistant) | **Lu (P)** : tickets des intégrations Roborock (Home Assistant Core) et Dreame/MOVA (Tasshack). |

**Comptes écartés** : les auteurs des bons plans Dealabs (certains bons plans portent la mention « Vendeur Roborock ») ; les « Roboter-Forum Review » 🧪, appareils prêtés par la marque (le forum publie lui-même un avertissement de transparence) ; une partie du fil allemand MOVA V70, alimenté par une **campagne de test MOVA**.

---

## 1. Roborock Saros 10R

| Problème | Nb | Exemples et liens |
|---|---|---|
| ✅ **Pas de cheveux ni de poils enroulés** | 3 | Dealabs (E) : un foyer avec « femmes aux cheveux longs, 2 chats, un chien qui perd énormément ». Il remplace un ancien Roborock qui se bloquait à cause des poils : rouleau « zéro intervention ». https://www.dealabs.com/bons-plans/robot-aspirateur-roborock-saros-10r-22-000-pa-vendeur-roborock-3450017 · roboter-forum (E) : 2 chiens, « aucun problème avec les poils », ouvertures larges vers le bac. https://www.roboter-forum.com/threads/tier-hundehaare-ohne-verstopfung.73552/ · roboter-forum (E) : brosses « encore assez propres après une semaine » malgré beaucoup de poils de chien. https://www.roboter-forum.com/threads/roborock-saros-10r-erste-erfahrungen.71019/page-44 |
| ❌ **Serpillières trop sèches** (souvent celle de gauche) | ≥3 | roboter-forum (E) : Roborock remplace le robot. Un remplaçant a le même défaut et repart aussi. Avant l'échange, le support conseille d'augmenter le débit d'eau et de raccourcir l'intervalle de relavage. https://www.roboter-forum.com/threads/roborock-saros-10r-erste-erfahrungen.71019/page-61 · fil dédié : https://www.roboter-forum.com/threads/wo-ist-der-wasserauslass-fuer-die-mopps-bei-einem-saros-10r.77351/ |
| ❌ **Tapis** : brosse latérale relevée sur tapis, zones de tapis oubliées, robot qui dérive | ≥3 | roboter-forum (E). Deux propriétaires trouvent « illogique » que la brosse latérale ne tourne pas sur les tapis. Un autre a un tapis bien fait et un autre mal fait. https://www.roboter-forum.com/threads/roborock-saros-10r-erste-erfahrungen.71019/page-22 · https://www.roboter-forum.com/threads/roborock-saros-10r-erste-erfahrungen.71019/page-52 |
| ⚠️ Panne matérielle sous garantie | 1 | Roue motrice qui grince. Vidéo envoyée, robot échangé, enlèvement UPS vers la Pologne (Allemagne). https://www.roboter-forum.com/threads/roborock-saros-10r-erste-erfahrungen.71019/page-16 (E) |
| ⚠️ Divers (Dealabs, modèle pas sûr d'après l'extrait) | 1–2 | Après 6 mois : niveau d'eau qui baisse vite, détection des humains aléatoire. Brosse latérale à problème au bout d'un mois. Une « erreur 106 après 2 ans » concerne un **robot acheté en Chine**, peut-être pas un 10R. https://www.dealabs.com/bons-plans/robot-aspirateur-roborock-saros-10r-22-000-pa-vendeur-roborock-3450017 (E) |
| ✅ Satisfait sur la durée | 1 | Dealabs (E) : « depuis l'été 2025, très satisfait », entretien 2 fois par an. Même lien. |
| 🏠 Home Assistant | 4 tickets | Intégration officielle **dans Home Assistant de base**, qui fonctionne. Petits bugs : robot « indisponible » par moments, ticket clos https://github.com/home-assistant/core/issues/172552 ; intensité de serpillière inconnue, ticket ouvert https://github.com/home-assistant/core/issues/153638 ; capteur de charge, ouvert https://github.com/home-assistant/core/issues/169151 (P) |

## 2. Dreame X50 Ultra Complete

| Problème | Nb | Exemples et liens |
|---|---|---|
| Poils et cheveux | 1 ✅ / 1 ❓ | roboter-forum (E). Des propriétaires aux cheveux longs disent que peu de cheveux se prennent dans la double brosse. Un autre est passé à la brosse **TriCut** parce que la brosse en caoutchouc ramassait mal les poils de chien (modèle X40 ou X50, pas sûr). https://www.roboter-forum.com/threads/dreame-l50-x50-erste-erfahrungen-tipps-tricks-allgemeiner-austausch.71969/page-6 · *Testeur, pas propriétaire* : Smart Home Fox voit des poils rester dans les brosses, à retirer à la main. |
| ❌ **Navigation** : coins oubliés, trajets bizarres, zones sautées | ≥2 | Un fil entier « Dreame X50 navigue mal ». Un propriétaire a rendu le robot. https://www.roboter-forum.com/threads/dreame-x50-navigiert-nicht-gut.72526/ (E) |
| ❌ **Brosse latérale** : ne tourne plus (défaut reconnu par le support sur vidéo), ou tombe sans arrêt | 2 | https://www.roboter-forum.com/threads/dreame-x50-verliert-immer-wieder-die-seitenbuerste.76952/ (E) |
| ❌ Odeur de brûlé au lavage des serpillières (pompe de vidange), robot renvoyé | 1 | https://www.roboter-forum.com/threads/x50-ultra-complete-verbrannter-geruch.72688/ (E) |
| ⚠️ Batterie plus sollicitée que sur le X40, forte conso en veille, tourelle laser qui claque | 1–2 | Fil de discussion général sur le X50 (E) : https://www.roboter-forum.com/threads/dreame-x50-ultra-complete-erste-erfahrungen-tipps-tricks-allgemeiner-austausch.71969/ |
| SAV Dreame France (autres modèles) | 2 | Station du X40 fissurée après 2 ans : « Dreame France leur service client une honte ». X50 **Master** défectueux à l'arrivée, puis remplacé et « parfait depuis ». https://www.dealabs.com/bons-plans/aspirateur-robot-avec-station-de-vidage-automatique-dreame-x50-master-3443861 (E) |
| 🏠 Home Assistant | 5+ tickets | **Pas intégré à Home Assistant de base** : il faut l'intégration non officielle Tasshack, via HACS. Avec la v2.0.0 sur X50, Home Assistant a planté par manque de mémoire, corrigé : https://github.com/Tasshack/dreame-vacuum/issues/1840 ; le robot ne se mettait plus en veille : https://github.com/Tasshack/dreame-vacuum/issues/1822 ; des variantes du X50 encore non reconnues : https://github.com/Tasshack/dreame-vacuum/issues/1901 (ouvert, 10/2026) (P) |

## 3. Dreame Matrix10 Ultra

| Problème | Nb | Exemples et liens |
|---|---|---|
| ❌ **Panne au bout de quelques mois / SAV à répétition** | ≥2 | Dealabs (E) : « en panne au bout de 6 mois ». Deux passages au SAV, puis demande de remboursement : « il passait plus de temps en SAV qu'à nettoyer ». https://www.dealabs.com/bons-plans/dreame-matrix10-ultra-robot-aspirateur-laveur-multi-serpilliere-30-000-pa-3442874 |
| ❌ **Mécanisme d'échange des serpillières défectueux dès l'arrivée** (grincement fort) | 1 | https://www.roboter-forum.com/threads/dreame-matrix10-ultra.76616/ (E) |
| ❌ Support de roulette qui casse « assez souvent » (cité pour le Matrix10, Pro ou Ultra) | 1 | https://www.dealabs.com/bons-plans/robot-aspirateur-laveur-dreame-matrix10-pro-multi-serpillieres-avec-station-noir-3448744 (E) |
| ⚠️ Station très grosse et bruyante (vidage, séchage) | 1–2 | Même fil Dealabs Matrix10 Ultra (E) |
| ✅ Poils : peu d'enroulement, chez un propriétaire d'animaux | 1 | Même fil Dealabs Matrix10 Ultra (E) |
| ✅ Satisfaits après quelques semaines | 2 | « une vraie petite pépite », « machine incroyable ». Même fil Dealabs (E) |
| 🧪 Test prêté par la marque | — | Échange des serpillières fiable (environ 2 min), mais **ménage nettement plus long**. Navigation sous les meubles faible. https://www.roboter-forum.com/threads/roboter-forum-review-dreame-matrix-10-ultra-wischpadwechsel-fuer-jedermann.78598/ |
| 🏠 Home Assistant | 2 tickets | Reconnu par Tasshack depuis début 2026 après plusieurs demandes. Bug du type de serpillière par pièce, qui remplit le journal d'erreurs, corrigé : https://github.com/Tasshack/dreame-vacuum/issues/1946 (P) |

## 4. Roborock Saros 20

| Problème | Nb | Exemples et liens |
|---|---|---|
| ❌ Seuil de 3 cm passé seulement avec de l'élan, bruyamment | ≥2 | https://www.roboter-forum.com/threads/saros-20-schafft-keine-3-cm-tuerschwelle.79650/ (E) |
| ⚠️ Tapis : il oublie des zones jusqu'à ce que la carte « apprenne » | 1 | https://www.roboter-forum.com/threads/saros-20-bereiche-werden-ausgelassen.79313/ (E) |
| ❌ Robot devenu inutilisable après une mise à jour, rendu | 1 | Fil Saros 20 contre MOVA V70 (E) : https://www.roboter-forum.com/threads/roborock-saros-20-sonic-vs-mova-v70-ultra-vs-dreame-x60-pro.79735/ |
| ✅ Très satisfait après quelques mois | 1 | Dealabs (E, modèle pas sûr) : https://www.dealabs.com/bons-plans/robot-aspirateur-saros-20-complete-1l-offert-3450520 |
| 🏠 Home Assistant | 2 tickets ouverts | Réservoir d'eau non remonté, intensité de serpillière « inconnue », mode « aspiration coupée » qui échoue. 2 utilisateurs, ouvert depuis 08/2026 : https://github.com/home-assistant/core/issues/178659 ; carte non décodée : https://github.com/Python-roborock/python-roborock/issues/947 (P) |

Rien sur les poils de chien ni sur les serpillières venant de propriétaires.

## 5. Roborock Saros 20 Neo (Qrevo Edge 3 Pro)

| Problème | Nb | Exemples et liens |
|---|---|---|
| ✅ Facile, bonne navigation, nettoie bien | 2 (courts) | https://www.dealabs.com/bons-plans/roborock-saros-20-neo-3450581 (E) |
| 🏠 Home Assistant | 1 ticket | Photos d'obstacles non récupérées : https://github.com/Python-roborock/python-roborock/issues/991 (P) |

Trop récent : **aucun retour à plusieurs semaines** sur les poils, les serpillières ou les tapis.

## 6. MOVA V70 Ultra Complete

| Problème | Nb | Exemples et liens |
|---|---|---|
| ❌ **La station ne reprend pas les serpillières** (message « échec d'installation des serpillières » après une mise à jour) | ≥2 | Réglé chez certains en vidant le cache de l'appli, chez d'autres par un firmware de débogage. https://www.roboter-forum.com/threads/erste-erfahrung-zum-mova-v70-ultra-complete.79207/page-3 · https://www.roboter-forum.com/threads/mova-v70-ultra-complete-x-erfahrungen-fragen-und-austausch.79327/page-6 (E) |
| ❌ **Retour à la base raté** (contacts de charge) | ≥2 | Même fil (E). Le support demande de nettoyer les contacts, y compris des **cheveux**. |
| ❌ **La serpillière sur bras extensible se détache** (moins de 30 jours), robot rendu | 1 | Fil V70 Complete X (E) : https://www.roboter-forum.com/threads/mova-v70-ultra-complete-x-erfahrungen-fragen-und-austausch.79327/ |
| ❌ Serpillières peu mouillées en ligne droite, ou serpillière droite sans eau | 1–2 | Même fil (E). Le support confirme que c'est le « comportement normal ». |
| ✅ Aspiration sur tapis, chez un propriétaire de chien | 1 | Même fil (E) |
| 🧪 Test prêté par la marque | — | Lavage doux, donc **serpillières visiblement sales** à la longue. **Pas de poils d'animaux** pendant le test. https://www.roboter-forum.com/threads/roboter-forum-review-mova-v70-ultra-complete-x-innovative-technik-im-alltagstest.79286/ |
| SAV MOVA France | 0 propriétaire du V70 | Sur Dealabs, seulement des avis de seconde main (« le SAV est long et compliqué visiblement »). Non compté. Le grand frère **V50** : « navigation catastrophique », tombé en panne et renvoyé (computerbase, 1 propriétaire) : https://www.computerbase.de/forum/threads/roborock-saros-20-sonic-vs-mova-v70-ultra.2274103/ (P) |
| 🏠 Home Assistant | 1 ticket | Pris en charge par Tasshack. Le bug de la carte interactive, qui ne réagissait pas aux clics, a été corrigé en v2.0.2 ; le nettoyage par pièce marche : https://github.com/Tasshack/dreame-vacuum/issues/1879 (P) |

---

## 7. Robots secondaires (très peu de données)

| Robot | Ce qu'on trouve | Liens |
|---|---|---|
| **Dreame Matrix10 Pro** | 1 acheteur récent satisfait. 1 signale une roulette fragile et trouve l'échange des serpillières « complexe mécaniquement ». Pas de tourelle rétractable. | https://www.dealabs.com/bons-plans/robot-aspirateur-laveur-dreame-matrix10-pro-multi-serpillieres-avec-station-noir-3448744 (E) |
| **Roborock Qrevo Edge 2X** | Aucun propriétaire trouvé. Sur le Edge 2 : 1 propriétaire qui a aussi un 10R ne voit « pas de différence de performance ». Famille Qrevo : sur l'ancien Q Revo, la **brosse silicone enroule les poils**, à nettoyer un passage sur deux (HFR, 13/05/2024, P). Station bouchée par des poils de chien devant le sac (1, DE). Home Assistant : capteurs de station disparus après la version 2026.7 (23 commentaires, corrigé). | https://www.roboter-forum.com/threads/qrevo-edge-2-erfahrung.79738/ (E) · https://forum.hardware.fr/hfr/Discussions/Viepratique/unik-robot-domestique-sujet_45375_446.htm (P) · https://github.com/home-assistant/core/issues/175353 (P) |
| **Ecovacs T90 Max Pro Omni** | Aucun propriétaire (sorti à l'IFA 2026). T90 Pro Omni, test 🧪 : cheveux longs sans nœuds, mais **le rouleau se tasse et laisse des traces**. T90S : poils de chat restés sur le parquet (1). Cousin T80S, propriétaires HFR (P) : roues prises dans les franges d'un tapis (1), parquet imitation pris pour des taches (2), serpillière lente à sécher (1), historique vide réglé par le SAV en ~15 j (1). | https://www.roboter-forum.com/threads/roboter-forum-review-der-ecovacs-deebot-t90-pro-omni-komfortable-bodenreinigung-im-praxistest.77897/ · https://forum.hardware.fr/hfr/Discussions/Viepratique/unik-robot-domestique-sujet_45375_512.htm |
| **MOVA S70 Ultra Roller** | Test 🧪 : **le rouleau lave mal les coins et les bords**, ménage long, station massive. La brosse CleanChop limite l'enroulement. Sur le S70 Roller (sans « Ultra ») : propriétaires mitigés (reconnaissance d'objets, robot qui goutte). | https://www.roboter-forum.com/threads/roboter-forum-review-mova-s70-ultra-roller-wischrolle-flache-bauweise-und-starke-saugleistung.80036/ · https://www.roboter-forum.com/threads/mova-s70-roller-erste-erfahrungen.77637/ (E) |

---

## Conclusion pour notre foyer

1. **Poils et cheveux longs** : seul le **Saros 10R** a plusieurs propriétaires (3) avec chien ou cheveux longs qui confirment « pas d'enroulement ». Pour les X50, V70 et Saros 20, ce point n'est confirmé par **aucun propriétaire**.
2. **Fiabilité** : le **Matrix10 Ultra** cumule les signaux négatifs (panne à 6 mois, mécanisme défectueux, SAV Dreame lent). Son échange de serpillières est une pièce mobile de plus.
3. **Serpillières** : le **MOVA V70** a le plus de soucis de serpillières (reprise ratée, serpillière qui se détache, peu d'eau). Le **Saros 10R** a un défaut connu de serpillière sèche, mais Roborock échange le robot.
4. **Tapis** : on ne voit pas de défaut grave. Il y a des agacements chez Roborock (brosse latérale relevée, zones de tapis oubliées).
5. **Home Assistant** : c'est **plus simple chez Roborock**, intégré à Home Assistant de base, avec des bugs mineurs. Chez Dreame et MOVA, il faut l'intégration non officielle Tasshack, qui marche mais a eu de vrais bugs en 2026.

**Limite** : les comptes sont tous très petits (1 à 3 personnes). Les extraits (E) sont à reconfirmer en ouvrant les pages dans un vrai navigateur, surtout les commentaires Dealabs.
