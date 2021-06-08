computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"] #A list

#For loop using iterable
for part in computer_parts:
    print(part)

print()
#For loop using index
length = len(computer_parts)

for i in range(length):
    print(computer_parts[i])

print()
#We can also use slicing
print(computer_parts[0:3])
print(computer_parts[-1])