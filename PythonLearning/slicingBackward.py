letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

backwards = letters[::-1]
print(backwards)


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[0:-1:5])
print(data[:-1:5])

flower = "blue violet"
print('blue' in flower)

flower = 'rose'
colour = "red"

print("The {1} is {0}".format(flower, colour))