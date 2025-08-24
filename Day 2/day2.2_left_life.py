age = input("Please enter your age: ")
age = int(age)

die_age = input("In what age you think you will be die? ")
die_age = int(die_age)

month = (die_age - age) * 12
weak = (die_age - age) * 52
day = (die_age - age) * 365.25


print(f"if you die when you are 90, you will see {day} days and {weak} weaks and {month} months")
