# Notation v2 (méthode validée le 2026-11-08) : barèmes fixes appliqués mécaniquement.
# Données : achats/2026-10-aspirateur-laveur/mesures.md et entretien-allergies.md (sources A et B uniquement).
import json, os, glob, statistics
OUT=os.path.join(os.path.dirname(__file__),"data")
VWU="https://vacuumwars.com/"; RT="https://www.rtings.com/robot-vacuum/reviews/"
THU="https://www.thesmarthomehookup.com/2026-ultimate-robot-vacuum-and-mop-comparison/"
EU="https://www.greenme.it/?p=1431832"

def g_pct(p):  return 10 if p>=95 else 8 if p>=90 else 6 if p>=85 else 4 if p>=80 else 2
def g_wrap(w): return 10 if w==0 else 7 if w<=10 else 4 if w<=30 else 1
def g_obs(n):  return 10 if n>=22 else 8 if n>=19 else 6 if n>=16 else 4 if n>=13 else 2
def g_stain(pts,avg):
    d=(pts-avg)/avg*100
    return 10 if d>=30 else 8 if d>=10 else 6 if d>-10 else 4 if d>-30 else 2
def g_mud(rank): return 9 if rank<=2 else 6 if rank<=5 else 3
def g_kit(eur): return 10 if eur<40 else 7 if eur<70 else 5 if eur<100 else 3
WORD={"excellent":10,"great":10,"very good":9,"good":8,"best":10,"decent":6,"adequate":6,"satisfactory":6,"alright":6,"fine":6,"isn't bad":6,"manageable":6,"reasonable":6,"pretty average":6,
      "passable":5,"acceptable":5,"won't be wowed":5,"several passes":5,"inconsistent":5,
      "mediocre":3,"sub-par":3,"disappointing":3,"poor":3,"lackluster":3,"limited":3,"many parts":3,"tricky":3,"more effort":3,"really struggled":3,"won't thoroughly clear":3,
      "performs poorly":2,"terrible":1,"gut":8}

