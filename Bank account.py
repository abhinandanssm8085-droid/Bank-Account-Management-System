class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def debit(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Rs.", amount, "debited")

    def credit(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        else:
            self.balance += amount
            print("Rs.", amount, "credited")

    def get_balance(self):
        return self.balance


user1 = Account(12345, 1000)

while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        user1.credit(amount)
        print("Balance:", user1.get_balance())

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        user1.debit(amount)
        print("Balance:", user1.get_balance())

    elif choice == "3":
        print("Current balance:", user1.get_balance())

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice. Try again.")