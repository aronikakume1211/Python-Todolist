def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


print("Select operation: +, -, *, /")
op = input("Enter operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == "+":
    print(add(a, b))
elif op == "-":
    print(subtract(a, b))
elif op == "*":
    print(multiply(a, b))
elif op == "/":
    print(divide(a, b))
else:
    print("Invalid operation")
