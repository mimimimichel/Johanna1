# Notes refaites le 2026-10-31 selon la règle : seules les sources A (indépendantes) et B (protocole publié) comptent.
# Sans donnée A/B : note neutre 5 « pas de donnée fiable ». Les avis C restent mentionnés, sans peser.
RT="https://www.rtings.com/robot-vacuum/reviews/"
VW="https://vacuumwars.com/"
HU="https://www.thesmarthomehookup.com/2026-ultimate-robot-vacuum-and-mop-comparison/"
SW="https://www.test.de/Saugroboter-im-Test-4806685-0/"
EU="https://www.greenme.it/?p=1431832"
N="Pas de donnée fiable (aucun test indépendant ni protocole publié)."
def r(s,v,*src): return (s,v,list(src))
FIA_DREAME=r(8,"Enquête Euroconsumers 2026 (Test-Achats, Altroconsumo… 8 500 propriétaires) : Dreame 96/100 en fiabilité, la meilleure note.",("Euroconsumers (A, via GreenMe)",EU))
FIA_ROBO=r(7,"Enquête Euroconsumers 2026 : Roborock 83/100 en fiabilité (Dreame 96, Ecovacs 75).",("Euroconsumers (A, via GreenMe)",EU))
FIA_ECO=r(6,"Enquête Euroconsumers 2026 : Ecovacs 75/100 en fiabilité.",("Euroconsumers (A, via GreenMe)",EU))
FIA_NONE=r(5,"Marque absente des enquêtes de fiabilité trouvées.")
OV={
"roborock-saros20":{
 "poils":r(7.5,"Rtings (A) : « clears most hair in a single pass ». Vacuum Wars (B) : 88 % de poils, 0 % d'enroulement. The Hook Up (B) : enroulement « dans la moyenne ».",("Rtings (A)",RT+"roborock/saros-20"),("Vacuum Wars (B)",VW+"roborock-saros-20-review/"),("The Hook Up (B)",HU)),
 "entretien":r(6.5,"Rtings (A) : la station assure l'essentiel de l'entretien courant. Score d'entretien détaillé payant. Petit bac de 260 ml.",("Rtings (A)",RT+"roborock/saros-20")),
 "tapis_mop":r(6.5,"Peut déposer ses serpillières (fabricant). Mais The Hook Up (B) a vu ses serpillières traîner sur un tapis ; Rtings (A) : se prend dans les franges.",("The Hook Up (B)",HU),("Rtings (A)",RT+"roborock/saros-20")),
 "tapis_asp":r(8,"Rtings (A) : retire la plupart des poils d'animaux des tapis en un seul passage.",("Rtings (A)",RT+"roborock/saros-20")),
 "obstacles":r(5.5,"Vacuum Wars (B) : 17/24. Rtings (A) : évitement peu fiable sur tapis.",("Vacuum Wars (B)",VW+"roborock-saros-20-review/")),
 "lavage":r(6.5,"Vacuum Wars (B) : au-dessus de la moyenne sur taches séchées. The Hook Up (B) : moyen sur la boue. Rtings (A) : bien pour le quotidien, pas pour les taches tenaces.",("Vacuum Wars (B)",VW+"roborock-saros-20-review/"),("The Hook Up (B)",HU)),
 "fiabilite":FIA_ROBO},
"roborock-saros20-neo":{
 "poils":r(6,"Expert Reviews (B) : aucun cheveu enroulé en 2 mois. Pas de mesure des poils ramassés.",("Expert Reviews (B)","https://www.expertreviews.co.uk/home-garden/vacuums-cleaning/roborock-saros-20-neo-review")),
 "entretien":r(5,"Expert Reviews (B) : brosses propres en 2 mois, mais filtre du bac vite encrassé et salissant à nettoyer.",("Expert Reviews (B)","https://www.expertreviews.co.uk/home-garden/vacuums-cleaning/roborock-saros-20-neo-review")),
 "tapis_mop":r(7,"Dépose ses serpillières (fabricant). Pas de test A/B sur tapis."),
 "tapis_asp":r(5,N),"obstacles":r(5,N),"lavage":r(5,N),"fiabilite":FIA_ROBO},
"roborock-saros20-sonic":{
 "poils":r(6,"Vacuum Wars (B) : 78 % de poils, 0 % d'enroulement.",("Vacuum Wars (B)",VW+"roborock-saros-20-sonic-review/")),
 "entretien":r(5,N),"tapis_mop":r(7,"Plaque laissée à la station (fabricant). Pas de test A/B sur tapis."),
 "tapis_asp":r(5,N),"obstacles":r(5,N),
 "lavage":r(3,"Vacuum Wars (B) : 62 points contre 108 de moyenne sur taches séchées.",("Vacuum Wars (B)",VW+"roborock-saros-20-sonic-review/")),
 "fiabilite":FIA_ROBO},
"roborock-saros10r":{
 "poils":r(5.5,"Rtings (A) : ramassage des poils d'animaux « décevant », plusieurs passages nécessaires. Vacuum Wars (B) : 92 %, 0 % d'enroulement.",("Rtings (A)",RT+"roborock/saros-10r")),
 "entretien":r(5,"Vacuum Wars (B, problèmes fréquents) : cheveux qui bouchent l'espace entre les deux rouleaux, pas toujours signalé. Rtings (A) : entretien « raisonnable ».",("Vacuum Wars (B)",VW+"roborock-saros-10r-common-problems-and-fixes/")),
 "tapis_mop":r(7,"Dépose ses serpillières (fabricant)."),
 "tapis_asp":r(3.5,"Rtings (A) : la brosse en deux parties n'agite pas assez le tapis pour les poils incrustés.",("Rtings (A)",RT+"roborock/saros-10r")),
 "obstacles":r(5,N),
 "lavage":r(7,"Rtings (A) : très bon lavage. Vacuum Wars (B) : dans la moyenne.",("Rtings (A)",RT+"roborock/saros-10r")),
 "fiabilite":FIA_ROBO},
"mova-v70":{
 "poils":r(7.5,"Vacuum Wars (B) : 94 % de poils, 0 % d'enroulement, son choix « anti-emmêlement ». Aucun test indépendant (A).",("Vacuum Wars (B)",VW+"best-robot-vacuum-for-pet-hair/")),
 "entretien":r(5,"Pas de donnée fiable. Un testeur isolé (TechRadar, C) signale des cheveux emmêlés dans la brosse latérale et les roues ; station sans sac non testée avec beaucoup de poils."),
 "tapis_mop":r(7,"Dépose ses serpillières avant les tapis (fabricant). Pas de test A/B sur tapis."),
 "tapis_asp":r(8,"Vacuum Wars (B) : 92 % en nettoyage profond des tapis.",("Vacuum Wars (B)",VW+"best-robot-vacuum-for-pet-hair/")),
 "obstacles":r(5,N),"lavage":r(5,N),"fiabilite":FIA_NONE},
"mova-mobius60":{
 "poils":r(5.5,"Rtings (A) : ramassage des poils « sub-par », traîne des poils. Vacuum Wars (B) : 94 %, 0 % d'enroulement.",("Rtings (A)",RT+"mova/mobius-60"),("Vacuum Wars (B)",VW+"mova-mobius-60-review/")),
 "entretien":r(4,"Rtings (A) : entretien plus lourd que voulu, beaucoup de pièces à nettoyer régulièrement ; se prend dans les franges.",("Rtings (A)",RT+"mova/mobius-60")),
 "tapis_mop":r(6.5,"Dépose ses serpillières (fabricant), mais The Hook Up (B) les a vues traîner sur un tapis.",("The Hook Up (B)",HU)),
 "tapis_asp":r(5,"Vacuum Wars (B) : 88 % en profondeur ; Rtings (A) : traîne les poils.",("Rtings (A)",RT+"mova/mobius-60")),
 "obstacles":r(8,"Vacuum Wars (B) : 22/24.",("Vacuum Wars (B)",VW+"mova-mobius-60-review/")),
 "lavage":r(3.5,"Vacuum Wars (B) : sous la moyenne. The Hook Up (B) : faible sur la boue. Rtings (A) : n'enlève pas complètement les taches séchées.",("The Hook Up (B)",HU)),
 "fiabilite":FIA_NONE},
"dreame-matrix10-ultra":{
 "poils":r(7,"Vacuum Wars (B) : 92 % de poils, 0 % d'enroulement. Aucun test indépendant (A).",("Vacuum Wars (B)",VW+"dreame-matrix10-ultra-review/")),
 "entretien":r(5,"Pas de donnée fiable. Même famille de double brosse que le X50 (bouchons signalés par Vacuum Wars sur le X50)."),
 "tapis_mop":r(7,"Dépose ses serpillières sur tapis (fabricant). Pas de test A/B sur tapis."),
 "tapis_asp":r(6.5,"Vacuum Wars (B) : 84 % en nettoyage profond des tapis.",("Vacuum Wars (B)",VW+"dreame-matrix10-ultra-review/")),
 "obstacles":r(5,N),
 "lavage":r(8.5,"Vacuum Wars (B) : nettement au-dessus de la moyenne sur taches séchées (136 et 147 points).",("Vacuum Wars (B)",VW+"mova-mobius-60-review/")),
 "fiabilite":FIA_DREAME},
"dreame-x50":{
 "poils":r(8,"Stiftung Warentest (A) : « bon avec les cheveux longs ». Rtings (A) : poils « acceptable ». Vacuum Wars (B) : 98 %, 0 % d'enroulement.",("Stiftung Warentest (A, via résumé)",SW),("Rtings (A)",RT+"dreame/x50-ultra"),("Vacuum Wars (B)",VW+"dreame-x50-ultra-review-is-it-the-best-yet")),
 "entretien":r(5.5,"Rtings (A) : la station fait l'essentiel. Vacuum Wars (B) : avec un chien qui perd beaucoup, boudins de cheveux qui bouchent l'entrée du bac (une testeuse).",("Rtings (A)",RT+"dreame/x50-ultra"),("Vacuum Wars (B)",VW+"dreame-x50-ultra-robot-vacuum-common-complaints-and-how-to-fix-them/")),
 "tapis_mop":r(6.5,"Dépose ses serpillières sur tapis épais (fabricant)."),
 "tapis_asp":r(6,"Rtings (A) : laisse des poils incrustés dans les tapis.",("Rtings (A)",RT+"dreame/x50-ultra")),
 "obstacles":r(5,N),
 "lavage":r(4.5,"Vacuum Wars (B) : sous la moyenne sur taches séchées. Rtings (A) : un passage de plus nécessaire.",("Rtings (A)",RT+"dreame/x50-ultra")),
 "fiabilite":FIA_DREAME},
"dreame-x60-pro":{
 "poils":r(6.5,"Modèle proche X60 Max : Rtings (A) poils « passable », Vacuum Wars (B) 100 %, 0 % d'enroulement.",("Rtings (A, X60 Max)",RT+"dreame/x60-max-ultra-complete")),
 "entretien":r(5,"Pas de donnée fiable. Rtings (A, X60 Max) : les franges de tapis s'enroulent dans la brosse."),
 "tapis_mop":r(6.5,"Dépose ses serpillières sur tapis épais (fabricant), mais The Hook Up (B) a vu celles du X60 Max traîner sur un tapis.",("The Hook Up (B)",HU)),
 "tapis_asp":r(6,"Modèle proche X60 Max : Vacuum Wars (B) 89 % en profondeur ; Rtings (A) poils « passable »."),
 "obstacles":r(5,N),
 "lavage":r(4.5,"The Hook Up (B) : le X60 Max est le dernier sur la boue séchée. Détection des liquides frais : seulement des sources C.",("The Hook Up (B)",HU)),
 "fiabilite":FIA_DREAME},
"dreame-l40s-pro":{
 "poils":r(6.5,"Modèle proche L40s Ultra : Vacuum Wars (B) 91 %, 0 % d'enroulement.",("Vacuum Wars (B)",VW+"dreame-l40s-series-review/")),
 "entretien":r(5,N),"tapis_mop":r(6.5,"Dépose ses serpillières (fabricant)."),"tapis_asp":r(5,N),
 "obstacles":r(7,"Modèle proche L40s Ultra AE : Vacuum Wars (B) 19/24.",("Vacuum Wars (B)",VW+"dreame-l40s-series-review/")),
 "lavage":r(5,N),"fiabilite":FIA_DREAME},
"ecovacs-t50-gen3":{
 "poils":r(6,"Pas de test de la Gen3. T50 Pro gen 1 : Vacuum Wars (B) 86 %, 0 % d'enroulement.",("Vacuum Wars (B, gen 1)",VW+"t50-max-pro-omni-and-t50-pro/")),
 "entretien":r(5,N),"tapis_mop":r(5,"Dépose des serpillières non confirmée."),"tapis_asp":r(5,N),
 "obstacles":r(4,"T50 Pro gen 1 : Vacuum Wars (B) 15/24, sous la moyenne.",("Vacuum Wars (B, gen 1)",VW+"t50-max-pro-omni-and-t50-pro/")),
 "lavage":r(7.5,"T50 Pro gen 1 : Vacuum Wars (B), meilleur score de taches jamais mesuré (170 contre 98).",("Vacuum Wars (B, gen 1)",VW+"t50-max-pro-omni-and-t50-pro/")),
 "fiabilite":FIA_ECO},
"ecovacs-x12s":{
 "poils":r(7,"Modèle proche X12 : Vacuum Wars (B) 100 %, 0 % d'enroulement.",("Vacuum Wars (B)",VW+"ecovacs-x12-omnicyclone-long-term-review/")),
 "entretien":r(5,"Version Pro Omni (avec sac) non testée. La version sans sac s'est bouchée de poils de chien en 2 semaines (Vacuum Wars, B, 3 mois).",("Vacuum Wars (B)",VW+"ecovacs-x12-omnicyclone-long-term-review/")),
 "tapis_mop":r(3,"The Hook Up (B) : le X12 a mouillé un tapis par l'arrière malgré son capot.",("The Hook Up (B)",HU)),
 "tapis_asp":r(5,N),
 "obstacles":r(7,"The Hook Up (B) : X12, 6/6 au test des déjections factices (meilleur score).",("The Hook Up (B)",HU)),
 "lavage":r(5,"The Hook Up (B) : X12 étonnamment faible sur la boue pour un rouleau.",("The Hook Up (B)",HU)),
 "fiabilite":FIA_ECO},
"narwal-flow2":{
 "poils":r(6.5,"Rtings (A) : les cheveux ne s'emmêlent pas, mais ramassage faible. Vacuum Wars (B) : 0 % d'enroulement. The Hook Up (B) : 1er sur les poils.",("Rtings (A)",RT+"narwal/flow-2"),("The Hook Up (B)",HU)),
 "entretien":r(5.5,"Rtings (A) : pas d'emmêlement. Pas de test longue durée.",("Rtings (A)",RT+"narwal/flow-2")),
 "tapis_mop":r(3,"The Hook Up (B) : a mouillé les tapis.",("The Hook Up (B)",HU)),
 "tapis_asp":r(5.5,"Vacuum Wars (B) : 84 % en profondeur ; Rtings (A) : ramassage faible."),
 "obstacles":r(6.5,"Vacuum Wars (B) : 20/24 ; The Hook Up (B) : 3/6.",("The Hook Up (B)",HU)),
 "lavage":r(7,"The Hook Up (B) : très bon sur la boue séchée (2e). Rtings (A) : plusieurs passages sur les taches tenaces.",("The Hook Up (B)",HU)),
 "fiabilite":FIA_NONE},
"dreame-l50-ae":{
 "poils":r(5,"Pas de donnée fiable : seuls deux testeurs de niveau C signalent des cheveux emmêlés dans la brosse TriCut."),
 "entretien":r(5,N),"tapis_mop":r(4,"Simple relevage de 10,5 mm (fabricant)."),"tapis_asp":r(5,N),"obstacles":r(5,N),"lavage":r(5,N),"fiabilite":FIA_DREAME},
"roborock-qrevo-s-pro":{
 "poils":r(5,N),"entretien":r(5,N),"tapis_mop":r(4,"Simple relevage de 10 mm (fabricant)."),
 "tapis_asp":r(4,"Modèle proche Qrevo S : Rtings (A) faible sur les poils dans les tapis.",("Rtings (A, Qrevo S)","https://www.rtings.com/vacuum/reviews/roborock/qrevo-s")),
 "obstacles":r(3,"Pas de caméra (fabricant)."),"lavage":r(5,N),"fiabilite":FIA_ROBO},
}
TXT={
"roborock-saros20":("top","Le plus solide sur les preuves indépendantes : Rtings (A) le juge bon sur les poils, y compris dans les tapis.",["Rtings (A) : retire la plupart des poils, même dans les tapis","Serpillières déposables, 7,95 cm","Intégration Home Assistant officielle"],["Obstacles moyens (Vacuum Wars 17/24)","Serpillières vues traînant sur un tapis (The Hook Up)","Petit bac de 260 ml"]),
"roborock-saros20-neo":("meh","Probablement proche du Saros 20, mais presque aucun test indépendant.",["Brosses propres après 2 mois (Expert Reviews)","Serpillières déposables"],["Peu testé","Filtre du bac vite encrassé"]),
"roborock-saros20-sonic":("no","Faible sur les taches séchées et moyen sur les poils selon Vacuum Wars.",["Plaque laissée à la station"],["78 % de poils (Vacuum Wars)","Lavage très sous la moyenne"]),
"roborock-saros10r":("meh","Rtings (A) le trouve décevant sur les poils dans les tapis.",["Très bon lavage (Rtings)","Serpillières déposables"],["Poils dans les tapis : « décevant » (Rtings)","Cheveux qui bouchent l'espace entre les rouleaux (Vacuum Wars)"]),
"mova-v70":("good","Très bon chez Vacuum Wars sur les poils et les tapis, mais aucun test indépendant.",["94 % de poils, 0 % d'enroulement (Vacuum Wars)","92 % en profondeur sur tapis (Vacuum Wars)","Dépose ses serpillières"],["Aucun test indépendant (A)","Station sans sac non testée avec beaucoup de poils","Marque absente des enquêtes de fiabilité"]),
"mova-mobius60":("no","Rtings (A) : poils « sub-par » et entretien lourd.",["Obstacles 22/24 (Vacuum Wars)"],["Poils « sub-par » (Rtings)","Entretien lourd, beaucoup de pièces (Rtings)","Lavage sous la moyenne"]),
"dreame-matrix10-ultra":("good","Le meilleur lavage mesuré par Vacuum Wars, bon sur les poils, prix bas ; pas de test indépendant.",["Lavage nettement au-dessus de la moyenne (Vacuum Wars)","92 % de poils, 0 % d'enroulement (Vacuum Wars)","540,83 €"],["Aucun test indépendant (A)","Pas de donnée sur l'entretien dans la durée"]),
"dreame-x50":("good","Seul modèle salué par Stiftung Warentest pour les cheveux longs ; lavage faible.",["« Bon avec les cheveux longs » (Stiftung Warentest)","98 % de poils (Vacuum Wars)","599 €"],["Laisse des poils incrustés dans les tapis (Rtings)","Lavage sous la moyenne","Bouchons de cheveux signalés avec un gros chien (Vacuum Wars)"]),
"dreame-x60-pro":("meh","Haut de gamme, mais les tests du modèle proche (X60 Max) sont moyens sur les poils et la boue.",["Détecte les liquides (fabricant)"],["1 499 €","Poils « passable » sur le X60 Max (Rtings)","Dernier sur la boue (The Hook Up, X60 Max)"]),
"dreame-l40s-pro":("meh","Correct d'après des modèles proches, mais 10,35 cm.",["459 €","Obstacles 19/24 sur un modèle proche"],["10,35 cm : à mesurer sous le lit","Peu de données propres"]),
"ecovacs-t50-gen3":("meh","Le moins cher sous 8,1 cm, mais aucun test de cette version.",["299–399 €","8,1 cm","Excellent lavage sur la génération précédente"],["Aucun test de la Gen3","Obstacles sous la moyenne (gen 1)"]),
"ecovacs-x12s":("no","Mouille les tapis selon The Hook Up.",["Évite très bien les obstacles (The Hook Up)"],["A mouillé un tapis (The Hook Up)","Faible sur la boue"]),
"narwal-flow2":("no","A mouillé les tapis selon The Hook Up.",["Ne s'emmêle pas (Rtings)","Très bon sur la boue (The Hook Up)"],["A mouillé les tapis (The Hook Up)","Ramassage des poils faible (Rtings)"]),
"dreame-l50-ae":("meh","Pas de test fiable ; deux avis isolés signalent des cheveux emmêlés.",["Prix"],["Pas de test fiable","Simple relevage des serpillières"]),
"roborock-qrevo-s-pro":("no","Pas de caméra, simple relevage des serpillières, faible sur les tapis (modèle proche, Rtings).",["379,99 €","Home Assistant officiel"],["Pas de caméra","Faible sur les poils dans les tapis (Qrevo S, Rtings)"]),
}
