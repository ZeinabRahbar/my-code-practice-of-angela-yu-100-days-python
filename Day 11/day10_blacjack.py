import randomy

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def generate_cards():
    my_cards  = [] 

    for i in range(2):
        my_cards.append(random.choice(cards))

    return my_cards

def calculate_score(points):
    """
    take a list of cards
    returns cards point
    """
    return sum(points)

my_card = generate_cards()
computer_card = generate_cards()

print("The first computer card is: ", computer_card[0])
print("Your card is: ", my_card)


computer_point = calculate_score(computer_card)
my_point = calculate_score(my_card)


while my_point<21:
    continung = input("if you want to add another card print 'y': ")
    print("The first computer card is: ", computer_card[0])
    print("Your card is: ", my_card)


    if continung =='y':
            my_card.append(random.choice(cards))
            my_point = calculate_score(my_card)
    else:
        break


print("############################################################\n############################################################\nThe computer card is: ", computer_card)
print("Your card is: ", my_card)


if 11 in my_card and my_point> 21:
    my_point -=10

if 11 in my_card and computer_point> 21:
    computer_card -=10

if my_point>21:
    if computer_point>21:
        print("draw")
    else:
        print("computer is the winner")
else:
    if computer_point>21:
        print("you are the winner")

    elif my_point> computer_point:
            print("you are the winner")

    elif my_point == computer_point:
        print("Draw")

    elif computer_point> my_point:
        print("computer is the winner")











