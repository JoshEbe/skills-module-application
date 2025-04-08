num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("plus or minus: ")

if operator == "+":
    result = num1 + num2
if operator == "-":
    result = num1 - num2

print("Result:", result)