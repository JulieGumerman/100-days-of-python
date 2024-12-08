# I got curious about how to calculate a factorial using a loop, so here it is.

def factorial(integer):
    int_range = range(1, integer + 1)
    factorial = 1
    for i in int_range:
        print(factorial)
        factorial = factorial * i

    print(factorial)

factorial(5)

# That turned out to be really easy.