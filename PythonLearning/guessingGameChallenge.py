import random

highest = 10
answer = random.randint(1, highest)

print(answer)

number = int(input("Enter the number: "))

while(True):
    if number == answer:
        print("Wow!! You guessed the right number!!")
        break
    elif number == 0:
        print("You have opted for quitting the game. ")
        break
    else:
        if number < answer:
            number = int(input("Wrong Answer!! Please try guessing higher than {}. Enter number: ".format(number)))
        else:
            number = int(input("Wrong guess!! Please try guessing lower than {}. Enter number: ".format(number)))
