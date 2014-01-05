#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Switch

switch = dict(one = 'one', 
              two = 'twoo', 
              three = 'three')

var = 'two'
print(switch[var])

var = 'four'
print(switch.get(var, 'default'))


#END