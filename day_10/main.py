# Calculator
import art

def add(n1, n2):
    """Add the number"""
    return n1 + n2

def subtract(n1, n2):
    """Subtract the number"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply the number"""
    return n1 * n2

def divide(n1, n2):
    """Divide the numbers"""
    if n2 == 0:
        print("Invalid input, division by zero is not allowed!.") 
        new_start = input("To restart type 'r': ").lower()
        if new_start == "r":
            calculator()
    else:
        return n1 / n2

oprations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number? "))
    for symbol in oprations:
        print(symbol)

    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number? "))
    calculation_function = oprations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')

    continue_operating = True
    while continue_operating:
        
        continue_cal = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if continue_cal == 'y':
            operation_symbol = input("Pick another operation: ")
            num3 = float(input("What's the next number? "))
            calculation_function = oprations[operation_symbol]
            second_answer = calculation_function(answer, num3) 
            print(f'{answer} {operation_symbol} {num3} = {second_answer}')
            
        elif continue_cal == 'n':
            continue_operating = False
            calculator()

calculator()

