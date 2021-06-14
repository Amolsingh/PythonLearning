# Examples
#
# Was it a car, or a cat, I saw?
# Do geese see god?
# Desnes not far, Rafton sensed.

def is_sentence_palindrome(string: str) -> bool:
    """

    :param string: The entered string will be a sentence. Only alphanumeric characters will be considered for
                    palindrome check. The special characters will be ignored.
    :return: The string which tells if the sentence provided is a palindrome or not
    """
    without_aplpha = ""
    for char in string:
        if char.casefold().isalnum():
            without_aplpha += char.casefold()

    if without_aplpha[::-1] == without_aplpha:
        return "String is a palindrome!!"
    else:
        return "Not a palindrome!!"

    return ""


print(is_sentence_palindrome("Desnes not far, Rafton sensed."))