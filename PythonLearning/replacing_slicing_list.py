computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse rat"]
print(computer_parts)

computer_parts[3] = "trackball"
print(computer_parts)

#computer_parts[3] = "trackball"
print(computer_parts[3:])

computer_parts[3:] = ["trackball"]
print(computer_parts)

print("\n \n \n \n")
data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
#
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# for index, item in enumerate(data):
#     if(item < min_valid) or (item > max_valid):
#         del data[index]
#
# print(data)

stop = 0
for index, item in enumerate(data):
    if item >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

#process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)
del data[start:]
print(data)