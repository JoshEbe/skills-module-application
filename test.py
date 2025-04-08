num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("What operation would you like to perform (+, -, *): ")

if operator == "+":
    result = num1 + num2
if operator == "-":
    result = num1 - num2
if operator == "*":
    result = num1 * num2

print("Result:", result)