import random

back = '''
    _______
---'   ___|_)____
          _____|_)
          ______|_)
         ______|_)
---._________|_)
'''

palm = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

choices = []
choices.extend([back, palm])

print("Welcome to \"Hand, hand, overhand\" game!"
      "You can either choose \"back\" or \"palm\"")
your_hand = input("What are you waiting for? Bring your hand!\n")
npc1 = random.choice(choices)
npc2 = random.choice(choices)

if your_hand == "back":
    print("You:\n" + choices[0])
    print("NPC 1 :\n" + npc1)
    print("NPC 2 :\n" + npc2)
    if npc1 == back and npc2 == back:
        print("DRAW, try again!")
    elif npc1 == palm and npc2 == back:
        print("NPC 1 won!")
    elif npc1 == back and npc2 == palm:
        print("NPC 2 won!")
    else:
        print("Congratulations! You won!")
elif your_hand == "palm":
    print("You:\n" + choices[1])
    print("NPC 1 :\n" + npc1)
    print("NPC 2 :\n" + npc2)
    if npc1 == palm and npc2 == palm:
        print("DRAW, try again!")
    elif npc1 == palm and npc2 == back:
        print("NPC 2 won!")
    elif npc1 == back and npc2 == palm:
        print("NPC 1 won!")
    else:
        print("Congratulations! You won!")
else:
    print("Invalid input, please try again!")