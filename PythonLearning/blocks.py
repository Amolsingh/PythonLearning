for i in range(1, 13) :
    print("No {} squared is {} and cubed is {}".format(i, i**2, i **3))
print("*" * 80)

name = input("Please enter your name ")
age = int(input("Whats your name {0} ? ".format(name)))

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18-age))

if age < 18:
    print("Please come back in {0} years".format(18-age))
else:
    print("You are old enough to vote")
    print("Please put an X in the box")