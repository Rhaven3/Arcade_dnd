from Class.Character import Character

class Fighter(Character):
    def __init__(self, name, lvl, historique, race, age, taille, yeux, peau, cheveux, poids, For, Dex, Con, Int, Wis, Cha):
        self.class_name = "Guerrier"
        super().__init__( name, lvl, historique, race, age, taille, yeux, peau, cheveux, poids, For, Dex, Con, Int, Wis, Cha)

        # Stats
        self.DV = 10
