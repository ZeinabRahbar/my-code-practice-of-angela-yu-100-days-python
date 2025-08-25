height = input("Please enter your height in m: ")
weight = input("Please enter your weight in kg: ")

height = float(height)
weight = int(weight)

BMI = weight/height**2
BMI = round(BMI,2)



###########################################################################################

if BMI<18.5:
    print(f"your BMI is {BMI}, you are underwight!!!")


elif 18.5<BMI and BMI <25:
    print(f"your BMI is {BMI}, you have a normal weight!!!")

elif 25<BMI and BMI <30:
    print(f"your BMI is {BMI}, you are overwight!!!")


elif 30<BMI and BMI <35:
    print(f"your BMI is {BMI}, you are obese!!!")

elif BMI>25:
    print(f"your BMI is {BMI}, You are clinically obese!!!")

