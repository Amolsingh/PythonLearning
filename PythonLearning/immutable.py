result = True
another_result = result

print(id(result))
print(id(another_result))
#id is guaranteed to be unique and constant for this object during its lifetime
#The CPython implementation does return the objects memory address,
#but not all Pythons will do that

#Python has to destroy this object and re create it then its ID will change

result= "correct"
print(id(result))
result += "ish"
print(id(result)) #Generates new ID