#Remember how string slices returned the characters up to but not including the end number.
#Ranges work in the same way. The last value specified is not included.
for i in range(1, 21):
    print("i is now {0}".format(i))

print()
#No starting index starts from 0
for i in range(10):
    print(i)

print()
#Gives no output, trying to step over by 2 without giving starting index
for i in range(10, 2):
    print(i)

print()

for i in range(0, 10, 2):
    print(i)
print()

for i in range(10, 0, -2):
    print(i)
print()

#No need to give the start value
for i in range(10):
    print(i)
print()

#For 0 to 10, incrementing by 2
for i in range(0, 10, 2):
    print(i)
print()

for i in range(0, 101):
    if i%7 == 0:
        print(i)