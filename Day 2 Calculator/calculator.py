# 🎯 Mini Project – Simple Calculator
# Create a calculator that:
# Takes two numbers.
# Prints:
# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Power
# Use f-strings for the output.
print("==========Welcome to My Calculator==========")
a = int(input("Please enter the first number: "))
o = input("Please enter the operator you want to use from the given operators: + , - , * , / , // , % , **:")
b = int(input("Please Enter the sencond number: "))

if o == '+':
    print(f"The Result of {a} {o} {b} is", a + b)

elif o == '-':
    print(f"The Result of {a} {o} {b} is", a - b)

elif o == '*':
    print(f"The Result of {a} {o} {b} is", a * b)

elif o == '/':
    print(f"The Result of {a} {o} {b} is", a / b)

elif o == '//':
    print(f"The Result of {a} {o} {b} is", a // b)

elif o == '%':
    print(f"The Result of {a} {o} {b} is", a % b)

elif o == '**':
    print(f"The Result of {a} {o} {b} is", a ** b)

else:
    print("Invalid value")

