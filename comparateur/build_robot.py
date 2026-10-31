import json, os
OUT = os.path.join(os.path.dirname(__file__), "data")
SHA = "https://www.smarthomeassistent.de/saugroboter/"
VW = "https://vacuumwars.com/"

criteria = [
 {"key":"poils","short":"Poils","label":"Poils et cheveux","weight":25,
  "explain":"Part des poils de chien ramassés et cheveux longs qui s'enroulent (ou pas) dans les brosses. Le nom de la brosse ne prouve rien : seuls les tests comptent.",
  "how":"Vacuum Wars : 2 g de poils d'animaux incrustés + 1 g de cheveux de 18 cm. smarthomeassistent : 1 g de vrais cheveux sur stratifié, tapis ras et tapis épais, −1 point si ça s'enroule."},
 {"key":"tapis_mop","short":"Tapis au sec","label":"Tapis au sec","weight":15,
  "explain":"Le robot ne doit jamais poser de serpillière mouillée sur un tapis. Le plus sûr : il dépose ses serpillières à la station avant d'aller sur les tapis.",
  "how":"Fiche fabricant (dépose automatique, hauteur de relevage) + tests (tapis mouillés ou non, détection des tapis)."},
 {"key":"tapis_asp","short":"Tapis épais","label":"Poils dans les tapis","weight":10,
  "explain":"Capacité à extraire les poils incrustés dans un tapis épais, là où le sous-poil du chien s'accroche.",
  "how":"smarthomeassistent : grammes récupérés sur 100 g dans un tapis épais. Vacuum Wars : nettoyage en profondeur des tapis."},
 {"key":"obstacles","short":"Obstacles","label":"Évite les obstacles","weight":8,
  "explain":"Contourner la gamelle, les câbles, les chaussettes et les jouets sans les pousser ni s'y coincer.",
  "how":"smarthomeassistent : parcours de 53 points (câbles, chaussettes, jouets, et aussi de fausses déjections en plastique, un test standard pour les foyers avec chien). Vacuum Wars : 24 obstacles."},
 {"key":"lavage","short":"Lavage","label":"Lavage et traces de pattes","weight":12,
  "explain":"Qualité du lavage, notamment sur les traces de pattes mouillées de l'entrée et de la cuisine, et hygiène de la station : eau chaude, séchage à l'air chaud, dosage du détergent.",
  "how":"Fiche fabricant + mesures de température et de lavage dans les tests."},
 {"key":"hauteur","short":"Hauteur","label":"Passe sous le lit","weight":8,
  "explain":"Le lit laisse environ 10 cm. Sous 9 cm, aucun souci ; 9,5 à 9,8 cm, ça passe de justesse ; 10,4 cm, il faut mesurer.",
  "how":"Hauteur du robot, laser rentré pour les modèles à tourelle rétractable."},
 {"key":"domotique","short":"Domotique","label":"Home Assistant et Google","weight":7,
  "explain":"Commande à la voix et routines Google Home, intégration Home Assistant (officielle ou communautaire), Matter.",
  "how":"Doc Home Assistant, listes Matter, intégrations communautaires."},
 {"key":"prix","short":"Prix","label":"Prix","weight":10,"auto":"price","best":300,"worst":1500,
  "explain":"Calculé automatiquement : 10/10 à 300 €, 5/10 à 900 €, 0/10 à 1 500 €. Prix chez un vendeur sûr à la date indiquée.",
  "how":"Boutiques officielles et grandes enseignes, relevés du 31/10/2026."},
 {"key":"fiabilite","short":"Fiabilité","label":"Fiabilité et SAV","weight":5,
  "explain":"Réputation du service après-vente en France, pièces détachées, et solidité des preuves (modèle testé par plusieurs labos ou pas du tout).",
  "how":"Retours SAV, nombre de tests indépendants concordants."},
]

def S(s, v, *src): return {"s": s, "v": v, "src": [{"label":a,"url":b} for a,b in src]}

P = []
def add(**k): P.append(k)

