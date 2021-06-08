#Python has several built-in data types, that can be classed as:
 #numeric
 #iterator
 #sequence(Which are also Iterators)
 #mapping
 #file
 #class
 #exception

 #Python 3 has 3 numeric data types
    #int - whole number does not having a fractional part
    #float - They have the fractional part
    #complex - They have real and imaginary part

    #Python int effectively has no aximum size. You will run out of memory before you exceed the size because there isnt any limit on the size

    #The maximum float value on a 64 bit computer is 1.7976931348623157e+308 which means move the decimal point 308 places right

    #The smallest float is 2.2250738585072014e-308, which has 307 zeroes before the decimal point.

a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a//b) #Integer division, rounded down towards minus infinity
print(a%b) #The remainder after integer division

print()
for i in range(1, a//b):
    print(i)


#Python is strongly typed and cant use float in the place of using an int
#BODMAS

print(a + b / 3 - 4 * 12)
print(a + (b/3) - (4*12))
print((((a+b)/3)-4)*12)