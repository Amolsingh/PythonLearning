numbers = (0, 1, 2, 3, 4, 5)

print(numbers)
print(*numbers, sep=";")

print(0, 1, 2, 3, 4, 5, sep=";")

#*args gets sent as a tuple
def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)