from lib2to3.pgen2.token import NEWLINE
import random  # Importing the random module
import datetime # Importing the datetime module
from time import time
from tracemalloc import start 
import csv

myList = []
header = ["Game","Player_ID","Date_of_Play","Points"]


for i in range(500):
    
    game_id = random.randint(1, 5)   ### There can be any number of games within the limit of five
    
    player_id = random.randint(75, 125) ### The number of players in each game can be from 75 to 125.

    startDate = datetime.date(2021, 8, 1) ### Generating a random date in the month of August 2021
    endDate = datetime.date(2021, 8, 31)
    timeBetweenDays = endDate - startDate
    daysBetweenDays = timeBetweenDays.days
    randomNumberOfDays = random.randrange(daysBetweenDays)
    played_date = startDate + datetime.timedelta(days=randomNumberOfDays) ### Date the player has played the game

    points = random.randint(75, 200)  ### Points for each player in the range 75 to 200.
    
    myList.append(game_id)
    myList.append(player_id)
    myList.append(str(played_date))
    myList.append(points)

    print(game_id,player_id,played_date,points, sep = ",")
    #myList = myList.split(',')
    #print(myList.split(','))
    #myList = []
    
  
    
"""with open('gameData.csv', 'w') as f:
    write = csv.writer(f)

    write.writerow(myList)"""
    # Emptying the list to append new entries




"""with open('gameData.csv', 'w', encoding='UTF8', newline='') as f:
    new_writer = csv.writer(f)

    
    new_writer.writerows()"""



