import math, random

from data.Data import PV_rule, PV_roll, d20, finesse_rule, Action, Action_bonus, Reaction, taille_list, listing, comp_list, comp_int, comp_sag, type_list, Regen_rule
from equipment.Equipment import Weapon, Armor


class Character:
    def __init__(self, name, lvl, historique, race, age, taille, yeux, peau, cheveux, poids, For, Dex, Con, Int, Wis, Cha):
        self.name = name
        self.lvl = lvl 
        self.encombrement = 0
        self.epuisement = 0
        self.debuff_epuisement = 0
        # self.epuisement_prec = 0
        self.Distance = 10
        self.Player_Action = Action
        self.Player_Action_Bonus = Action_bonus
        self.Player_Reaction = Reaction
        self.etat = {"prone": False, 
                    "grappled": False,
                    "grappled_name": None,
                    "deafened": False, 
                    "blinded": False,
                    "charmed": False, 
                    "charmed_name": None,
                    "frightened": False, 
                    "frightened_name": None,
                    "poisoned": False, 
                    "restrained": False, 
                    "stunned": False, 
                    "incapacited": False,
                    "unconscious": False, 
                    "invisible": False, 
                    "paralyzed": False, 
                    "petrified": False}
        self.charm_list = [self.name]
        self.fright_list = [self.name]
        self.disease = []
        self.inventory = []
        # action modifier
        self.Modifier = 0
        self.Dodge = 0
        self.Help = 0
        self.lourd = 0

        # Details
        self.historique = historique
        self.race = race
        self.age = age
        self.yeux = yeux
        self.peau = peau
        self.cheveux = cheveux
        self.size = taille
        self.poids = poids
        self.language = None

        # Stat principale
        self.attributes = [For, Dex, Con, Int, Wis, Cha]
        self.CC = math.floor(self.attributes[0]*7.5)
        self.Charge = 0

        # Limite
        self.limite = [20, 20, 20, 20, 20, 20]
        # Modificateur
        self.mod_For = math.floor((self.attributes[0]-10)/2)
        self.mod_Dex = math.floor((self.attributes[1]-10)/2)
        self.mod_Con = math.floor((self.attributes[2]-10)/2)
        self.mod_Int = math.floor((self.attributes[3]-10)/2)
        self.mod_Wis = math.floor((self.attributes[4]-10)/2)
        self.mod_Cha = math.floor((self.attributes[5]-10)/2)

        # arms
        self.left_arm = None
        self.attack_weapon = None
        self.right_arm = None
        self.Nat_weapon = None
        # Armor
        self.equiped_armor = None
        # Backpack
        self.equiped_backpack = None

        # Stats
        self.DV = 0
        self.DV_nbr = 0
        self.lvl_up = []
        self.PV_base = self.get_DV()+self.mod_Con
            # Verif rule
        PV_roll()
        self.finesse_dex = finesse_rule()
        self.regen_pv = Regen_rule()
        self.PV_lvl = 0
        for lvls in range(self.lvl-1):# gain HP par lvl + save []
            PV_rule(10)[0]
            print("pvrule : ", type(PV_rule(10)))
            self.PV_lvl += PV_rule(10)[0] + self.mod_Con
            self.get_lvl_up().append(self.PV_lvl)
        self.PV_tot = self.PV_base + self.PV_lvl
        self.check_pv_tot = False
        self.PV_Max = self.PV_base + self.PV_lvl
        self.check_pv_max = False
        self.PV_fixe = self.PV_base + self.PV_lvl
        self.check_pv_fixe = False
        self.PV_Temp = 0
        self.class_armor = 10 + self.mod_Dex
        self.prof = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
        self.proficiency = self.prof[self.lvl-1]
        # deplacement
        self.Speed = 0
        self.Speed_base = 0
        self.long_jump = self.attributes[0]/3
        self.long_jump_SE = self.long_jump/2
        self.jump = max(self.long_jump+1, 0)
        self.jump_BT = self.jump+self.size/2
        self.jump_SE = self.jump/2
        # res/imun/vul
        self.Res = []
        self.Imun = []
        self.Vul = []
        self.Res_base = []
        self.Imun_base = []
        self.Vul_base = []

        # proficiencies
        self.prof_weapon = None
        self.prof_armor = None
        self.prof_tool = None

        # initiative
        self.initiative = self.mod_Dex
        # Competence
        self.Acrobaties = self.mod_Dex # (DEX)
        self.Arcanes = self.mod_Int # (INT)
        self.Athletisme = self.mod_For # (FOR)
        self.Discretion = self.mod_Dex # (DEX)
        self.Dressage = self.mod_Wis # (SAG)
        self.Escamotage = self.mod_Dex # (DEX)
        self.Histoire = self.mod_Int # (INT)
        self.Intimidation = self.mod_Cha # (CHA)
        self.Intuition = self.mod_Wis # (SAG)
        self.Investigation = self.mod_Int # (INT)
        self.Medecine = self.mod_Wis # (SAG)
        self.Nature = self.mod_Int # (INT)
        self.Perception = self.mod_Wis # (SAG)
        self.Perspicacite = self.mod_Wis # (SAG)
        self.Persuasion = self.mod_Cha # (CHA)
        self.Religion = self.mod_Int # (INT)
        self.Representation = self.mod_Cha # (CHA)
        self.Survie = self.mod_Wis # (SAG)
        self.Tromperie = self.mod_Cha # (CHA)
        # Competence passive
        self.Sag_Perception_Pass = 10+self.Perception
        self.Sag_Intuition_Pass = 10+self.Intuition
        # JdS For/Dex/Con/Int/Sag/Cha
        self.jds = [self.mod_For, self.mod_Dex, self.mod_Con, self.mod_Int, self.mod_Wis, self.mod_Cha]

    # Jet de Caracteristique
    def jet_For(self, modifier=0,competence=""):
        modifier += self.Help
        modifier += self.encombrement
        modifier += self.debuff_epuisement
        if self.etat["poisoned"]:
            modifier -= 1
        if self.etat["frightened_name"]: # charm limit
                x = input("Es que la personne qui vous effrez est dans votre champs de vision ? (oui ou non)\n")
                if x == "oui": # si personne effrayante champ de vision
                    modifier -= 1
        jet = d20(modifier)# jet de de
        print(f"Jet brut : {jet[0]}")
        if jet == 20:
            print("C'est un miracle !")
        elif jet == 1:
            print("C'est un désastre !")
        self.Help = 0  # reset de Help
        if competence != "":# si comp bonus comp
            jet += competence
            print(f"Le bonus de votre compétence : {competence}\nJet final : {jet}")
            return jet
        else:# sinon simple jet for
            jet += self.mod_For
            print(f"Votre modificateur de force : {self.mod_For}\nJet final : {jet}")
            return jet
    
    def jet_Dex(self, modifier=0,competence=""):
        if self.Dodge <= 1: # si dodge action
            modifier += self.Dodge
            self.Dodge = 0
        modifier += self.Help
        modifier += self.debuff_epuisement
        modifier += self.encombrement
        if self.etat["poisoned"]:
            modifier -= 1
        if self.etat["frightened_name"]: # charm limit
                x = input("Es que la personne qui vous effrez est dans votre champs de vision ? (oui ou non)\n")
                if x == "oui": # si personne effrayante champ de vision
                    modifier -= 1
        jet = d20(modifier)
        print(f"Jet brut : {jet[0]}")
        if jet == 20:
            print("C'est un miracle !")
        elif jet == 1:
            print("C'est un désastre !")
        self.Help = 0  # reset de Help
        if competence != "":
            jet += competence
            print(f"Le bonus de votre compétence : {competence}\nJet final : {jet}")
            return jet
        else:
            jet += self.mod_Dex
            print(f"Votre modificateur de dextérité : {self.mod_Dex}\nJet final : {jet}")
            return jet

    def jet_Con(self, modifier=0,competence=""):
        modifier += self.Help
        modifier += self.debuff_epuisement
        modifier += self.encombrement
        if self.etat["poisoned"]:
            modifier -= 1
        if self.etat["frightened_name"]: # charm limit
                x = input("Es que la personne qui vous effrez est dans votre champs de vision ? (oui ou non)\n")
                if x == "oui": # si personne effrayante champ de vision
                    modifier -= 1
        jet = d20(modifier)
        print(f"Jet brut : {jet[0]}")
        if jet == 20:
            print("C'est un miracle !")
        elif jet == 1:
            print("C'est un désastre !")
        self.Help = 0  # reset de Help
        if competence != "":
            jet += competence
            print(f"Le bonus de votre compétence : {competence}\nJet final : {jet}")
            return jet
        else:
            jet += self.mod_Con
            print(f"Votre modificateur de constitution : {self.mod_Con}\nJet final : {jet}")
            return jet
    
    def jet_Int(self, modifier=0,competence=""):
        modifier += self.Help
        modifier += self.debuff_epuisement
        if self.etat["poisoned"]:
            modifier -= 1
        if self.etat["frightened_name"]: # charm limit
                x = input("Es que la personne qui vous effrez est dans votre champs de vision ? (oui ou non)\n")
                if x == "oui": # si personne effrayante champ de vision
                    modifier -= 1
        jet = d20(modifier)
        print(f"Jet brut : {jet[0]}")
        if jet == 20:
            print("C'est un miracle !")
        elif jet == 1:
            print("C'est un désastre !")
        self.Help = 0  # reset de Help
        if competence != "":
            jet += competence
            print(f"Le bonus de votre compétence : {competence}\nJet final : {jet}")
            return jet
        else:
            jet += self.mod_Int
            print(f"Votre modificateur de intélligence : {self.mod_Int}\nJet final : {jet}")
            return jet

    def jet_Wis(self, modifier=0,competence=""):
        modifier += self.Help
        modifier += self.debuff_epuisement
        if self.etat["poisoned"]:
            modifier -= 1
        if self.etat["frightened_name"]: # charm limit
                x = input("Es que la personne qui vous effrez est dans votre champs de vision ? (oui ou non)\n")
                if x == "oui": # si personne effrayante champ de vision
                    modifier -= 1
        jet = d20(modifier)
        print(f"Jet brut : {jet[0]}")
        if jet == 20:
            print("C'est un miracle !")
        elif jet == 1:
            print("C'est un désastre !")
        self.Help = 0  # reset de Help
        if competence != "":
            jet += competence
            print(f"Le bonus de votre compétence : {competence}\nJet final : {jet}")
            return jet
        else:
            jet += self.mod_Wis
            print(f"Votre modificateur de Sagesse : {self.mod_Wis}\nJet final : {jet}")
            return jet

    def jet_Cha(self, modifier=0,competence="", target=None):
        modifier += self.Help
        modifier += self.debuff_epuisement
        if self.etat["poisoned"]:
            modifier -= 1
        if target in self.charm_list:
            modifier += 1
        if self.etat["frightened_name"]: # charm limit
            x = input("Es que la personne qui vous effrez est dans votre champs de vision ? (oui ou non)\n")
            if x == "oui": # si personne effrayante champ de vision
                modifier -= 1
        jet = d20(modifier)
        print(f"Jet brut : {jet[0]}")
        if jet == 20:
            print("C'est un miracle !")
        elif jet == 1:
            print("C'est un désastre !")
        self.Help = 0  # reset de Help
        if competence != "":
            jet += competence
            print(f"Le bonus de votre compétence : {competence}\nJet final : {jet}")
            return jet
        else:
            jet += self.mod_Cha
            print(f"Votre modificateur de charisme : {self.mod_Cha}\nJet final : {jet}")
            return jet
    
    def jet_initiative(self, modifier=0):
        modifier += self.Help
        modifier += self.debuff_epuisement
        if self.etat["poisoned"]:
            modifier -= 1
        if self.etat["frightened_name"]: # charm limit
            x = input("Es que la personne qui vous effrez est dans votre champs de vision ? (oui ou non)\n")
            if x == "oui": # si personne effrayante champ de vision
                modifier -= 1
        jet = d20(modifier)
        if jet == 20:
            print("C'est un miracle !")
        elif jet == 1:
            print("C'est un désastre !")
        print(f"Jet brut : {jet[0]}\n Votre initiative : {self.initiative}")
        jet += self.initiative
        print(f"Jet final : {jet}")
        return jet


    def JdS(self, stats,modifier=0):
        stat = None
        modifier += self.Help
        modifier += self.debuff_epuisement
        if self.etat["poisoned"]:
            modifier -= 1
        match stats:
            case "For":
                if self.etat["stunned"]:
                    jet = -30
                    return jet
                if self.etat["unconscious"]:
                    jet = -30
                    return jet
                if self.etat["paralyzed"]:
                    jet = -30
                    return jet
                if self.etat["petrified"]:
                    jet = -30
                    return jet
                stat = self.jds[0]
            case "Dex":
                if self.etat["restrained"]:
                    modifier -= 1
                if self.etat["stunned"]:
                    jet = -30
                    return jet
                if self.etat["unconscious"]:
                    jet = -30
                    return jet
                if self.etat["paralyzed"]:
                    jet = -30
                    return jet
                if self.etat["petrified"]:
                    jet = -30
                    return jet
                stat = self.jds[1]
            case "Con":
                stat = self.jds[2]
            case "Int":
                stat = self.jds[3]
            case "Sag":
                stat = self.jds[4]
            case "Cha":
                stat = self.jds[5]
        jet = d20(modifier)
        print(f"Jet brut : {jet}\n Votre bonus au jet de sauvegarde de {stats} : {stat}")
        if jet == 20:
            print("C'est un miracle !")
        elif jet == 1:
            print("C'est un désastre !")
        jet += stat
        return jet

    # encombrement
    def Encombrement(self):
        if self.Charge > 2.5 * self.attributes[0]:
            self.Speed -= 3
        elif self.Charge > 5 * self.attributes[0]:
            self.Speed -= 6
            self.encombrement -= 1
        elif self.Charge >= self.CC:
            self.Speed = 0
            self.encombrement -= 1
        else:
            self.Speed = self.Speed_base
            self.encombrement = 0



    # Check HP
    def check_hp(self, pourcentage=False, div=0):
        if pourcentage:
            self.PV_tot /= div
        else:
            if self.PV_tot > self.PV_Max:
                self.PV_tot = self.PV_Max


    #epuisement
    def Epuisement(self):
        # Dictionnaire pour stocker les malus/debuffs en fonction de l'epuisement
        epuisement_effects = {
            0: (0, -1 , None, False),
            1: (-1, -1, None, False),
            2: (-1, 2, None, False),
            3: (-1, 2, None, False),
            4: (-1, 2, 2, False),
            5: (-1, 0, 2, False),
            6: (-1, 0, 2, True),
        }

        # Verifier si l'epuisement a change depuis la derniere fois
        if self.epuisement != self.epuisement_prec:
            # Recuperer les effets associes a l'epuisement actuel
            effect = epuisement_effects.get(self.epuisement, None)
            if effect:
                debuff, speed_modifier, malus_hp, death = effect

                # Annuler les malus/debuffs de l'epuisement precedent
                """if self.epuisement_prec in epuisement_effects:
                    prev_effect = epuisement_effects[self.epuisement_prec]
                    prev_debuff, prev_speed_modifier, prev_malus_hp, prev_death = prev_effect
                    self.debuff_epuisement -= prev_debuff
                    if prev_speed_modifier is not None:
                        self.Speed = prev_speed_modifier"""

                # Appliquer les malus/debuffs de l'epuisement actuel
                self.debuff_epuisement = debuff
                if speed_modifier == 0:
                    self.Speed = 0
                elif speed_modifier == -1:
                    self.Speed = self.Speed_base
                else:
                    self.Speed /= speed_modifier
                if malus_hp == 2:
                    self.PV_Max /= malus_hp
                    self.check_hp()
                else:
                    self.PV_Max *= malus_hp
                    self.check_hp()
                if death:
                    self.PV_tot -= self.PV_Max *2
                else:
                    self.PV_tot += self.PV_Max *2
                    
            # Mettre a jour l'epuisement precedent
            self.epuisement_proc = self.epuisement

    
    # rest
    def short_rest(self):
        x=1
        global d
        for i in range(x):
            dd = input(f"Combien de dé de vie voulait vous utilisez pour regagner des points de vie ?\n Il vous reste : {self.DV} Dé de Vie\n")
            if dd > self.lvl:
                x+=1
                print(" Mec y en a trop là t'es dans l'excès")
        self.DV_nbr -= dd
        print(f"Nombre de dé utiliser : {dd}\n modificateur de Constitution : {self.mod_Con}\n Dé de Vie restant : {self.DV_nbr}")
        jet_dd = d(self.DV, 0, dd)
        print(f"chaque dé : {jet_dd[1]}\n le total brut: {jet_dd[0]}")
        jet_dd = jet_dd[0] + self.mod_Con*dd
        jet_dd = max(jet_dd, 0)
        print(f"Total de PV restauré : {jet_dd}")
        self.PV_tot += jet_dd
        self.check_hp()


    def long_rest(self):
        x=1
        y=1
        ep = False
        global d
        for i in range(x):
            if not self.regen_pv:
                dd = input(f"Combien de dé de vie voulait vous utilisez pour regagner des points de vie ?\n Il vous reste : {self.DV} Dé de Vie\n")
            if self.regen_pv and dd > self.lvl/2:
                x+=1
                print(" Mec y en a trop là t'es dans l'excès")
        for i in range(y):
            nut = input("Es que vous avez bu et mangé ?")
            match nut:
                case "oui":
                    ep = True
                case "non":
                    ep = False
                case other:
                    y += 1
        if self.regen_pv:
            self.DV_nbr = self.lvl
            print(f"Nombre de dé utiliser : {dd}\n modificateur de Constitution : {self.mod_Con}")
            jet_dd = d(self.DV, 0, dd)
            print(f"chaque dé : {jet_dd[1]}\n le total brut: {jet_dd[0]}")
            jet_dd = jet_dd[0] + self.mod_Con*dd
            jet_dd = max(jet_dd, 0)
            print(f"Total de PV restauré : {jet_dd}")
        else:
            self.DV_nbr = self.lvl/2
            jet_dd = self.PV_Max
        self.PV_tot += jet_dd
        self.check_hp()
        if ep and self.epuisement != 0:
                self.epuisement -= 1
                self.Epuisement()


    # Distance
    # a voir


    # get stats principal
    def get_action(self):
        return self.Player_Action
    
    def get_action_bonus(self):
        return self.Player_Action_Bonus
    
    def get_reaction(self):
        return self.Player_Reaction
    
    def get_class_armor(self):
        return self.class_armor
    
    def get_initiative(self):
        return self.initiative
    
    def get_mod_con(self):
        return self.mod_Con

    def get_lvl_up(self):
        return self.lvl_up

    def get_lvl(self):
        return self.lvl

    def get_pv_lvl(self):
        return self.PV_lvl

    def get_pv_base(self):
        self.PV_base = self.get_DV() + self.mod_Con
        return self.PV_base

    def get_DV(self):
        return self.DV

    def get_pv_tot(self):
        if self.check_pv_tot is not True:
            self.PV_tot = self.PV_base + self.PV_lvl
            self.check_pv_tot = True
        return self.PV_tot

    def get_pv_max(self):
        if self.check_pv_max is not True:
            self.PV_Max = self.PV_base + self.PV_lvl
            self.check_pv_max = True
        return self.PV_Max
    
    def get_pv_fixe(self):
        if self.check_pv_fixe is not True:
            self.PV_fixe = self.PV_base + self.PV_lvl
            self.check_pv_fixe = True
        return self.PV_fixe

    def get_help(self):
        return self.Help
    
    def get_size(self):
        return self.size
    
    def get_etat(self):
        return self.etat
    
    def get_res(self):
        return self.Res
    
    def get_imun(self):
        return self.Imun
    
    def get_vul(self):
        return self.Vul


    # Etat
    def Prone(self, target=None, desapply=False):
        if target == None:
                target = self
        etat = target.get_etat()
        if desapply:
            etat["prone"] = False
            print(f"{target.name}. Vous n'êtes plus à terre !")
        else:
            # opton mouvement restreint
            etat["prone"] = True
            print(f"{target.name}. Vous êtes à terre !")

        

    def Grappled(self, target=None, desapply=False):
        if target == None:
            target = self
        target_etat = target.get_etat()
        if target is not None and not self.etat["incapacited"]:   
            target_etat["grappled"] = True
            target_etat["grappled_name"] = self.name
            target.Speed = 0
        else:
            desapply = True
        # if out of distance end grappled
        if desapply:
            target_etat["grappled"] = False
            target_etat["grappled_name"] = self.name
            print(f"{target.name}. Vous n'êtes plus aggrippé !")
            target.Speed = target.Speed_base


    def Deafened(self, target=None, desapply=False):
        if target == None:
            target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["deafaned"] = False
            print(f"{target.name}. Vous n'êtes plus assourdi !")
        else:
            target_etat["deafened"] = True
            print(f"{target.name}. Vous êtes assourdi !")



    def Blinded(self, target=None, desapply=False):
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["blinded"] = False
            print(f"{target.name}. Vous n'êtes plus aveuglé !")
        else:
            target_etat["blinded"] = True
            print(f"{target.name}. Vous êtes aveuglé !")

        

    def Charmed(self, target=None, desapply=False):
        if target == None:
            target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["charmed"] = False
            target_etat["charmed_name"] = None
            self.charm_list.remove(target.name)
            print(f"{target.name}. Vous êtes charmé ! Et {self.name} est Charmant !")
        else:
            target_etat["charmed"] = True
            target_etat["charmed_name"] = self.name
            self.charm_list.append(target.name)
            print(f"{target.name}. Vous êtes charmé ! Et {self.name} est Charmant !")

    
    def Frightened(self, target=None, desapply=False):
        if target == None:
            target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["frightened"] = False
            target_etat["frightened_name"] = None
            self.fright_list.remove(target.name)
            print(f"{target.name}. Vous êtes charmé ! Et {self.name} est Charmant !")
        else:
            target_etat["frightened"] = True
            target_etat["frightened_name"] = self.name
            self.fright_list.append(target.name)
            print(f"{target.name}. Vous êtes effrayé ! Et {self.name} est effrayant !")
        # finir deplacement
        

    def Poisoned(self, target=None, desapply=False):
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["poisoned"] = False
            print(f"{target.name}. Vous n'êtes plus empoisonné !")
        else:
            target_etat["poisoned"] = True
            print(f"{target.name}. Vous êtes empoisonné !")


    def Restrained(self, target=None, desapply = False):
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["restrained"] = False
            print(f"{target.name}. Vous n'êtes plus restreint !")
            target.Speed = target.Speed_base
        else:
            target_etat["restrained"] = True
            print(f"{target.name}. Vous êtes restreint !")
            target.Speed = 0
    

    def Incapacited(self, target=None, desapply=False):
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["incapacited"] = False
            print(f"{target.name}. Vous n'êtes plus Incapacité !")
        else:
            target_etat["incapacited"] = True
            print(f"{target.name}. Vous êtes Incapacité !")
            target.Player_Action = 0
            target.Player_Reaction = 0


    def Stunned(self, target=None, desapply=False):
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["stunned"] = False
            print(f"{target.name}. Vous n'êtes plus étourdi !")
            target.Incapacited(self, True)
        else:
            target_etat["stunned"] = True
            print(f"{target.name}. Vous êtes étourdi !")
            target.Incapacited()
        
    def Unconscious(self, target=None, desapply=False):
        ground = []
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["unconscious"] = False
            print(f"{target.name}. Vous n'êtes plus inconscient !")
            target.Incapacited(self, True)
            target.left_arm = ground[0]
            target.right_arm = ground[1]
            ground = None 
        else:
            target_etat["unconscious"] = True
            print(f"{target.name}. Vous êtes inconscient !")
            target.Incapacited()
            ground = [target.left_arm, target.right_arm]
            target.right_arm = None
            target.left_arm = None
    

    def Invisible(self, target=None, desapply=False):
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["invisible"] = False
            print(f"{target.name}. Vous n'êtes plus invisible !")
        else:
            target_etat["invisible"] = True
            print(f"{target.name}. Vous êtes invisible !")


    def Paralysed(self, target=None, desapply=False):
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["paralyzed"] = False
            print(f"{target.name}. Vous n'êtes plus paralysé !")
            target.Incapacited(self, True)
        else:
            target_etat["paralyzed"] = True
            print(f"{target.name}. Vous êtes paralysé !")
            target.Incapacited()


    def Petrified(self, target=None, desapply=False):
        if target == None:
                target = self
        target_etat = target.get_etat()
        if desapply:
            target_etat["petrified"] = False
            print(f"{target.name}. Vous n'êtes plus pétrifier !")
            target.Incapacited(self, True)
            target.Res = target.Res_base
            target.Imun.remove("poison")
        else:
            target_etat["petrified"] = True
            print(f"{target.name}. Vous êtes pétrifier !")
            target.Incapacited()
            for types in type_list:
                target.Res.append(types)
            target.Imun.append("poison")
            # no effect disease

    # Menu
    def Menu(self):
        if not self.etat["lutte"]:
            Action = input(f"C'est à votre tour, vous avez [{self.Player_Action}] Action\n 1°) Attaquer\n 2°) Aider\n 3°) Rechercher\n 4°) Esquiver\n 5°) Se Cacher\n 6°) Se préparer\n 7°) Prise de lutte\n 8°) Passer son tour\n 9°) Un jet de dé banal\n 10°) Regarder son inventaire\n")
            match Action:
                case "1": # Attack
                    Player_party = listing().Player_party
                    target = input(f"Qui que vous ciblez\n Les personnages actuel en combat sont: {Player_party}\n")
                    weapon = input(f"Avec qu'elle arme voulez vous tapez ?\n Bras Gauche: {self.left_arm}\n Bras droit: {self.right_arm}")
                    modifier = input("Y a t'il un désavantage (D) ou un Avantage (A) qui s'applique sur ce jet d'attaque ?")
                    match modifier:
                        case "D":
                            modifier = -1
                            return modifier
                        case "A":
                            modifier = 1
                            return modifier
                        case _:
                            modifier = 0
                            return modifier
                    return self.attack_action(target, weapon, modifier)
                case "2": # Help
                    target = input(f"Qui que vous ciblez\n Les personnages actuel en combat sont: {Player_party}\n")
                    return self.help_action(target)
                case "3": # Search
                    modifier = input("Y a t'il un désavantage (D) ou un Avantage (A) qui s'applique sur ce jet d'attaque ?\n")
                    comp = input(f"Qu'elles compétences voulez vous utilisez pour ce jet de recherche ?\n Liste des compétences lié à l'intelligence ou à la Sagesse: {comp_int, comp_sag}\n")
                    match comp:
                        case "Arcane":
                            comp = self.Arcanes
                            return comp
                        case "Histoire":
                            comp = self.Histoire
                            return comp
                        case "Investigation":
                            comp = self.Investigation
                            return comp
                        case "Nature":
                            comp = self.Nature
                            return comp
                        case "Religion":
                            comp = self.Religion
                            return comp
                        case "Dressage":
                            comp = self.Dressage
                            return comp
                        case "Intuition":
                            comp = self.Intuition
                            return comp
                        case "Medecine":
                            comp = self.Medecine
                            return comp
                        case "Perception":
                            comp =  self.Perception
                            return comp
                        case "Perspicacité":
                            comp = self.Perspicacite
                            return comp
                        case "Survie":
                            comp = self.Survie
                            return comp
                    return self.search_action(modifier, comp)
                case "4": # Esquive
                    print("Vous êtes prêt à esquiver !!\n")
                    return self.dodge_action()
                case "5": # Hide
                    modifier = input("Y a t'il un désavantage (D) ou un Avantage (A) qui s'applique sur ce jet d'attaque ?\n")
                    return self.hide_action(modifier)
                case "6": # Ready
                    print("Vous vous tenez prêt à faire un truc pendant votre Réaction\n")
                    return self.ready_action()
                case "7": # Lutte
                    Player_party = listing().Player_party
                    target = input(f"qui que vous voulez attaquer ? {Player_party}\n")
                    modifier = input("Y a t'il un désavantage (D) ou un Avantage (A) qui s'applique sur ce jet d'attaque ?\n")
                    return self.lutte(target, modifier)
                case "8": # Pass
                    print("vous venez de passer votre tour\n")
                    return self.pass_tour()
                case "9": # jet de dé
                    stat = input("Qu'elles  stats ? For / Dex / Con / Int / Wis / Cha\n")
                    modifier = input("Y a t'il un désavantage (D) ou un Avantage (A) qui s'applique sur ce jet d'attaque ?\n")
                    comp = input(f"Qu'elles compétences voulez vous utilisez pour ce jet ?\n Liste des compétences: {comp_int, comp_sag}\n")
                    match comp:
                        case "Acrobaties":
                            comp = self.Acrobaties
                            return comp
                        case other:
                            print("va te faire foutre recommence\n")
                            return self.Menu()
                    
                    match stat:
                        case "For":
                            self.Player_Action -= 1
                            return self.jet_For(modifier)
                        case "Dex":
                            self.Player_Action -= 1
                            return self.jet_Dex(modifier)
                        case "Con":
                            self.Player_Action -= 1
                            return self.jet_Con(modifier)
                        case "Int":
                            self.Player_Action -= 1
                            return self.jet_Int(modifier)
                        case "Wis":
                            self.Player_Action -= 1
                            return self.jet_Wis(modifier)
                        case "Cha":
                            self.Player_Action -= 1
                            return self.jet_Cha(modifier)
                        case other:
                            print("va te faire foutre recommence\n")
                            return self.Menu()
                case "10": # show inventory
                    return self.show_inventory()


    def Modifier(self, modifier, arme,  target):
        modifier += self.Help  # aide
        modifier += self.lourd  # arme lourde
        if self.etat["prone"]: # desavantage a terre
            modifier -= 1
        target_etat = target.get_etat()
        if target_etat["prone"]: # si cible a terre
            if isinstance(arme, Weapon):
                allonge = arme.get_allonge()
                if allonge <= 1.5:
                    modifier += 1
                else:
                    modifier -= 1
        if target_etat["charmed_name"]:
            print("vous ne pouvez pas attaquez ce bogoss")
            return
        if target_etat["frightened_name"]: # charm limit
            x = input("Es que la personne qui vous effrez est dans votre champs de vision ? (oui ou non)\n")
            if x == "oui": # si personne effrayante champ de vision
                modifier -= 1
        if self.etat["blinded"]: # desavantage aveugle
            modifier -= 1
        if target_etat["blinded"]: # si cible est aveugle
            modifier += 1
        if self.etat["poisoned"]: # empoisonne
            modifier -= 1
        if target_etat["restrained"]:
            modifier += 1
        if self.etat["restrained"]:
            modifier -= 1
        if target_etat["stunned"]:
            modifier += 1
        if target_etat["unconscious"]:
            modifier += 1
        if target_etat["invisible"]:
            modifier -= 1
        if self.etat["invisible"]:
            modifier += 1
        if target_etat["paralyzed"]:
            modifier += 1
        if target_etat["petrified"]:
            modifier += 1
        if self.epuisement <= 3: # epuisement
            modifier += self.debuff_epuisement


    # Action divers
    def pass_tour(self):
        self.Player_Action -= 1
        self.Player_Action_Bonus -= 1

    def dgt_nat_weapon(self):
        self.PV_tot -= self.mod_For + 1
        dgt_type = "contendant"

    def damage(self, arme, bonus=0, crit=1):
        if arme != self.Nat_weapon:
            dmg = (arme.get_Dgt() + bonus)*crit
            if arme.get_dgt_type() in self.Res:
                dmg /= 2
            if arme.get_dgt_type() in self.Imun:
                dmg = 0
            if arme.get_dgt_type() in self.Vul:
                dmg *= 2
            print("Vous avez fait ", dmg, "de dégats à ", self.name)
            self.PV_tot -= dmg

    def attack_action(self, target, arme, modifier=0):
        bonus = self.mod_For
        bonus_dgt = self.mod_For
        self.Modifier(modifier, arme,target)
        cost = 1
        if self.Player_Action > 0:
            if self.left_arm or self.right_arm != None:  # si il y a une arme en main
                if isinstance(arme, Weapon):
                    if arme not in self.left_arm or arme not in self.right_arm:  # si pas arme dans mains
                        print("Erreur")
                        return
                    for prop in arme.get_proprietes():  # si arme finesse
                        match arme.get_proprietes()[prop]:
                            case "finesse":
                                if self.finesse_dex:  # et si finesse dex
                                    bonus = self.mod_Dex  # bonus dex
                                    bonus_dgt = self.mod_Dex  # bonus dgt dex
                            case "chargement":
                                cost = 10
                    if arme in self.prof_weapon:  # si arm proficiency bonus proficiency
                        bonus += self.proficiency
                else:
                    arme = self.Nat_weapon  # sinon attack with naturel weapon
                self.attack_weapon = arme
                jet_attack = d20(modifier) + bonus
                print(f"Jet brut : {jet_attack - bonus}\nBonus d'attaque : {bonus}\nJet final : {jet_attack}")
                if jet_attack - bonus == 20:
                    print("Vous avez réussi un coup critique !")
                    crit = 2
                elif jet_attack - bonus == 1:
                    print("Vous avait fait un désastre !")
                    crit = 1
                else:
                    crit = 1
                    target_etat = target.get_etat()
                    if target_etat["unconscious"] and isinstance(arme, Weapon):
                        allonge = arme.get_allonge()
                        if allonge <= 1.5:
                            crit = 2
                    if target_etat["paralyzed"] and isinstance(arme, Weapon):
                        allonge = arme.get_allonge()
                        if allonge <= 1.5:
                            crit = 2
                    print(f"Votre jet d'attaque = {jet_attack}")
                if jet_attack >= target.get_class_armor():  # si jet > CA
                    print("Vous avez réussi a touché !")
                    if arme == self.Nat_weapon and self.Nat_weapon == None:  # et si Nat_weapon used & = None
                        target.damage(self.Nat_weapon, 0, crit)  # PV target - mod.For
                    else:
                        target.damage(arme, bonus_dgt, crit)
                    self.Player_Action -= cost

    def help_increment(self):
        self.Help += 1

    def help_action(self, target):
        if self.Player_Action > 0:
            target.help_increment()
            self.Player_Action -= 1

    def search_action(self, modifier=0, comp=""):
        if self.Player_Action > 0:
            if self.etat["poisoned"]: # empoisonne
                modifier -= 1
            if comp != "":
                jet = d20(modifier) + comp
                print(jet)
            else:
                x = random.randint(1, 2)
                match x:
                    case 1:
                        jet = d20(modifier) + self.Perception
                        print(jet)
                    case 2:
                        jet = d20(modifier) + self.Investigation
                        print(jet)
            self.Player_Action -= 1

    def dodge_action(self):
        if self.Player_Action > 0:
            self.Dodge += 1
            self.Player_Action -= 1

    # Dash

    def hide_action(self, modifier=""):
        if self.Player_Action > 0:
            jet = d20(modifier) + self.Discretion
            print(jet)
            self.Player_Action -= 1

    # disengage

    def ready_action(self):
        if self.Player_Reaction > 0:
            self.Menu()
            self.Player_Action += 1
            self.Player_Reaction -= 1

    def two_weaponed_attack_AB(self, target,modifier=0):
        bonus = self.mod_For
        arme = None
        cost = 1
        if self.Player_Action_Bonus > 0:
            if isinstance(self.left_arm, Weapon) and isinstance(self.right_arm, Weapon):
                if self.left_arm == self.attack_weapon:  # si arme d'attack
                    arme = self.right_arm
                    self.Modifier(modifier, arme, target)
                    for prop in self.right_arm.get_proprietes():  # si arme finesse
                        match self.right_arm.get_proprietes()[prop]:
                            case "finesse":
                                if self.finesse_dex:  # et si finesse dex
                                    bonus = self.mod_Dex  # bonus dex
                            case "légère":
                                jet = d20(modifier) + bonus
                    if self.right_arm in self.prof_weapon:  # si arm proficiency bonus proficiency
                        bonus += self.proficiency
                elif self.right_arm == self.attack_weapon:
                    arme = self.left_arm
                    self.Modifier(modifier, arme, target)
                    for prop in self.left_arm.get_proprietes():  # si arme finesse
                        match self.left_arm.get_proprietes()[prop]:
                            case "finesse":
                                if self.finesse_dex:  # et si finesse dex
                                    bonus = self.mod_Dex  # bonus dex
                            case "légère":
                                jet = d20(modifier) + bonus
                            case "chargement":
                                cost = 10
                    if self.right_arm in self.prof_weapon:  # si arm proficiency bonus proficiency
                        bonus += self.proficiency

                if jet >= target.get_class_armor():  # si jet >= CA
                    target.damage(arme)
                self.Player_Action_Bonus -= cost

    def contre_lutte(self, modifier=""):
        x=1
        for i in range(x):
            contre_lutte = input("Voulez vous faire un jet d'Athlétisme ou un jet d'Acrobaties pour résister à la lutte ? \n 1°) jet d'Athlétisme \n 2°) jet d'Acrobaties \n 3°) Ne rien faire\n")
            modifier += self.Help # aide
            if self.etat["poisoned"]: # empoisonne
                modifier -= 1
            match contre_lutte:
                case "1":
                    contre_lutte = d20(modifier) + self.Athletisme
                    return contre_lutte
                case "2":
                    contre_lutte = d20(modifier) + self.Acrobaties
                    return contre_lutte
                case "3":
                    contre_lutte = 0
                    return contre_lutte
                case other:
                    x += 1
                    print("vous avez fait une erreur !")
            
    def lutte(self, target=None, modifier=""):
        x=1
        Player_party = listing().Player_party
        if target is None:
            target = self
        for i in range(x): # Boucle pour etre sure de la cible
            target = input(f"Ils faut choisir ine cible existante dans cette liste :\n{Player_party}\n")
            if target not in Player_party:
                x+=1
                print("je veux un vrai joueur")

        global taille_list
        modifier += self.Help  # aide
        if self.etat["poisoned"]: # empoisonne
            modifier -= 1
        if self.Player_Action > 0 and taille_list.index(target.get_size()) <= self.size and self.left_arm or self.right_arm == None:
            jet = d20(modifier) + self.Athletisme
        target.contre_lutte()
        if target.contre_lutte <= jet:
            self.Grappled()



    # inventaire
    def add_item(self, item):
        if self.Charge + item.get_poids() < self.CC:
            self.inventory.append(item)
            self.Charge += item.get_poids()
        else:
            print("Vous n'avez plus d'espace dans l'inventaire.")

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.Charge -= item.get_poids()
        else:
            print("Cet objet n'est pas dans l'inventaire.")

    def show_inventory(self):
        if self.inventory:
            print("Inventaire de", self.name + ":")
            for item in self.inventory:
                print("-", item.name)
        else:
            print("L'inventaire de", self.name, "est vide.")

    def equip_weapon(self, weapon):
        if weapon in self.inventory:
            for prop in self.left_arm.get_proprietes():
                match prop:
                    case "deux mains":
                        self.left_arm = None
                        self.right_arm = None
            if self.left_arm == None:
                self.left_arm = weapon
                print("Arme équipée :", weapon.name, " en main gauche")
            elif self.right_arm == None:
                self.right_arm = weapon
                print("Arme équipée :", weapon.name, " en main droite")
            elif self.left_arm != None:
                self.left_arm = weapon
                print("Arme équipée :", weapon.name, " en main gauche")
            
            for prop in weapon:
                match weapon.get_proprietes()[prop]:
                    case "deux mains":
                        self.left_arm = weapon
                        self.right_arm = weapon
                    case "lourd":
                        if self.size == "P" or "TP":
                            self.lourd -= 1
                        return
                    case "polyvalent":
                        if self.left_arm and self.right_arm == weapon:
                            weapon.get_dgt()[0] += 2 
        else:
            print("Cet objet n'est pas dans l'inventaire.")

    def unequip_weapon(self, arm):
        match arm:
            case "gauche":
                self.left_arm = None
                print("vous n'avez plus d'arme dans la main gauche")
            case "droite":
                self.right_arm = None
                print("vous n'avez plus d'arme dans la main droite")

    def equip_armor(self, armor):
        if armor in self.inventory:
            self.equiped_armor = armor
            print("Armure équipée :", armor.get_name())
        else:
            print("Cet objet n'est pas dans l'inventaire.")

    def unequip_armor(self):
        self.equip_armor = None
        print("vous n'avez plus d'armure équipée")

    def equip_backpack(self, backpack):
        if backpack in self.inventory and backpack.get_categories() == "backpack":
            self.CC += backpack.get_proprietes()
            self.Charge -= backpack.get_poids()
            self.equip_backpack = backpack
            print("Stockage équipée :", backpack.get_name())
        else:
            print("Cet objet n'est pas dans l'inventaire.")

    def unequip_backpack(self):
        self.equiped_backpack = None
        print("vous n'avez plus de stockage équipée")
    

    # Verif limite
    def verif_lim(self):
        x = 0
        for i in self.attributes:
            if i < self.limite[x]:
                self.attributes[x] = self.limite[x]
            x += 1

    # get competence et initiative
    def get_initiative(self):
        return self.initiative
    
    def get_acrobaties(self):
        return self.Acrobaties
    
    def get_arcanes(self):
        return self.Arcanes
    
    def get_athletisme(self):
        return self.Athletisme
    
    def get_discretion(self):
        return self.Discretion
    
    def get_dressage(self):
        return self.Dressage
    
    def get_escamotage(self):
        return self.Escamotage
    
    def get_histoire(self):
        return self.Histoire
    
    def get_intimidation(self):
        return self.Intimidation
    
    def get_intuition(self):
        return self.Intuition
    
    def get_investigation(self):
        return self.Investigation
    
    def get_medecine(self):
        return self.Medecine
    
    def get_nature(self):
        return self.Nature
    
    def get_perception(self):
        return self.Perception
    
    def get_perspicacite(self):
        return self.Perspicacite
    
    def get_persuasion(self):
        return self.Persuasion
    
    def get_religion(self):
        return self.Religion
    
    def get_representation(self):
        return self.Representation
    
    def get_survie(self):
        return self.Survie
    
    def get_tromperie(self):
        return self.Tromperie
    
    def get_sag_perception_pass(self):
        return self.Sag_Perception_Pass
    
    def get_sag_intuition_pass(self):
        return self.Sag_Intuition_Pass