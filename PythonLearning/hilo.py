low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please ENTER to start: ")
guesses = 1

while low != high:
    print("low {0} and high {1}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower? Enter h or l, or c if my guess was correct ".format(guess)).casefold()

    if high_low == 'h':
        #Guess higher. The low end of the range becomes 1 greater than the guess
        #pass
        #pass statement is used to pass the specific block of code
        low = guess + 1
    elif high_low == 'l':
        #Guess higher. The low end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == 'c':
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h,l or c")

    guesses = guesses + 1
    # We can use Augmented assignment over here as guesses += 1
    # Augmented assignment makes the code more efficient
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guess")