# adding team scores

team_scores = {"team 1" : 10,
               "team 2" : 17}

print(team_scores["team 1"])

team_scores["team 1"] += 5
print(team_scores)

# team_scores["team 3"] += 12 # this doesn't work because "team 3" isn't an existing key
team_scores["team 3"] = 12
print(team_scores)

team_name = "team 84"
team_score = 16
if team_name in team_scores.keys():
    # if the team is in the dict already, increment
    team_scores[team_name] += team_score
else:
    # if not, assign the value to a new entry
    team_scores[team_name] = team_score


