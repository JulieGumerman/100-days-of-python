target = int(input())

counter = 0
for number in range(1, (target + 1)):
    if number % 2 == 0:
        counter += number

print(f"You are adding even numbers up to {target}. Your total is {counter}")


