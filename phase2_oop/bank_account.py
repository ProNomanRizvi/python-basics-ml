class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount} | New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount} | New Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"Owner: {self.owner} | Balance: {self.balance}")


# Menu lives OUTSIDE the class — it is not the account's responsibility
def main():
    account = BankAccount("Noman", 1000)
    print("=== Bank Account System ===")

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Display\n5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            amount = float(input("Amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Amount: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Balance: {account.get_balance()}")
        elif choice == "4":
            account.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()