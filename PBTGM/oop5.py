class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)
    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa : ' + str(round(attack_diterima, 2)))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(round(self.health, 2)))

class Tim:
    def __init__(self, nama):
        self.nama = nama
        self.anggota = []

    def tambah_anggota(self, hero):
        self.anggota.append(hero)

jefri = Hero('jefri', 100, 50, 5)
yahya = Hero('yahya', 100, 37, 10)
revaldo = Hero('revaldo', 100, 55, 4)
arka = Hero('arka', 100, 23, 6)

tim1 = Tim('Tim 1')
tim1.tambah_anggota(jefri)
tim1.tambah_anggota(revaldo)

tim2 = Tim('Tim 2')
tim2.tambah_anggota(yahya)
tim2.tambah_anggota(arka)

tim1.anggota[0].serang(tim2.anggota[0])
print('\n')
tim2.anggota[0].serang(tim1.anggota[1])
print('\n')
tim1.anggota[1].serang(tim2.anggota[1])