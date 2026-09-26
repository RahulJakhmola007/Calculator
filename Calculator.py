a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /, %, **): ")

if operator == '+':
        print(a + b)
elif operator == '-':
        print(a - b)
elif operator == '*':
        print(a * b)
elif operator == '/':
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero is not allowed.")
elif operator == '%':
        if b != 0:
            print(a % b)
        else:
            print("Error: Division by zero is not allowed.")
elif operator == '**':
        print(a ** b)
else:
        print("Error: Invalid operator. Please use one of the following: +, -, *, /, %, **.")