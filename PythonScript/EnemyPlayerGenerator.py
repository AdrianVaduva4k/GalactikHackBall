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
        return {'nameOfPlayer': self.nameOfPlayer, 'raceOfPlayer': self.raceOfPlayer,
                'playerStamina': self.staminaOfPlayer, 'playerDeffence': self.deffenceOfPlayer,
                'playerAtack': self.atackOfPlayer, 'overallOfPlayer': self.overallOfPlayer}

def nameGenrator():
    global nameOfPlayer

    first_names = ("Kane" , "Ezreal", "Caitlyn", "Fernando", "Dreaven", "Varus", "Super", "Bruce")
    last_names = ("Waine", "Pulsfire", "Void", "Energy", "Fire", "Mordor", "Sparrow", "Kabuto")

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
random_player8 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)

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
random_player9 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
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
random_player10 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
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
random_player11 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
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
random_player12 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
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
random_player13 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
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
random_player14 = Player(nameOfPlayer, raceOfPlayer, playerStamina, playerDeffence, playerAtack)
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
