from Player import *
from EnemyPlayerGenerator import *
import string
import json

class EnemyTeam:
    def __init__(self, nume, EnemyTeam):
        self.nameOfTeam = nume
        self.playerOne = EnemyTeam[0]
        self.playerTwo = EnemyTeam[1]
        self.playerThree = EnemyTeam[2]
        self.playerFour = EnemyTeam[3]
        self.playerFive = EnemyTeam[4]
        self.playerSix = EnemyTeam[5]
        self.playerSeven = EnemyTeam[6]
        self.teamScore = 0


    def toJson(self):
        return {'nameOfTeam': self.nameOfTeam, 'players': [self.playerOne.toJson(), self.playerTwo.toJson(),
                 self.playerThree.toJson(), self.playerFour.toJson(), self.playerFive.toJson(),
                 self.playerSix.toJson(), self.playerSeven.toJson()], 'teamScore': self.teamScore}


playerTeam2 = EnemyTeam("Orc", [random_player8, random_player9, random_player10, random_player11,
                      random_player12, random_player13, random_player14])

team_score = (playerTeam2.playerOne.overallOfPlayer + playerTeam2.playerTwo.overallOfPlayer +
             playerTeam2.playerThree.overallOfPlayer + playerTeam2.playerFour.overallOfPlayer +
             playerTeam2.playerFive.overallOfPlayer + playerTeam2.playerSix.overallOfPlayer +
             playerTeam2.playerSeven.overallOfPlayer)


stamina_overall = (playerTeam2.playerOne.staminaOfPlayer + playerTeam2.playerTwo.staminaOfPlayer +
                   playerTeam2.playerThree.staminaOfPlayer + playerTeam2.playerFour.staminaOfPlayer +
                   playerTeam2.playerFive.staminaOfPlayer + playerTeam2.playerSix.staminaOfPlayer +
                   playerTeam2.playerSeven.staminaOfPlayer)

stamina_overall = stamina_overall / 7


deffence_overall = (playerTeam2.playerOne.deffenceOfPlayer + playerTeam2.playerTwo.deffenceOfPlayer +
             playerTeam2.playerThree.deffenceOfPlayer + playerTeam2.playerFour.deffenceOfPlayer +
             playerTeam2.playerFive.deffenceOfPlayer + playerTeam2.playerSix.deffenceOfPlayer +
             playerTeam2.playerSeven.deffenceOfPlayer)

deffence_overall = deffence_overall / 7

atack_overall = (playerTeam2.playerOne.atackOfPlayer + playerTeam2.playerTwo.atackOfPlayer +
             playerTeam2.playerThree.atackOfPlayer + playerTeam2.playerFour.atackOfPlayer +
             playerTeam2.playerFive.atackOfPlayer + playerTeam2.playerSix.atackOfPlayer +
             playerTeam2.playerSeven.atackOfPlayer)

atack_overall = atack_overall / 7

def teamScoreBonusStamina(team_score):
    if stamina_overall >= 90:
        team_score += 150
    elif stamina_overall >= 80:
        team_score += 100
    elif stamina_overall >= 70:
        team_score += 75
    elif stamina_overall >= 60:
        team_score +=50
    elif stamina_overall >=50:
        team_score += 25
    return team_score

def teamScoreBonusDeffence(team_score):
    if deffence_overall >= 90:
        team_score += 150
    elif deffence_overall >= 80:
        team_score += 100
    elif deffence_overall >= 70:
        team_score += 75
    elif deffence_overall >= 60:
        team_score +=50
    elif deffence_overall >=50:
        team_score += 25
    return team_score

def teamScoreBonusAtack(team_score):
    if atack_overall >= 90:
        team_score += 150
    elif atack_overall >= 80:
        team_score += 100
    elif atack_overall >= 70:
        team_score += 75
    elif atack_overall >= 60:
        team_score +=50
    elif atack_overall >=50:
        team_score += 25
    return team_score


def raceBonus(team_score, actualRace):
    if (actualRace == 7):
        team_score+=250
    elif (actualRace == 6):
        team_score+=200
    elif (actualRace == 5):
        team_score+=150
    elif (actualRace == 4):
        team_score+=95
    elif (actualRace == 3):
        team_score+=60
    elif (actualRace == 2):
        team_score+=25
    return team_score

team_score = teamScoreBonusStamina(team_score)
team_score = teamScoreBonusDeffence(team_score)
team_score = teamScoreBonusAtack(team_score)

