#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Modules

import datetime
now = datetime.datetime.now()
print(now)

print()

start = datetime.datetime.now()

i = 0
while i < 1000000:
    i += 1 
end = datetime.datetime.now()
print(end - start)


import sys
path = sys.path
print(path)

import os
name = os.name
print(name)

import say
print(say.hello())
print(say.x)
#END