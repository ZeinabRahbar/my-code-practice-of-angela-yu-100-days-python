import random
is_winned = False

def is_won(num, guess):
    if num== guess:
        print("You won!")
    elif guess< num:
        print("your guess is lower than the number!")
    else:
        print("your guess is more than the number!")


print("Welcome to the Number Guessing Game!")
print("I'm thinking if a number between 1 and 100.")


difficulty = input("choose a difficulty, type 'easy' or 'hard': ")

num = random.randint(1, 100)

if difficulty == 'hard':
    print("you have 5 guess")

    for i in range(5):
        guess = int(input("make a guess: "))
        is_won(num, guess)

        if num == guess:
            is_winned = True
            break


elif difficulty == 'easy':
    print("you have 10 guess")

    for i in range(10):
        guess = int(input("make a guess: "))
        is_won(num, guess)

        if num == guess:
            is_winned = True
            break

if is_winned == False:
    print("You ran out of guess and you lost, the number was", num)
