print("Welcome to the tip calculator.")
bill_string = input("What was the total bill? ")
bill_int = int(bill_string.replace(bill_string[0],""))

people_splitting = int(input("How many people to split the bill? "))
pre_tip_total_per_person = bill_int/people_splitting
percentage_tip_string =  input("What percentage tip would you like to give: 10, 12 or 15?")
percentage_tip = int(percentage_tip_string)/100
tip_amount = percentage_tip*pre_tip_total_per_person
print(f"Each person should pay ${pre_tip_total_per_person + tip_amount}.")

