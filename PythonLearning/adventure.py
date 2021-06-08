available_exits = ["north", "south", "east", "west"]

chosen_exit = ""


while chosen_exit not in available_exits:
    chosen_exit = input("Please enter a direction ")
    if chosen_exit.casefold() == "quit":
        print("Game Over!!")
        break
else:
    print("Arn't you glad you got out of there")

for i in range(0,21):
    if i%3 == 0 and i%5 == 0:
        continue
    else:
        print(i)
