import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!"
      "This program will give you a strong password based on your preferences.")
letter_count = int(input("How many letter would you like in your password? "))
number_count = int(input("How many numbers would you like? "))
symbol_count = int(input("Lastly, how many symbols would you like in your password? "))

password = []
for num in range(0, letter_count):
    password.append(random.choice(letters))

for num in range(0, number_count):
    password.append(random.choice(numbers))

for num in range(0, symbol_count):
    password.append(random.choice(symbols))

random.shuffle(password)
print(f"Your generated password is: {"".join(password)}")