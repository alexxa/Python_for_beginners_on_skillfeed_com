#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Conditionals.

a,b = 0,1
if a == b:
    print(True)
    
if not a == b:
    print(False)
    
if a != b:
    print('Not equal')

if a > b:
    print('Greater')
    
if a >= b:
    print('Greater or equal')
    
if a < b:
    print('Smaller')

if a <= b: # not =>
    print('Smaller or equal')

if a==b or a < b:
    print('This is True')
    
if a!=b and b > 0:
    print('This is also True')    
    
if a!=b and b < 0:
    print('This is also True')  
    
    
if a > b:
    print('a is greater than b')    
elif a < b:
    print('a is less than b')  
else:
    print('a s equal to b')
#END