class BankAccount:
    
    def __init__(self, owner, balance=0):
        
        self._owner = owner
        self.__balance = balance
    
    def get_owner(self):
        return self._owner
    
    def get_balance(self):
        return self.__balance
    
    def set_owner(self, name):
        if len(name.strip()) == 0:
            print("Name cannot be empty")
        else:
            self._owner = name
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.__balance += amount
            print(f"Deposited: {amount} | Balance: {self.__balance}")
    
    def withdraw(self, amount):
            if amount <= 0:
                print("Withdrawal amount must be positive")
                return
            if amount > self.__balance:
                print("Insufficient balance")
                return
            self.__balance -= amount
            print(f"Withdrawn: {amount} | Balance: {self.__balance}")
    
    def display(self):
        print(f"Owner Name: {self._owner}")
        print(f"Current Balance: {self.__balance}")
    
    # For humans — print()
    def __str__(self):
        return f"Account[{self._owner}] | Balance: ${self.__balance}"

    # For developers
    def __repr__(self):
        return f"BankAccount(owner='{self._owner}', balance={self.__balance})"


def main():
    account = BankAccount("Noman Rizvi")
    print("Welcome to Bank Account")

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Account Details\n4. Exit")
        choice = int(input("Choice: "))

        if choice == 1:
            amount = float(input("Amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Amount: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display()
        elif choice == 4:
            print("Thank You")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()

