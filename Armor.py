import random


class Equipment (object):
    RARITY = ["Poor", "Common", "Rare", "Legendary", "Divine"]
    def __init__(self,eqTpye):
        self.rarity_lv, self.rare_mod = self.pick_rare()
        self.eq_type = eqTpye

    def pick_rare(self):
        x = random.randint(1,10)
        if 1 <= x <= 2:
            return Equipment.RARITY[0], 2
        elif 2 < x <= 5:
            return Equipment.RARITY[1], 4
        elif 5 < x <= 7:
            return Equipment.RARITY[2], 8
        elif 7 < x <= 9:
            return Equipment.RARITY[3], 16
        elif x == 10:
            return Equipment.RARITY[4], 32

class Armor(Equipment):
    ARMORTYPE = ["Helm", "Chest", "Legs", "Boots", "Gloves"]

    def __init__(self,aType):
        super(Armor,self).__init__("Armor")
        self.armor_type = aType
        self.armor = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0


    def __str__(self):
        return"""
        armorType: {}
        Rarity Level: {}
        Armor: {}
        Luck:{}
        Stamina: {}
        IQ: {}
        Agility: {}""".format(self.armor_type, self.rarity_lv, self.armor, self.luck, self.stamina, self.iq, self.agi)

class Helm(Armor):
    def __init__(self):
        super(Helm,self).__init__(Armor.ARMORTYPE[0])
        self.armor = random.randint(5,10) *self.rare_mod
        self.stamina = random.randint(0,8) +self.rare_mod
        self.agi = random.randint(0, 8) + self.rare_mod
        self.iq = random.randint(0, 8) + self.rare_mod
        self.luck = random.randint(0, 8) + self.rare_mod

class Chest(Armor):
    def __init__(self):
        super(Chest,self).__init__(Armor.ARMORTYPE[1])
        self.armor = random.randint(10,20) *self.rare_mod
        self.stamina = random.randint(0,5) +self.rare_mod
        self.agi = random.randint(0, 5) + self.rare_mod
        self.iq = random.randint(0, 5) + self.rare_mod
        self.luck = random.randint(0, 5) + self.rare_mod

class Legs(Armor):
    def __init__(self):
        super(Legs,self).__init__(Armor.ARMORTYPE[2])
        self.armor = random.randint(6,15) *self.rare_mod
        self.stamina = random.randint(0,10) +self.rare_mod
        self.agi = random.randint(0, 8) + self.rare_mod
        self.iq = random.randint(0, 8) + self.rare_mod
        self.luck = random.randint(0, 8) + self.rare_mod

class Boots(Armor):
    def __init__(self):
        super(Boots,self).__init__(Armor.ARMORTYPE[3])
        self.armor = random.randint(1,5) *self.rare_mod
        self.stamina = random.randint(0,2) +self.rare_mod
        self.agi = random.randint(0, 2) + self.rare_mod
        self.iq = random.randint(0, 2) + self.rare_mod
        self.luck = random.randint(0, 2) + self.rare_mod

class Gloves(Armor):
    def __init__(self):
        super(Gloves,self).__init__(Armor.ARMORTYPE[4])
        self.armor = random.randint(1,5) *self.rare_mod
        self.stamina = random.randint(0,2) +self.rare_mod
        self.agi = random.randint(0, 2) + self.rare_mod
        self.iq = random.randint(0, 2) + self.rare_mod
        self.luck = random.randint(0, 2) + self.rare_mod

class Weapon(Equipment):
    WEAPONTYPE = ["Sword","Ax", "Dagger", "Horns"]
    def __init__(self, aType):
        super(Weapon, self).__init__("Weapon")
        self.weapon_type = aType
        self.attack = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return """
        Weapon Type: {}
        Rarity Level: {}
        Attack: {}
        Luck: {}
        Stamina: {}
        IQ: {}
        Agility: {}""".format(self.weapon_type, self.rarity_lv, self.attack, self.luck, self.stamina, self.iq,
                                      self.agi)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(Weapon.WEAPONTYPE[0])
        self.attack = random.randint(10,20) *self.rare_mod
        self.stamina = random.randint(0,5) +self.rare_mod
        self.agi = random.randint(0, 5) + self.rare_mod
        self.iq = random.randint(0, 5) + self.rare_mod
        self.luck = random.randint(0, 5) + self.rare_mod

class Ax(Weapon):
    def __init__(self):
        super(Ax, self).__init__(Weapon.WEAPONTYPE[1])
        self.attack = random.randint(10,20) *self.rare_mod
        self.stamina = random.randint(0,10) +self.rare_mod
        self.agi = random.randint(0, 5) + self.rare_mod
        self.iq = random.randint(0, 5) + self.rare_mod
        self.luck = random.randint(0, 5) + self.rare_mod

class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__(Weapon.WEAPONTYPE[2])
        self.attack = random.randint(1, 10) *self.rare_mod
        self.stamina = random.randint(0,5) +self.rare_mod
        self.agi = random.randint(0, 5) + self.rare_mod
        self.iq = random.randint(0, 5) + self.rare_mod
        self.luck = random.randint(0, 20) + self.rare_mod

class Horns(Weapon):
    def __init__(self):
        super(Horns, self).__init__(Weapon.WEAPONTYPE[3])
        self.attack = random.randint(10,100) *self.rare_mod
        self.stamina = random.randint(0,10) +self.rare_mod
        self.agi = random.randint(0, 10) + self.rare_mod
        self.iq = random.randint(0, 10) + self.rare_mod
        self.luck = random.randint(0, 10) + self.rare_mod