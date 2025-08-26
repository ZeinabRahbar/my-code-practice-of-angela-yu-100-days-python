import random

your_choice = int(input("pick your choice rock:0, scissors:1 or paper:2  "))
computer_choice = random.randint(0, 2)

print(f"your choice is {your_choice}, computer choice is {computer_choice}.")
if your_choice == 0:
    if computer_choice == 0 :
        print("It's a draw!!!!")
        
    elif computer_choice == 1:
        print("You Won!!!")

    elif computer_choice == 2:
        print("Computer won!!!")
    
elif your_choice == 1:
    if computer_choice == 1 :
        print("It's a draw!!!!")
        
    elif computer_choice == 2:
        print("You Won!!!")

    elif computer_choice == 0:
        print("Computer won!!!")

    
elif your_choice == 2:
    if computer_choice == 2 :
        print("It's a draw!!!!")
        
    elif computer_choice == 0:
        print("You Won!!!")

    elif computer_choice == 1:
        print("Computer won!!!")