add(id="dreame-x60-pro", name="Dreame X60 Pro Ultra Complete", brand="Dreame", price=1499, target=1099,
 priceNote="1 499 € chez Dreame aujourd'hui. Déjà vu à 1 099 € en France et 899 € en Allemagne : attendre le Black Friday.",
 where=[{"shop":"Dreame FR","price":1499,"url":"https://fr.dreametech.com/"}],
 height=8.9, tags=["8,9 cm","Serpillières déposées","Matter","HA communautaire"],
 verdict="good", verdictText="Le plus complet sur les poils et les tapis, mais trop cher aujourd'hui.",
 pros=["Aucun cheveu enroulé, 10/10 partout chez smarthomeassistent","Aspire 89,5 g/100 dans un tapis épais","Dépose ses serpillières avant les tapis épais"],
 cons=["1 499 € : attendre ≤ 1 099 €","Lavelab : serpillières qui frottent un tapis, un petit tapis non détecté"],
 scores={
  "poils":S(10,"10/10 sur stratifié, tapis et tapis épais, aucun enroulement (smarthomeassistent). 100 % / 0 % sur le X60 Max (Vacuum Wars).",("smarthomeassistent",SHA+"dreame-x60-pro-ultra-complete-nachtest/"),("Vacuum Wars (X60 Max)",VW+"dreame-x60-max-ultra-complete-review/")),
  "tapis_mop":S(8,"Dépose automatique des serpillières sur tapis épais + relevage 21,5 mm. Lavelab : un petit tapis non détecté, serpillières qui frottent.",("Lavelab","https://lavelab.com/tests/dreame-x60-pro-ultra-complete/")),
  "tapis_asp":S(9,"89,5 g récupérés sur 100 g dans un tapis épais.",("smarthomeassistent",SHA+"dreame-x60-pro-ultra-complete-nachtest/")),
  "obstacles":S(8,"47/53 (smarthomeassistent).",("Lavelab","https://lavelab.com/tests/dreame-x60-pro-ultra-complete/")),
  "lavage":S(8,"Lavage à 100 °C, séchage à air chaud, détergent automatique, sac 3,2 L."),
  "hauteur":S(10,"8,9 cm laser rentré."),
  "domotique":S(7,"Home Assistant via l'extension communautaire Dreame (très complète). Google Home. Matter : oui."),
  "fiabilite":S(6,"Dreame : SAV France critiqué. Modèle bien testé (smarthomeassistent, Lavelab, Vacuum Wars)."),
 })

add(id="mova-v70", name="MOVA V70 Ultra Complete", brand="MOVA (Dreame)", price=949, target=849,
 priceNote="949 € sur la boutique MOVA. Vu à 849 € sur Amazon au Prime Day d'octobre.",
 where=[{"shop":"MOVA FR","price":949,"url":"https://fr.mova-tech.com/"}],
 height=8.8, tags=["8,8 cm","Serpillières déposées","Station sans sac","HA communautaire"],
 verdict="top", verdictText="Le meilleur sur les tapis épais, très bon sur les poils, et il dépose ses serpillières.",
 pros=["Meilleur score tapis épais testé : 93,4 g/100","0 % de cheveux enroulés, 94 % de poils (Vacuum Wars)","Obstacles 46/53","Station sans sac : pas de sacs à racheter"],
 cons=["Un point perdu pour des poils enroulés sur tapis épais (smarthomeassistent)","Eau de lavage mesurée bien sous les 100 °C annoncés","Matter non confirmé"],
 scores={
  "poils":S(8.5,"10 / 7,8 / 8,2 sur 10, un léger enroulement sur tapis épais (smarthomeassistent). 94 % de poils, 0 % d'enroulement (Vacuum Wars).",("smarthomeassistent",SHA+"mova-v70-ultra-complete/")),
  "tapis_mop":S(8.5,"Laisse ses serpillières à la station avant les tapis (smarthomeassistent). Navigation sur tapis 19,25/21.",("smarthomeassistent",SHA+"mova-v70-ultra-complete/")),
  "tapis_asp":S(9.5,"93,4 g/100 dans un tapis épais (meilleur score testé). 92 % en profondeur chez Vacuum Wars.",("smarthomeassistent",SHA+"mova-v70-ultra-complete/")),
  "obstacles":S(8,"46/53.",("smarthomeassistent",SHA+"mova-v70-ultra-complete/")),
  "lavage":S(7,"100 °C annoncés mais mesuré nettement en dessous. Station sans sac (cyclone)."),
  "hauteur":S(10,"8,8 cm laser rentré."),
  "domotique":S(5.5,"Home Assistant via l'extension communautaire (compte MovaHome). Google Home. Matter non confirmé."),
  "fiabilite":S(5,"MOVA = sous-marque récente de Dreame, SAV peu documenté. Un seul test complet."),
 })

