#Team Octoquackers - Cathy Cai and Jason Lin
#SoftDev1 pd07
#K3 -- StI/O: Divine your Destiny!
#2018-09-13

import csv
from random import randint

def makeDict(file, dictionary):

    ##open csv file
    with open(file, newline='') as csvfile:

        ##separate each row by comma into a string array
        csvfile = csv.reader(csvfile, delimiter=',')

        ##for each row, assign string 0 as the key, and
        ##string 1 in float form as the value
        ##exclude the first and the "Total" row
        rowNum = 0
        for row in csvfile:
            if rowNum != 0:
                dictionary[row[0]] = float(row[1])
            rowNum += 1
        dictionary.pop('Total')

occupations = {} 
makeDict('occupations.csv', occupations)

def randOccupation():

    ##num is a random float from 0 - 99.8 with 1 decimal point
    num = randint(0, 998) / 10.

    ##sum the percentages of the occupations until
    ##you get to a sum greater than num
    ##(the interval between sums is your percentage)
    ##break once this is true
    Sum = 0
    for occupation in occupations:
        Sum += occupations[occupation]
        if Sum >= num:
            print (occupation)
            break
        
randOccupation()

    
