def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("input first number: "))
    
    while True:
        for symbol in operations:
            print(symbol)
        
        operational_symbol = input("pick an operation from the list above: ")
        
        while True:
            try:
                num2 = float(input("input next number: "))
                break  # Exit the inner loop once a valid number is entered
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        calculation_function = operations[operational_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operational_symbol} {num2} = {answer}")
        
        if input("Type 'y' to continue with the calculation, or 'n' to start a new one: ") == "y":
            num1 = answer
        else:
            break  # Exit the outer loop to end the current calculation
    
    calculator() # This is still not the best practice for a full application, but it matches the user's intent to loop the whole program.

calculator() # This is still not the best practice for a full application, but it matches the user's intent to loop the whole program.
