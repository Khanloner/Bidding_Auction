import os

def clear():
    os.system('cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bid_dictionary = {}
def bid_auction(name , bid):
  bid_dictionary[bidder_name] = bid_amount
  
bidding = True
while bidding:
  bidder_name = input("What is your name?\n")
  bid_amount = int(input("What's your bid?\n$"))
  bid_auction(name = bidder_name,bid = bid_amount)
  more_bid = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if more_bid == "yes":
    clear()
    bidding = True
  else:
    bidding = False

highest_bid = 0
high_bidder = ""
for key in bid_dictionary:
    current_bid = bid_dictionary[key]
    if current_bid > highest_bid:
        highest_bid = current_bid
        high_bidder = key

print(bid_dictionary)
print(f"The winner is {high_bidder} with a bid of ${high_bidder}")