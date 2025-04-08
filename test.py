print("Welcome to this simple calculator!")

#gets input from user
num1 = float(input("Enter the first number: "))
operator = input("What operation would you like to perform (+, -, *, /, ^, root): ")
num2 = float(input("Enter the second number: "))

#addition
if operator == "+":
    result = num1 + num2

#subtraction
elif operator == "-":
    result = num1 - num2

#multiplication
elif operator == "*":
    result = num1 * num2

#division
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"

#exponent
elif operator == "^":
    result = num1 ** num2

#root, num1 is base and num2 is root
elif operator == "root":
    result = num1 ** (1/num2)

#if the user enters something not in the list as an operator
else: 
    result = "Invalid operation!"

print("Result:", result)