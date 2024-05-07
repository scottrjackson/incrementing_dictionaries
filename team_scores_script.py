# adding team scores

################################################
# turn this into a function

# Steps to make a good function
# 0. come up with a name and start the def line
# 1. figure out what you want out of this function (return)
# 2. figure out what you want the input to be (arguments)
# 3. figure out how to get from input (arguments) to output (return)
# 4. test it!
# 5. write a helpful doctstring

def add_scores_to_team_dictionary(team_dict, name, score):
    """
    Takes a dictionary of team scores, and then a name
    and score of a team, and either adds to the team's 
    score, or creates an entry if that team is not alread
    in the disctionary.
    """
    if name in team_dict.keys():
        # if the team is in the dict already, increment
        team_dict[name] += score
    else:
        # if not, assign the value to a new entry
        team_dict[name] = score

    # we want to update the dictionary
    # but since dictionaries are mutable, 
    # we don't need to return it
    return None

# team_scores = {"team 1" : 10,
#                "team 2" : 17}
# add_scores_to_team_dictionary(team_scores, "team 82", 34)
# print(team_scores)
# add_scores_to_team_dictionary(team_scores, "team 2", 13)
# print(team_scores)

###################################
# run a bunch of updates

team_score_dictionary = {}

add_scores_to_team_dictionary(team_score_dictionary, "Team Alpha", 12)
add_scores_to_team_dictionary(team_score_dictionary, "Team Gamma", 18)
add_scores_to_team_dictionary(team_score_dictionary, "Team Strike Force", 23)
add_scores_to_team_dictionary(team_score_dictionary, "Team Discovery Channel", 84)
add_scores_to_team_dictionary(team_score_dictionary, "Team Gamma", 44)

print(team_score_dictionary)
