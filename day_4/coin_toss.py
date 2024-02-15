import random

users_choice = input ("Heads or tails? \n")

result = random.seed(2)
print(result)

choice_as_number = 3
if input == "heads":
    choice_as_number = 0
elif input == "tails":
    choice_as_number = 1


if choice_as_number == result:
    print("you win")
else:
    print("you lose")


