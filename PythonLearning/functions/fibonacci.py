
def triangle(n):
    if n == 1:
        return 1
    else:
        print(n)
        return n + triangle(n - 1)

#Using Recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #print(n)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

#Using Approach 2
def fib(n: int) -> int:
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range(36):
    print(i, fib(i))

