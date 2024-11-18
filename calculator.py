def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    print("-----------------")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    print("\nAvailable operations:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    for key, (name, func) in operations.items():
        print(f"\nPerforming {name}:")
        result = func(num1, num2)
        print(f"{name} of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    calculator()
