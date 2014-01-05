#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Custom functions.

def function_name():
    "This is tagline"
    
    return "Hello!"

print(function_name())
print("Hello, world!");

list1 = [1,2,3,4]
def my_function(lists):
    "This is simply will demonstrate by reference"
    lists.append([5,6,7,8])
    return
print("The values are: ", list1)
my_function(list1)
print("The values are: ", list1)


def function():
    return "Fine."
    #return [1,2,3]
    #return #returns NULL if nth is specified

print(function())
#END