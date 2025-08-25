print("###############################################################################\n###############################################################################\n###############################################################################\n###############################################################################\n")

print("Welcome to Tresure Island!\nYour mission is to find the treasure.")
left_or_right = input("you or on a crossroad, pick left way or right way: ")

if left_or_right == "right":
    print("You fall to the hole, Game Over!!!")
else:
    swim_or_wait = input("you riched a river you can swim or you can wait for a boat, pick swim or wait: ")

    if swim_or_wait == "swim":
        print("You drawn, Game Over!!!")
    else:
        which_dooer = input("You reached 3 doors, one is yellow, one blue and one red, the treasure is behind one of them. pick yellow or blue or red door: ")
        if which_dooer == "blue" or which_dooer == "red":
            print("The beasts destroyed you. Game Over!!!")
        else:
            print("hurray, you won!!!!")
    
