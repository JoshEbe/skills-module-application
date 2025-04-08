print("Welcome to this simple calculator!")

num1 = float(input("Enter the first number: "))
operator = input("What operation would you like to perform (+, -, *, /, ^): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
if operator == "-":
    result = num1 - num2
if operator == "*":
    result = num1 * num2
if operator == "/":
    result = num1 / num2
if operator == "^":
    result = num1 ** num2

print("Result:", result)