height = input("Please enter your height in m: ")
weight = input("Please enter your weight in kg: ")

height = float(height)
weight = int(weight)

BMI = weight/height**2
BMI = round(BMI,2)

print(f"your BMI is {BMI}")

###########################################################################################
