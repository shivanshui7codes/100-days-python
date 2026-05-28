from art import logo
print(logo)

def info():
    name = input("What is your name? \n")
    price = int(input("What is your bid? \n$"))
    details[name] = price

details = {}
info()
ask = input("Are there any other bidders? Type 'yes or 'no'.").lower()

while ask == "yes":
    print("\n" * 100)
    info()
    ask = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

highest_bid = 0
winner = ""
for bids in details:
    bid_amount = details[bids]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bids
print(f"The winner is {winner} with a bid of ${highest_bid}")
