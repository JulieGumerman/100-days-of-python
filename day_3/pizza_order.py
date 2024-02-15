print("Thank you for choosing Python Pizza Deliveries!")
cost = 0
size = input("What size do you want: S, M or L?")
if size == "S":
    cost += 13
if size == "M":
    cost += 16
if size == "L":
    cost += 19

add_pepperoni = input("Do you want peperoni: Y or N?")
if add_pepperoni == "Y":
    cost += 3
extra_cheese = input("Do you want extra cheese? Y or N")
if extra_cheese == "Y":
    cost += 2

print(f"Your total is ${cost}")