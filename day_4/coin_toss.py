import random

users_choice = input ("Heads or tails? \n")
print(f"You chose {users_choice}")



coin_toss_result = random.randint(0,1)

if coin_toss_result == 0:
    print("The coin landed on heads.")
elif coin_toss_result == 1:
    print("The coin landed on tails.")


choice_as_number = 3
if users_choice == "heads":
    choice_as_number = 0
elif users_choice == "tails":
    choice_as_number = 1


if choice_as_number == coin_toss_result:
    print("you win")
else:
    print("you lose")


