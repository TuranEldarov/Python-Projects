import art
from game_data import data
import random

original = data
print(art.logo)
print(f"{'*' * 20}Welcome to HigherOrLower game!{'*' * 20}")
print(f"Your goal is to choose which of the two famous Instagram accounts has more followers."
      f" Try your best and keep the streak alive!")

def comp(acc1, acc2):
    if acc1["follower_count"] > acc2["follower_count"]:
        return 'a'
    else:
        return 'b'

def new():

    maximus = len(data) - 1
    cont = 1
    acc1 = random.choice(data)
    name1 = acc1["name"]
    description1 = acc1["description"]
    country1 = acc1["country"]
    cur = 0
    yay = 0
    while cont:
        print(art.logo)
        if yay:
            print("That's right🎉!")
        print(f"Current Score: {cur}")
        data.remove(acc1)
        acc2 = random.choice(data)
        print(f"Variant A: {name1}, {description1}, {country1}.")
        print(art.versus)
        name2 = acc2["name"]
        description2 = acc2["description"]
        country2 = acc2["country"]
        print(f"Variant B: {name2}, {description2}, {country2}.")
        player = input("Enter your answer. 'A' or 'B': ").lower()
        real_ans = comp(acc1, acc2)
        if player == real_ans:
            yay = 1
            cur += 1
            if cur == maximus:
                break
        else:
            cont = 0
        print('\n' * 20)
        name1 = name2
        description1 = description2
        country1 = country2
        acc1 = acc2

    print(art.logo)
    if cur == maximus:
        print("YOU HAVE REACHED THE HIGHEST SCORE POSSIBLE🔥🔥. CONGRATULATIONS!")
        print(f"Final Score: {maximus}")
    else:
        print("Sorry, wrong answer😓.")
        print(f"Final Score: {cur}")
    return cur

big = 0
while input("To play a new game, enter 'X'.\n").lower() == 'x':
    big = max(big, new())
    print(f"Highest score: {big}")
    data = original