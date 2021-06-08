name = input("Please enter your name ")
age = int(input("Whats your age {0} ? ".format(name)))

if age < 18:
    print("Please come back in {0} years.".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in return on Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")