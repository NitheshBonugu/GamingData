import csv

with open('gameData.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[0]) # Just printing the whole csv file. We can use line[x][x] for a specific column where x is the column number starting from 0.

    
