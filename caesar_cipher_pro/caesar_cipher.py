import sys

def encrypt(textf, shiftf):
    for i in range(len(textf)):
        ind = alphabet.index(textf[i])
        ind += shiftf
        ind %= 26
        textf[i] = alphabet[ind]
    print(''.join(textf))

def decipher(textf, shiftf):
    for i in range(len(textf)):
        ind = alphabet.index(textf[i])
        ind -= shiftf
        if ind < 0:
            ind = -(abs(ind) % 26)
        textf[i] = alphabet[ind]
    print(''.join(textf))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

command = input("Type 'encode' to encrypt, type 'decode' to decipher:\n").lower()
if command != "encode" and command != "decode":
    print("Invalid input. Please, try again.")
    sys.exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text = list(text)
if command == "encode":
    print("Encrypted result:")
    encrypt(text, shift)
elif command == "decode":
    print("Deciphered result:")
    decipher(text, shift)