add(id="dreame-matrix10-ultra", name="Dreame Matrix10 Ultra", brand="Dreame", price=649, target=649,
 priceNote="649 € chez Dreame (au lieu de 1 199 €).",
 where=[{"shop":"Dreame FR","price":649,"url":"https://fr.dreametech.com/"},{"shop":"Fnac","price":749,"url":"https://www.fnac.com/"}],
 height=8.9, tags=["8,9 cm","Serpillières déposées","Obstacles 53/53","Matter"],
 verdict="good", verdictText="Champion des obstacles, très bon prix, mais faible sur les tapis épais.",
 pros=["53/53 aux obstacles (parcours complet)","Dépose ses serpillières sur les tapis, capteur ultrasons","3 types de serpillières changées automatiquement"],
 cons=["Tapis épais : 0/10 sur les cheveux (enroulés) et 43 g/100 aspirés","Bon seulement si tes tapis sont ras ou moyens"],
 scores={
  "poils":S(7,"10/10 sur sol dur et tapis ras, mais 0/10 sur tapis épais avec enroulement (smarthomeassistent). 92 % chez Vacuum Wars.",("smarthomeassistent",SHA+"dreame-matrix10-ultra/"),("Vacuum Wars",VW+"dreame-matrix10-ultra-review/")),
  "tapis_mop":S(8.5,"Capteur ultrasons, relevage 10,5 mm, dépose automatique des serpillières sur tapis épais. Navigation 19/21.",("smarthomeassistent",SHA+"dreame-matrix10-ultra/")),
  "tapis_asp":S(5,"43,1 g/100 sur tapis épais ; 84 % en profondeur chez Vacuum Wars."),
  "obstacles":S(10,"53/53, parcours complet sans faute.",("smarthomeassistent",SHA+"dreame-matrix10-ultra/")),
  "lavage":S(8,"3 jeux de serpillières, 3 détergents, séchage DashDry."),
  "hauteur":S(10,"8,9 cm laser rentré."),
  "domotique":S(7,"Home Assistant via l'extension communautaire Dreame. Google Home. Matter : oui."),
  "fiabilite":S(6,"Dreame : SAV France critiqué. Bien testé."),
 })

add(id="dreame-x50", name="Dreame X50 Ultra Complete", brand="Dreame", price=599, target=599,
 priceNote="599 € chez Dreame (au lieu de 999 €). Reconditionné B3 vu à 349–399 € chez Cdiscount.",
 where=[{"shop":"Dreame FR","price":599,"url":"https://fr.dreametech.com/"}],
 height=8.9, tags=["8,9 cm","Serpillières déposées","Matter","⚠ obstacles"],
 verdict="meh", verdictText="Excellent sur les poils pour 599 €, mais moyen pour éviter les obstacles.",
 pros=["98 % de poils, 0 % d'enroulement (Vacuum Wars)","Aucun enroulement chez smarthomeassistent","599 € chez Dreame"],
 cons=["Obstacles moyens : 32/53","Tapis épais moyen : 56 g/100"],
 scores={
  "poils":S(9,"98 % / 0 % (Vacuum Wars). 10 / 10 / 6,4, aucun enroulement (smarthomeassistent).",("Vacuum Wars",VW+"dreame-x50-ultra-review-is-it-the-best-yet"),("smarthomeassistent","https://www.smarthomeassistent.de/dreame-x50-ultra-complete-test/")),
  "tapis_mop":S(7.5,"Relevage 10,5 mm, dépose automatique sur tapis épais, serpillières laissées en mode aspiration seule."),
  "tapis_asp":S(6,"56,2 g/100 sur tapis épais. Rtings : laisse des poils incrustés."),
  "obstacles":S(3,"32/53, le plus faible des Dreame haut de gamme.",("smarthomeassistent","https://www.smarthomeassistent.de/dreame-x50-ultra-complete-test/")),
  "lavage":S(7.5,"Lavage 80 °C, séchage, détergent, sac."),
  "hauteur":S(10,"8,9 cm laser rentré."),
  "domotique":S(7,"Home Assistant via l'extension communautaire Dreame. Google Home. Matter 1.4."),
  "fiabilite":S(6,"Dreame : SAV France critiqué. Modèle de 2025, bien testé."),
 })

add(id="mova-mobius60", name="MOVA Mobius 60", brand="MOVA (Dreame)", price=569, target=569,
 priceNote="569 € sur la boutique MOVA (au lieu de 1 199 €).",
 where=[{"shop":"MOVA FR","price":569,"url":"https://fr.mova-tech.com/"}],
 height=8.9, tags=["≈ 8,9 cm","Serpillières déposées","Peu testé"],
 verdict="meh", verdictText="Même base que le Matrix10, bon sur les poils, mais un seul test.",
 pros=["94 % de poils, enroulement « parfait » (Vacuum Wars)","Change et dépose ses serpillières"],
 cons=["Aucun test smarthomeassistent","Matter non confirmé"],
 scores={
  "poils":S(8,"94 % de poils, aucun enroulement (Vacuum Wars). Pas d'autre test.",("Vacuum Wars",VW+"mova-mobius-60-review/")),
  "tapis_mop":S(8,"Serpillières laissées à la base, relevage 10,5 mm (Vacuum Wars)."),
  "tapis_asp":S(7,"88 % en profondeur sur tapis (Vacuum Wars)."),
  "obstacles":S(6.5,"22/24 chez Vacuum Wars."),
  "lavage":S(7.5,"Lavage 100 °C, sac 3,2 L."),
  "hauteur":S(9.5,"Environ 8,9 cm (3,5 pouces)."),
  "domotique":S(5.5,"Home Assistant via l'extension communautaire. Google Home. Matter non confirmé."),
  "fiabilite":S(4.5,"Sous-marque récente, un seul test indépendant."),
 })

