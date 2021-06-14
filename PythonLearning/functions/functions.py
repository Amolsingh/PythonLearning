
def multiply(a, b):
    result = a * b
    return result


answer = multiply(10.5, 5)
print(answer)

for val in range(5):
    print(multiply(5, val + 1))


def is_palindrome(string):
    backwards = string[::-1]
    return backwards == string


#Approach 2 More concise
def is_palindrome_2(string):
    return string[::-1].casefold() == string.casefold()

word = input("Please enter a word to check: ")
if is_palindrome_2(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

