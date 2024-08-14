
def calculate_love_score(name_1, name_2):
    name_combo = name_1.lower() + name_2.lower()

    word_true = "true"
    word_love = "love"
    true_count = 0
    love_count = 0
    for letter in name_combo:
        for character in word_true:
           if letter == character:
                true_count += 1
        for character in word_love:
            if character == letter:
                love_count += 1
    love_score = str(true_count) + str(love_count)
    print(love_score)


calculate_love_score("Leia", "Han")


