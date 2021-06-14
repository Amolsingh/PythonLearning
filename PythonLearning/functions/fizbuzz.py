
def fizz_buzz(i: int) -> str:
    """

    :param i: Integer to be fizzed  bizzed with
    :return: String that says fizz, bizz or fizz buzz
    """
    if i%3 == 0 and i%5 == 0:
        return "fizz buzz"
    elif i%3 == 0:
        return "fizz"
    elif i%5 == 0:
        return "buzz"
    else:
        return "{}".format(i)


next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go:")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))