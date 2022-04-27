import csv
import operator
from more_itertools import first
import pandas as pd

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


print("=====================================================================")
print("How many players who scored more than the average for each game:     ")
print("=====================================================================")
average = data['Points'].mean()

gameOnePlayer, gameTwoPlayer, gameThreePlayer, gameFourPlayer, gameFivePlayer = 0, 0, 0, 0, 0

for i in range(len(data['Points'])):

    firstColumn = data["Game"]
    secondColumn = data["Points"]

    if firstColumn[i] == 1 and secondColumn[i] >= average:
        gameOnePlayer += 1
    if firstColumn[i] == 2 and secondColumn[i] >= average:
        gameTwoPlayer += 1
    if firstColumn[i] == 3 and secondColumn[i] >= average:
        gameThreePlayer += 1
    if firstColumn[i] == 4 and secondColumn[i] >= average:
        gameFourPlayer += 1
    if firstColumn[i] == 5 and secondColumn[i] >= average:
        gameFivePlayer += 1

    for row in range(5):
        if firstColumn[i] == 1 and secondColumn[i] >= average:
            data[data['Points']]

print("Players from game one who scored above the average: ", gameOnePlayer)
print("Players from game two who scored above the average: ", gameTwoPlayer)
print("Players from game three who scored above the average: ", gameThreePlayer)
print("Players from game four who scored above the average: ", gameFourPlayer)
print("Players from game five who scored above the average: ", gameFivePlayer)



