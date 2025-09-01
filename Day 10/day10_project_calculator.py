def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

num1 = int(input("input first number: "))

for sumbol in operations:
    print(sumbol)
operational_symbol = input("pick an operation of the list above: ")

should_continue = True

while should_continue:
    num2 = int(input("input second number: "))

    calculation_function = operations[operational_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operational_symbol} {num2} = {answer}")



    a = input (f"Type 'y' if you want continue calculation: ")

    if a == 'y':
        num1 = answer
    else:
        should_continue = False

    operational_symbol = input("pick another operation: ")

