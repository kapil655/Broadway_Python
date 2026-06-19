class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount
        print(f"Withdrawn Rs {amount}")

    def show_balance(self):
        print(f"Current balance: Rs {self.balance}")


# Creating object
account1 = BankAccount("Kapil", 15000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        account1.deposit(amount)

    elif choice == "2":
       withdraw_amount = int(input("Enter withdraw amount: "))
       account1.withdraw(withdraw_amount)
       if withdraw_amount > account1.balance:
           break
       else:
           pass


    elif choice == "3":
        account1.show_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")