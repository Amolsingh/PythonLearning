#day = "Monday"
day = "Saturday"
temprature = 30
raining = True

#if day == "Saturday" and temprature > 27 and not raining:
if day == "Saturday" and temprature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn Python")


if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")