a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
operator = input("Enter an operation (+, -, *, /): ")
# choosing which operation to be made between the numbers
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")
