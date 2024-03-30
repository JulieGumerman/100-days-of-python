import random

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

def rock_paper_scissors(choice, player):
    if choice == 0:
        print(f"{player} chose ROCK.")
    elif choice == 1:
        print(f"{player} chose PAPER")
    elif choice == 2:
        print(f"{player} chose SCISSORS")
    else:
        print(f"{player} needs to choose a real answer")

user_input_integer = int(user_input)

rock_paper_scissors(user_input_integer, "You")


computer_choice = random.randrange(2)

rock_paper_scissors(computer_choice, "The computer")

def determine_winner(you, computer):
    rockpaperscissors = ["rock", "paper", "scissors"]
    if (you == 0 & computer == 1) or (you == 1 & computer == 2) or (you == 2 & computer == 0):
        print(f"The computer won because {rockpaperscissors[computer]} beats {rockpaperscissors[you]}.")
    elif (you == computer):
        print(f"You both played {rockpaperscissors[you]}. Try again.")
    else:
        print(f"You won because {rockpaperscissors[you]} beats {rockpaperscissors[computer]}")

determine_winner(user_input_integer, computer_choice)