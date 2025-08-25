print("welcome to rollercoaster!!!")

height = input("Please enter your height in cm: ")
height = int(height)

age = input("Please enter your height in cm: ")
age = int(age)

if height<120:
    print("You have to grow taller to be able to ride!!!!!")
else:
    print("Hurray, you are able to ride!!!!!!")

    if age <= 12:
        bill = 5
        print("you should pay $5 for ticket.")

    elif age > 12 and age <18:
        bill = 7
        print("you should pay $7 for ticket.")

    elif age <= 55 and age >= 45:
        print("everything is gonna be ok. Your ride is on us.")
        bill = 0
        
    else:
        bill = 12
        print("you should pay $12 for ticket.")


    take_photo = input("Do you want to take the photo, y or n?")

    if take_photo == "y":
        bill +=3

    print(f"your bill is {bill}")
    

    

    


