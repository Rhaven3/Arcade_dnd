from Equipment import Weapon
from data.Data import d10, d12, d4, d6, d8, platinium, gold, etherum, copper, silver
# dgt dé / nb / modifier

# Armes courantes de corps à corps [CAC_C]
Quaterstaff = Weapon("Bâton", "CAC_C", [6, 1, 0], "contendant", 2000, silver(2), ["polyvalent"], 1.5)
Dagger = Weapon("Dague", "CAC_C", [4, 1, 0], "perforant", 500, gold(2), ["finesse", "légère", "lancer"], 1.5 )
Club = Weapon("Gourdin", "CAC_C", [4, 1, 0], "contendant", 1000, silver(1), ["légère"], 1.5 )
Handaxe = Weapon("Hachette", "CAC_C", [6, 1, 0], "tranchant", 1000, gold(5), ["légère", "lancer"], 1.5)
Javelin = Weapon("Javeline", "CAC_C", [6, 1, 0], "perforant", 1000, silver(5), ["lancer"], 1.5)
Spear = Weapon("lance", "CAC_C", [6, 1, 0], "perforant", 1500, ["lancer", "polyvalent"], 1.5)
Light_hammer = Weapon("Marteau léger", "CAC_C", [4, 1, 0], 1000, gold(2), ["légère, lancer"], 1.5)
Mace = Weapon("Masse d'armes", "CAC_C", [6, 1, 0], "contendant", 2000, gold(5), [], 1.5)
Greatclub = Weapon("Massue", "CAC_C", [8, 1, 0], "contendant", 5000, gold(2), ["deux mains"], 1.5)
Sickle = Weapon("Serpe", "CAC_C", [4, 1, 0], "tranchant", 1000, gold(1), ["légère"], 1.5)

# Armes courantes à distance [D_C]
Shortbow = Weapon("Arc court", "D_C", [6, 1, 0], "perforant", 1000, gold(25), ["munition", "deux mains"], [24, 96])
Crossbow_light = Weapon("Arbalète légère", "D_C", [8, 1, 0], "perforant", 2500, gold(25), ["muniton", "chargment", "deux mains"], [24, 96])
Dart = Weapon("Fléchette", "D_C", [4, 1, 0], "perforant", 100, copper(5), ["finesse"], [6, 18])
Sling = Weapon("Fronde", "D_C", [4, 1, 0], "contendant", 0, silver(1), ["finesse"], [9, 36])

# Armes de guerre de corps à corps [CAC_M]
Longsword = Weapon("Épée longue", "CAC_M", [8, 1, 0], "tranchant", 1500, gold(15), ["polyvalent"], 1.5)
Shortsword = Weapon("Épée courte", "CAC_M", [6, 1, 0], "tranchant", 1000, gold(10), ["finesse", "légère"], 1.5)

# Armes de querre à distance [D_M]
Crossbow_hand = Weapon("Arbalète de poing", "D_M", [6, 1, 0], "perforant", 1500, gold(75), ["munition", "légère", "chargement"], [9, 36])
