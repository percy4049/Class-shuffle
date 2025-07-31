import random
males = [] #male members without leaders
females = [] #female members without leaders
team1 = ["leader1"]
team2 = ["leader2"]
team3 = ["leader3"]
team4 = ["leader4"]
random.shuffle(males)
random.shuffle(females)
team_sizes = [7, 7, 7, 8]
teams = [team1, team2, team3, team4]
for _ in range(4):
    if males: 
        team4.append(males.pop())
for x in range(2):
    if males:
        team3.append(males.pop())
for team, size in zip(teams[:-1], team_sizes[:-2]):
    male_count = 1
    female_count = 0
    while len(team) < size:
        if male_count < size // 2 and males: 
            team.append(males.pop())
            male_count += 1
        elif female_count < size // 2 and females: 
            team.append(females.pop())
            female_count += 1
        elif males:
            team.append(males.pop())
            male_count += 1
        elif females:
            team.append(females.pop())
            female_count += 1
while len(team4) < team_sizes[3]:
    if females: 
        team4.append(females.pop())
while len(team3) < team_sizes[2]:
    if females:
        team3.append(females.pop())
for i, team in enumerate(teams, 1):
    print(f"Team {i}: {team}")
