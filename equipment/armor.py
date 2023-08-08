from abc import abstractproperty
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Equipment import Armor
from data.Data import d10, d12, d4, d6, d8, platinium, gold, etherum, copper, silver

# Armure légères [L]
Leather = Armor("Cuir", "L", 11, "", "D", 5000, gold(10))
Padded = Armor("Matelassée", "L", 11, "", "", 4000, gold(5))
Studded_leather = Armor("Cuir clouté", "L", 12, "", "", 6500, gold(45))

# Armure Intermédiaires [M]
Half_plate = Armor("Demi-plate", "M",  15, "", "D", 20000, gold(750))
Breastplate = Armor("Cuirasse", "M", 14, "", "", 10000, gold(400))
Scale_mail = Armor("Écailles", "M", 14, "", "D", 22500, gold(50))
Chain_shirt	= Armor("Chemise de mailles", "M", 13, "", "", 10000, gold(50))
Hide =  Armor("Peaux", "M", 12, "", "", 6000, gold(10))

# Armure Lourde [H]
Plate = Armor("Harnois", "H", 18, 15, "D", 32500, gold(1500))
Splint = Armor("Clibanion", "H", 17, 15, "D", 30000, gold(200))
Chain_mail = Armor("Cotte de mailles", "H", 16, 13, "D", 27500, gold(75))
Ring_mail = Armor("Broigne", "H", 14, "", "D", 20000, gold(30))

# Shield [S]
Shield = Armor("Bouclier", "S", 2, "", "", 3000, gold(10))