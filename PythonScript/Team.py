from Player import *
import string
import json

class Team:
    def __init__(self, nume, Team):
        self.nameOfTeam = nume
        self.playerOne = Team[0]
        self.playerTwo = Team[1]
        self.playerThree = Team[2]
        self.playerFour = Team[3]
        self.playerFive = Team[4]
        self.playerSix = Team[5]
        self.playerSeven = Team[6]
        self.teamScore = 0

    def toJson(self):
        return {'nameOfTeam': self.nameOfTeam, 'players': [self.playerOne.toJson(),
                self.playerTwo.toJson(), self.playerThree.toJson(),
                self.playerFour.toJson(), self.playerFive.toJson(),
                self.playerSix.toJson(), self.playerSeven.toJson()], 'teamScore' : self.teamScore}

playerTeam = Team("Avengers", [random_player1, random_player2, random_player3, random_player4,
                      random_player5, random_player6, random_player7])

team_score = (playerTeam.playerOne.overallOfPlayer + playerTeam.playerTwo.overallOfPlayer +
             playerTeam.playerThree.overallOfPlayer + playerTeam.playerFour.overallOfPlayer +
             playerTeam.playerFive.overallOfPlayer + playerTeam.playerSix.overallOfPlayer +
             playerTeam.playerSeven.overallOfPlayer)


stamina_overall = (playerTeam.playerOne.staminaOfPlayer + playerTeam.playerTwo.staminaOfPlayer +
                   playerTeam.playerThree.staminaOfPlayer + playerTeam.playerFour.staminaOfPlayer +
                   playerTeam.playerFive.staminaOfPlayer + playerTeam.playerSix.staminaOfPlayer +
                   playerTeam.playerSeven.staminaOfPlayer)

stamina_overall = stamina_overall / 7


deffence_overall = (playerTeam.playerOne.deffenceOfPlayer + playerTeam.playerTwo.deffenceOfPlayer +
             playerTeam.playerThree.deffenceOfPlayer + playerTeam.playerFour.deffenceOfPlayer +
             playerTeam.playerFive.deffenceOfPlayer + playerTeam.playerSix.deffenceOfPlayer +
             playerTeam.playerSeven.deffenceOfPlayer)

deffence_overall = deffence_overall / 7

atack_overall = (playerTeam.playerOne.atackOfPlayer + playerTeam.playerTwo.atackOfPlayer +
             playerTeam.playerThree.atackOfPlayer + playerTeam.playerFour.atackOfPlayer +
             playerTeam.playerFive.atackOfPlayer + playerTeam.playerSix.atackOfPlayer +
             playerTeam.playerSeven.atackOfPlayer)

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

#print(int(team_score))

team_score = raceBonus(team_score, humanRace)
team_score = raceBonus(team_score, asgardianRace)
team_score = raceBonus(team_score, frostGiantRace)
team_score = raceBonus(team_score, floraColossusRace)
team_score = raceBonus(team_score, centaurianRace)
team_score = raceBonus(team_score, theSoverign)
team_score = raceBonus(team_score, kreeRace)

#print(int(team_score))

#print("Human: " + str(humanRace))
#print("Asgard " + str(asgardianRace))
#print("Frost " + str(frostGiantRace))
#print("Floral " + str(floraColossusRace))
#print("Centaurian " + str(centaurianRace))
#print("Sove " + str(theSoverign))
#print("kree " + str(kreeRace))

playerTeam.teamScore = team_score


'''print (" Team Neame: " + playerTeam.nameOfTeam + " ----------> Team Score: " + str(int(playerTeam.teamScore)) + "\n",
       "Player One   --> " + "Name: " + playerTeam.playerOne.nameOfPlayer,
       "; Race: " + playerTeam.playerOne.raceOfPlayer,
       "; Stamina: " + str(playerTeam.playerOne.staminaOfPlayer),
       "; Deffence: " + str(playerTeam.playerOne.deffenceOfPlayer),
       "; Atack: " + str(playerTeam.playerOne.atackOfPlayer),
       "; Overall: " + str(int(playerTeam.playerOne.overallOfPlayer)),
        "\n",
       "Player Two   --> " + "Name: " + playerTeam.playerTwo.nameOfPlayer,
       "; Race: " + playerTeam.playerTwo.raceOfPlayer,
       "; Stamina: " + str(playerTeam.playerTwo.staminaOfPlayer),
       "; Deffence: " + str(playerTeam.playerTwo.deffenceOfPlayer),
       "; Atack: " + str(playerTeam.playerTwo.atackOfPlayer),
       "; Overall: " + str(int(playerTeam.playerTwo.overallOfPlayer)),
        "\n",
       "Player Three --> " + "Name: " + playerTeam.playerThree.nameOfPlayer,
       "; Race: " + playerTeam.playerThree.raceOfPlayer,
       "; Stamina: " + str(playerTeam.playerThree.staminaOfPlayer),
       "; Deffence: " + str(playerTeam.playerThree.deffenceOfPlayer),
       "; Atack: " + str(playerTeam.playerThree.atackOfPlayer),
       "; Overall: " + str(int(playerTeam.playerThree.overallOfPlayer)),
        "\n",
       "Player Four  --> " + "Name: " + playerTeam.playerFour.nameOfPlayer,
       "; Race: " + playerTeam.playerFour.raceOfPlayer,
       "; Stamina: " + str(playerTeam.playerFour.staminaOfPlayer),
       "; Deffence: " + str(playerTeam.playerFour.deffenceOfPlayer),
       "; Atack: " + str(playerTeam.playerFour.atackOfPlayer),
       "; Overall: " + str(int(playerTeam.playerFour.overallOfPlayer)),
        "\n",
       "Player Five  --> " + "Name: " + playerTeam.playerFive.nameOfPlayer,
       "; Race: " + playerTeam.playerFive.raceOfPlayer,
       "; Stamina: " + str(playerTeam.playerFive.staminaOfPlayer),
       "; Deffence: " + str(playerTeam.playerFive.deffenceOfPlayer),
       "; Atack: " + str(playerTeam.playerFive.atackOfPlayer),
       "; Overall: " + str(int(playerTeam.playerFive.overallOfPlayer)),
        "\n",
       "Player Six   --> " + "Name: " + playerTeam.playerSix.nameOfPlayer,
       "; Race: " + playerTeam.playerSix.raceOfPlayer,
       "; Stamina: " + str(playerTeam.playerSix.staminaOfPlayer),
       "; Deffence: " + str(playerTeam.playerSix.deffenceOfPlayer),
       "; Atack: " + str(playerTeam.playerSix.atackOfPlayer),
       "; Overall: " + str(int(playerTeam.playerSix.overallOfPlayer)),
        "\n",
       "Player Seven --> " + "Name: " + playerTeam.playerSeven.nameOfPlayer,
       "; Race: " + playerTeam.playerSeven.raceOfPlayer,
       "; Stamina: " + str(playerTeam.playerSeven.staminaOfPlayer),
       "; Deffence: " + str(playerTeam.playerSeven.deffenceOfPlayer),
       "; Atack: " + str(playerTeam.playerSeven.atackOfPlayer),
       "; Overall: " + str(int(playerTeam.playerSeven.overallOfPlayer)),
        ) '''

print(playerTeam.toJson())