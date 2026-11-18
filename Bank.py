class BankAccount:
    def __init__(self, name, account_no, pin, balance=0):
        self.name = name
        self.account_no = account_no
        self.pin = pin
        self.balance = balance
        self.history = []

    def validate_pin(self, entered_pin):
        return entered_pin == self.pin

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0")
            return
        self.balance += amount
        self.history.append(f"Deposited: {amount} | Balance: {self.balance}")
        print(f"{amount} deposited successfully!")
        print(f"Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            print(f"Your balance is only {self.balance}")
            return
        self.balance -= amount
        self.history.append(f"Withdrawn: {amount} | Balance: {self.balance}")
        print(f"{amount} withdrawn successfully!")
        print(f"Current Balance: {self.balance}")

    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Account No: {self.account_no}")
        print(f"Current Balance: {self.balance}")

    def show_history(self):
        print("TRANSACTION HISTORY")
        if not self.history:
            print("No transactions yet.")
        else:
            for i, txn in enumerate(self.history, 1):
                print(f"{i}. {txn}")

def main():
    print("Welcome to Bank")
    name = input("Enter your name: ")
    acc_no = input("Enter account number: ")

    while True:
        pin = input("Create a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            break
        print("PIN must be 4 digits!")

    account = BankAccount(name, acc_no, pin, balance=1000)
    print("Account created! Starting balance 1000")

    attempts = 3
    while attempts > 0:
        entered = input("Enter your PIN to login: ")
        if account.validate_pin(entered):
            print(f"Welcome back, {name}!")
            break
        else:
            attempts -= 1
            print(f"Wrong PIN! {attempts} attempts left.")
            if attempts == 0:
                print("Account locked. Try again later.")
                return

    while True:
        print("MENU")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.show_history()

        elif choice == "5":
            print("Thank you for using Bank! Bye")
            break
        else:
            print("Invalid choice! Please choose 1-5.")

if __name__ == "__main__":
    main()