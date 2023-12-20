import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from Class.Fighter import Fighter
from Classe.Character import *
# name / lvl / historique / race / age / taille / yeux / peau / cheveux / poids / For / Dex / Con / Int / Wis / Cha
test = Character("Test", 5, "", "", "", "P", "", "", "", 60000, 15, 14, 12, 10, 12, 14)
"""print("DV: ", test.get_DV())
print("PV base: ", test.get_pv_base())
print("Mod.Con", test.get_mod_con())
print("lvl: ", test.get_lvl())
x=0
print(test.get_lvl_up())
for i in test.get_lvl_up():
    print("Pv au niveau ", x+1, ": ", i)
    x += 1
print("PV lvl: ", test.get_pv_lvl())
print("Pv actuel: ", test.get_pv_tot())"""

test.Menu()