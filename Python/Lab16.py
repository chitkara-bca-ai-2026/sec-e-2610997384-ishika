

def add(a, b):
    """Returns a + b"""
    return a + b

def subtract(a, b):
    """Returns a - b"""
    return a - b

def multiply(a, b):
    """Returns a * b"""
    return a * b

def divide(a, b):
    """Returns a / b, returns None if b == 0"""
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    """Returns a % b, returns None if b == 0"""
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    """Uses a default argument exp=2, omitting exponent squares the base"""
    return base ** exp

def format_number(n):
    """Returns an integer if value has no decimal part, otherwise float"""
    if n == int(n):
        return int(n)
    return n

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


history = []

while True:
    print("\n" + "="*50)
    print("      ENTERPRISE MODULAR UTILITY CALCULATOR")
    print("="*50)
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == '1':
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        result = add(a, b)
        print(f"[RESULT] {format_number(a)} + {format_number(b)} = {format_number(result)}")
        history.append(f"{format_number(a)} + {format_number(b)} = {format_number(result)}")

    elif choice == '2':
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        result = subtract(a, b)
        print(f"[RESULT] {format_number(a)} - {format_number(b)} = {format_number(result)}")
        history.append(f"{format_number(a)} - {format_number(b)} = {format_number(result)}")

    elif choice == '3':
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        result = multiply(a, b)
        print(f"[RESULT] {format_number(a)} * {format_number(b)} = {format_number(result)}")
        history.append(f"{format_number(a)} * {format_number(b)} = {format_number(result)}")

    elif choice == '4':
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        result = divide(a, b)
        if result is None:
            print("[ERROR] Cannot divide by zero!")
        else:
            print(f"[RESULT] {format_number(a)} / {format_number(b)} = {format_number(result)}")
            history.append(f"{format_number(a)} / {format_number(b)} = {format_number(result)}")

    elif choice == '5':
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        result = modulus(a, b)
        if result is None:
            print("[ERROR] Cannot find modulus by zero!")
        else:
            print(f"[RESULT] {format_number(a)} % {format_number(b)} = {format_number(result)}")
            history.append(f"{format_number(a)} % {format_number(b)} = {format_number(result)}")

    elif choice == '6':
        base = get_number("Enter base: ")
        exp_input = input("Enter exponent (Press Enter for Square): ")
        if exp_input == "":
            result = power(base)  # default exp=2
            print(f"[RESULT] {format_number(base)} ^ 2 = {format_number(result)}")
            history.append(f"{format_number(base)} ^ 2 = {format_number(result)}")
        else:
            exp = float(exp_input)
            result = power(base, exp)
            print(f"[RESULT] {format_number(base)} ^ {format_number(exp)} = {format_number(result)}")
            history.append(f"{format_number(base)} ^ {format_number(exp)} = {format_number(result)}")

    elif choice == '7':
        print("\n--- Calculation History ---")
        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            for i, record in enumerate(history, 1):
                print(f"{i}. {record}")

    elif choice == '8':
        print("\nThank you for using Utility Calculator. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 to 8.")