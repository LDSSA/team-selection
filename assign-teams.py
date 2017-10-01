import sys
import random
import json

with open('participants.txt') as fh:
    people = fh.readlines()

random.shuffle(people)

nteams = int(sys.argv[1])

teams = {team_num: [] for team_num in range(0, nteams)}

while people:
    for i in range(0, nteams):
        if not people:
            break
        teams[i].append(people.pop()) 


print(json.dumps(teams, sort_keys=True, indent=4, separators=(',', ': ')))

