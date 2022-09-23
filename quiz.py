import pandas as pd

def interpret_results():

    # is half pseudocode om m'n idee uit te werken, runt niet.
    newlist = []
    if user.endurance >= 6.5:
        newlist.append(sports[sports.endurance >= 6.5])
    elif user.endurance >= 4:
        newlist.append(sports[sports.endurance >= 4])
    else:
        newlist.append(sports[sports.endurance < 4])

    #calculate frequency van newlist

# Endurance 
# Your friends asks you if you'd like to sign up for a charity run with them. What do you say?
# a) Absolutely! (6,5+)
# b) If it's no more than 5 km, you'll consider it. (4-6,5)
# b) You'll cheer them on from the sidelines. (4-)

# Strength 

# Power 
# Throw a ball really hard or jump far/high

# Speed
# Reactievermogen 

# Agility (5)
# Quick feet
# Dance tiles arcade

# Flexibility
# If you were to take a yoga class, what would it look like?
# a) Master (7+)
# b) Doing alright (4-7)
# c) Nope (4-)

# Nerve
# How do you feel about adenaline sports?
# a) Skydiving is my biggest dream (8+)
# b) Rollercoasters are fine but skydiving is a bit much (4-8)
# c) Nope nope nope (4-)

# Durability
# Kun je tegen een stootje?

# Hand-eye coordination
# When someone throws you a ball, you are
# a) confident you'll catch it (6+)
# b) nervous, you're not great at catching things (6-)

# Analytical aptitude
# Do you like to think about tactics? (puzzles, chess etc)
# a) Yes, I love figuring out the best strategy (6+)
# b) No, I don't want to think too much during my workout (6-)

# intense
# beter of niet (niet -> reverse list)
