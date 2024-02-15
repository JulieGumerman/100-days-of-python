print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction_1 = input("Would you like to go left or right?\n")

if direction_1 == "left":
    action = input("Swim or wait?\n")
    if action == "wait":
        print("keep going")
        door_color = input("Which color door: red, yellow or blue")
        if door_color == "red":
            print("Game over. You just got annihilated by fire.")
        elif door_color == "blue":
            print("You got eaten by beasts! Game over.")
        elif door_color == "yellow":
            print("You found the treasure. You found your way out! And you are still friends with everyone you came in with.")
        else:
            print("You just died of starvation because you never picked a door that was an option.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. \nGame over")



