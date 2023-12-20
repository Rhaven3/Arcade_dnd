from math import floor, ceil
from random import randint
import sqlite3

# le système de jet de dé
def d100(modifier=0, x=1):
    rd100 = []
    sumd = 0
    if modifier > 1:
        modifier = 1
    elif modifier < -1:
        modifier = -1
    match modifier:
        case 1:
            for i in range(2):
                rd100.append(randint(1, 100))
                sumd = max(rd100)
            return sumd
        case -1:
            for i in range(2):
                rd100.append(randint(1, 100))
                sumd = min(rd100)
            return sumd
        case other:
            for i in range(0, x):
                rd100.append(randint(1, 100))
                sumd += rd100[i]
            return [sumd, rd100]


def d20(modifier=0, x=1):
    rd20 = []
    sumd = 0
    if modifier > 1:
        modifier = 1
    elif modifier < -1:
        modifier = -1
    match modifier:
        case 1:
            for i in range(2):
                rd20.append(randint(1, 20))
                sumd = max(rd20)
            return sumd
        case -1:
            for i in range(2):
                rd20.append(randint(1, 20))
                sumd = min(rd20)
            return sumd
        case other:
            for i in range(0, x):
                rd20.append(randint(1, 20))
                sumd += rd20[i]
            return [sumd, rd20]


def d12(modifier=0, x=1):
    rd12 = []
    sumd = 0
    if modifier > 1:
        modifier = 1
    elif modifier < -1:
        modifier = -1
    match modifier:
        case 1:
            for i in range(2):
                rd12.append(randint(1, 12))
                sumd = max(rd12)
            return sumd
        case -1:
            for i in range(2):
                rd12.append(randint(1, 12))
                sumd = min(rd12)
            return sumd
        case other:
            for i in range(0, x):
                rd12.append(randint(1, 12))
                sumd += rd12[i]
            return [sumd, rd12]


def d10(modifier=0, x=1):
    rd10 = []
    sumd = 0
    if modifier > 1:
        modifier = 1
    elif modifier < -1:
        modifier = -1
    match modifier:
        case 1:
            for i in range(2):
                rd10.append(randint(1, 10))
                sumd = max(rd10)
            return sumd
        case -1:
            for i in range(2):
                rd10.append(randint(1, 10))
                sumd = min(rd10)
            return sumd
        case other:
            for i in range(0, x):
                rd10.append(randint(1, 10))
                sumd += rd10[i]
            return [sumd, rd10]


def d8(modifier=0, x=1):
    rd8 = []
    sumd = 0
    if modifier > 1:
        modifier = 1
    elif modifier < -1:
        modifier = -1
    match modifier:
        case 1:
            for i in range(2):
                rd8.append(randint(1, 8))
                sumd = max(rd8)
            return sumd
        case -1:
            for i in range(2):
                rd8.append(randint(1, 8))
                sumd = min(rd8)
            return sumd
        case other:
            for i in range(0, x):
                rd8.append(randint(1, 8))
                sumd += rd8[i]
            return [sumd, rd8]


def d6(modifier=0, x=1):
    rd6 = []
    sumd = 0
    if modifier > 1:
        modifier = 1
    elif modifier < -1:
        modifier = -1
    match modifier:
        case 1:
            for i in range(2):
                rd6.append(randint(1, 6))
                sumd = max(rd6)
            return sumd
        case -1:
            for i in range(2):
                rd6.append(randint(1, 6))
                sumd = min(rd6)
            return sumd
        case other:
            for i in range(0, x):
                rd6.append(randint(1, 6))
                sumd += rd6[i]
            return [sumd, rd6]


def d4(modifier=0, x=1):
    rd4 = []
    sumd = 0
    if modifier > 1:
        modifier = 1
    elif modifier < -1:
        modifier = -1
    match modifier:
        case 1:
            for i in range(2):
                rd4.append(randint(1, 4))
                sumd = max(rd4)
            return sumd
        case -1:
            for i in range(2):
                rd4.append(randint(1, 4))
                sumd = min(rd4)
            return sumd
        case other:
            for i in range(0, x):
                rd4.append(randint(1, 4))
                sumd += rd4[i]
            return [sumd, rd4]

