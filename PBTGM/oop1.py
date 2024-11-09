class hero:  # template
    pass

hero1 = hero()  # object / instance
hero2 = hero()
hero3 = hero()

hero1.name = "Sniper"
hero1.health = 100

hero2.name = "Sven"
hero2.health = 100

hero3.name = "Daffa"
hero3.health = 10

print(hero1)
print(hero1.__dict__)  
print(hero1.name)