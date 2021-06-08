a = b = c = d = e = f = 12

print(c)

x, y = 1, 2

print(x)
print(y)

print()

print("Unpacking a tuple")
data = 1, 2, 76
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list = [12, 13, 14]
#data_list.append(15)
p, q, r = data_list
print(p)
print(q)
print(r)

#Any sequence type can be unpacked
#The above code at line 21 will fail cause we are tyring to change the list which we are unpacking at line 22

