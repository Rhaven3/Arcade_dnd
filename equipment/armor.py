import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Equipment import Armor
from data.Data import d10, d12, d4, d6, d8, platinium, gold, etherum, copper, silver

# Armure légères [L]
Leather = Armor("Cuir", "L", 11, "", "", 5000, gold(10))

# Armure Intermédiaires [M]
Half_plate = Armor("Demi-plate", "M",  15, "", "D", 20000, gold(750))

# Armure Lourde [H]
Plate = Armor("Harnois", "H", 18, 15, "D", 32500, gold(1500))

# Shield [S]
Shield = Armor("Bouclier", "S", 2, "", "", 3000, gold(10))