team_score = raceBonus(team_score, humanRace)
team_score = raceBonus(team_score, asgardianRace)
team_score = raceBonus(team_score, frostGiantRace)
team_score = raceBonus(team_score, floraColossusRace)
team_score = raceBonus(team_score, centaurianRace)
team_score = raceBonus(team_score, theSoverign)
team_score = raceBonus(team_score, kreeRace)

playerTeam2.teamScore = team_score


'''print ("\n Team Neame: " + playerTeam2.nameOfTeam + " ----------> Team Score: " + str(int(playerTeam2.teamScore)) + "\n",
       "Player One   --> " + "Name: " + playerTeam2.playerOne.nameOfPlayer,
       "; Race: " + playerTeam2.playerOne.raceOfPlayer,
       "; Stamina: " + str(playerTeam2.playerOne.staminaOfPlayer),
       "; Deffence: " + str(playerTeam2.playerOne.deffenceOfPlayer),
       "; Atack: " + str(playerTeam2.playerOne.atackOfPlayer),
       "; Overall: " + str(int(playerTeam2.playerOne.overallOfPlayer)),
        "\n",
       "Player Two   --> " + "Name: " + playerTeam2.playerTwo.nameOfPlayer,
       "; Race: " + playerTeam2.playerTwo.raceOfPlayer,
       "; Stamina: " + str(playerTeam2.playerTwo.staminaOfPlayer),
       "; Deffence: " + str(playerTeam2.playerTwo.deffenceOfPlayer),
       "; Atack: " + str(playerTeam2.playerTwo.atackOfPlayer),
       "; Overall: " + str(int(playerTeam2.playerTwo.overallOfPlayer)),
        "\n",
       "Player Three --> " + "Name: " + playerTeam2.playerThree.nameOfPlayer,
       "; Race: " + playerTeam2.playerThree.raceOfPlayer,
       "; Stamina: " + str(playerTeam2.playerThree.staminaOfPlayer),
       "; Deffence: " + str(playerTeam2.playerThree.deffenceOfPlayer),
       "; Atack: " + str(playerTeam2.playerThree.atackOfPlayer),
       "; Overall: " + str(int(playerTeam2.playerThree.overallOfPlayer)),
        "\n",
       "Player Four  --> " + "Name: " + playerTeam2.playerFour.nameOfPlayer,
       "; Race: " + playerTeam2.playerFour.raceOfPlayer,
       "; Stamina: " + str(playerTeam2.playerFour.staminaOfPlayer),
       "; Deffence: " + str(playerTeam2.playerFour.deffenceOfPlayer),
       "; Atack: " + str(playerTeam2.playerFour.atackOfPlayer),
       "; Overall: " + str(int(playerTeam2.playerFour.overallOfPlayer)),
        "\n",
       "Player Five  --> " + "Name: " + playerTeam2.playerFive.nameOfPlayer,
       "; Race: " + playerTeam2.playerFive.raceOfPlayer,
       "; Stamina: " + str(playerTeam2.playerFive.staminaOfPlayer),
       "; Deffence: " + str(playerTeam2.playerFive.deffenceOfPlayer),
       "; Atack: " + str(playerTeam2.playerFive.atackOfPlayer),
       "; Overall: " + str(int(playerTeam2.playerFive.overallOfPlayer)),
        "\n",
       "Player Six   --> " + "Name: " + playerTeam2.playerSix.nameOfPlayer,
       "; Race: " + playerTeam2.playerSix.raceOfPlayer,
       "; Stamina: " + str(playerTeam2.playerSix.staminaOfPlayer),
       "; Deffence: " + str(playerTeam2.playerSix.deffenceOfPlayer),
       "; Atack: " + str(playerTeam2.playerSix.atackOfPlayer),
       "; Overall: " + str(int(playerTeam2.playerSix.overallOfPlayer)),
        "\n",
       "Player Seven --> " + "Name: " + playerTeam2.playerSeven.nameOfPlayer,
       "; Race: " + playerTeam2.playerSeven.raceOfPlayer,
       "; Stamina: " + str(playerTeam2.playerSeven.staminaOfPlayer),
       "; Deffence: " + str(playerTeam2.playerSeven.deffenceOfPlayer),
       "; Atack: " + str(playerTeam2.playerSeven.atackOfPlayer),
       "; Overall: " + str(int(playerTeam2.playerSeven.overallOfPlayer)),
        )'''

print(playerTeam2.toJson())