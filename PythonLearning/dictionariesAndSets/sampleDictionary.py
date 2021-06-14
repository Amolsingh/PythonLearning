#Since Python 3.6 the original ordering of the keys is preserved
#That means you wont see random behavior wen printing the dictionary keys

#In Python 3.6 and earlier we could have used sorted to sort the dictionary as shown below

numbers = {
    1: "one",
    3: "three",
    5: "five",
    7: "seven",
    9: "nine"
}

print("I can't count odd numbers in order")
for key in numbers:
    print(numbers[key])

numbers[8] = "eight"
numbers[2] = "two"
numbers[6] = "six"
numbers[4] = "four"

print()
print("I can count to 9 in order")

for key in numbers:
    print(numbers[key])

# If your code relies on the keys being sorted, sort them first
print()
print("I really can")
for key in sorted(numbers):
    print(numbers[key])

print()
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in branches",
         "lime": "a sour, green citrus fruit"}

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])


print(fruit)
print()
print(fruit["lemon"])
print(fruit["lime"])

fruit["pear"] ="an odd shaped apple"


print(fruit)
fruit["pear"] = "great with tequilla"

print(fruit)

#delete an entry from Dictionary
del fruit["lemon"]
print(fruit)

#del fruit will delete the Dictionary but fruit.clear() will only delete the content
#If we try to print the key which is not present in the Dictionary we get KeyError

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == 'quit':
        break
    # description = fruit.get(dict_key, "We dont have a " + dict_key)
    # print(description)
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)

for snack in fruit:
    print(fruit(snack))

for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit(snack))
    print('-' + 40)

ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f + " - " + fruit(f))