add(id="roborock-saros20", name="Roborock Saros 20", brand="Roborock", price=989, target=939,
 priceNote="989 € chez Darty (Saros 20X, date non visible). Vu à 939 €. Prix à confirmer avant achat.",
 where=[{"shop":"Darty (Saros 20X)","price":989,"url":"https://www.dealabs.com/bons-plans/robot-aspirateur-laveur-roborock-saros-20x-36-000-pa-adaptilift-30-starsight-20-station-rockdock-3353232"}],
 height=7.95, tags=["7,95 cm","Serpillières déposées","HA officiel","Matter"],
 verdict="top", verdictText="Le meilleur équilibre : poils, tapis, lavage des traces de pattes, et la meilleure domotique.",
 pros=["Serpillières laissées à la station ou relevées de 20 à 35 mm","Meilleur score de lavage chez Vacuum Wars (pattes boueuses)","Intégration Home Assistant officielle + Matter","7,95 cm, sans tourelle"],
 cons=["Petit bac (259 ml) : vidage fréquent en mue","Rtings : se prend dans les franges de tapis","88 % de poils, un peu moins que les meilleurs"],
 scores={
  "poils":S(8.5,"88 % de poils, 0 % d'enroulement (Vacuum Wars). 10 / 9,9 sur tapis (smarthomeassistent).",("Vacuum Wars",VW+"roborock-saros-20-review/"),("smarthomeassistent",SHA+"roborock-saros-20/")),
  "tapis_mop":S(8.5,"Serpillières laissées à la station (modes aspiration seule / tapis d'abord) ou relevées de 20 à 35 mm, châssis relevable. Franges : contourner par une zone interdite.",("Rtings","https://www.rtings.com/robot-vacuum/reviews/roborock/saros-20")),
  "tapis_asp":S(7,"81 / 71 sur 100 (tapis ras / épais).",("smarthomeassistent",SHA+"roborock-saros-20/")),
  "obstacles":S(7,"38,5/53 (smarthomeassistent), 17/24 (Vacuum Wars)."),
  "lavage":S(9,"Meilleur score de lavage du lot chez Vacuum Wars (25,2)."),
  "hauteur":S(10,"7,95 cm, pas de tourelle."),
  "domotique":S(9.5,"Intégration Home Assistant officielle (en partie locale), Google Home, Matter."),
  "fiabilite":S(8,"Roborock : meilleure réputation SAV et pièces en France. Bien testé."),
 })

add(id="roborock-saros20-neo", name="Roborock Saros 20 Neo", brand="Roborock", price=899, target=799,
 priceNote="899 € sur la boutique Roborock. Vu à 799 €.",
 where=[{"shop":"Roborock FR","price":899,"url":"https://fr.roborock.com/pages/roborock-saros-20-neo"}],
 height=7.98, tags=["7,98 cm","Serpillières déposées","HA officiel","Tapis épais"],
 verdict="good", verdictText="Même système de serpillières que le Saros 20, meilleur sur les tapis épais, moins testé.",
 pros=["Meilleure aspiration de tapis : 96 / 92 sur 100","Serpillières déposées à la station","HA officiel"],
 cons=["Pas de test Vacuum Wars","smarthomeassistent : gestion des serpillières sur tapis irrégulière d'un passage à l'autre"],
 scores={
  "poils":S(8,"10 / 8,7 sur tapis ras / épais (smarthomeassistent). Pas de test Vacuum Wars.",("smarthomeassistent",SHA+"roborock-saros-20-neo/")),
  "tapis_mop":S(7.5,"Dépose et relevage comme le Saros 20, mais comportement irrégulier en test."),
  "tapis_asp":S(9.5,"96 / 92 sur 100 (meilleur de Roborock).",("smarthomeassistent",SHA+"roborock-saros-20-neo/")),
  "obstacles":S(7.5,"41,5/53."),
  "lavage":S(7,"Lavage moyen chez smarthomeassistent, meilleur des Saros 20 chez netzwelt."),
  "hauteur":S(10,"7,98 cm laser rentré."),
  "domotique":S(9,"Home Assistant officiel, Google Home, Matter probable."),
  "fiabilite":S(7.5,"Roborock : bon SAV. Moins de tests que le Saros 20."),
 })

