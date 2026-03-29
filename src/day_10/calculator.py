from src.utils.input_helpers import get_input


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate(a, b, operator):
    if not a or not b or not operator:
        return None
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    return None


def calculator():
    print("===================================================================")
    print("==================Welcome to the calculator!=======================")
    print("===================================================================")

    use_result_as_input = False
    result = 0
    while True:
        first_num = (
            result
            if use_result_as_input
            else get_input("What is the first number?\n>>> ", cast=float)
        )
        operator = get_input(
            "What is the operation? (+, -, *, /)\n>>> ",
            choices=["+", "-", "*", "/"],
        )
        second_num = get_input("What is the second number?\n>>> ", cast=float)

        result = calculate(first_num, second_num, operator)

        next_choice = get_input(
            f"The result is {result:.2f}. Would you like to use that as the input for the next calculation? Or type 'q' to quit (y/n/q)\n>>> ",
            choices=["y", "n", "q"],
        )

        if next_choice == "y":
            use_result_as_input = True
        elif next_choice == "n":
            use_result_as_input = False
        elif next_choice == "q":
            break
