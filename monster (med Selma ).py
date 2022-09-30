from random import randint

class Monster:
    def __init__(self,navn,helse,styrke,svakhet):
        self.navn = navn
        self.helse = helse
        self.styrke = styrke
        self.svakhet = svakhet
        self.forfall = 10
        self.inventory = []

    def sloss(self):
        self.helse = self.helse - self.forfall
        if (self.helse <= 0):
            print("du er død :(")
            pass
    
    def oppStyrke(self,pluss):
        print("Mat, søvn og trening gjør underverker. Styrken øker.")
        self.styrke = self.styrke + pluss
        
    def misteHelse(Monster, minus):
        Monster.helse = Monster.helse - minus
        if (Monster.helse <= 0):
            
            print("Monsteret døde! Du vant!")
            
         
monster1 = Monster("Gnarl",100,80,"Pixiedust")


class Spiller(Monster):
    def __init__(self,navn,helse,styrke, svakhet):
        super().__init__(navn,helse,styrke,svakhet)


spiller1 = Spiller("Hero",100,65,"Damsels in distress")

#def finnPixieDust():
#    self.inventory = 

while (True):
    print()
    print(vars(spiller1))
    print(vars(monster1))

    print("Gå en tur og se hva som hender (g)")
    print("Sloss med monster1 (s)")
    print("Heal (h)")
    print("Avslutt spillet (q)")
    svar = input("Hva vil du gjøre? ")

    if (svar == "q"):
        break
    elif (svar == "g"):
        hendelse = randint(1,2)
        if (hendelse == 1):
            print("ikke ferdig, sloss med monster1")
        elif (hendelse == 2):
            print("ikke ferdig, finn Pixiedust")
    elif (svar == "s"):
        spiller1.sloss()
        monster1.misteHelse(20)
    elif (svar == "h"):
        spiller1.oppStyrke()
        
        


print("OK bye!")

"""
print(type(monster1))
print(vars(monster1))
print(type(spiller1))
print(vars(spiller1))
"""