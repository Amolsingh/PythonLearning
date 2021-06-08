# Python provides Several ways to repeat a block of code - things like:
#     - For Loops
#     - while loops
#     - list comprehensions and generator expressions

# A for loop works by iterating over some set of values

# It assigns each of values, one by one, to one or more variables

# It then executes a block of code once for each value.

# The set of values comes from a sequence, or some other iterable object

# An iterable object is anything that can be iterated over. That means a sequence is also an iterable

# Range is iterable

tag = "We are Blueyonder"
for i in tag:
    print(i)

number = "9,223;372:036 854,775;807"
seprators = ""

for char in number:
    if not char.isnumeric():
        seprators = seprators + char

print(seprators)

values = "".join(char if char not in seprators else " " for char in number).split()
print([int(val) for val in values])

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
capital = ""
# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        capital = capital + char

print(capital)
values = "".join(char if char in capital else " " for char in quote).split()
print([val for val in values])


#In C and Java the for loops work differently. In those languages, you provide a starting value and an ending value,
#and increment a variable each time round the loop. Pythons different approach to for loops makes them incredibly powerful and
#also very flexible. We can get the same effect as C for loops, by iterating over a range of values.

