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
        self.Helm_ep = []
        self.chest_ep = []
        self.legs_ep = []
        self.boots_ep = []
        self.gloves_ep = []
        self.right_hand = []
        self.left_hand = []
        self.pop_inv()

        self.health_mod = 10
        self.max_health = self.level * self.health_mod
        self.health_act = self.max_health

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
            self.add_to_inv(weapon)


    def add_to_inv(self,item):
            if len(self.inventory) < self.inventory_max:
                self.inventory.append(item)
            else:
                print("you have to many items in your inventory")
                return





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
            self.atklist = ["normal", "med", "strong"]
            self.stamina = random.randint(5,15)
            self.agi = random.randint(5,10)
            self.iq = random.randint(1,10)
            self.deff = random.randint(5,15)
            self.atk = random.randint(5,20)
        if self.playerclass == "Scholar":
            self.atklist = ["normal", "med", "strong"]
            self.stamina = random.randint(5,10)
            self.iq = random.randint(5,20)
            self.atk = random.randint(5,10)
        if self.playerclass == "Elk":
            self.atklist = ["normal", "med", "strong"]
            self.deff = random.randint(10,15)
            self.atk = random.randint(10,20)
            self.iq = random.randint(1,5)
            self.agi = random.randint(5,15)
            self.stamina = random.randint(5, 15)
        if self.playerclass == "Killer":
            self.atklist = ["normal", "med", "strong"]
            self.atk = random.randint(20,25)
            self.luck = random.randint(5,15)
            self.iq = 10
            self.stamina = random.randint(5, 15)
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
            self.luck += 2
            self.deff += 2
            self.atk += 2
        if self.race == "Dwarf":
            self.stamina += 2
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

    def add_exp(self, xp):
        print("picked up " +str(xp) + " xp")
        self.exp += xp
        if self.exp >= self.level_up:
            self.levelUp()

    def equip_gloves(self):
        for i in self.inventory:
            x = type(i)
            if "Gloves" in str(x):
                if len(self.gloves_ep) < 1:
                    print("you equipped a set of gloves")
                    print(i)
                    self.gloves_ep.append(i)
                    self.inventory.remove(i)
                    self.deff += self.gloves_ep[0].armor
                    self.deff += self.gloves_ep[0].stamina
                    self.deff += self.gloves_ep[0].luck
                    self.deff += self.gloves_ep[0].iq
                    self.deff += self.gloves_ep[0].agi
                else:
                    print("you need to remove your equipped gloves first")
                    print("you are wearing a pair of gloves")
                    print(self.gloves_ep[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your gloves")
                            self.deff -= self.gloves_ep[0].armor
                            self.stamina -= self.gloves_ep[0].stamina
                            self.luck -= self.gloves_ep[0].luck
                            self.iq -= self.gloves_ep[0].iq
                            self.agi -= self.gloves_ep[0].agi
                            self.gloves_ep.remove(self.gloves_ep[0])
                            self.gloves_ep.append(i)
                            self.inventory.remove(i)
                            self.deff += self.gloves_ep[0].armor
                            self.deff += self.gloves_ep[0].stamina
                            self.deff += self.gloves_ep[0].luck
                            self.deff += self.gloves_ep[0].iq
                            self.deff += self.gloves_ep[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_chest(self):
        for i in self.inventory:
            x = type(i)
            if "Chest" in str(x):
                if len(self.chest_ep) < 1:
                    print("you equipped a set of chest")
                    print(i)
                    self.chest_ep.append(i)
                    self.inventory.remove(i)
                    self.deff += self.chest_ep[0].armor
                    self.deff += self.chest_ep[0].stamina
                    self.deff += self.chest_ep[0].luck
                    self.deff += self.chest_ep[0].iq
                    self.deff += self.chest_ep[0].agi
                else:
                    print("you need to remove your equipped chest first")
                    print("you are wearing a chest")
                    print(self.chest_ep[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your chest")
                            self.deff -= self.chest_ep[0].armor
                            self.stamina -= self.chest_ep[0].stamina
                            self.luck -= self.chest_ep[0].luck
                            self.iq -= self.chest_ep[0].iq
                            self.agi -= self.chest_ep[0].agi
                            self.chest_ep.remove(self.chest_ep[0])
                            self.chest_ep.append(i)
                            self.inventory.remove(i)
                            self.deff += self.chest_ep[0].armor
                            self.deff += self.chest_ep[0].stamina
                            self.deff += self.chest_ep[0].luck
                            self.deff += self.chest_ep[0].iq
                            self.deff += self.chest_ep[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_helm(self):
        for i in self.inventory:
            x = type(i)
            if "Helm" in str(x):
                if len(self.Helm_ep) < 1:
                    print("you equipped a set of Helm")
                    print(i)
                    self.Helm_ep.append(i)
                    self.inventory.remove(i)
                    self.deff += self.Helm_ep[0].armor
                    self.deff += self.Helm_ep[0].stamina
                    self.deff += self.Helm_ep[0].luck
                    self.deff += self.Helm_ep[0].iq
                    self.deff += self.Helm_ep[0].agi
                else:
                    print("you need to remove your equipped Helm first")
                    print("you are wearing a Helm")
                    print(self.Helm_ep[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your Helm")
                            self.deff -= self.Helm_ep[0].armor
                            self.stamina -= self.Helm_ep[0].stamina
                            self.luck -= self.Helm_ep[0].luck
                            self.iq -= self.Helm_ep[0].iq
                            self.agi -= self.Helm_ep[0].agi
                            self.Helm_ep.remove(self.Helm_ep[0])
                            self.Helm_ep.append(i)
                            self.inventory.remove(i)
                            self.deff += self.Helm_ep[0].armor
                            self.deff += self.Helm_ep[0].stamina
                            self.deff += self.Helm_ep[0].luck
                            self.deff += self.Helm_ep[0].iq
                            self.deff += self.Helm_ep[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_legs(self):
        for i in self.inventory:
            x = type(i)
            if "Legs" in str(x):
                if len(self.legs_ep) < 1:
                    print("you equipped a set of Legs")
                    print(i)
                    self.legs_ep.append(i)
                    self.inventory.remove(i)
                    self.deff += self.legs_ep[0].armor
                    self.deff += self.legs_ep[0].stamina
                    self.deff += self.legs_ep[0].luck
                    self.deff += self.legs_ep[0].iq
                    self.deff += self.legs_ep[0].agi
                else:
                    print("you need to remove your equipped Legs first")
                    print("you are wearing a pair of Legs")
                    print(self.legs_ep[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your Legs")
                            self.deff -= self.legs_ep[0].armor
                            self.stamina -= self.legs_ep[0].stamina
                            self.luck -= self.legs_ep[0].luck
                            self.iq -= self.legs_ep[0].iq
                            self.agi -= self.legs_ep[0].agi
                            self.legs_ep.remove(self.legs_ep[0])
                            self.legs_ep.append(i)
                            self.inventory.remove(i)
                            self.deff += self.legs_ep[0].armor
                            self.deff += self.legs_ep[0].stamina
                            self.deff += self.legs_ep[0].luck
                            self.deff += self.legs_ep[0].iq
                            self.deff += self.legs_ep[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_boots(self):
        for i in self.inventory:
            x = type(i)
            if "Boots" in str(x):
                if len(self.boots_ep) < 1:
                    print("you equipped a set of Boots")
                    print(i)
                    self.boots_ep.append(i)
                    self.inventory.remove(i)
                    self.deff += self.boots_ep[0].armor
                    self.deff += self.boots_ep[0].stamina
                    self.deff += self.boots_ep[0].luck
                    self.deff += self.boots_ep[0].iq
                    self.deff += self.boots_ep[0].agi
                else:
                    print("you need to remove your equipped Boots first")
                    print("you are wearing a pair of Boots")
                    print(self.boots_ep[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your Boots")
                            self.deff -= self.boots_ep[0].armor
                            self.stamina -= self.boots_ep[0].stamina
                            self.luck -= self.boots_ep[0].luck
                            self.iq -= self.boots_ep[0].iq
                            self.agi -= self.boots_ep[0].agi
                            self.boots_ep.remove(self.boots_ep[0])
                            self.boots_ep.append(i)
                            self.inventory.remove(i)
                            self.deff += self.boots_ep[0].armor
                            self.deff += self.boots_ep[0].stamina
                            self.deff += self.boots_ep[0].luck
                            self.deff += self.boots_ep[0].iq
                            self.deff += self.boots_ep[0].agi
                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_all(self):
        self.equip_helm()
        self.equip_chest()
        self.equip_legs()
        self.equip_gloves()
        self.equip_boots()
        self.equip_Weapon()

    def equip_Weapon(self):
        for i in self.inventory:
            print(i)
            x = type(i)
            if "Sword" in str(x) or "Ax" in str(x) or "Dagger" in str(x) or "Horns" in str(x):
            #if i.eq_type == "Weapon":
                while True:
                    x = input("would you like to equip the weapon in your right or left hand")
                    if x == "right":
                        if len(self.right_hand) < 1:
                            print("you equipped a weapon in your right hand")
                            print(i)
                            self.right_hand.append(i)
                            self.inventory.remove(i)
                            self.atk += self.right_hand[0].attack
                            self.luck += self.right_hand[0].luck
                            self.stamina += self.right_hand[0].stamina
                            self.iq += self.right_hand[0].iq
                            self.agi += self.right_hand[0].agi
                            break
                        else:
                            print("you already have a weapon in that hand")
                            print(self.right_hand[0])
                            print("would you like replace it with")
                            print(i)
                            while True:
                                x = input("yes or no")
                                if x == "yes":
                                    print("you have replace your right hand weapon")
                                    self.atk -= self.right_hand[0].attack
                                    self.luck -= self.right_hand[0].luck
                                    self.stamina-= self.right_hand[0].stamina
                                    self.iq -= self.right_hand[0].iq
                                    self.agi -= self.right_hand[0].agi
                                    self.right_hand.remove(self.right_hand[0])
                                    self.right_hand.append(i)
                                    self.inventory.append(i)
                                    self.atk += self.right_hand[0].attack
                                    self.luck += self.right_hand[0].luck
                                    self.stamina += self.right_hand[0].stamina
                                    self.iq += self.right_hand[0].iq
                                    self.agi += self.right_hand[0].agi
                                    break
                                if x == "no":
                                    self.inventory.append(i)
                                    break
                    elif x == "left":
                        if len(self.left_hand) < 1:
                            print("you equipped a weapon in your left hand")
                            print(i)
                            self.left_hand.append(i)
                            self.inventory.remove(i)
                            self.atk += self.left_hand[0].attack
                            self.luck += self.left_hand[0].luck
                            self.stamina += self.left_hand[0].stamina
                            self.iq += self.left_hand[0].iq
                            self.agi += self.left_hand[0].agi
                            break
                        else:
                            print("you already have a weapon in that hand")
                            print(self.left_hand[0])
                            print("would you like replace it with")
                            print(i)
                            while True:
                                x = input("yes or no")
                                if x == "yes":
                                    print("you have replace your left hand weapon")
                                    self.atk -= self.left_hand[0].attack
                                    self.luck -= self.left_hand[0].luck
                                    self.stamina -= self.left_hand[0].stamina
                                    self.iq -= self.left_hand[0].iq
                                    self.agi -= self.left_hand[0].agi
                                    self.left_hand.remove(self.left_hand[0])
                                    self.left_hand.append(i)
                                    self.inventory.append(i)
                                    self.atk += self.left_hand[0].attack
                                    self.luck += self.left_hand[0].luck
                                    self.stamina += self.left_hand[0].stamina
                                    self.iq += self.left_hand[0].iq
                                    self.agi += self.left_hand[0].agi
                                    break
                                if x == "no":
                                    self.inventory.append(i)
                                    break
                    else:
                        print("not an option")

    def use_hp_Potion(self):
        for i in self.inventory:
            if i == "Health potion":
                self.health_act = self.max_health
                self.inventory.remove(i)
                return

    def Attack_turn(self):
        roll = random.randint(1,6)
        if roll == 1:
            print(self.name,"Missed")
            return 0
        roll = random.randint(1,12)
        if self.playerclass == "Warrior":
            for i in range((self.atklist)):
                print(i + 1, self.atklist[i])
            while True:
                x = input("What attack would you like to use 1 2 3 or 4  use a health potion")
                if x == "1":
                    attk = ((self.atk + self.stamina)*roll)*.1
                    break
                elif x == "2" and self.stamina > 10:
                    attk = ((self.atk + self.stamina)*roll)*.2
                    self.stamina -= 10
                    break
                elif x == "3" and self.stamina > 20:
                    attk = ((self.atk + self.stamina)*roll)*.3
                    self.stamina -= 20
                    break
                elif x == "4":
                    self.use_hp_Potion()
                    break
                else:
                    print("not an option")
        elif self.playerclass == "Scholar":
            for i in range(len(self.atklist)):
                print(i + 1, self.atklist[i])
            while True:
                x = input("What attack would you like to use 1 2 3 or 4  use a health potion")
                if x == "1":
                    attk = ((self.atk + self.iq)*roll)*.1
                    break
                elif x == "2" and self.iq > 10:
                    attk = ((self.atk + self.iq)*roll)*.2
                    self.iq -= 10
                    break
                elif x == "3" and self.iq > 20:
                    attk = ((self.atk + self.iq)*roll)*.3
                    self.iq -= 20
                    break
                elif x == "4":
                    self.use_hp_Potion()
                    break
                else:
                    print("not an option")
        elif self.playerclass == "Elk":
            for i in range(len(self.atklist)):
                print(i + 1, self.atklist[i])
            while True:
                x = input("What attack would you like to use 1 2 3 or 4  use a health potion")
                if x == "1":
                    attk = ((self.atk + self.stamina)*roll)*.1
                    break
                elif x == "2" and self.stamina > 10:
                    attk = ((self.atk + self.stamina)*roll)*.2
                    self.stamina -= 10
                    break
                elif x == "3" and self.stamina > 20:
                    attk = ((self.atk + self.stamina)*roll)*.3
                    self.stamina -= 20
                    break
                elif x == "4":
                    self.use_hp_Potion()
                    break
                else:
                    print("not an option")
        elif self.playerclass == "Killer":
            for i in range(len(self.atklist)):
                print(i + 1, self.atklist[i])
            while True:
                x = input("What attack would you like to use 1 2 3 or 4  use a health potion")
                if x == "1":
                    attk = ((self.atk + self.luck)*roll)*.1
                    break
                elif x == "2" and self.luck > 10:
                    attk = ((self.atk + self.luck)*roll)*.2
                    self.luck -= 1
                    break
                elif x == "3" and self.luck > 20:
                    attk = ((self.atk + self.luck)*roll)*.3
                    self.luck -= 2
                    break
                elif x == "4":
                    self.use_hp_Potion()
                    break
                else:
                    print("not an option")
        roll = random.randint(1,20)
        if roll == 12:
             attk = attk*3
        print(self.name, "did", attk, "damage")
        return attk

    def defend(self, damage):
        dmg = damage
        roll = random.randint(1,20)
        if roll == 20:
            print("Blocked")
            dmg = 0
        if self.playerclass == "Warrior":
            block = ((self.deff + self.agi)*roll)*0.1
        elif self.playerclass == "Scholar":
            block = ((self.deff + self.agi)*roll)*0.1
        elif self.playerclass == "Elk":
            block = ((self.deff + self.agi)*roll)*0.1
        elif self.playerclass == "Killer":
            block = ((self.deff + self.luck)*roll)*0.1
        print(self.name,"blocked", block,"damage")
        dmg_dealt = dmg - block
        if dmg_dealt >= 0:
            self.health_act = self.health_act - dmg_dealt
        if self.health_act <= 0:
            self.alive = False