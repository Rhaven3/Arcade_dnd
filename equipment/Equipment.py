import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.Data import d

class Weapon:
    def __init__(self, name, categories, dgt, dgt_type, poids, prix, proprietes, allonge):
        self.name = name
        self.categories = categories
        self.dgt = dgt
        self.Dgt = d(dgt[0], dgt[2], dgt[1])[0]
        self.dgt_type = dgt_type
        self.poids = poids
        self.prix = prix
        self.proprietes = proprietes
        self.allonge = allonge

    def get_name(self):
        return self.name

    def get_categories(self):
        return self.categories

    def get_Dgt(self):
        return self.Dgt
    
    def get_dgt(self):
        return self.dgt
    
    def get_dgt_type(self):
        return self.dgt_type

    def get_poids(self):
        return self.poids

    def get_prix(self):
        return self.prix

    def get_proprietes(self):
        return self.proprietes
    
    def get_allonge(self):
        return self.allonge

"""
        for prop in self.proprietes:
            match self.proprietes[prop]:
                case "deux mains":
                case "allonge":
                case "chargement":
                case "finesse":
                case "lancer":
                case "légère":
                case "lourde":
                case "munition":
                case "polyvalent":
                case "Portée":
                case "filet":
                case "lance arçon":
"""

class Armor:
    def __init__(self, name, categories, class_armor, Force, Discretion, Poids, Prix):
        self.name = name
        self.categories = categories
        self.CA = class_armor
        self.force = Force
        self.Discretion = Discretion
        self.Poids = Poids
        self.Prix = Prix

    def get_name(self):
        return self.name

    def get_categories(self):
        return self.categories

    def get_CA(self):
        return self.CA

    def get_Force(self):
        return self.Force

    def get_Discretion(self):
        return self.Discretion

    def get_poids(self):
        return self.Poids

    def get_prix(self):
        return self.Prix


class Equipment:
    def __init__(self, name, categories, Prix, Poids, proprietes):
        self.name = name
        self.categories = categories
        self.Prix = Prix
        self.Poids = Poids
        self.proprietes = proprietes

    def get_name(self):
        return self.name

    def get_categories(self):
        return self.categories

    def get_prix(self):
        return self.Prix

    def get_poids(self):
        return self.Poids

    def get_proprietes(self):
        return self.proprietes


class tool:
    def __init__(self, name, poids, prix):
        self.name = name
        self.poids = poids
        self.prix = prix

    def get_name(self):
        return self.name

    def get_poids(self):
        return self.poids

    def get_prix(self):
        return self.prix


class monture:
    def __init__(self, name, prix, speed, charge_c):
        self.name = name
        self.prix = prix
        self.speed = speed
        self.CC = charge_c

    def get_name(self):
        return self.name

    def get_prix(self):
        return self.prix

    def get_speed(self):
        return self.speed

    def get_CC(self):
        return self.CC

class equipment_vehicule:
    def __init__(self, name, categories, prix, poids, charge_c):
        self.name = name
        self.categories = categories
        self.prix = prix
        self.poids = poids
        self.CC = charge_c

    def get_name(self):
        return self.name

    def get_categories(self):
        return self.categories

    def get_prix(self):
        return self.prix

    def get_poids(self):
        return self.poids

    def get_CC(self):
        return self.CC

class vehicule:
    def __init__(self, name, prix, speed, team, passenger, motor, charge_c):
        self.name = name
        self.prix = prix
        self.speed = speed
        self.team = team
        self.passenger = passenger
        self.motor = motor
        self.CC = charge_c

    def get_name(self):
        return self.name

    def get_prix(self):
        return self.prix

    def get_speed(self):
        return self.speed

    def get_team(self):
        return self.team

    def get_passenger(self):
        return self.passenger

    def get_motor(self):
        return self.motor

    def get_CC(self):
        return self.CC

class marchandise:
    def __init__(self, name, quantity, prix):
        self.name = name
        self.poids = quantity
        self.prix = prix

    def get_name(self):
        return self.name

    def get_poids(self):
        return self.poids

    def get_prix(self):
        return self.prix