from art import logo
print(logo)

def finding_best_bid(data):
    maxi = 0
    winner = ""
    for names in data:
        if data[names] > maxi:
            maxi = data[names]
            winner = names
    return maxi, winner
print("Welcome to blind auction program for brand new Legion Legion 9i Gen 9 with liquid cooling system!")
bids = {}

other = 'yes'
while other == 'yes':
    name = input("Please, enter your name: ")
    bid = int(input("What is your bid: $"))
    bids[name] = bid
    other = input("Are there other bidders? 'Yes' or 'No': ").lower()
    if other == 'yes':
        print('\n' * 20)
maximal_bid, owner = finding_best_bid(bids)
print(f"The new owner of Legion 9i is {owner} with the highest bid of ${maximal_bid}!"
      f" Congratulations!")