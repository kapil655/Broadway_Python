import random
import os

print("-------------------welcome to ATM------------------")

bank_bal = 0

while True:

    print("enter your pin ")
    pin = int(input("enter: "))

    if pin == 1234:

        opt = int(input("1.cash deposit: \n2.cash withdraw: \n3.check balance: \n4.exit: "))

        if opt == 1:
            cash_depo = int(input("enter the amount you want to deposit: "))
            bank_bal += cash_depo
            print(f"you have deposited {cash_depo} and your current balance is {bank_bal}")

        elif opt == 2:
            cash_drawn = int(input("enter the amount you want to withdraw: "))

            if bank_bal >= cash_drawn:
                bank_bal -= cash_drawn
                print(f"Withdrawal successful. Current balance is {bank_bal}")
            else:
                print("insufficient balance")

        elif opt == 3:
            print(f"Current balance: {bank_bal}")

        elif opt == 4:
            break

        else:
            print("invalid option")

    else:
        print("Wrong PIN")