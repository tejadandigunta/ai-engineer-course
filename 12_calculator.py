num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Operator you entered is not supported")
