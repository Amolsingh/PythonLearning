import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return  int(temp)
        #else:
        print("{0} is not a valid number".format(temp))


highest = 10
answer = random.randint(1, highest)
print("Please guess number between 1 and {}: ".format(highest))
#guess = int(input())
guess = get_integer(": ")

#Test for the too low guess
if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")