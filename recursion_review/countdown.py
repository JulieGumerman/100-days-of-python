def countdown(i):
    print(i)
    # The line above takes care of business: It prints the variable "i." Easy.

    # The if-else block below does the heavy lifting.
    #
    # The "else" section calls the outer function, with an integer one less than the one the outer function called.
    # However, there is always one lower number, so you need a base case.
    # Enter the "if" section. If the number is less than one, game over. You exit the loop, and it returns.
    
    if i < 1:
        print("Yay!!!! No infinite loop!")
        return
    else:
        countdown(i-1)


countdown(15)