# m = mesures : liste de (critère, libellé, note, source, url)
D={}
def M(rid,*items): D[rid]=list(items)
def vw(rid): return VWU
# --- Roborock
M("roborock-saros20",
 ("poils","Poils ramassés 88 % (Vacuum Wars, B)",g_pct(88),"Vacuum Wars (B)",VWU+"roborock-saros-20-review/"),
 ("poils","Cheveux 18 cm enroulés 0 % (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"roborock-saros-20-review/"),
 ("poils","Rtings (A) : « good » sur les poils dans les tapis",WORD["good"],"Rtings (A)",RT+"roborock/saros-20"),
 ("poils","The Hook Up (B) : enroulement « pretty average »",WORD["pretty average"],"The Hook Up (B)",THU),
 ("tapis_mop","Dépose ses serpillières (fabricant) : 10",10,"",""),
 ("tapis_mop","The Hook Up (B) : serpillières qui frottent le tapis : −3",-3,"The Hook Up (B)",THU),
 ("sale","Taches séchées 116 pts / moyenne 94 (Vacuum Wars, B)",g_stain(116,94),"Vacuum Wars (B)",VWU+"roborock-saros-20-review/"),
 ("sale","Boue séchée 4e sur 7 (The Hook Up, B)",g_mud(4),"The Hook Up (B)",THU),
 ("sale","Rtings (A) : « fine for everyday messes »",WORD["fine"],"Rtings (A)",RT+"roborock/saros-20"),
 ("tapis_asp","Nettoyage profond tapis 89 % (Vacuum Wars, B)",g_pct(89),"Vacuum Wars (B)",VWU+"roborock-saros-20-review/"),
 ("tapis_asp","Rtings (A) : tapis « decent »",WORD["decent"],"Rtings (A)",RT+"roborock/saros-20"),
 ("entretien","Rtings (A) : la station fait l'essentiel (« takes care of most »)",WORD["good"],"Rtings (A)",RT+"roborock/saros-20"),
 ("entretien","Kit pièces 1 an : 89,99 € (officiel, Amazon.fr)",g_kit(89.99),"",""),
 ("obstacles","Obstacles 17/24 (Vacuum Wars, B)",g_obs(17),"Vacuum Wars (B)",VWU+"roborock-saros-20-review/"),
 ("obstacles","Rtings (A) : « inconsistent »",WORD["inconsistent"],"Rtings (A)",RT+"roborock/saros-20"))
M("roborock-saros20-neo",
 ("poils","Poils ramassés 87,5 % (Vacuum Wars, B ; Qrevo Edge 3 Pro = même robot)",g_pct(87.5),"Vacuum Wars (B)",VWU+"roborock-qrevo-edge-3-pro-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"roborock-qrevo-edge-3-pro-review/"),
 ("tapis_mop","Dépose ses serpillières (fabricant)",10,"",""),
 ("sale","Taches séchées 115 pts / moyenne 107,8 (Vacuum Wars, B)",g_stain(115,107.8),"Vacuum Wars (B)",VWU+"roborock-qrevo-edge-3-pro-review/"),
 ("tapis_asp","Nettoyage profond tapis 93 % (Vacuum Wars, B)",g_pct(93),"Vacuum Wars (B)",VWU+"roborock-qrevo-edge-3-pro-review/"),
 ("obstacles","Obstacles 18/24 (Vacuum Wars, B)",g_obs(18),"Vacuum Wars (B)",VWU+"roborock-qrevo-edge-3-pro-review/"))
M("roborock-saros20-sonic",
 ("poils","Poils ramassés 78 % (Vacuum Wars, B)",g_pct(78),"Vacuum Wars (B)",VWU+"roborock-saros-20-sonic-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"roborock-saros-20-sonic-review/"),
 ("tapis_mop","Plaque laissée à la station (fabricant)",10,"",""),
 ("sale","Taches séchées 62 pts / moyenne 108 (Vacuum Wars, B)",g_stain(62,108),"Vacuum Wars (B)",VWU+"roborock-saros-20-sonic-review/"),
 ("tapis_asp","Nettoyage profond tapis 92 % (Vacuum Wars, B)",g_pct(92),"Vacuum Wars (B)",VWU+"roborock-saros-20-sonic-review/"),
 ("obstacles","Obstacles 19/24 (Vacuum Wars, B)",g_obs(19),"Vacuum Wars (B)",VWU+"roborock-saros-20-sonic-review/"))
M("roborock-saros10r",
 ("poils","Poils ramassés 92 % (Vacuum Wars, B)",g_pct(92),"Vacuum Wars (B)",VWU+"roborock-saros-10r-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"roborock-saros-10r-review/"),
 ("poils","Rtings (A) : « disappointing »",WORD["disappointing"],"Rtings (A)",RT+"roborock/saros-10r"),
 ("poils","Bouchage par les cheveux entre les brosses (Vacuum Wars, B) : −2",-2,"Vacuum Wars (B)",VWU+"roborock-saros-10r-common-problems-and-fixes/"),
 ("tapis_mop","Dépose ses serpillières (fabricant)",10,"",""),
 ("sale","Taches séchées 103 pts / moyenne 98 (Vacuum Wars, B)",g_stain(103,98),"Vacuum Wars (B)",VWU+"roborock-saros-10r-review/"),
 ("sale","Rtings (A) : « great mopping performance »",WORD["great"],"Rtings (A)",RT+"roborock/saros-10r"),
 ("tapis_asp","Nettoyage profond tapis 80 % (Vacuum Wars, B)",g_pct(80),"Vacuum Wars (B)",VWU+"roborock-saros-10r-review/"),
 ("tapis_asp","Rtings (A) : tapis « adequate »",WORD["adequate"],"Rtings (A)",RT+"roborock/saros-10r"),
 ("entretien","Rtings (A) : entretien « reasonable »",WORD["reasonable"],"Rtings (A)",RT+"roborock/saros-10r"),
 ("entretien","Kit pièces 1 an : 89,99 € (officiel FR, en rupture)",g_kit(89.99),"",""),
 ("obstacles","Obstacles 24/24 (Vacuum Wars, B)",g_obs(24),"Vacuum Wars (B)",VWU+"roborock-saros-10r-review/"),
 ("obstacles","Rtings (A) : « very good »",WORD["very good"],"Rtings (A)",RT+"roborock/saros-10r"))
M("roborock-qrevo-s-pro",
 ("poils","Poils ramassés 43 % (Vacuum Wars, B)",g_pct(43),"Vacuum Wars (B)",VWU+"roborock-qrevo-s-pro-review/"),
 ("poils","Cheveux enroulés 62 % (Vacuum Wars, B)",g_wrap(62),"Vacuum Wars (B)",VWU+"roborock-qrevo-s-pro-review/"),
 ("poils","Rtings (A, Qrevo S proche) : « disappointing »",WORD["disappointing"],"Rtings (A)",RT+"roborock/qrevo-s"),
 ("tapis_mop","Relevage 10 mm (fabricant)",5,"",""),
 ("sale","Taches séchées 149 pts / moyenne 108 (Vacuum Wars, B)",g_stain(149,108),"Vacuum Wars (B)",VWU+"roborock-qrevo-s-pro-review/"),
 ("sale","Rtings (A, Qrevo S) : lavage « very effective »",WORD["very good"],"Rtings (A)",RT+"roborock/qrevo-s"),
 ("tapis_asp","Nettoyage profond tapis 81 % (Vacuum Wars, B)",g_pct(81),"Vacuum Wars (B)",VWU+"roborock-qrevo-s-pro-review/"),
 ("tapis_asp","Rtings (A, Qrevo S) : tapis « isn't bad »",WORD["isn't bad"],"Rtings (A)",RT+"roborock/qrevo-s"),
 ("entretien","Rtings (A, Qrevo S) : « many parts », coûts récurrents élevés",WORD["many parts"],"Rtings (A)",RT+"roborock/qrevo-s"),
 ("obstacles","Obstacles 5/24 (Vacuum Wars, B)",g_obs(5),"Vacuum Wars (B)",VWU+"roborock-qrevo-s-pro-review/"),
 ("obstacles","Rtings (A, Qrevo S) : « terrible »",WORD["terrible"],"Rtings (A)",RT+"roborock/qrevo-s"))
M("roborock-saros20-flow")
# --- Dreame
MX=[("poils","Poils ramassés 92 % (Vacuum Wars, B)",g_pct(92),"Vacuum Wars (B)",VWU+"dreame-matrix10-ultra-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"dreame-matrix10-ultra-review/"),
 ("tapis_mop","Dépose ses serpillières sur tapis (fabricant)",10,"",""),
 ("sale","Taches séchées 136 pts / moyenne 112 (Vacuum Wars, B)",g_stain(136,112),"Vacuum Wars (B)",VWU+"dreame-matrix10-ultra-review/"),
 ("sale","Nouveau test taches 147 pts / moyenne 98 (Vacuum Wars, B)",g_stain(147,98),"Vacuum Wars (B)",VWU+"mova-mobius-60-review/"),
 ("tapis_asp","Nettoyage profond tapis 80 % (Vacuum Wars, B ; 84 % sur une autre page)",g_pct(80),"Vacuum Wars (B)",VWU+"dreame-matrix10-ultra-review/"),
 ("entretien","Kit pièces 1 an : 139,99 € (Dreame FR)",g_kit(139.99),"",""),
 ("obstacles","Obstacles 19/24 (Vacuum Wars, B)",g_obs(19),"Vacuum Wars (B)",VWU+"dreame-matrix10-ultra-review/")]
M("dreame-matrix10-ultra",*MX)
M("dreame-matrix10-pro",*[(c,l+" — données du Matrix10 Ultra (modèle proche)" if s>0 and u else l,s,src,u) for c,l,s,src,u in MX])
M("dreame-x50",
 ("poils","Poils ramassés 98 % (Vacuum Wars, B)",g_pct(98),"Vacuum Wars (B)",VWU+"dreame-x50-ultra-review-is-it-the-best-yet/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"dreame-x50-ultra-review-is-it-the-best-yet/"),
 ("poils","Rtings (A) : poils « acceptable »",WORD["acceptable"],"Rtings (A)",RT+"dreame/x50-ultra"),
 ("poils","Stiftung Warentest (A, via résumé) : « gut bei langen Haaren »",WORD["gut"],"Stiftung Warentest (A)","https://www.test.de/Saugroboter-im-Test-4806685-0/"),
 ("poils","Bouchage par les cheveux, bac et station (Vacuum Wars, B) : −2",-2,"Vacuum Wars (B)",VWU+"dreame-x50-ultra-robot-vacuum-common-complaints-and-how-to-fix-them/"),
 ("tapis_mop","Dépose ses serpillières sur tapis épais (fabricant)",10,"",""),
 ("sale","Taches séchées 80 pts / moyenne 94 (Vacuum Wars, B)",g_stain(80,94),"Vacuum Wars (B)",VWU+"dreame-x50-ultra-review-is-it-the-best-yet/"),
 ("sale","Rtings (A) : « mediocre on stains »",WORD["mediocre"],"Rtings (A)",RT+"dreame/x50-ultra"),
 ("tapis_asp","Nettoyage profond tapis 83 % (Vacuum Wars, B)",g_pct(83),"Vacuum Wars (B)",VWU+"dreame-x50-ultra-review-is-it-the-best-yet/"),
 ("tapis_asp","Rtings (A) : tapis « satisfactory »",WORD["satisfactory"],"Rtings (A)",RT+"dreame/x50-ultra"),
 ("entretien","Rtings (A) : la station fait l'essentiel",WORD["good"],"Rtings (A)",RT+"dreame/x50-ultra"),
 ("entretien","Kit pièces 1 an : 139,99 € (Dreame FR, Boulanger)",g_kit(139.99),"",""),
 ("obstacles","Obstacles 20/24 (Vacuum Wars, B)",g_obs(20),"Vacuum Wars (B)",VWU+"dreame-x50-ultra-review-is-it-the-best-yet/"),
 ("obstacles","Rtings (A) : « great »",WORD["great"],"Rtings (A)",RT+"dreame/x50-ultra"))
M("dreame-x60-pro",
 ("poils","Poils ramassés 100 % (Vacuum Wars, B, X60 Max proche)",g_pct(100),"Vacuum Wars (B)",VWU+"dreame-x60-max-ultra-complete-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B, X60 Max)",g_wrap(0),"Vacuum Wars (B)",VWU+"dreame-x60-max-ultra-complete-review/"),
 ("poils","Rtings (A, X60 Max) : « passable »",WORD["passable"],"Rtings (A)",RT+"dreame/x60-max-ultra-complete"),
 ("poils","The Hook Up (B, X60 Max) : « pretty average »",WORD["pretty average"],"The Hook Up (B)",THU),
 ("tapis_mop","Dépose ses serpillières sur tapis épais (fabricant)",10,"",""),
 ("tapis_mop","The Hook Up (B, X60 Max) : serpillières qui frottent le tapis : −3",-3,"The Hook Up (B)",THU),
 ("sale","Taches séchées 136 pts / moyenne 93 (Vacuum Wars, B, X60 Max)",g_stain(136,93),"Vacuum Wars (B)",VWU+"dreame-x60-max-ultra-complete-review/"),
 ("sale","Boue séchée 7e sur 7 (The Hook Up, B, X60 Max)",g_mud(7),"The Hook Up (B)",THU),
 ("sale","Rtings (A, X60 Max) : « won't be wowed »",WORD["won't be wowed"],"Rtings (A)",RT+"dreame/x60-max-ultra-complete"),
 ("tapis_asp","Nettoyage profond tapis 89 % (Vacuum Wars, B, X60 Max)",g_pct(89),"Vacuum Wars (B)",VWU+"dreame-x60-max-ultra-complete-review/"),
 ("tapis_asp","Rtings (A, X60 Max) : « good choice for carpeted homes »",WORD["good"],"Rtings (A)",RT+"dreame/x60-max-ultra-complete"),
 ("entretien","Rtings (A, X60 Max) : la station fait l'essentiel",WORD["good"],"Rtings (A)",RT+"dreame/x60-max-ultra-complete"),
 ("obstacles","Obstacles 22/24 (Vacuum Wars, B, X60 Max)",g_obs(22),"Vacuum Wars (B)",VWU+"dreame-x60-max-ultra-complete-review/"),
 ("obstacles","Rtings (A, X60 Max) : « very good »",WORD["very good"],"Rtings (A)",RT+"dreame/x60-max-ultra-complete"))
M("dreame-l40s-pro",
 ("poils","Poils ramassés 91 % (Vacuum Wars, B, L40s Ultra proche)",g_pct(91),"Vacuum Wars (B)",VWU+"dreame-l40s-series-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B, L40s Ultra)",g_wrap(0),"Vacuum Wars (B)",VWU+"dreame-l40s-series-review/"),
 ("poils","Rtings (A, L40 Ultra proche) : « poor job »",WORD["poor"],"Rtings (A)","https://www.rtings.com/robot-vacuum/reviews/dreame/l40-ultra"),
 ("tapis_mop","Dépose ses serpillières (fabricant)",10,"",""),
 ("sale","Rtings (A, L40 Ultra) : lavage « acceptable »",WORD["acceptable"],"Rtings (A)","https://www.rtings.com/robot-vacuum/reviews/dreame/l40-ultra"),
 ("tapis_asp","Nettoyage profond tapis 92 % (Vacuum Wars, B, L40s Ultra)",g_pct(92),"Vacuum Wars (B)",VWU+"dreame-l40s-series-review/"),
 ("tapis_asp","Rtings (A, L40 Ultra) : tapis « alright »",WORD["alright"],"Rtings (A)","https://www.rtings.com/robot-vacuum/reviews/dreame/l40-ultra"),
 ("entretien","Rtings (A, L40 Ultra) : « many parts », coûts récurrents élevés",WORD["many parts"],"Rtings (A)","https://www.rtings.com/robot-vacuum/reviews/dreame/l40-ultra"),
 ("entretien","Kit pièces 1 an : 139,99 € (Dreame FR, Boulanger)",g_kit(139.99),"",""),
 ("obstacles","Obstacles 7/24 (Vacuum Wars, B, L40s Ultra)",g_obs(7),"Vacuum Wars (B)",VWU+"dreame-l40s-series-review/"),
 ("obstacles","Rtings (A, L40 Ultra) : « good »",WORD["good"],"Rtings (A)","https://www.rtings.com/robot-vacuum/reviews/dreame/l40-ultra"))
M("dreame-l50-ae",
 ("poils","Poils ramassés 100 % (Vacuum Wars, B, L50 Ultra proche)",g_pct(100),"Vacuum Wars (B)",VWU+"dreame-l50-ultra-robot-vacuum-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B, L50 Ultra)",g_wrap(0),"Vacuum Wars (B)",VWU+"dreame-matrix10-ultra-review/"),
 ("poils","Rtings (A, L50 Ultra) : « mediocre »",WORD["mediocre"],"Rtings (A)",RT+"dreame/l50-ultra"),
 ("poils","Bouchage par les poils chaque semaine, 3 mois (Vacuum Wars, B, L50 Ultra) : −2",-2,"Vacuum Wars (B)",VWU+"dreame-l50-ultra-robot-vacuum-review/"),
 ("tapis_mop","Relevage 10,5 mm (fabricant ; dépose non confirmée)",5,"",""),
 ("sale","Rtings (A, L50 Ultra) : taches « limited »",WORD["limited"],"Rtings (A)",RT+"dreame/l50-ultra"),
 ("tapis_asp","Nettoyage profond tapis 90 % (Vacuum Wars, B, L50 Ultra)",g_pct(90),"Vacuum Wars (B)",VWU+"dreame-l50-ultra-robot-vacuum-review/"),
 ("tapis_asp","Rtings (A, L50 Ultra) : tapis « adequate »",WORD["adequate"],"Rtings (A)",RT+"dreame/l50-ultra"),
 ("entretien","Rtings (A, L50 Ultra) : entretien « manageable »",WORD["manageable"],"Rtings (A)",RT+"dreame/l50-ultra"),
 ("obstacles","Pas de caméra sur l'AE (fabricant) : plafond 3",3,"",""))
# --- MOVA
M("mova-v70",
 ("poils","Poils ramassés 94 % (Vacuum Wars, B)",g_pct(94),"Vacuum Wars (B)",VWU+"mova-v70-ultra-complete-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"mova-v70-ultra-complete-review/"),
 ("tapis_mop","Dépose ses serpillières avant les tapis (fabricant)",10,"",""),
 ("sale","Taches café 100 pts / moyenne 94 (Vacuum Wars, B)",g_stain(100,94),"Vacuum Wars (B)",VWU+"mova-v70-ultra-complete-review/"),
 ("sale","Taches café + raisin 133 pts / moyenne 108 (Vacuum Wars, B)",g_stain(133,108),"Vacuum Wars (B)",VWU+"mova-v70-ultra-complete-review/"),
 ("tapis_asp","Nettoyage profond tapis 92 % (Vacuum Wars, B)",g_pct(92),"Vacuum Wars (B)",VWU+"mova-v70-ultra-complete-review/"),
 ("allergies","Station sans sac : −2 (fabricant)",-2,"",""),
 ("obstacles","Obstacles 23/24 (Vacuum Wars, B)",g_obs(23),"Vacuum Wars (B)",VWU+"mova-v70-ultra-complete-review/"))
M("mova-mobius60",
 ("poils","Poils ramassés 94 % (Vacuum Wars, B)",g_pct(94),"Vacuum Wars (B)",VWU+"mova-mobius-60-review/"),
 ("poils","Enroulement : « perfect score » (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"mova-mobius-60-review/"),
 ("poils","Rtings (A) : « sub-par »",WORD["sub-par"],"Rtings (A)",RT+"mova/mobius-60"),
 ("poils","The Hook Up (B) : boule de cheveux dans le logement de roue",4,"The Hook Up (B)",THU),
 ("tapis_mop","Dépose ses serpillières (fabricant)",10,"",""),
 ("tapis_mop","The Hook Up (B) : serpillières qui frottent le tapis : −3",-3,"The Hook Up (B)",THU),
 ("sale","Taches 98 pts / moyenne 112 (Vacuum Wars, B)",g_stain(98,112),"Vacuum Wars (B)",VWU+"mova-mobius-60-review/"),
 ("sale","Nouveau test taches 89 pts / moyenne 98 (Vacuum Wars, B)",g_stain(89,98),"Vacuum Wars (B)",VWU+"mova-mobius-60-review/"),
 ("sale","Boue séchée 6e sur 7 (The Hook Up, B)",g_mud(6),"The Hook Up (B)",THU),
 ("sale","Rtings (A) : « won't thoroughly clear stains »",WORD["won't thoroughly clear"],"Rtings (A)",RT+"mova/mobius-60"),
 ("tapis_asp","Nettoyage profond tapis 88 % (Vacuum Wars, B)",g_pct(88),"Vacuum Wars (B)",VWU+"mova-mobius-60-review/"),
 ("tapis_asp","Rtings (A) : tapis « mediocre »",WORD["mediocre"],"Rtings (A)",RT+"mova/mobius-60"),
 ("entretien","Rtings (A) : « more effort than you might like »",WORD["more effort"],"Rtings (A)",RT+"mova/mobius-60"),
 ("obstacles","Obstacles 22/24 (Vacuum Wars, B)",g_obs(22),"Vacuum Wars (B)",VWU+"mova-mobius-60-review/"),
 ("obstacles","Rtings (A) : « great »",WORD["great"],"Rtings (A)",RT+"mova/mobius-60"))
# --- Ecovacs
M("ecovacs-t50-gen3",
 ("poils","Poils ramassés 86 % (Vacuum Wars, B, T50 Pro Omni proche)",g_pct(86),"Vacuum Wars (B)",VWU+"t50-max-pro-omni-and-t50-pro/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B, T50 Pro)",g_wrap(0),"Vacuum Wars (B)",VWU+"t50-max-pro-omni-and-t50-pro/"),
 ("sale","Taches 170 pts / moyenne 98 (Vacuum Wars, B, T50 Pro)",g_stain(170,98),"Vacuum Wars (B)",VWU+"t50-max-pro-omni-and-t50-pro/"),
 ("tapis_asp","Nettoyage profond tapis 79 % (Vacuum Wars, B, T50 Pro)",g_pct(79),"Vacuum Wars (B)",VWU+"t50-max-pro-omni-and-t50-pro/"),
 ("entretien","Pièces : 79 € le kit 6 mois, soit 158 €/an (Ecovacs FR)",g_kit(158),"",""),
 ("obstacles","Obstacles 15/24 (Vacuum Wars, B, T50 Pro)",g_obs(15),"Vacuum Wars (B)",VWU+"t50-max-pro-omni-and-t50-pro/"))
M("ecovacs-x12s",
 ("poils","Poils ramassés 100 % (Vacuum Wars, B, X12 proche)",g_pct(100),"Vacuum Wars (B)",VWU+"ecovacs-x12-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B, X12)",g_wrap(0),"Vacuum Wars (B)",VWU+"ecovacs-x12-review/"),
 ("poils","The Hook Up (B, X12) : « really struggled », amas derrière le rouleau",WORD["really struggled"],"The Hook Up (B)",THU),
 ("poils","Bouchage par les poils (The Hook Up et Vacuum Wars, B) : −2",-2,"Vacuum Wars (B)",VWU+"ecovacs-x12-omnicyclone-long-term-review/"),
 ("tapis_mop","Rouleau relevé de 15 mm + capot (fabricant)",5,"",""),
 ("tapis_mop","The Hook Up (B, X12) : tapis mouillés : −3",-3,"The Hook Up (B)",THU),
 ("sale","Taches 112 pts / moyenne 108 (Vacuum Wars, B, X12)",g_stain(112,108),"Vacuum Wars (B)",VWU+"ecovacs-x12-review/"),
 ("sale","Boue séchée 5e sur 7 (The Hook Up, B, X12)",g_mud(5),"The Hook Up (B)",THU),
 ("tapis_asp","Nettoyage profond tapis 76 % (Vacuum Wars, B, X12)",g_pct(76),"Vacuum Wars (B)",VWU+"ecovacs-x12-review/"),
 ("obstacles","Obstacles 23/24 (Vacuum Wars, B, X12)",g_obs(23),"Vacuum Wars (B)",VWU+"ecovacs-x12-review/"))
# --- Narwal
M("narwal-flow2",
 ("poils","Poils ramassés 88 % (Vacuum Wars, B)",g_pct(88),"Vacuum Wars (B)",VWU+"narwal-flow-2-review/"),
 ("poils","Cheveux enroulés 0 % (Vacuum Wars, B)",g_wrap(0),"Vacuum Wars (B)",VWU+"narwal-flow-2-review/"),
 ("poils","Rtings (A) : « mediocre »",WORD["mediocre"],"Rtings (A)",RT+"narwal/flow-2"),
 ("poils","The Hook Up (B) : meilleur du test, aucun emmêlement",WORD["best"],"The Hook Up (B)",THU),
 ("tapis_mop","Rouleau sans capot, relevage limité (fabricant)",5,"",""),
 ("tapis_mop","The Hook Up (B) : tapis mouillés : −3",-3,"The Hook Up (B)",THU),
 ("sale","Boue séchée 2e sur 7 (The Hook Up, B)",g_mud(2),"The Hook Up (B)",THU),
 ("sale","Rtings (A) : « several passes for tough stains »",WORD["several passes"],"Rtings (A)",RT+"narwal/flow-2"),
 ("tapis_asp","Nettoyage profond tapis 84 % (Vacuum Wars, B)",g_pct(84),"Vacuum Wars (B)",VWU+"narwal-flow-2-review/"),
 ("tapis_asp","Rtings (A) : « performs poorly on carpet »",WORD["performs poorly"],"Rtings (A)",RT+"narwal/flow-2"),
 ("entretien","Rtings (A) : « tricky », beaucoup de pièces",WORD["tricky"],"Rtings (A)",RT+"narwal/flow-2"),
 ("entretien","Kit pièces : 139,99 € (Narwal, sans sacs)",g_kit(139.99),"",""),
 ("obstacles","Obstacles 20/24 (Vacuum Wars, B)",g_obs(20),"Vacuum Wars (B)",VWU+"narwal-flow-2-review/"),
 ("obstacles","Rtings (A) : « good »",WORD["good"],"Rtings (A)",RT+"narwal/flow-2"))

# Critères par marque (faits)
BRAND={"Roborock":dict(fiab=(8.3,"Fiabilité Roborock 83/100 (Euroconsumers 2026, A)"),dom=(10,"Home Assistant : intégration officielle"),allerg=(3,"Filtre lavable, pas de classe HEPA annoncée (fabricant)")),
       "Dreame":dict(fiab=(9.6,"Fiabilité Dreame 96/100 (Euroconsumers 2026, A)"),dom=(8,"Google Home natif (voix + routines) ; Home Assistant seulement via extension non officielle"),allerg=(6,"Filtre « HEPA » sans classe (fabricant)")),
       "MOVA (Dreame)":dict(fiab=None,dom=(6,"Home Assistant via extension non officielle ; Google Home non vérifié"),allerg=None),
       "Ecovacs":dict(fiab=(7.5,"Fiabilité Ecovacs 75/100 (Euroconsumers 2026, A)"),dom=(10,"Home Assistant : intégration officielle (cloud, nouveaux modèles parfois incomplets)"),allerg=(3,"Filtre « haute efficacité », pas de classe HEPA (fabricant)")),
       "TP-Link Tapo":dict(fiab=None,dom=(6,"Matter / Home Assistant non vérifiés pour ce modèle"),allerg=None),
       "Narwal":dict(fiab=None,dom=(8,"Google Home via Matter ; Home Assistant via extension non officielle"),allerg=(6,"Filtre « HEPA » sans classe (fabricant)"))}
CRIT=[("poils","Poils","Poils et cheveux",25,"Ramassés, sans s'emmêler ni boucher l'aspiration."),
 ("tapis_mop","Tapis au sec","Tapis au sec",15,"Les serpillières ne touchent jamais les tapis."),
 ("sale","Sol sale","Sol très sale",15,"Boue, taches séchées. Les aliments ramollis (croquettes) ne sont testés par aucun labo sur robot."),
 ("tapis_asp","Tapis épais","Poils incrustés dans les tapis",12,"Extraire les poils coincés dans un tapis."),
 ("entretien","Entretien","Entretien facile, pièces abordables",10,"Facile à nettoyer, rarement, pièces de rechange disponibles et pas trop chères."),
 ("allergies","Allergies","Allergies et acariens",8,"Filtre HEPA certifié, station à sac fermé. Aucun fabricant n'annonce de HEPA certifié H12/H13 ; aucune mesure d'émission de poussière publique."),
 ("fiabilite","Fiabilité","Fiabilité de la marque",8,"Enquête indépendante auprès des propriétaires (Euroconsumers 2026)."),
 ("domotique","Domotique","Home Assistant ou Google Home",7,"Home Assistant officiel = 10 ; Google Home réellement connecté = 8 ; extension non officielle = 6."),
 ("obstacles","Obstacles","Évite les obstacles",7,"Parcours Vacuum Wars de 24 objets (câbles, tissus, chaussures, jouets, excréments factices), verdicts Rtings.")]
GRID={c[0]:"" for c in CRIT}
for f in ["../achats/2026-10-aspirateur-laveur/methode.md"]: pass

def r1(x): return round(x*2)/2  # au demi-point
for path in sorted(glob.glob(os.path.join(OUT,"robot.*.json"))):
    if path.endswith(".project.json"): continue
    p=json.load(open(path)); rid=p["id"]; items=D.get(rid,[]); b=BRAND.get(p["brand"],{})
    sc={}
    for key,*_ in CRIT:
        base=[(l,s,src,u) for c,l,s,src,u in items if c==key and s>0]
        mal=[(l,s,src,u) for c,l,s,src,u in items if c==key and s<0]
        val=None; parts=[]; vwonly=False
        if key=="fiabilite" and b.get("fiab"): val=b["fiab"][0]; parts=[(b["fiab"][1],val,"Euroconsumers (A)",EU)]
        elif key=="domotique" and b.get("dom"): val=b["dom"][0]; parts=[(b["dom"][1],val,"","")]
        elif key=="allergies":
            if b.get("allerg"): val=b["allerg"][0]; parts=[(b["allerg"][1],val,"","")]
            if mal and val is not None: val=max(0,val+sum(m[1] for m in mal)); parts+=mal
        elif base:
            wts=[(0.5 if src.startswith("Vacuum Wars") else 1.0) for _,_,src,_ in base]
            val=sum(s*wt for (_,s,_,_),wt in zip(base,wts))/sum(wts)+sum(m[1] for m in mal); val=max(0,min(10,val)); parts=base+mal
            vwonly=all(src.startswith("Vacuum Wars") for _,_,src,_ in base)
        if val is None:
            sc[key]={"s":None,"v":"Non mesuré : aucune donnée A ou B, critère retiré du calcul.","src":[]}
        else:
            txt=" ; ".join(f"{l} → {('+' if s>0 and l.startswith('Bouch') else '')}{str(s).replace('.',',')}" for l,s,_,_ in parts)
            if len(base)>1: txt+=f". Moyenne (Vacuum Wars compte à moitié) : {str(round(val,1)).replace('.',',')}"
            src=[{"label":srcl,"url":u} for _,_,srcl,u in parts if u]
            seen=set(); src=[x for x in src if not (x["url"] in seen or seen.add(x["url"]))]
            if vwonly: txt+=". Repose sur Vacuum Wars seul (compte à moitié dans la couverture)"
            if p["brand"] in ("Roborock","Ecovacs") and any(src.startswith("Vacuum Wars") for _,_,src,_ in parts): txt+=". ⚠ Conflit d'intérêts : Vacuum Wars a fait du conseil pour "+p["brand"]
            SIB={"dreame-x60-pro","dreame-l40s-pro","dreame-l50-ae","ecovacs-t50-gen3","ecovacs-x12s","dreame-matrix10-pro"}
            conf=(0.5 if vwonly else 1)*(0.5 if rid in SIB and key not in ("fiabilite","domotique","allergies") else 1)
            if rid in SIB and key not in ("fiabilite","domotique","allergies"): txt+=". Mesures d'un modèle proche (compte à moitié dans la couverture)"
            sc[key]={"s":round(val,2),"v":txt+".","src":src,"conf":conf}
    p["scores"]=sc
    H=p.get("height")
    p["heightFlag"]= "⚠ à mesurer sous le lit" if H and H>10 else None
    json.dump(p,open(path,"w"),ensure_ascii=False,indent=1)

pr=json.load(open(os.path.join(OUT,"robot.project.json")))
pr["criteria"]=[{"key":k,"short":sh,"label":lb,"weight":w,"explain":ex,"how":"Barème : voir la méthode ci-dessous."} for k,sh,lb,w,ex in CRIT]
pr["method"]=open(os.path.join(os.path.dirname(__file__),"..","achats","2026-10-aspirateur-laveur","methode.md")).read()
pr["presets"]=[{"label":"Priorité poils","weights":{"poils":35,"tapis_mop":15,"sale":10,"tapis_asp":15,"entretien":10,"allergies":5,"fiabilite":5,"domotique":3,"obstacles":2}},
               {"label":"Priorité sol sale","weights":{"poils":20,"tapis_mop":15,"sale":30,"tapis_asp":8,"entretien":8,"allergies":6,"fiabilite":6,"domotique":4,"obstacles":3}}]
pr["updated"]="2026-11-11"
json.dump(pr,open(os.path.join(OUT,"robot.project.json"),"w"),ensure_ascii=False,indent=1)

# classement
W={c[0]:c[3] for c in CRIT}; T=sum(W.values()); rows=[]
for path in sorted(glob.glob(os.path.join(OUT,"robot.*.json"))):
    if path.endswith(".project.json"): continue
    p=json.load(open(path)); tot=0; w=0
    for k,wt in W.items():
        s=p["scores"][k]["s"]
        if s is not None: tot+=s*wt; w+=wt*p["scores"][k].get("conf",1)
    ws=sum(wt for k,wt in W.items() if p["scores"][k]["s"] is not None)
    rows.append((round(tot/ws,2) if ws else 0, round(100*w/T), p["name"], p["price"], p.get("heightFlag") or ""))
for r in sorted(rows,reverse=True): print(r)

# --- Verdicts, points forts/faibles et choix, générés depuis les notes (pas de texte libre)
ALERTS={"mova-v70":["Vacuum Wars (B) a retiré sa recommandation le 04/11/2026 : serpillières qui sèchent et se décrochent selon des propriétaires."],
        "dreame-matrix10-pro":["Aucune mesure à son nom : notes reprises du Matrix10 Ultra (modèle proche)."]}
LBL={c[0]:c[2] for c in CRIT}
res=[]
for path in sorted(glob.glob(os.path.join(OUT,"robot.*.json"))):
    if path.endswith(".project.json"): continue
    p=json.load(open(path)); tot=0; w=0
    for k,wt in W.items():
        s=p["scores"][k]["s"]
        if s is not None: tot+=s*wt; w+=wt; 
    cw=sum(wt*p["scores"][k].get("conf",1) for k,wt in W.items() if p["scores"][k]["s"] is not None)
    g=tot/w if w else 0; cov=cw/T
    meas=[(k,p["scores"][k]["s"]) for k in W if p["scores"][k]["s"] is not None]
    nm=[LBL[k] for k in W if p["scores"][k]["s"] is None]
    p["pros"]=[f"{LBL[k]} : {str(round(s,1)).replace('.',',')}/10" for k,s in sorted(meas,key=lambda x:(-x[1],-W[x[0]])) if s>=8][:3]
    p["cons"]=[f"{LBL[k]} : {str(round(s,1)).replace('.',',')}/10" for k,s in sorted(meas,key=lambda x:(x[1],-W[x[0]])) if s<=4.5][:3]+([f"Non mesuré : {', '.join(nm)}"] if nm else [])
    p["alerts"]=ALERTS.get(p["id"],[])
    if p.get("heightFlag"): p["alerts"]=p["alerts"]+[f"Hauteur {str(p['height']).replace('.',',')} cm : ne passe sous le lit que si le dégagement est supérieur."]
    p["verdictText"]= "Pas assez de données fiables pour le classer." if cov<0.5 else f"Score {str(round(g,1)).replace('.',',')}/10, calculé sur {round(cov*100)} % des critères (le reste n'est pas mesuré)."
    p["verdict"]= "meh" if cov<0.5 else ("top" if g>=7.5 and cov>=0.75 else "good" if g>=6.75 else "meh" if g>=5.5 else "no")
    json.dump(p,open(path,"w"),ensure_ascii=False,indent=1)
    res.append((g,cov,p))
ok=sorted([x for x in res if x[1]>=0.75 and not x[2].get("heightFlag")],key=lambda x:-x[0])
best=ok[0][2]; val=min([x for x in ok if x[0]>=ok[0][0]-1.0],key=lambda x:x[2]["price"])[2]
pr=json.load(open(os.path.join(OUT,"robot.project.json")))
pr["picks"]=[{"label":"Meilleur score (≥ 75 % mesuré par des sources fiables, passe sous le lit)","product":best["id"],"why":"Choix calculé automatiquement avec la méthode et tes poids. Voir sa fiche pour le détail des mesures."}]
if val["id"]!=best["id"]: pr["picks"].append({"label":"Le moins cher à moins d'un point du meilleur","product":val["id"],"why":"Le moins cher parmi les robots à moins d'un point du meilleur score (≥ 75 % mesuré). Prix à revérifier le jour de l'achat."})
pr["notes"]=[n for n in pr.get("notes",[]) if not n.startswith("Méthode")]
pr["notes"].insert(0,"Méthode v2 (11/11/2026) : barèmes fixes appliqués mécaniquement, sources A et B uniquement, critère non mesuré retiré du calcul, prix à part. Détail dans l'onglet Critères.")
json.dump(pr,open(os.path.join(OUT,"robot.project.json"),"w"),ensure_ascii=False,indent=1)
print("picks:",[x["product"] for x in pr["picks"]])
