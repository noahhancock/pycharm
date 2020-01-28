import random
from Armor import *
class Hero(object):
    race_list = ["Human","Elf","Dwarf","Elk"]
    class_list = ["Warrior","Scholar","Killer","Elk"]
    def __init__(self):
        self.alive= True
        self.name= ""
        self.name= self.enter_name()

        self.level= 1
        self.exp= 0
        self.level_up= 90 + (self.level*10)

        self.race= self.pick_race()
        self.playerclass= self.pick_class()

        self.deff= 0
        self.atk= 0
        self.mana_mod= 10
        self.luck= 0
        self.stamina= 0
        self.iq= 0
        self.agi= 0
        self.attack_list= []
        self.set_mods()


        self.inventory= []
        self.inventory_max= 10
        self.head= []
        self.chest= []
        self.legs= []
        self.boots= []
        self.gloves= []
        self.right_hand= []
        self.left_hand= []
        self.pop_inv()

    def pop_inv(self):
            x = random.randint(0,3)
            for i in range(x):
                self.inventory.append("Health potion")
            helm = Helm()
            chest = Chest()
            legs = Legs()
            boots = Boots()
            gloves = Gloves()
            x = random.randint(0,3)
            if x == 0:
                weapon = Sword()
            elif x == 1:
                weapon = Ax()
            elif x == 2:
                weapon = Dagger()
            elif x == 3:
                weapon = Horns()
            self.add_to_inv(helm)
            self.add_to_inv(chest)
            self.add_to_inv(legs)
            self.add_to_inv(boots)
            self.add_to_inv(gloves)


        def add_to_inv(self,item):
            if len(self.inventory) < self.inventory_max:
                self.inventory.append(item)
            else:
                print("you have to many items in your inventory")
                return



        self.health_mod = 10
        self.max_health = self.level * self.health_mod
        self.health_act = self.max_health

    def __str__(self):
        return"""
        Name: {} \t Race: {} \t Class: {} \t Level: {}
        Atack: {}
        Deffence: {}
        Luck: {}
        Stamina: {}
        IQ: {}
        Agility: {} """.format(self.name,self.race,self.playerclass,self.level,self.atk,self.deff,self.luck,self.stamina,self.iq,self.agi)

    def pick_race(self):
        while True:
            try:
                print(Hero.race_list)
                x = input("pick your Race ")
                if x in Hero.race_list:
                    return x
            except:
                print("not a good option")

    def pick_class(self):
        while True:
            try:
                print(Hero.class_list)
                x = input("pick your Class ")
                if x in Hero.class_list:
                    return x
            except:
                print("not a good option")


    def enter_name(self):
        while self.name == "":
            self.name = input("What is this characters name ")

    def set_mods(self):
        if self.playerclass == "Warrior":
            self.stamina = random.randint(5,15)
            self.agi = random.randint(5,10)
            self.iq = random.randint(1,10)
            self.deff = random.randint(5,15)
            self.atk = random.randint(5,20)
        if self.playerclass == "Scholar":
            self.stamina = random.randint(5,10)
            self.iq = random.randint(5,20)
            self.atk = random.randint(5,10)
        if self.playerclass == "Elk":
            self.deff = random.randint(10,15)
            self.atk = random.randint(10,20)
            self.iq = random.randint(1,5)
            self.agi = random.randint(5,15)
        if self.playerclass == "Killer":
            self.atk = random.randint(20,25)
            self.luck = random.randint(5,15)
            self.iq = 10
        if self.race == "Human":
            self.stamina += 2
            self.agi += 2
            self.iq += 2
            self.luck += 2
            self.deff += 2
            self.atk += 2
        if self.race == "Elf":
            self.stamina += 8
            self.iq += 4
        if self.race == "Dwarf":
            self.iq -= 2
            self.deff += 4
        if self.race == "Elk":
            self.stamina += 10
            self.agi += 10
            self.iq += 100
            self.luck += 15
            self.deff += 20
            self.atk += 20

    def Die(self, winner):
        self.alive= False
        drop_xp = 10 *self.level
        #winner.givexp(drop_xp)
        print(drop_xp)
        item =random.choice(self.inventory)
        print(item)
       # winner.giveitem(item)

    def levelUp(self):
        print("You have leveled up")
        if self.exp >= self.level_up:
            self.level += 1
            rem_xp = self.exp - self.level_up
            self.exp = rem_xp
            self.level_up = 90 + (self.level * 10)
            self.health_mod += self.level
            self.max_health = self.level * self.health_mod
            self.health_act = self.max_health
            self.mana_mod += self.level
            self.lev_up_mod()
            self.__str__()

    def lev_up_mod(self):
        points = random.randint(1,self.level//2 + 1)
        while points > 0:
            print("""
            Luck: {}
            Stamina: {}
            IQ: {}
            Agility: {}""".format(self.luck,self.stamina,self.iq,self.agi))
            x = input("What Stat would you like to add points to: ")
            y = 0
            while y== 0:
                try:
                    y = int(input(" you have "+ str(points) +" points to spend. how many would you like to put in " + x + ": "))
                except:
                    print("that wasn't a number")
            if y <=points:
                if x == "Stamina":
                    self.stamina += y
                    points -= y
                elif x == "Luck":
                    self.luck += y
                    points -= y
                elif x == "IQ":
                    self.iq += y
                    points -= y
                elif x == "Agility":
                    self.agi += y
                    points -= y
                else:
                    print("Not an option")
            else:
                print("you don't have that many points")

    def add_exp(self,xp):
        print("picked up " +str(xp) + " xp")
        self.exp += xp
        if self.exp >= self.level_up:
            self.levelUp()
    def equip_golves(self):
        if len(self.gloveseq) < 1:
            for i in self.inventory:
                x = type(i)
                if "Gloves" in str(x):
                    print("you equiped a set of gloves")
                    print(i)
                    self.gloveseq