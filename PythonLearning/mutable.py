#A mutable object is one whose value can be changed
#Python has the following mutable objects built in:
    #list
    #dict
    #set
    #Bytearray

#We can change the value of the mutable objects, without the object
#being destroyed and re-created

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
another_list = shopping_list

print(id(shopping_list))
print(id(shopping_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

#Python allows chain assignmen
a = b = c = d = e = f = another_list
print(a)

print("Adding Cream")
b.append("cream")
print(c)
print(d)