
def factorial(i: int) -> int:
    """

    :param i: Integer whose factorial has to be calculated
    :return: Factorial Integer of the entered number
    """
    if i == 0:
        return 1
    elif i == 1:
        return 1

    return i * factorial(i-1)


for i in range(0, 36):
    print("{0}: {1}".format(i, factorial(i)))