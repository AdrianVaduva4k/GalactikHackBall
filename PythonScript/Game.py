from Player import *
from Team import *
from EnemyTeam import *
from EnemyPlayerGenerator import *
from decimal import Decimal
import time

team_one_score = 0
team_two_score = 0

upper_factor = playerTeam.teamScore
lower_factor = playerTeam.teamScore + playerTeam2.teamScore

#print(upper_factor)
#print(lower_factor)

probability_of_succesful_task = round((upper_factor / lower_factor), 2)

probability_of_unuccesful_task = round((1 - probability_of_succesful_task), 2)

print("\n")
#print(probability_of_succesful_task)
#print(probability_of_unuccesful_task)

def coinTosser():
    global firstToBegin
    default_probability = 0.5
    random_event = randrange(0 , 100) / 100
    if default_probability > random_event:
        print("You attack!")
        playerStart = 1
        firstToBegin = 1
        return playerStart
    else:
        print("The enemy attacks!")
        firstToBegin = 2
        playerStart = 2
        return playerStart

playerStart = coinTosser()

def shoot_the_ball():
    global team_one_score
    global team_two_score
    default_probability = 0.5
    random_event = randrange(0, 100) / 100
    if default_probability > random_event:
        print("GOOOAAAL!")
        if playerStart == 1:
            team_one_score+=1
            print("Your team has scored!")
            time.sleep(1)
            print(str(team_one_score) + " - " + str(team_two_score))
            return team_one_score
        else:
            team_two_score+=1
            print("The enemy team has scored!")
            time.sleep(1)
            print(str(team_one_score) + " - " + str(team_two_score))
            return team_two_score

    else:
        print("WHAT A MISS!")
        numberOfPasses = 0
        time.sleep(1)
        print("Ball lost to the other team.")


def passing_the_ball():
    global numberOfPasses
    global playerStart
    global numberOfMoves

    randomiser_of_chaces = randrange(0, 100) / 100

    if numberOfMoves == 5:
        return
    else:
        if randomiser_of_chaces <= probability_of_succesful_task:
            numberOfMoves +=1
            time.sleep(1)
            numberOfPasses+=1

            if numberOfPasses == 2:
                numberOfPasses = 0
                if playerStart == 1:
                    team_one_score = shoot_the_ball()
                    playerStart = 2
                else:
                    team_two_score = shoot_the_ball()
                    playerStart = 1

            passing_the_ball()
        else:
            numberOfPasses = 0
            if playerStart == 1:
                playerStart = 2
                time.sleep(1)
                print("The other team has recovered the ball!")
                time.sleep(1)
                print("Enemy player attacks!")
            else:
                playerStart = 1
                time.sleep(1)
                print("You have recovered the ball!")
                time.sleep(1)
                print("You attack!")
            passing_the_ball()


numberOfMoves = 0
numberOfPasses = 0
passing_the_ball()

print("Final score: " + str(team_one_score) + " - " + str(team_two_score))

if str(team_one_score) == str(team_two_score):
    time.sleep(1)
    print("--------------------------------")
    time.sleep(1)
    print("We have extra time!")
    time.sleep(1)
    if firstToBegin == 1:
        print("The enemy begins this time!")
    else:
        print("You begin this time!")
    numberOfMoves = 0
    passing_the_ball()
    print("Final score after extra time: " + str(team_one_score) + " - " + str(team_two_score))

def penaltyShoot():
    global team_score_one
    global team_score_two
    global firstToBegin

    randomiser_of_chaces = randrange(0, 100) / 100

    if team_score_one == 3 or team_score_two == 3:
        return
    else:
        time.sleep(1)
        print("The player prepares...")
        time.sleep(1)
        print("He goes...")
        time.sleep(1)
        print("He shoots...")

        if randomiser_of_chaces >= 0.5:
            time.sleep(1)
            print("GOOOAAAL")
            if firstToBegin == 1:
                team_score_one += 1
                firstToBegin = 2
            else:
                team_score_two +=1
                firstToBegin = 1
            time.sleep(1)
            print(str(team_score_one) + " - " + str(team_score_two))
            time.sleep(1)
        else:
            time.sleep(1)
            print("THAT WAS CLOSE!")
            if firstToBegin == 1:
                firstToBegin = 2
            else:
                firstToBegin = 1
                time.sleep(1)
                print(str(team_score_one) + " - " + str(team_score_two))
                time.sleep(1)
        penaltyShoot()

team_score_one = 0
team_score_two = 0

if str(team_one_score) == str(team_two_score):
    time.sleep(1)
    print("--------------------------------")
    time.sleep(1)
    print("We have penalties!")
    time.sleep(1)

    if firstToBegin == 1:
        print("You go first!")
        time.sleep(1)
        penaltyShoot()

    else:
        print("The enemy goes first!")
        time.sleep(1)
        penaltyShoot()
    print("Final score: " + str(team_score_one) + " - " + str(team_score_two))
    team_one_score = team_score_one
    team_two_score = team_score_two

    if team_score_one > team_score_two:
        print("You have won!")
    else:
        print("You have lost!")