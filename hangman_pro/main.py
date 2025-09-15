import random
import hangman_words
import hangman_art

stages = hangman_art.stages
stages.reverse()
logo = hangman_art.logo
word_list = hangman_words.word_list
word = random.choice(word_list)
print(logo)
array = []
blanks = "_" * len(word)
print(stages[0])
print(blanks)
level = 0
lost = False
health = len(stages) - 1
all_let = []
while blanks != word:
    check = False
    blanks = ""
    your_letter = input("Guess a letter: ").lower()
    if your_letter in all_let:
        print("Invalid input. You can't choose the letter you have chosen before.")
        continue
    all_let.append(your_letter)
    for char in word:
        if char in array:
            blanks += char
        elif your_letter == char:
            check = True
            blanks += char
            array.append(char)
        else:
            blanks += '_'
    if not check:
        health -= 1
        level += 1

    if level == len(stages) - 1:
        lost = True
        print(f"{blanks}\n{health} lives left")
        print(stages[level])
        print(f"The word was \"{word}\". You lost.")
        break
    print(f"{blanks}\n{health} lives left")
    print(stages[level])
if not lost:
    print("YOU WON!")