# adding team scores

import adding_scores
# from adding_scores import add_scores_to_team_dictionary # alternative if you're lazy

###################################
# run a bunch of updates

team_score_dictionary = {}

adding_scores.add_scores_to_team_dictionary(team_score_dictionary, "Team Alpha", 12)
adding_scores.add_scores_to_team_dictionary(team_score_dictionary, "Team Gamma", 18)
adding_scores.add_scores_to_team_dictionary(team_score_dictionary, "Team Strike Force", 23)
adding_scores.add_scores_to_team_dictionary(team_score_dictionary, "Team Discovery Channel", 84)
adding_scores.add_scores_to_team_dictionary(team_score_dictionary, "Team Gamma", 44)

print(team_score_dictionary)
