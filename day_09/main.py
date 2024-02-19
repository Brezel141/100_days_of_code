# The secret auction

from replit import clear
import art

print(art.logo)

other_bid = True
bider = {}

def find_winner(bidding_record):
    highest_bid = 0
    winner = ""
    #{"Angela": 123, "Jam":444}
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
    print(f'The winner is {winner}, whit ${highest_bid}!')

while other_bid:
    name = input("What's yor name?\n")
    bid = int(input("How much you like to bid?\n$"))
    bider[name] = bid
    other_name = input("There is another bider? 'Yes' or 'No'\n").lower()
    
    if other_name == "no":
        other_bid = False
        find_winner(bider)
    elif other_name == 'yes':
        clear()

