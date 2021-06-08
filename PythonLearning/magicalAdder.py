
enter_int_list = input("Please enter 3 integer separated by coma: ")
convert_list = enter_int_list.split(",")



for i in range(len(convert_list)):
    convert_list[i] = int(convert_list[i])

#print(convert_list)

result= 0
for i in convert_list:
    if convert_list.index(i) == 0:
        result += i
    elif convert_list.index(i) == 1:
        result += i
    elif convert_list.index(i) == 2:
        result -= i

print(result)