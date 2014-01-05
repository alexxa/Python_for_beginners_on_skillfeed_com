#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: File Handling

# opening file
file = open('text.txt')

for line in file:
    print(line, end = '')
    
# writing file

input1 = open('text.txt', 'r')
output1 = open('newfile.txt', 'w')
for line in input1:
    print(line, file = output1, end = '')
    
print()
# handling big files

buffersize = 2
input2 = open('text.txt', 'r')
output2 = open('newbigdata.txt', 'w')
buffer = input2.read(buffersize)
bufferlimit = 40
while bufferlimit > 0:
    output2.write(buffer)
    print('.', end = '')
    bufferlimit = bufferlimit - buffersize
    
print()
# binary files

buffersize = 10000
input3 = open('pic.jpg', 'rb')
output3 = open('newpic.jpg', 'wb')
buffer = input3.read(buffersize)

while len(buffer):
    output3.write(buffer)
    print('.', end = '')
    buffer = input3.read(buffersize)

#END