# recherche de d avec chiffre
def d(d, modifier=0,  nb=1):
    match d:
        case 4:
            return d4(modifier, nb)
        case 6:
            return d6(modifier, nb)
        case 8:
            return d8(modifier, nb)
        case 10:
            return d10(modifier, nb)
        case 12:
            return d12(modifier, nb)
        case 20:
            return d20(modifier, nb)
        case other:
            return 0


# Système monétaire
class Monaie:
    def __init__(self, amount):
        self.amount = amount
        
    def __add__(self, other):
        return Monaie(self.amount + other.amount)
    
    def __sub__(self, other):
        return Monaie(self.amount - other.amount)
    
    def __mul__(self, other):
        return Monaie(self.amount * other)
    
    def __truediv__(self, other):
        return Monaie(self.amount / other)

# Or
class gold(Monaie):
    name = "Pièce d'Or"
    def __str__(self):
        return "{:.0f} po".format(self.amount)

# Argent
class silver(Monaie):
    name = "Pièce d'Argent"
    def __str__(self):
        return "{:.0f} pa".format(self.amount)

# Cuivre
class copper(Monaie):
    name = "Pièce de Cuivre"
    def __str__(self):
        return "{:.0f} pc".format(self.amount)

# Platine
class platinium(Monaie):
    name = "Pièce de Platinium"
    def __str__(self):
        return "{:.0f} pp".format(self.amount)

# Etherum
class etherum(Monaie):
    name = "Pièce d'Etherum"
    def __str__(self):
        return "{:.0f} pe".format(self.amount)

class Currency:
    def __init__(self, name, symbol, rate, conversion_symbols):
        self.name = name
        self.symbol = symbol
        self.rate = rate
        self.conversion_symbols = conversion_symbols

    def convert(self, amount, to_currency, money):
        if to_currency.symbol not in self.conversion_symbols:
            raise ValueError(f"{self.name} cannot be converted to {to_currency.name}")
        money.amount = int(amount * (self.rate / to_currency.rate))
        return money

# Les monaies
# l'Or
gold_currency = Currency("Pièce d'Or", "po", 100, ["po", "pa", "pc", "pp", "pe"])
# l'argent
silver_currency = Currency("Pièce d'Argent", "pa", 10, ["pa", "pc", "po", "pp", "pe"])
# le cuivre
copper_currency = Currency("Pièce de Cuivre", "pc", 1, ["pc", "pa", "po", "pp", "pe"])
# le platine
platinium_currency = Currency("Pièce de Platinium", "pp", 1000, ["pp", "po", "pa", "pc", "pe"])
# l'etherum
etherum_currency = Currency("Pièce d'Etherum", "pe", 200, ["pe", "pp", "po", "pa", "pc"])

# taille list
taille_list = ["TP", "P", "M", "G", "TG", "Gig"]
# Compétence Int
comp_list = ["Acrobaties", "Arcanes", "Athletisme", "Discretion", "Dressage", "Escamotage", "Histoire", "Intimidation", "Intuition", "Investigation", "Medecine", "Nature", "Perception", "Perspicacite", "Persuasion", "Religion", "Representation", "Survie", "Tromperie"]
comp_int = ["Arcane", "Histoire", "Investigation", "Nature", "Religion"]
comp_sag = ["Dressage", "Intuition", "Medecine", "Perception", "Perspicacité", "Survie"]
# type list
type_list = ["tranchant", "contendant", "perforant", "acide", "feu", "force", "foudre", "froid", "necrotique", "poison", "psychique", "radiant", "tonnerre"]

# Tour
Action = 1
Action_bonus = 1
Reaction = 1
time_tour = 6
compte_tour = 1
Party = {}
Player_combat = []
Enemy_combat = []
P1 = None
P2 = None
P3 = None
P4 = None
P5 = None
P6 = None
P7 = None
P8 = None
P9 = None
P10 = None
Player_list = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]
E1 = None
E2 = None
E3 = None
E4 = None
E5 = None
E6 = None
E7 = None
E8 = None
E9 = None
E10 = None
Enemy_list = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]

