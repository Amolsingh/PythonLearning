letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

backwards = letters[::-1]
print(backwards)

#Print qpo
qpo = letters[16:13:-1]
print(qpo)

#Print edcba
edcba = letters[4::-1]
print(edcba)

#Print last 4 letters wxyz
print(letters[-4:])

#Print zyxwvuts
zyxwvuts = letters[25:17:-1]
print(zyxwvuts)

#Print z
print(letters[-1:])

#Print a
print(letters[:1])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[0:-1:5])
print(data[:-1:5])

flower = "blue violet"
print('blue' in flower)

flower = 'rose'
colour = "red"

print("The {1} is {0}".format(flower, colour))