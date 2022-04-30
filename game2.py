import csv
import operator
from time import strptime
from tracemalloc import start
from matplotlib.pyplot import axis
from more_itertools import first, last
import pandas as pd
from datetime import datetime

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
print("=============================================================")
print("Players who scored more than the average for each game:    ")
print("=============================================================")
<<<<<<< HEAD
#data = pd.read_csv("gameData.csv")
#nextData = data.reindex(['Game', 'Player_ID', 'Date_Of_Play', 'Points'], axis = 1)
=======
>>>>>>> 19e71babe078d27009756288f4e8c12acdcf343f
average = data['Points'].mean()

gameOnePlayer, gameTwoPlayer, gameThreePlayer, gameFourPlayer, gameFivePlayer = 0, 0, 0, 0, 0

<<<<<<< HEAD
for i in range(len(data['Game'])):
=======
for i in range(len(data['Points'])):
>>>>>>> 19e71babe078d27009756288f4e8c12acdcf343f

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
print("Players from game five who scored above the average: ", gameFivePlayer)"""

# =================================================================
# Now, we are going to look at the players who scored the 
# highest points per week.
# =================================================================

# Sort the data according to the date of play
data.sort_values("Date_Of_Play", axis = 0, ascending = True, inplace= True, na_position= 'last')
startDate = "2021-08-01" # Start date to get games between two dates
endDate = "2021-08-07" # End date
mask = ((data['Date_Of_Play'] >= startDate) & (data['Date_Of_Play'] <= endDate)) # Get the data between these two dates
selectedData = data.loc[mask]

# Sort these games according to the points
selectedData.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last')


print("=====================================")
print("Top five players during week one: ")
print("=====================================")
print(selectedData.head(5))

startDate = "2021-08-08" # Start date to get games between two dates
endDate = "2021-08-15" # End date
mask = ((data['Date_Of_Play'] >= startDate) & (data['Date_Of_Play'] <= endDate)) # Get the data between these two dates
selectedData = data.loc[mask]

# Sort these games according to the points
selectedData.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last')


print(" ")
print("=====================================")
print("Top five players during week two: ")
print("=====================================")
print(selectedData.head(5))

startDate = "2021-08-15" # Start date to get games between two dates
endDate = "2021-08-22" # End date
mask = ((data['Date_Of_Play'] >= startDate) & (data['Date_Of_Play'] <= endDate)) # Get the data between these two dates
selectedData = data.loc[mask]

# Sort these games according to the points
selectedData.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last')


print(" ")
print("=====================================")
print("Top five players during week three: ")
print("=====================================")
print(selectedData.head(5))

startDate = "2021-08-22" # Start date to get games between two dates
endDate = "2021-08-29" # End date
mask = ((data['Date_Of_Play'] >= startDate) & (data['Date_Of_Play'] <= endDate)) # Get the data between these two dates
selectedData = data.loc[mask]

# Sort these games according to the points
selectedData.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last')


print(" ")
print("=====================================")
print("Top five players during week four: ")
print("=====================================")
print(selectedData.head(5))

startDate = "2021-08-30" # Start date to get games between two dates
endDate = "2021-08-31" # End date
mask = ((data['Date_Of_Play'] >= startDate) & (data['Date_Of_Play'] <= endDate)) # Get the data between these two dates
selectedData = data.loc[mask]

# Sort these games according to the points
selectedData.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last')


print(" ")
print("=====================================")
print("Top five players during week five: ")
print("=====================================")
print(selectedData.head(5))

# =================================================================
# Now, we are going to look at the players who scored the 
# highest points biweekly.
# =================================================================

startDate = "2021-08-01" # Start date to get games between two dates
endDate = "2021-08-14" # End date
mask = ((data['Date_Of_Play'] >= startDate) & (data['Date_Of_Play'] <= endDate)) # Get the data between these two dates
selectedData = data.loc[mask]

# Sort these games according to the points
selectedData.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last') 


print(" ")
print("==========================================")
print("Top five players during week one and two: ")
print("==========================================")
print(selectedData.head(5))

startDate = "2021-08-14" # Start date to get games between two dates
endDate = "2021-08-28" # End date
mask = ((data['Date_Of_Play'] >= startDate) & (data['Date_Of_Play'] <= endDate)) # Get the data between these two dates
selectedData = data.loc[mask]

# Sort these games according to the points
selectedData.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last') 


print(" ")
print("============================================")
print("Top five players during week two and three: ")
print("============================================")
print(selectedData.head(5))

startDate = "2021-08-17" # Start date to get games between two dates
endDate = "2021-08-31" # End date
mask = ((data['Date_Of_Play'] >= startDate) & (data['Date_Of_Play'] <= endDate)) # Get the data between these two dates
selectedData = data.loc[mask]

# Sort these games according to the points
selectedData.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last') 


print(" ")
print("=============================================")
print("Top five players during the final two weeks: ")
print("=============================================")
print(selectedData.head(5))


"""
startGame = "1"
mask2 = (selectedData['Game'] <= startGame)
selectedData2 = selectedData.loc[mask2]
print(selectedData2.head(5))"""


"""
selectedData = selectedData.sort_values('Points')
print(selectedData.head(15))

selectedData2.sort_values("Points", axis = 0, ascending=False, inplace=True, na_position='last')

print(selectedData2.head(5))



#print(max(data['Date_Of_Play'].head(5)))
"""

