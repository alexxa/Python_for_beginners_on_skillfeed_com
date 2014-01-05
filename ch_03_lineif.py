#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Conditionals.

a,b = 0,1
if a == b:
    print(True)
else:
    print(False)
    
print(True if a==b else False)    
print('this is True' if a==b else 'this is False') 

var = 'this is True' if a==b else 'this is False'
print(var)
#END