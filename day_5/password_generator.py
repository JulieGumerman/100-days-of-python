import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the PyPassword Generator!")
r_letters = int(input("How many letters would you like in your password?\n"))
r_symbols = int(input("How many symbols would you like?\n"))
r_numbers = int(input("How many numbers would you like?\n"))

new_password = random.sample(letters, r_letters)
new_password += random.sample(numbers,r_numbers)
new_password += random.sample(symbols, r_symbols)
random.shuffle(new_password)
password= ''.join(new_password)


print("here is your password",password)