#Tianrun Liu and Cathy Cai -- FunRun!
#SoftDev1 pd6
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

db = sqlite3.connect("sp_database.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#**************FILL TABLE COURSES********************

#open and read csv file
file = open('data/courses.csv')
reader = csv.DictReader(file)

#create courses table
command = "CREATE TABLE courses_table(code TEXT,mark INTEGER,id INTEGER)"
c.execute(command)    #run SQL statement

#add data by key into table
for row in reader:
	command2 = 'INSERT INTO courses_table VALUES("' + row['code'] + '",' +  row['mark'] + ',' + row['id'] + ')'
	c.execute(command2,row)

#**************FILL TABLE PEEPS********************

#open and read csv file
file = open('data/peeps.csv')
new_reader = csv.DictReader(file)

#create peeps table
command3 = "CREATE TABLE peeps_table(name TEXT,age INTEGER,id INTEGER)"
c.execute(command3)

#add data by key into table
for row in new_reader:
	command4 = 'INSERT INTO peeps_table VALUES("' + row['name'] + '",' +  row['age'] + ',' + row['id'] + ')'
	c.execute(command4,row)

#==========================================================

db.commit() #save changes #test code
print("**************************COURSES TABLE*********************************")
c.execute("SELECT * FROM courses_table")
print(c.fetchall())
print("**************************PEEPS TABLE*********************************")
c.execute("SELECT * FROM peeps_table")
print(c.fetchall())
print("***********************************************************")
db.close()  #close database
