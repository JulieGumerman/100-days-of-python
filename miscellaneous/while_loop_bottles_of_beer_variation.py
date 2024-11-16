# Earlier today, in the "recursive" directory in this repo, I wrote "99 Bottles of Beer on the Wall" as a recursive function.

# However, life is short, and I realized I could do the same thing with a while loop.

def bottles_of_beer_while_loop(bottle_number):

    while bottle_number > 0:
        print(f"{bottle_number} bottles of beer on the wall. \n {bottle_number} bottles of beer. \nTake one down. \nPass it around.")
        bottle_number = bottle_number - 1
        print(f"{bottle_number} bottles of beer on the wall.")

    print("Congrats! You did it! And you didn't infinite loop, and you didn't lose your place.")

bottles_of_beer_while_loop(99)