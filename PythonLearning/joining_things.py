flowers = ["Daffodil", "Evening Prirose", "Hydrangea", "Iris", "Lavender", "Sunflower", "Tiger Lily"]

for flower in flowers:
    print(flower)

separator = " | "
output = separator.join(flowers)
print(output)

#Split function by default splits using space
panagram = """The quick brown fox jumps over the lazy dog"""
words = panagram.split()
print(words)

numbers = "9|223|372|036|854|775|807"
print(numbers.split("|"))

values = "".join(char if char not in separator else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7', ' ']
values = "".join(generated_list).split()
print(values)


for i in range(len(values)):
    values[i] = int(values[i])

print(values)

#Create a new list
integer_values = []
for value in values:
    integer_values.append(value)

print(integer_values)