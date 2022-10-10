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
            
         
    def misteHelseS(self, minus):
        self.helse = self.helse - minus
        if (self.helse <= 0):
            print("Game Over")
                    
    ting = {}        
    def finneStøv(self):
        self.inventory = self.inventory.append["støv"]
        
         
monster1 = Monster("Gnarl",100,80,"Pixiedust")


class Spiller(Monster):
    def __init__(self,navn,helse,styrke, svakhet):
        super().__init__(navn,helse,styrke,svakhet)


spiller1 = Spiller("Hero",100,65,"Damsels in distress")

print(vars(spiller1))
print(vars(monster1))

while (input == True):
    print()

    
        
    if (svar == "g"):
        hendelse = randint(1,2)
        if (hendelse == 1):
            print("Du er midt inne i ingenmannsland, og hører noe rart? Skal du undersøke det?J/n")
            if (svar == "J"):
                print("Du møtte et monster, og du slår han før han ser deg.")
                spiller1.sloss()
                monster1.misteHelse(20)
                print("")
            elif (svar == "n"):
                print("Du leter etter noe brukbart, og ser høyt og lav etter et magisk pulver.")
        elif (hendelse == 2):
            print("Du har møtt en heks! Hun kommer til å kaste trolldom på deg, du må rømme! Hva gjør du?")
            print("Løpe eller kjempe? L/k")
            if (svar == "L"):
                print("Du ble slått av heksen og miste litt helse!")
                spiller1.misteHelseS(10)
            elif (svar == "k"):
                spiller1.sloss()
        elif (svar == "h"):
                    spiller1.oppStyrke()
        elif (svar == "q"):  
            print("OK bye!")
            break



    """
print(type(monster1))
print(vars(monster1))
print(type(spiller1))
print(vars(spiller1))
"""