#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Lists.

list1 = [1,2,3,4,5,6,7,8,9,10,11]
print(list1, list1[2], list1[-2], list1[0:5])
print(len(list1))

length = len(list1)
print(list1[length-2])
print(list1[0:10:3])

list1.append(12)
print(list1)

list2 = [12,0,13,14]
list1.extend(list2)
print(list1)

list1.insert(5,12)
print(list1)

list1[5]=0
print(list1)

list1[5] = list1[5] + 10
print(list1)

del list1[5:7]
print(list1)

list1.remove(9) #not index but value!!!!!
print(list1)


list1.reverse()
list1.append(100)
list1.reverse()
print(list1)

list1.sort()
print(list1)

list3 = sorted(list2)
print(list3)
#END