def player_listing():
    for player in Player_list:
        if player is not None:
            Player_combat.append(player)

def enemy_listing():
    for enemy in Enemy_list:
        if enemy is not None:
            Enemy_combat.append(enemy)

def HP_Ally():
    HP_ally = 0
    for player in Player_list:
        if player is not None:
            HP_ally += player.get_pv_tot()
    return HP_ally

def HP_Enemy():
    HP_enemy = 0
    for enemy in Enemy_list:
        if enemy is not None:
            HP_enemy += enemy.get_pv_tot()
    return HP_enemy

def listing():
    player_listing()
    enemy_listing()

    for player in Player_combat:
        if player is not None:
            Party[player] = player.jet_initiative()
    for enemy in Enemy_combat:
        if enemy is not None:
            Party[enemy] = enemy.jet_initiative()
    Party_order = {k: v for k, v in sorted(Party.items(), key=lambda item: item[1])}
    Player_party = Party_order.keys()
    return Party_order, Player_party


def tour():
    global Action, Action_bonus, Reaction, Party, Player_party
    HP_ally = HP_Ally()
    HP_enemy = HP_Enemy()
    player_listing()
    enemy_listing()

    for player in Player_combat:
        if player is not None:
            Party[player] = player.jet_initiative()
    for enemy in Enemy_combat:
        if enemy is not None:
            Party[enemy] = enemy.jet_initiative()
    Party_order = {k: v for k, v in sorted(Party.items(), key=lambda item: item[1])}
    Player_party = Party_order.keys()
    while HP_ally > 0 and HP_enemy > 0:
        for perso in Player_party:
            perso.Menu()
            Action_perso = perso.get_action()
            Action_Bonus_perso = perso.get_action_bonus()
            Reaction_perso = perso.get_reaction()
            if Action > 0:
                print("il vous reste ", Action_perso, " action")
            elif Action_bonus > 0:
                print("il vous reste", Action_Bonus_perso, " action bonus")
            else:
                Action_perso = 1
                Action_Bonus_perso = 1
                Reaction_perso = 1
            HP_ally = HP_Ally()
            HP_enemy = HP_Enemy()

"""
wallet_gold = gold(20)
wallet_argent = gold_currency.convert(wallet_gold.amount, silver_currency, silver(0))
print(f"{wallet_gold} is equivalent to {wallet_argent}")

conn = sqlite3.connect('BDD_DND/dnd.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM `dnd5_classes`')
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
"""

# Règles
PV_Roll = False
Finesse_dex = False
Regen_PV = False

# Def règles
def PV_roll():
    global PV_Roll
    x = 1
    for i in range(x):
        rule = input("Vos PV sont lancé avec des dés, ou une valeurs fixe ? (oui ou non)\n")
        match rule:
            case "oui":
                PV_Roll = True
            case "non":
                PV_Roll = False
            case other:
                x += 1
def PV_rule(d1, modifier="", lvl=1):
    match PV_Roll:
        case True:
            return d(d1, modifier,  lvl)
        case False:
            match d1:
                case 6:
                    return 4
                case 8:
                    return 5
                case 10:
                    return 6
                case 12:
                    return 7
                case other:
                    return 0

def finesse_rule():
    global Finesse_dex
    x = 1
    for i in range(x):
        rule = input("Vous utilisé des armes finesse avec For ou dex ?\n")
        match rule:
            case "For":
                Finesse_dex = False
                return Finesse_dex
            case "Dex":
                Finesse_dex = True
                return Finesse_dex
            case other:
                x += 1

def Regen_rule():
    global Regen_PV
    x = 1
    for i in range(x):
        rule = input("Voulez vous utilisez une règle variante pour les repos long ?\nSi oui, Vous ne pourrez utilisez que la moitié de vos dé de vie durant un repos long et il seront complètement récuperer après\n")
        match rule:
            case "oui":
                Regen_PV = True
                return Regen_PV
            case "non":
                Regen_PV = False
                return Regen_PV
            case other:
                x += 1