add(id="roborock-saros20-sonic", name="Roborock Saros 20 Sonic", brand="Roborock", price=899, target=899,
 priceNote="899 € sur la boutique Roborock (promo Black Friday anticipée).",
 where=[{"shop":"Roborock FR","price":899,"url":"https://fr.roborock.com/"}],
 height=8.0, tags=["8 cm","Serpillière déposée","HA officiel","Évite 47/53"],
 verdict="meh", verdictText="Excellent pour éviter les obstacles, plus faible sur les poils et le lavage.",
 pros=["47/53 aux obstacles, le meilleur des Roborock","Tapis : 92 / 86 sur 100"],
 cons=["78 % de poils seulement (Vacuum Wars)","Lavage faible chez Vacuum Wars (15,8)"],
 scores={
  "poils":S(7,"78 % de poils, 0 % d'enroulement (Vacuum Wars) ; 10 / 9,8 (smarthomeassistent).",("Vacuum Wars",VW+"roborock-saros-20-sonic-review/")),
  "tapis_mop":S(8,"Plaque vibrante relevée ou laissée à la station."),
  "tapis_asp":S(8.5,"92 / 86 sur 100.",("smarthomeassistent",SHA+"roborock-saros-20-sonic/")),
  "obstacles":S(8.5,"47/53, le meilleur des Roborock."),
  "lavage":S(6,"Score de lavage 15,8 chez Vacuum Wars, en dessous des autres."),
  "hauteur":S(10,"Environ 8 cm."),
  "domotique":S(9,"Home Assistant officiel, Google Home."),
  "fiabilite":S(7.5,"Roborock : bon SAV."),
 })

add(id="roborock-saros10r", name="Roborock Saros 10R", brand="Roborock", price=699, target=699,
 priceNote="699,99 € sur la boutique Roborock.",
 where=[{"shop":"Roborock FR","price":699.99,"url":"https://fr.roborock.com/"}],
 height=7.98, tags=["7,98 cm","Serpillières déposées","HA officiel","⚠ tapis"],
 verdict="meh", verdictText="Bonne domotique et bons obstacles, mais déçoit sur les poils dans les tapis.",
 pros=["44/53 aux obstacles","Serpillières déposées","HA officiel + Matter"],
 cons=["Rtings : 5/10 sur les poils d'animaux dans les tapis","Tapis épais : 7,5/10 sur les cheveux"],
 scores={
  "poils":S(6,"92 % chez Vacuum Wars, mais Rtings 5/10 (« décevant ») sur poils dans les tapis et 8,5 / 7,5 chez smarthomeassistent.",("Rtings","https://rtings.com/robot-vacuum/reviews/roborock/saros-10r")),
  "tapis_mop":S(8,"Serpillières déposées + relevage."),
  "tapis_asp":S(6,"80 / 66 sur 100."),
  "obstacles":S(8,"44/53."),
  "lavage":S(7,"Lavage correct."),
  "hauteur":S(10,"7,98 cm."),
  "domotique":S(9.5,"Home Assistant officiel, Google Home, Matter."),
  "fiabilite":S(7.5,"Roborock : bon SAV."),
 })

add(id="dreame-l40s-pro", name="Dreame L40s Pro Ultra", brand="Dreame", price=459, target=429,
 priceNote="459 € sur Amazon (offre Dealabs du 30/10). 429 € annoncé par Dreame pour le Black Friday.",
 where=[{"shop":"Amazon (vendu par Amazon)","price":459,"url":"https://www.amazon.fr/"}],
 height=10.35, tags=["10,35 cm ⚠","Serpillières déposées","Dealabs"],
 verdict="meh", verdictText="Bon prix, mais trop haut pour ton lit et faible sur les tapis épais.",
 pros=["459 €","Obstacles 42/53","Dépose ses serpillières"],
 cons=["10,35 cm : passe seulement si le lit dégage plus de 10,5 cm","Tapis épais : 23 g/100 aspirés, 5,4/10 sur les cheveux","Cartographie mal les tapis (navigation 12/21)"],
 scores={
  "poils":S(6.5,"8,9 (−1) / 10 / 5,4 (−1) sur 10 : enroulements sur stratifié et tapis épais (smarthomeassistent).",("smarthomeassistent",SHA+"dreame-l40s-pro-ultra/")),
  "tapis_mop":S(6,"Dépose automatique, mais repère mal les tapis et relève parfois les serpillières sans raison (12/21)."),
  "tapis_asp":S(3,"23,2 g/100 sur tapis épais."),
  "obstacles":S(7.5,"42/53."),
  "lavage":S(6.5,"75 °C annoncés, pas atteints en test."),
  "hauteur":S(3,"10,35 cm : à mesurer sous le lit."),
  "domotique":S(6,"Home Assistant via l'extension communautaire Dreame. Google Home."),
  "fiabilite":S(6,"Dreame : SAV France critiqué."),
 })

