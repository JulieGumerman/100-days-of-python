def bottles_of_beer(bottle_number):
    print(f"{bottle_number} bottles of beer on the wall.\n {bottle_number} bottles of beer. \nTake one down, pass it around.")
    if bottle_number < 1:
        print("Congrats. You counted down. \nYou are a legend among men.")
        return
    else:
        new_bottle_number = bottle_number - 1
        print(f"{new_bottle_number} bottles of beer on the wall.")
        bottles_of_beer(new_bottle_number)


bottles_of_beer(99)