#Program for Binary Search

orderedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = int(input("Enter the number to search in ordered List : "))
#Formula = low + (high - low) // 2

mid = 0
low = orderedList[0]
high = len(orderedList) - 1

if number == orderedList[mid]:
    print("nuber found at index 0")

if number == orderedList[high]:
    print("number found at index {}".format(high))

while number != orderedList[mid]:
    if (number not in orderedList):
        print("Sorry you have entered an invalid number")
        break
    mid = low + (high - low) // 2
    if orderedList[mid] > number:
        high = mid
    elif orderedList[mid] < number:
        low = mid
    else:
        print("number found at index {}".format(mid))
        break