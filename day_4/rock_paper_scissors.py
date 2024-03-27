user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

user_input_integer = int(user_input)
if user_input_integer == 0:
    print("You chose ROCK.")
elif user_input_integer == 1:
    print("You chose PAPER")
elif user_input_integer == 2:
    print("You chose SCISSORS")
else:
    print("Choose a real answer")

    