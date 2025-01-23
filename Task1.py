def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Welcome to the simple calculator!")

    while True:
        # Input two numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Input operation choice
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        operation = input("Choose operation (1/2/3/4/5): ")

        if operation == '1':
            print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
        elif operation == '2':
            print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '3':
            print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '4':
            print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
        elif operation == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid operation! Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    calculator()