add(id="ecovacs-t50-gen3", name="Ecovacs Deebot T50 Pro Omni Gen3", brand="Ecovacs", price=399, target=299,
 priceNote="399 € chez Ecovacs et Boulanger. Vu à 299 € chez Boulanger et Fnac début octobre.",
 where=[{"shop":"Boulanger","price":399,"url":"https://www.boulanger.com/"},{"shop":"Ecovacs FR","price":399,"url":"https://www.ecovacs.com/fr/shop/deebot-robotic-vacuum-cleaner/deebot-t50-pro-omni-gen3-white"}],
 height=8.1, tags=["8,1 cm","Petit prix","Non testé"],
 verdict="meh", verdictText="Le moins cher qui passe sous le lit, mais aucun test de cette version.",
 pros=["299–399 €","8,1 cm","Caméra qui repère les taches et repasse"],
 cons=["Aucun test indépendant de la Gen3","Modèle proche : beaucoup de cheveux sur la brosse latérale","La 1re génération ratait des obstacles","Bac de 260 ml"],
 scores={
  "poils":S(6,"Non testé. Modèles proches : 86 % / 0 % (T50 Pro gen 1, Vacuum Wars) mais cheveux enroulés sur la brosse latérale (T50 Max Pro, smarthomeassistent).",("Vacuum Wars (T50 gen 1)",VW+"t50-max-pro-omni-and-t50-pro/")),
  "tapis_mop":S(5,"Relevage des serpillières, dépose non confirmée."),
  "tapis_asp":S(5,"Non testé (modèle proche : 6,8/10 sur tapis épais)."),
  "obstacles":S(4,"La 1re génération ratait des obstacles (Vacuum Wars). Vision Gen3 non testée."),
  "lavage":S(7,"75 °C, séchage 45 °C, détergent, repasse sur les taches."),
  "hauteur":S(10,"8,1 cm."),
  "domotique":S(5.5,"Home Assistant officiel depuis 2026.10.2 (sauf version Care Kit), pièces et carte non garanties. Google Home."),
  "fiabilite":S(4,"Aucun test de cette version ; Ecovacs : SAV mitigé."),
 })

add(id="ecovacs-x12s", name="Ecovacs Deebot X12S Pro Omni", brand="Ecovacs", price=999, target=999,
 priceNote="999 € chez Boulanger, Fnac et Amazon (offre d'octobre). Prendre la version Pro Omni (avec sac).",
 where=[{"shop":"Boulanger","price":999,"url":"https://www.boulanger.com/"}],
 height=9.8, tags=["9,8 cm","Rouleau laveur","Évite 53/53","⚠ tapis épais"],
 verdict="no", verdictText="Parfait sur les obstacles, mais bloqué 3 fois sur un tapis épais.",
 pros=["53/53 aux obstacles","Rouleau laveur, bon sur les traces"],
 cons=["Bloqué 3 fois sur tapis épais (0/100)","Version sans sac : poils de chien qui bouchent la station","9,8 cm, très juste"],
 scores={
  "poils":S(7,"10 / 6,2 sur tapis ras / épais (smarthomeassistent). 100 % / 0 % sur le X12 (Vacuum Wars).",("smarthomeassistent",SHA+"ecovacs-deebot-x12s-pro-omni/")),
  "tapis_mop":S(4,"Rouleau relevé de 15 mm + capot, mais fermeture du capot pas fiable en test."),
  "tapis_asp":S(2,"85 / 0 sur 100 : bloqué 3 fois sur tapis épais."),
  "obstacles":S(10,"53/53."),
  "lavage":S(8.5,"Rouleau laveur rincé en continu."),
  "hauteur":S(6,"9,8 cm : passe de justesse."),
  "domotique":S(6,"Home Assistant officiel (cloud), nouveaux modèles souvent incomplets. Google Home."),
  "fiabilite":S(5.5,"Ecovacs : SAV mitigé. Station sans sac bouchée par les poils (Vacuum Wars)."),
 })

