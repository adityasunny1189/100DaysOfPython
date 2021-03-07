# Biding Problem

bidders = {}
name = input("Enter your name: ")
bid = int(input("Enter the bid: "))

bidding = True

def max_bidder_function(bidders):
	max_bidder = ''
	max_bid = 0
	for bidder in bidders:
		if bidders[bidder] > max_bid:
			max_bid = bidders[bidder]
			max_bidder = bidder
	print(f"Max bidder is {max_bidder} and his bid is {max_bid}")

while bidding:
	bidders[name] = bid
	continue_bidding = input("Continue bidding yes/no: ")
	if continue_bidding == "yes":
		name = input("Enter your name: ")
		bid = int(input("Enter the bid: "))
	else:
		bidding = False

max_bidder_function(bidders)