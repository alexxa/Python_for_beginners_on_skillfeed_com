#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Predefined string functions.

#string = ['s','t','r','i','n','g']
#string = 'string'
string = 'this is a string of text in a variable called string'

print(string)
print(string[:4])
print(string[:4:2])

for letter in string:
    print(letter)

print()    
print(string.count('s'))
print(string.title())
print(string.capitalize()) # capitalize only the 1st letter of the string

tire = '-'
sequence1 = ['s','t','r','i','n','g']
print(tire.join(sequence1))

sequence2 = 'a-b-c-d-e-f'
print(sequence2.split('-'))

#END