

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

#print number from 1 to 100
for x in range(1,101):
    if x%3 == 0 and x%5 != 0:
        print("Fizz")
    elif x%5 == 0 and x%3 != 0:
        print("Buzz")
    elif x%5 == 0 and x%3 == 0:
        print("FizzBuzz")
    else:
        print(x)