#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Classes and Objects.

class Person:
    def __init__(self,gender,name):
        self.gender = gender
        self.name = name
        
    def display(self):
        print('You are a ', self.gender, 'and your names is: ', self.name)
        print()
        
people = Person('Female','Irina')
people.display()

class Example:
    def __init__(self, **xwargs):
        # ** means any number of dictionaries
        # * any numnber of tuples
        self.variables = xwargs
            
    def set_vars(self,k,v):
        self.variables[k] = v
    def get_vars(self,k):
        return self.variables.get(k, None)
        
var = Example(Age = 17, Location = 'UK')
var.set_vars('name', 'Alex')
print(var.get_vars('name'))
print(var.get_vars('Location'))

# Inheiritance

class Animal:
    def eat(self):
        print('I like to eat Whiskas')
        
    def talk(self):
        print('Meow. Meow. I want Whiskas')
        
class Cat(Animal):
    def talk(self): #overwrites the parents method
        print('Meow.')
    def purr(self):
        print('I had Whiskas. Purr. Purr.')
    

Murka = Cat()
Murka.eat()
Murka.talk()
Murka.purr()
#END