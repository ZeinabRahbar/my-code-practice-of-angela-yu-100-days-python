import random
from game_data import data


score = 0
never_lost = True

for i in range(10):

    acount_a = random.choice(data)
    print(acount_a)
    print("acount a insta page:", acount_a['name'], ",job:", acount_a['description'],",country:", acount_a['country'])

    acount_b = random.choice(data)
    while  acount_a == acount_b:
            acount_b = random.choice(data)
        
    print("acount b insta page:", acount_b['name'], ",job:", acount_b['description'],",country:", acount_b['country'])
    choice = input("guess which acount has higher number of followers 'A' or 'B'???? ").lower()

    if choice == "a":
        picked_acount = acount_a
        rest_account = acount_b
    elif choice == "b":
        picked_acount = acount_b
        rest_account = acount_a

    if int(picked_acount['follower_count'])> int(rest_account['follower_count']):
        score += 1
        print(f"Continue game with score {score}.")

    else: 
        never_lost = False
        print(f"Game over with score {score}.")
        break


if never_lost == "True":
    print("Your score is the highest possible, you are the champion.")
    
        
