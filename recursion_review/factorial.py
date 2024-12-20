#factorials

#According to Oxford Languages, a FACTORIAL is the product of an integer and all the integers below it.

# For example, 3! = 3*2*1

# Per the book "Grokking Algorithms," this recursive function returns a factorial.

def factorial(x):
    if x == 1:
        # Base case: stop! You're down to 1.

        return 1
    else:
        #take the current input and multiply it by the next lowest number
        return x * factorial(x-1)


# However, it doesn't actually return the factorial product. It just counts it down. What happens if I print it out?

def factorialPrinted(x,y):
    # The variable y holds the factorial product as we are multiplying the different integers leading from x down to 1.
    if x == 1:
        # Base case: stop! You're down to 1.
        print("final", y)
        return 1
    else:
        # To keep multiplying, we multiply y by each integer smaller than x, one by one, as we count down from x to 1
        y = y * x
        #take the current input and multiply it by the next lowest number
        return x * factorialPrinted((x-1), y)


factorialPrinted(5,1)