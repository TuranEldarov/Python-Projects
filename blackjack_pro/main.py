from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def decks():
    deck = []
    for i in range(2):
        card = random.choice(cards)
        deck.append(card)
    return deck

def add(deck):
    deck.append(random.choice(cards))
    return deck

def conditions(deck1, deck2):
    if sum(deck1) > 21:
        return "You went over. You lost."
    elif sum(deck2) > 21:
        return "Opponent went over. You won!"
    elif 21 - sum(deck1) < 21 - sum(deck2):
        return "You are closer to the goal. You won!"
    elif 21 - sum(deck1) > 21 - sum(deck2):
        return "Opponent is closer to the goal. You lost."
    else:
        return "Draw."

def main():
    print("*" * 10 + "Welcome to BLACKJACK!" + "*" * 10)
    your_deck = decks()
    dealer_deck = decks()
    while sum(dealer_deck) < 17:
        dealer_deck = add(dealer_deck)
    cont = 'yes'
    first = 1
    while cont == 'yes':
        if first == 2:
            your_deck.append(random.choice(cards))
        print(f"{' ' * 10} Your deck: {your_deck}, current score = {sum(your_deck)}")
        print(f"{' ' * 10} Dealer's first card: [{dealer_deck[0]}]")
        if sum(your_deck) > 21:
            break
        if sum(your_deck) == 21 and first == 1:
            print('*' * 40)
            print("Final hands:")
            print(f"{' ' * 15} Your deck: {your_deck}, final score = {sum(your_deck)}")
            print(f"{' ' * 15} Dealer's deck: {dealer_deck}, final score = {sum(dealer_deck)}")
            print("BLACKJACK! You won!")
            return
        first = 2
        cont = input("Do you want to get another card? Type 'yes' or 'no': ")
    if sum(your_deck) > 21 and 11 in your_deck:
        your_deck.remove(11)
        your_deck.append(1)
    if sum(dealer_deck) > 21 and 11 in your_deck:
        dealer_deck.remove(11)
        dealer_deck.append(1)
    print('*' * 40)
    print("Final hands:")
    print(f"{' ' * 15} Your deck: {your_deck}, final score = {sum(your_deck)}")
    print(f"{' ' * 15} Dealer's deck: {dealer_deck}, final score = {sum(dealer_deck)}")
    print(conditions(your_deck, dealer_deck))

while input("Do you want to play a new blackjack game? Type 'yes' or 'no': ") == 'yes':
    print('\n' * 20)
    print(logo)
    main()