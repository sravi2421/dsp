# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv
import sys

file1 = open('football.csv')
reader = csv.reader(file1)

mydict = dict((rows[0],rows[1:8]) for rows in reader)
del mydict['Team']

highest_gd=0
highest_gd_team = "No one"
for key in mydict:
    goal_difference = int(mydict[key][4])-int(mydict[key][5])
    if goal_difference > highest_gd:
        highest_gd = int(mydict[key][4])-int(mydict[key][5])
        highest_gd_team = key
print highest_gd_team

file1.close()
