#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 18.12.2013
#SOURSE: https://www.skillfeed.com/courses/539-python-for-beginners
#PURPOSE: Variables. Data type. Typecasting.  

x = 42;
y = 42.5;
print(x, id(x), type(x));
print(y, id(y), type(y));

xx, yy, zz = 0, 1, 2
print(xx, yy, zz)

# typecasting

a = int(50.0);
print(a);

b = int(50.9);
print(b);

print(round(50.9));

c = float(50);
print(c);

# strings

s1 = 'Hello';
s2 = "world";
print(s1+' '+s2, type(s1));

s3 = '''            
    This
    is 
    a string
'''

print(s3, type(s3));

s4 = """\
    This\
    is\
    also\
    a string\
"""

print(s4, type(s4));

# substitution, old style
s5 = '%s, Sam!' % s1;
print(s5);
s6 = '%s, %s!' % (s1,s2)
print(s6);

# substitution, new style
s7 = '{}, Sam!'.format(s1);
print(s7);
s8 = '{}, {}!'.format(s1,s2);
print(s8);

# tuples
t = (1, 2, 3 , 4, 5)
print(t, type(t));

# list
l = [1, 2, 3, 4, 5]
l.append(6)
print(l, type(l), l[0], l[2:4]);

# dictionary
d = {'one':1, 'two': 2}
print(d, type(d))

dictionary = dict(
                  one = 1, 
                  two = 'two'
                  )
print(dictionary, type(dictionary))

# boolean
boolean = False
print(boolean, type(boolean))
#END