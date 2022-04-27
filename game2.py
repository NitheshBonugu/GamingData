import csv
import operator
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


