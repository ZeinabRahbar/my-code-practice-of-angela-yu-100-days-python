import random
import sys


def print_game_logo():
    logo = r"""
  _    _                                       
 | |  | |                                      
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
    """
    print(logo)

print_game_logo()


def find_all_occurrences(s, sub):
    positions = []
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            break
        positions.append(start)
        start += 1  # Move at least one position forward to find overlapping occurrences too
    return positions


#print num hearts each line
def print_hearts(num):
    print("♥" * num)


#Add game logo hear

#Extend list of words
word_lists = [
    "baboon", "ardvark", "donkey", "monkey",
    "elephant", "giraffe", "zebra", "tiger",
    "lion", "cheetah", "hippopotamus", "kangaroo",
    "ostrich", "rhinoceros", "buffalo", "alligator",
    "crocodile", "chimpanzee", "leopard", "panther",
    "python", "falcon", "eagle", "parrot",
    "dolphin", "whale", "shark", "octopus",
    "penguin", "flamingo", "peacock", "toucan"
]

picked_word = random.choice(word_lists)

temp_string = []

for i in range(len(picked_word)):
    temp_string.append("_")

print("Guess the string:\n",temp_string)

heart = 5

guessed_letter_list = []

while "_" in temp_string:

    print_hearts(heart)
    guessed_letter = input("guess a letter: ").lower()

    if guessed_letter not in guessed_letter_list:

        guessed_letter_list.append(guessed_letter)

        
        if picked_word.find(guessed_letter) == -1:
            heart -= 1
            if heart>0:
                print(f"you lost 1 heart, your hearts is {heart} now!!!")
            else:
                print(f"the word was {picked_word}")
                print("Game Over!!!")
                exit()
        else:
            place_list = find_all_occurrences(picked_word, guessed_letter)

            for i in place_list:
            
                temp_string[i] = guessed_letter

            print("updated: ", temp_string)

    else:
        heart -= 1
        if heart>0:
                print(f"you lost 1 heart, your hearts is {heart} now!!!")
        else:
                print(f"the word was {picked_word}")
                print("Game Over!!!")
                exit()
            
                

print("Hurray, you won!!!!!")

#make this a telegram bot game.
