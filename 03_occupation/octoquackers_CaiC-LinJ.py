#Team OctoQuackers -- Cathy Cai and Jason Lin
#SoftDev1 pd07
#K06 -- StI/O: Divine your Destiny!
#2018-09-13

import csv
from random import randint

def makeDict(file, dictionary):

    # Open csv file
    with open(file, newline='') as csvfile:

        # A reader object iterates through
        # and separates each row by comma into a string array
        csvfile = csv.reader(csvfile, delimiter=',')

        # For each row, assign string 0 as the key, and
        # string 1 in int (percentage*10) form as the value
        # exclude the first and the "Total" row
        rowNum = 0
        for row in csvfile:
            if rowNum != 0:
                dictionary[row[0]] = int(float(row[1])*10)
            rowNum += 1
        dictionary.pop('Total')

def randOccupation():

    occupations = {} 
    makeDict('occupations.csv', occupations)

    # num is a random int from 0 - 998
    num = randint(0, 998)

    # Sum the percentages of the occupations until
    # you get to a sum greater than num
    # (the interval between sums is your percentage)
    # Break once this is true
    Sum = 0
    for occupation in occupations:
        Sum += occupations[occupation] 
        if Sum >= num:
            return occupation
            break

print (randOccupation())



    
