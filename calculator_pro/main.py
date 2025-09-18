from art import logo


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calc():
    print(logo)
    nexto = 'continue'
    n1 = float(input("Insert first number: "))
    while nexto == 'continue':
        if nexto == 'new':
            n1 = float(input("Insert first number: "))
        command = input("Which operation do you want to do? +, -, *, or /: ")
        if command != '+' and command != '-' and command != '*' and command != '/':
            print("Invalid input. Try again.")
            continue
        n2 = float(input("Insert next number: "))
        res = int()
        if command == '+':
            res = add(n1, n2)
        elif command == '-':
            res = subtract(n1, n2)
        elif command == '*':
            res = multiply(n1, n2)
        else:
            res = divide(n1, n2)
        print(f"{n1} {command} {n2} = {res}")
        n1 = res
        nexto = input("If you want to continue calculation, enter 'continue'. If you want to start a new calculation, enter 'new': ").lower()
    if nexto == 'new':
        print('\n' * 20)
        calc()
    print("ERROR")

calc()