import random
from random import randrange
import json

class Player:
    def __init__(self, name, race, stamina, deffence, atack):
        self.nameOfPlayer = name
        self.raceOfPlayer = race
        self.staminaOfPlayer = stamina
        self.deffenceOfPlayer = deffence
        self.atackOfPlayer = atack
        self.overallOfPlayer = (stamina + deffence + atack) / 3

    def toJson(self):
        return {'nameOfPlayer' : self.nameOfPlayer, 'raceOfPlayer' : self.raceOfPlayer,
                'playerStamina' : self.staminaOfPlayer, 'playerDeffence' : self.deffenceOfPlayer,
                'playerAtack' : self.atackOfPlayer, 'overallOfPlayer' : self.overallOfPlayer}


def nameGenrator():
    global nameOfPlayer

    first_names = ("Elijea" , "Jacser", "Kayen", "Sylas", "Henry", "Trilla", "Missaos", "Obum")
    last_names = ("Ridwaan", "Mudric", "Arkaan", "Tetholin", "Jarnoli", "Madroot", "Groot", "Tony")

    full_name = random.choice(first_names) + " " + random.choice(last_names)

    nameOfPlayer = full_name

nameOfPlayer = ""

def raceGenerator():
    global raceOfPlayer

    races = ("Human", "Asgardian", "Frost Giant", "Flora Colossus", "Kree", "Centaurian", "The Sovereign")

    raceOfPlayer = random.choice(races)

raceOfPlayer = ""

def statsGenerator():
    global playerStamina
    global playerDeffence
    global playerAtack

    playerStamina =  randrange(30,100)
    playerDeffence = randrange(30,100)
    playerAtack = randrange(30,100)


playerStamina = 0
playerDeffence = 0
playerAtack = 0
humanRace = 0
asgardianRace = 0
frostGiantRace = 0
kreeRace = 0
floraColossusRace = 0
centaurianRace = 0
theSoverign = 0


nameGenrator()
statsGenerator()
raceGenerator()
random_player1 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)

if raceOfPlayer == "Human":
    humanRace +=1
elif raceOfPlayer == "Asgardian":
    asgardianRace +=1
elif raceOfPlayer == "Frost Giant":
    frostGiantRace +=1
elif raceOfPlayer == "Flora Colossus":
    floraColossusRace +=1
elif raceOfPlayer == "Centaurian":
    centaurianRace +=1
elif raceOfPlayer == "The Sovereign":
    theSoverign +=1
elif raceOfPlayer == "Kree":
    kreeRace +=1

nameGenrator()
statsGenerator()
raceGenerator()
random_player2 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
if raceOfPlayer == "Human":
    humanRace +=1
elif raceOfPlayer == "Asgardian":
    asgardianRace +=1
elif raceOfPlayer == "Frost Giant":
    frostGiantRace +=1
elif raceOfPlayer == "Flora Colossus":
    floraColossusRace +=1
elif raceOfPlayer == "Centaurian":
    centaurianRace +=1
elif raceOfPlayer == "The Sovereign":
    theSoverign +=1
elif raceOfPlayer == "Kree":
    kreeRace +=1

nameGenrator()
statsGenerator()
raceGenerator()
random_player3 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
if raceOfPlayer == "Human":
    humanRace +=1
elif raceOfPlayer == "Asgardian":
    asgardianRace +=1
elif raceOfPlayer == "Frost Giant":
    frostGiantRace +=1
elif raceOfPlayer == "Flora Colossus":
    floraColossusRace +=1
elif raceOfPlayer == "Centaurian":
    centaurianRace +=1
elif raceOfPlayer == "The Sovereign":
    theSoverign +=1
elif raceOfPlayer == "Kree":
    kreeRace +=1

nameGenrator()
statsGenerator()
raceGenerator()
random_player4 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
if raceOfPlayer == "Human":
    humanRace +=1
elif raceOfPlayer == "Asgardian":
    asgardianRace +=1
elif raceOfPlayer == "Frost Giant":
    frostGiantRace +=1
elif raceOfPlayer == "Flora Colossus":
    floraColossusRace +=1
elif raceOfPlayer == "Centaurian":
    centaurianRace +=1
elif raceOfPlayer == "The Sovereign":
    theSoverign +=1
elif raceOfPlayer == "Kree":
    kreeRace +=1

nameGenrator()
statsGenerator()
raceGenerator()
random_player5 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
if raceOfPlayer == "Human":
    humanRace +=1
elif raceOfPlayer == "Asgardian":
    asgardianRace +=1
elif raceOfPlayer == "Frost Giant":
    frostGiantRace +=1
elif raceOfPlayer == "Flora Colossus":
    floraColossusRace +=1
elif raceOfPlayer == "Centaurian":
    centaurianRace +=1
elif raceOfPlayer == "The Sovereign":
    theSoverign +=1
elif raceOfPlayer == "Kree":
    kreeRace +=1

nameGenrator()
statsGenerator()
raceGenerator()
random_player6 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
if raceOfPlayer == "Human":
    humanRace +=1
elif raceOfPlayer == "Asgardian":
    asgardianRace +=1
elif raceOfPlayer == "Frost Giant":
    frostGiantRace +=1
elif raceOfPlayer == "Flora Colossus":
    floraColossusRace +=1
elif raceOfPlayer == "Centaurian":
    centaurianRace +=1
elif raceOfPlayer == "The Sovereign":
    theSoverign +=1
elif raceOfPlayer == "Kree":
    kreeRace +=1

nameGenrator()
statsGenerator()
raceGenerator()
random_player7 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
if raceOfPlayer == "Human":
    humanRace +=1
elif raceOfPlayer == "Asgardian":
    asgardianRace +=1
elif raceOfPlayer == "Frost Giant":
    frostGiantRace +=1
elif raceOfPlayer == "Flora Colossus":
    floraColossusRace +=1
elif raceOfPlayer == "Centaurian":
    centaurianRace +=1
elif raceOfPlayer == "The Sovereign":
    theSoverign +=1
elif raceOfPlayer == "Kree":
    kreeRace +=1