add(id="narwal-flow2", name="Narwal Flow 2", brand="Narwal", price=935, target=935,
 priceNote="935 € sur la boutique Narwal (au lieu de 1 299 €).",
 where=[{"shop":"Narwal FR","price":935,"url":"https://fr.narwal.com/"}],
 height=9.5, tags=["9,5 cm","Rouleau laveur","⚠ tapis mouillés","⚠ obstacles"],
 verdict="no", verdictText="Très bon sur les poils, mais a mouillé les tapis en test.",
 pros=["0 % d'enroulement, 1er sur les poils chez The Hook Up","Rouleau laveur efficace"],
 cons=["A mouillé les tapis en test","Évitement d'obstacles moyen chez The Hook Up (3/6)","Ne dépose pas son rouleau"],
 scores={
  "poils":S(8.5,"0 % d'enroulement (Vacuum Wars), 100 % de poils chez The Hook Up.",("Vacuum Wars",VW+"narwal-flow-2-user-review/"),("The Hook Up","https://www.thesmarthomehookup.com/2026-ultimate-robot-vacuum-and-mop-comparison/")),
  "tapis_mop":S(3,"Rouleau relevé de 10 mm seulement ; a mouillé les tapis chez The Hook Up."),
  "tapis_asp":S(6,"84 % en profondeur ; tapis épais en 2 à 3 passages (Labo Maison)."),
  "obstacles":S(5,"3/6 chez The Hook Up, 20/24 chez Vacuum Wars."),
  "lavage":S(8.5,"Rouleau laveur, bon sur les traces."),
  "hauteur":S(7,"9,5 cm : passe de justesse."),
  "domotique":S(6,"Home Assistant via extension communautaire locale, Matter, Google Home via Matter."),
  "fiabilite":S(5,"Narwal : peu présent en France."),
 })

add(id="dreame-l50-ae", name="Dreame L50 Ultra AE", brand="Dreame", price=459, target=429,
 priceNote="459 € chez Dreame (offre Dealabs), 429 € chez Cdiscount.",
 where=[{"shop":"Dreame FR","price":459,"url":"https://fr.dreametech.com/"}],
 height=9.7, tags=["9,7 cm","Dealabs","⚠ cheveux"],
 verdict="no", verdictText="À éviter avec un chien : les cheveux s'emmêlent dans la brosse.",
 pros=["Prix","Lavage 100 °C"],
 cons=["« Beaucoup de cheveux emmêlés » : 2,1/10 sur tapis épais","16/53 aux obstacles"],
 scores={
  "poils":S(3,"6,4 / 8,8 / 2,1 sur 10, cheveux emmêlés dans la brosse TriCut.",("smarthomeassistent",SHA+"dreame-l50-ultra-ae/")),
  "tapis_mop":S(4,"Relevage 10,5 mm ; dépose annoncée mais non confirmée."),
  "tapis_asp":S(3.5,"36,9 g/100."),
  "obstacles":S(1,"16/53, le plus faible du lot."),
  "lavage":S(7,"100 °C."),
  "hauteur":S(7,"9,7 cm."),
  "domotique":S(7,"Extension communautaire Dreame, Google Home, Matter."),
  "fiabilite":S(5.5,"Dreame : SAV France critiqué."),
 })

add(id="roborock-qrevo-s-pro", name="Roborock Qrevo S Pro", brand="Roborock", price=379.99, target=349,
 priceNote="379,99 € sur la boutique Roborock (version blanche).",
 where=[{"shop":"Roborock FR","price":379.99,"url":"https://fr.roborock.com/"}],
 height=9.7, tags=["9,7 cm","HA officiel","Dealabs","⚠ poils"],
 verdict="no", verdictText="Bonne domotique pour pas cher, mais déconseillé avec des animaux.",
 pros=["379,99 €","HA officiel"],
 cons=["home&smart le déconseille avec des animaux","Pas de caméra : rate les câbles","Pas de dosage du détergent"],
 scores={
  "poils":S(4,"« Satisfaisant » sur les poils, en laisse sur les tapis (home&smart).",("home&smart","https://www.homeandsmart.de/roborock-qrevo-s-pro-18500-pa-saugkraft-test-0017-509669")),
  "tapis_mop":S(4,"Relevage 10 mm seulement."),
  "tapis_asp":S(4,"Moyen sur tapis."),
  "obstacles":S(2,"Pas de caméra."),
  "lavage":S(6,"75 °C, séchage 45 °C, pas de détergent auto."),
  "hauteur":S(7,"9,7 cm."),
  "domotique":S(8.5,"Home Assistant officiel, Google Home, pas de Matter."),
  "fiabilite":S(7,"Roborock : bon SAV."),
 })

