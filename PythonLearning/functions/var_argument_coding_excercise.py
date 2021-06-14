
def sum_numbers (*nums: float) -> float:
    """
    Function to take variable arguments of float as an input and return the
    sum of all the numbers
    :param nums: Float value tuple
    :return: sum(Float) of all the input numbers
    """
    sum = 0

    for i in nums:
        sum += i

    return sum


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
