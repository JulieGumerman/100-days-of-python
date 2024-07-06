# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
print(word)
word_success=list(word)
word_standin = ""

for letter in word:
    word_standin += "_ "

print(word_standin)



errors = 0

list(word)

while (errors <= 6) or word_success != []:
    guess = input("guess a letter\n").lower()
    if guess in word:
        #print("yes")
        for letter in list(word):
            print("my guess is" + guess)
            index = word.index(guess)
            print(guess, word_success)
            #print(guess, index)

        # replace that index in word_standin with the guess
        for letter in list(word):
            word_standin_array = list(word_standin)
            word_standin_array[index] = guess
            word_standin = "".join(word_standin_array)
            print(word_standin)

            word_success.remove(guess)
            #print("new_word_success_list", word_success)

    else:
        errors += 1
        print(errors)

