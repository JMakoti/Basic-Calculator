#Basic Calculator program

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        result = "Error! Division by zero."
        print(result)
else:
    result = "Invalid operation!"
    print(result)