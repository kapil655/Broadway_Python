class Wallet:

    def __init__(self, wallet_name, wallet_id):
        self.wallet_name = wallet_name
        self.wallet_id = wallet_id
        self.__balance = 0
        self.__transaction_logs = []

    def add_transaction_log(self, message):
        self.__transaction_logs.append(message)

    def deposit(self, amount):
        self.__balance += amount
        self.add_transaction_log(f"Deposited Rs.{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.add_transaction_log(f"Withdrawn Rs.{amount}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

    def view_transaction_history(self):
        print("\nTransaction History")
        for log in self.__transaction_logs:
            print(log)


class PremiumWallet(Wallet):

    def __init__(self, wallet_name, wallet_id, cashback_rate):
        super().__init__(wallet_name, wallet_id)
        self.cashback_rate = cashback_rate

    def deposit(self, amount):

        super().deposit(amount)

        cashback = amount * self.cashback_rate / 100

        super().deposit(cashback)

        print(f"Cashback Received: Rs.{cashback}")


# Object Creation
while True:
    wallet = PremiumWallet("Kapil", "PW001", 5)
    

    wallet.deposit(int(input("enter the amount : ")))
    wallet.withdraw(int(input("enter the amount to be withdrawn")))

    print("Current Balance:", wallet.get_balance())

    wallet.view_transaction_history()