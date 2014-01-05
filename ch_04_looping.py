#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Looping.

# while loops
a = 0
while a < 100:
    print(a)
    a +=1
    
print()

# for loops
for data in [1, 2, 3, 4, 5]:
    print(data)
    
print()

for data in 'string':
    print(data)
 
print()

for key,data in enumerate('string'):
    if key % 2 == 0:
        print('This letter {} is in an even location'.format(data))

print()
        
# exceptions

tuple1 = (1, 2, 3, 4, 5)
try:
    tuple1.append(6)
except:
    print('Error formed')
else:
    for each in tuple1:
        print(each)
        
print()        

tuple2 = (1, 2, 3, 4, 5)
try:
    tuple2.append(6)
except AttributeError as e:
    print('Error formed:', e)
else:
    for each in tuple2:
        print(each)
        
print()   

tuple3 = (1, 2, 3, 4, 5)
try:
    tuple3.append(6)
    for each in tuple3:
        print(each)
except AttributeError as e:
    print('Error formed:', e)
    
print()   

tuple3 = (1, 2, 3, 4, 5)
try:
    #tuple3.append(6)
    for each in tuple3:
        print(each)
except AttributeError as e:
    print('Error formed:', e)    
except IOError as e:
    print('File not found:', e)
    
print()  
# break, continue and else

list1 = [1,2,3,4,5,6,7,8,9]
for var in list1:
    if var ==7:
        break
    print(var)
else:
    print('default')

print()

list1 = [1,2,3,4,5,6,7,8,9]
for var in list1:
    if var ==7:
        continue
    print(var)
else:
    print('default')
    
#END
           