project = {
 "slug":"robot", "order":2, "name":"Robot aspirateur laveur", "short":"Robot",
 "status":"Comparaison", "updated":"2026-10-31",
 "need":"Appartement de 70–100 m², chien à poils longs qui mue beaucoup, cheveux longs et frisés, tapis un peu partout, lit à environ 10 cm du sol, Home Assistant + Google Home. Budget repère : 400 € (pas éliminatoire).",
 "criteria":criteria,
 "presets":[
   {"label":"Priorité poils de chien","weights":{"poils":35,"tapis_mop":15,"tapis_asp":15,"obstacles":8,"lavage":9,"hauteur":6,"domotique":4,"prix":5,"fiabilite":3}},
   {"label":"Priorité prix","weights":{"poils":20,"tapis_mop":12,"tapis_asp":8,"obstacles":7,"lavage":8,"hauteur":6,"domotique":4,"prix":30,"fiabilite":5}},
   {"label":"Priorité domotique","weights":{"poils":22,"tapis_mop":13,"tapis_asp":8,"obstacles":8,"lavage":9,"hauteur":7,"domotique":20,"prix":8,"fiabilite":5}}
 ],
 "picks":[
   {"label":"Meilleur choix","product":"roborock-saros20","why":"Le meilleur équilibre : serpillières qui ne touchent jamais les tapis, très bon sur les poils, meilleur lavage, et la meilleure intégration Home Assistant."},
   {"label":"Meilleur sur tapis épais","product":"mova-v70","why":"Aspire le mieux les poils incrustés dans les tapis épais, dépose ses serpillières, station sans sac."},
   {"label":"Meilleur rapport qualité/prix","product":"dreame-matrix10-ultra","why":"649 €, champion des obstacles, dépose ses serpillières. Seulement si tes tapis sont ras ou moyens."},
 ],
 "rejects":[
   {"name":"Dreame Aqua10 Ultra Roller","reason":"50 % des cheveux longs enroulés (Vacuum Wars)."},
   {"name":"Dreame L50s Pro Ultra","reason":"Ne dépose pas ses serpillières, 2,4 g/100 sur tapis épais, 10,4 cm."},
   {"name":"Dreame L40 Ultra A / AE, L10s Ultra Gen 3","reason":"Brosse qui emmêle les cheveux, simple relevage des serpillières."},
   {"name":"Roborock Qrevo Curv 2 Flow","reason":"11,9 cm : ne passe pas sous le lit, bloqué sur tapis épais."},
   {"name":"Ecovacs T90 Pro / T90S","reason":"Bloqués sur tapis épais (0/100)."},
   {"name":"eufy Omni S2","reason":"A mouillé les tapis en test, 1 499 €."},
   {"name":"eufy E28 / S1 Pro","reason":"Rtings : inadapté aux propriétaires d'animaux ; 26 % d'enroulement."},
   {"name":"DJI Romo P / Romo 2","reason":"Cheveux longs qui pendent de l'aspiration, pas de Home Assistant."},
   {"name":"iRobot Roomba 705 Combo","reason":"Pas d'intégration Home Assistant, avenir de la marque incertain après la faillite."},
   {"name":"Xiaomi X20 Max","reason":"Gestion des cheveux faible (Vacuum Wars)."},
 ],
 "notes":[
   "Aucun test ne reproduit le sous-poil dense d'un chien à poils longs : le test « poils d'animaux » de Vacuum Wars est ce qui s'en rapproche le plus.",
   "Tous les bacs des robots font 230 à 320 ml : en période de mue, la station videra après chaque passage.",
   "Pour les dégâts mouillés du chien (pattes boueuses, eau de gamelle, croquettes trempées), un balai aspirateur laveur reste le bon outil : Tineco Floor One Stretch S6 (≤ 200 €) ou Roborock F25 XT (≈ 260 €).",
   "Prix relevés le 31/10/2026. Black Friday le 27/11 : les prix cibles sont indiqués sur chaque fiche.",
 ],
}
os.makedirs(OUT, exist_ok=True)
json.dump(project, open(os.path.join(OUT,"robot.project.json"),"w"), ensure_ascii=False, indent=1)
for p in P:
    json.dump(p, open(os.path.join(OUT, f"robot.{p['id']}.json"),"w"), ensure_ascii=False, indent=1)

# quick ranking
W = {c["key"]:c["weight"] for c in criteria}
def price_score(p): return max(0,min(10,10*(1500-p)/(1500-300)))
rows=[]
for p in P:
    tot=0
    for c in criteria:
        s = price_score(p["price"]) if c["key"]=="prix" else p["scores"][c["key"]]["s"]
        tot+=s*W[c["key"]]
    rows.append((round(tot/sum(W.values()),2),p["name"],p["price"]))
for r in sorted(rows,reverse=True): print(r)
