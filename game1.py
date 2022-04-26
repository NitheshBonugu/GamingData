"""
A gaming system contains the following fields
game_id, player_id, played_date, points

1. Generate random synthetic data for the above fields with following constraints:
Number of games: 5

Number of players in each game: 75 to 125 (Note: same player can be repeated multiple times 
on different dates but on same date. Meaning, same player shouldn't play on the same date but can 
play on different dates)

played_date: All games should have played in the month of August 2021 but not on Tuesdays
points: The point for each player should be in the range of 75 to 200 only

2. Once the above random synthetic data is created then store the results in a CSV file

3. Read the above CSV file and perform the following aggregations:
    Find out the top 5 players by points in each of the games and display the results (game_id, player_id, total_points)
    Find out the bottom 5 players by points in each of the games and display the results (game_id, player_id, total_points)
    Find out the top 5 players in each game whose total points in a game is greater than the average of all players points of 
that game (hint: if average points of all players in game 1 is 90 then find out all the top 5 players whose points are greater than 90)
    Find out top 5 players in each game by their total points for each week (hint: list 5 players in game 1 with top scores between Aug 1st - Augt 7th)
    Find out top 5 players in each game by their total points bi-weekly - every 2 weeks (hint: list 5 players in game 1 with top scores between Aug 1st - Augt 14th)

4. Create a proper project structure for the above problem statement, indent the code properly, add comments to the code, perform all git operations on the code (git clone, add, commit, fetch, pull, etc). Each of the above requirements should be an individual commit to the github

"""

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



