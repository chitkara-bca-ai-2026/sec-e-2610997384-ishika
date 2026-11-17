

def factorial(n):
    """Takes a non-negative integer n, calculates factorial using recursion"""
    
    if n <= 1:
        return 1
    
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Takes an integer n (0-indexed), returns nth Fibonacci number using recursion"""
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    print("\n" + "="*50)
    print("      MATHEMATICS LEARNING TOOL")
    print("="*50)
    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    
    if choice == '1':
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("[ERROR] Please enter a non-negative integer!")
        else:
            result = factorial(n)
            print(f"[RESULT] Factorial of {n} ({n}!) = {result}")

    elif choice == '2':
        terms = int(input("Enter number of terms to generate: "))
        if terms <= 0:
            print("[ERROR] Please enter a positive number of terms!")
        else:
            series = []
            for i in range(terms):
                series.append(fibonacci(i))
            print(f"[RESULT] Fibonacci series ({terms} terms): {series}")

    
    elif choice == '3':
        print("\nThank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 to 3.")