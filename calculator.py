import sys
import os
print("------------------------- Calculator -------------------------")

count = 0


while True:

    os.system("cls")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == '-':
        print("Result:", num1 - num2)

    elif op == '+':
        print("Result:", num1 + num2)

    elif op == '*':
        print("Result:", num1 * num2)

    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid operator! Program terminated.")
        
        ch = input("do you want to continue (y/n)")
        
        if ch !='n':
            continue
        
        

    count += 1
    print(f"You have finished {count} operation(s).")