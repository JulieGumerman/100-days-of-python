target = int(input())

counter = 0

for number in range(0, target + 1, 2):
    counter += number


print(f"You are counting even numbers only. Your total is {counter}")