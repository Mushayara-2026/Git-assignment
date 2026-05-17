def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def square(a):
    return a * a

def power(a, b):
    return a ** b

if __name__ == "__main__":
    print("Welcome to the Mini Calculator!")
    print("Choose an operation: add, subtract, multiply, divide")
    choice = input("Enter choice: ").strip().lower()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "add":
        print("Result:", add(num1, num2))
    elif choice == "subtract":
        print("Result:", subtract(num1, num2))
    elif choice == "multiply":
        print("Result:", multiply(num1, num2))
    elif choice == "divide":
        print("Result:", divide(num1, num2))
    elif choice == "square":
        print("Result:", square(num1))
    elif choice == "power":
        num2 = float(input("Enter second number: "))
        print("Result:", power(num1, num2))
    else:
        print("Invalid choice!")