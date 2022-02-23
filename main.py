import random
class Speler:
    def __init__(self,naam,levenspunten,acties):
        self.naam = naam
        self.levenspunten = levenspunten
        self.acties = acties
    def toon_acties(self):
        tel = 1
        for x in self.acties:
            print(tel,x)
            tel = tel +1

class Vijand:
    def __init__(self,naam, levenspunten,acties):
        self.naam = naam
        self.levenspunten = levenspunten
        self.acties = acties

class Actie:
    def __init__(self,naam,levenspunten,aanvalspunten):
        self.naam = naam
        self.levenspunten = levenspunten
        self.aanvalspunten = aanvalspunten
    def __str__(self):
        return "{}: Healkracht {}, Aanvalskracht {}".format(self.naam,self.levenspunten,self.aanvalspunten)


class Gevecht:
    def __init__(self,id,speler,vijand):
        self.id = id
        self.speler = speler
        self.vijand = vijand

    def battle(self):
        while(self.vijand.levenspunten > 0 and self.speler.levenspunten > 0):
            print("Levenspunten speler: {}\nLevenspunten vijand: {}".format(self.speler.levenspunten,self.vijand.levenspunten))
            print(s.toon_acties())
            actie_speler = int(input("geef een actie in"))
            self.speler.levenspunten += self.speler.acties[actie_speler-1].levenspunten
            self.vijand.levenspunten -= self.speler.acties[actie_speler-1].aanvalspunten
            r = random.randint(0,4)
            self.vijand.levenspunten +=self.vijand.acties[r-1].levenspunten
            self.speler.levenspunten -= self.vijand.acties[r-1].aanvalspunten

        if(self.speler.levenspunten > 0):
            print("speler heeft gewonnen")
        else:
            print("Vijand heeft gewonnen")

a1 = Actie("Basis aanval",0,150)
a2 = Actie("Vuurbal",-50,200)
a3 = Actie("Basis Heal",200,0)
a4 = Actie("Zwaard aanval",-50,300)
a5 = Actie("Inferno",-100,400)
a6 = Actie("Balans",100,100)
a7 = Actie("Gedaan",0,5000)

aanvallen_speler = [a1,a3,a4,a6,a7]
aanvallen_vijand = [a2,a3,a5,a6]


s = Speler("Red Knight",200,aanvallen_speler)
v = Vijand("Black Dragon",1200,aanvallen_vijand)

g = Gevecht("G1",s,v)
g.battle()

