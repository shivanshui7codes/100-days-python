from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiplication(n1, n2_):
    return n1 * n2_

def divide(n1, n2):
    return n1 / n2

operations = {
"+": add ,
"-": subtract,
"*": multiplication,
"/": divide,
}

previous_result = [0]

def program(f1):

    for key in operations:
        print(key)
    choose = input("Pick an operation\n")
    next_num = float(input("What's the next number?\n"))

    result = operations[choose](f1, next_num)
    previous_result[0] = result

    show = f"{f1} {choose} {next_num} = {result} "
    print(show)



first_num = float(input("What's the first number?\n"))

while True:
    program(first_num)
    again = input(f"Type 'y' to continue calculating with {previous_result[0]} , or type 'n' to start a new calculation:").lower()

    if again == "y":
        first_num = previous_result[0]
    elif again == "n":
        print("\n" * 100)
        first_num = float(input("What's the first number?\n"))
    else:
        print("INVALID INPUT")
        break
