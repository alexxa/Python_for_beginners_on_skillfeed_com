#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Database handling

import sqlite3

db = sqlite3.connect('database.db')
db.execute('drop table if exists persons')
db.execute('create table persons (firstname text, secondname text, age int)')
db.execute('drop table if exists people')
db.execute('create table people (firstname text, secondname text, age int)')
db.execute('insert into persons (firstname, secondname, age) values ("alex", "bowers", 17)')
db.execute('insert into persons (firstname, secondname, age) values ("irina", "gulina", 27)')
db.commit()
#db.execute('update persons set firstname = "Alexander" where secondname = "bowers"')
#db.commit()

#table = db.execute('select * from persons')
#table = db.execute('select firstname,secondname from persons')
#db.row_factory = sqlite3.Row
table1 = db.execute('select secondname, firstname from persons')
for each in table1:
    print(each)
    #print(dict(each)) # comment together with line 21: db.row_factory = sqlite3.Row
    #print(each['firstname']) # comment together with line 21: db.row_factory = sqlite3.Row
print()    
db.execute('delete from persons where firstname = "irina"')
db.commit()
table2 = db.execute('select secondname, firstname from persons')
for each in table2:
    print(each)

#END