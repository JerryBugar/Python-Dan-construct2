class hero: #template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.health = inputHealth
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor

hero1 = hero("Arka", 100, 10, 4)
hero2 = hero("Revaldo", 100, 10, 4)
hero3 = hero("Jepri", 1000, 20, 5)
hero4 = hero("Oktavia", 2000, 5, 2)
hero5 = hero("Bima", 150, 12, 3)
hero6 = hero("Citra", 120, 15, 6)
hero7 = hero("Dewi", 180, 18, 7)
hero8 = hero("Eko", 130, 14, 4)
hero9 = hero("Fajar", 110, 11, 2)
hero10 = hero("Gilang", 160, 16, 5)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero4.__dict__)
print(hero5.__dict__)
print(hero6.__dict__)
print(hero7.__dict__)
print(hero8.__dict__)
print(hero9.__dict__)
print(hero10.__dict__)

print(hero.__dict__)