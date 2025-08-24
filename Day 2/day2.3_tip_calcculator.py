bill = input("How much is your bill? ")
bill = float(bill)

tip_percent = input("What percentage do you want to tip? ")
tip_percent = float(tip_percent)

people_num = input("You want to split bill among how many persons? ")
people_num = int(people_num)

full_bill = (1+ tip_percent/100)* bill

print(f"Each person should pay ${full_bill/people_num}")

full_bill_per_person = round(full_bill/people_num, 2)
print(f"Each person should pay ${full_bill_per_person}")

full_bill_per_person = "{:.2f}".format(full_bill_per_person)

print(f"Each person should pay ${full_bill_per_person}")
