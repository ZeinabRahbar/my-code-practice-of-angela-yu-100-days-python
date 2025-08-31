from replit import clear
        
print("Hear you need to put your name and price for your bid.")

people_tobid = True
bid_dict = {}

def find_highest_bidder(bidding_record): 
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if highest_bid<bid_amount:

           highest_bid = bid_amount
           winner = bidder

    print(f"The winner is {bidder}, and the highest bid is {highest_bid}")
         
    

while people_tobid:
    name = input("What is your name? ")
    bid = int(input("What is your offer for bid price in $? "))

    bid_dict[name] = bid

    people_tobid = input('If there is more people to bid write Yes else No: ')

    if people_tobid == 'No':
        people_tobid = False
    elif people_tobid == 'Yes':
        clear()

find_highest_bidder(bid_dict)


