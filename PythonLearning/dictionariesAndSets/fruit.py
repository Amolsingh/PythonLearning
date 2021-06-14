fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in branches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

print()
for val in fruit.values():
    print(val)

fruit_keys = fruit.keys()
print(type(fruit_keys))
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

print(type(fruit.values()))

print(fruit.items())


f_tuple = tuple(fruit.items())

print(f_tuple) #Returns tuple of tuples (key, values)
for f in f_tuple:
    item, description = f
    print(item + " is " + description)