shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item != "spam":
        print("Buy " + item)

print()

#Continue causes all the remaining code in the block to be skipped for that current iteration
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)

print()
item_to_find = "spam"
found_at = None

#for index in range(6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index

print("Item found at index {0}".format(found_at))

print()
item_to_find = "albatros"
found_at = None

#for index in range(6)
#break will end the loop and come out of it. No more iterations will be done further
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("Item found at index {0}".format(found_at))
else:
    print("{} not found".format(item_to_find))


print()

item_to_find = "pasta"
#Easier  way to do without using For loop
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
