print("Welcome to this simple calculator!")

#gets input from user
num1 = float(input("Enter the first number: "))
operator = input("What operation would you like to perform (+, -, *, /, ^): ")
num2 = float(input("Enter the second number: "))

#addition
if operator == "+":
    result = num1 + num2

#subtraction
if operator == "-":
    result = num1 - num2

#multiplication
if operator == "*":
    result = num1 * num2

#division
if operator == "/":
    result = num1 / num2

#exponent
if operator == "^":
    result = num1 ** num2

print("Result:", result)