#Isaac Jon and Cathy Cai -- Jones Beach
#SoftDev1 pd6
#K17 -- Average
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

db = sqlite3.connect("sp_database.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

##Store data with the student ID and mark of each course
command0 = 'SELECT id, mark FROM courses_table;'
c.execute(command0)
data = c.fetchall()

##Create peeps_avg table
##command1 = "CREATE TABLE {0}({1}, {2}, {3})".format("peeps_avg", "name TEXT", "id INTEGER", "avg NUMERIC")
##c.execute(command1)

##Initiate the loop
person = data[0][0]
avg = 0.
count = 0

##for every ID/course pair in data
for pair in data:

    ##sum the grades are of the same ID
    if pair[0] == person:
##        print (pair[0])
        avg += pair[1]
        count += 1

    ##add to table if you've finished with one ID/person
    else:
        command2 = "SELECT name FROM peeps_table WHERE id = " + str(person) + ";"
##        print (command2)
        c.execute(command2)
        name = c.fetchone()[0]
##        print (name)
        command3 = 'INSERT INTO peeps_avg VALUES("' + str(name) + '", "' + str(person) + '", "' + str(avg / count) + '")'
##        print (command3)
        c.execute(command3)
##        print (avg)
##        print (count)
##        print ('new person')
##        print (pair[0])
        person = pair[0]
        avg = float(pair[1])
        count = 1

##print out peeps_avg table
command4 = 'SELECT * FROM peeps_avg'
c.execute(command4)
print(c.fetchall())

#==========================================================

#save changes #test code
##db.commit()

#close database
db.close() 

