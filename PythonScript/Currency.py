from Player import *
from EnemyPlayerGenerator import  *
from Team import *
from EnemyTeam import *
from Game import *

starting_galactik_tokens = 5000
galactik_tokens = 0

if team_one_score < team_two_score:
    starting_galactik_tokens += (team_one_score * 10)
else:
    if playerTeam.teamScore >= playerTeam2.teamScore:
        starting_galactik_tokens += int((playerTeam.teamScore - playerTeam2.teamScore) * 20)
    else:
        starting_galactik_tokens += int((playerTeam2.teamScore - playerTeam.teamScore) * 50)

galactik_tokens = starting_galactik_tokens
print("You now have: " + str(galactik_tokens) + " galactik HackTones")


