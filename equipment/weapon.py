import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Equipment import Weapon
from data.Data import d10, d12, d4, d6, d8, platinium, gold, etherum, copper, silver
# dgt dé / nb / modifier

# Armes courantes de corps à corps [CAC_C]
Quaterstaff = Weapon("Bâton", "CAC_C", [6, 1, 0], "contendant", 2000, silver(2), ["polyvalent"], 1.5)

# Armes courantes à distance [D_C]
Shortbow = Weapon("Arc court", "D_C", [6, 1, 0], "perforant", 1000, gold(25), ["munition", "deux mains"], [24, 96])

# Armes de guerre de corps à corps [CAC_M]
Longsword = Weapon("Épée longue", "CAC_M", [8, 1, 0], "tranchant", 1500, gold(15), ["polyvalent"], 1.5)
Shortsword = Weapon("Épée courte", "CAC_M", [6, 1, 0], "tranchant", 1000, gold(10), ["finesse", "légère"], 1.5)

# Armes de querre à distance [D_M]
Crossbow_hand = Weapon("Arbalète de poing", "D_M", [6, 1, 0], "perforant", 1500, gold(75), ["munition", "légère", "chargement"], [9, 36])
