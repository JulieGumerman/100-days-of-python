import random
names_string = input("Enter a list of names")
names = names_string.split(", ")
print(f"{random.choice(names)} will pay.")
