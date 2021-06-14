def sum_eo(n, t):
    sum = 0
    if t == 'e':
        for i in range(n):
            if i % 2 == 0:
                sum += i
        return sum
    elif t == 'o':
        for i in range(1, n):
            if i % 2 != 0:
                sum += i
        return sum
    else:
        return -1

print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(7, 'spam'))