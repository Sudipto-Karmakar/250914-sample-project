#Python code for arithmetic operations
#addition
def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The sum is: {a + b}")
#subtraction
def subtract():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The difference is: {a - b}")
#multiplication
def multiply():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The product is: {a * b}")
#division
def divide():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print(f"The quotient is: {a / b}")
    else:
        print("Error: Division by zero is not allowed.")

print("Select operation:")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")  

choice = input("Enter choice(1/2/3/4): ")   
if choice == '1':
    add()
elif choice == '2':
    subtract()
elif choice == '3':
    multiply()
elif choice == '4':
    divide()
else:
    print("Invalid input")  