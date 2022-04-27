import csv
import operator
import sys
import pandas as pd
from sqlalchemy import asc


data = pd.read_csv("gameData.csv")
data.sort_values("Points", axis = 0, ascending = False, inplace= True, na_position= 'last')

# Return the top five players who got the most number of points. 
topFive = data.head(5)
print("====================================================")
print("Top five players who got the most number of points: ")
print("====================================================")
print(topFive)
print('\n')

# Return the bottom five players who got the least number of points. 
print("========================================================")
print("Bottom five players who got the least number of points: ")
print("========================================================")
bottomFive = data.tail(5)
print(bottomFive)
print('\n')


"""
with open("gameData.csv", "r") as wins:

    # Return the top five players who got the most number of points. 
    csv1 = csv.reader(wins, delimiter=",")
    sort = sorted(csv1,key=operator.itemgetter(3)) # Sort the dataset according to the fourth column: Points
    
    print("Players who got the most number of points: ")
    for eachline in sort[1:6]:
        print(eachline)

    print("Players who got the least number of points: ")
    for eachline in sort[-6:-1]:
        print(eachline)"""

    

"""csvData = pandaSorting.read_csv('gameData.csv')
csvData.sort_values(["Points"], axis=0, ascending=[False], inplace=True)
for eachLine in csvData[2]:
    print(eachLine)"""

"""reader = csv.reader(open("gameData.csv"), delimiter=",")

sortedList = sorted(reader, key=operator.itemgetter(-1), reverse=False)

print(sortedList[1:5][2])"""

"""with open('gameData.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[3]) # Just printing the whole csv file. We can use line[x][x] for a specific column where x is the column number starting from 0.

    csvData = pandaSorting.read_csv("gameData.csv")
    csvData.sort_values(["Points"], axis = 0, ascending=[False], inplace=True)"""
    
