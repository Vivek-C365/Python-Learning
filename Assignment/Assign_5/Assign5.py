import random
class Account:
    def __init__(self, account_no, name, balance=0, min_balance=0, pin=None):
        self.account_no = account_no
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        self.pin = pin 
        self.transaction_count = 0
        self.logs = [] 

    def deposit(self, amount):
        self.balance += amount
        self.add_log(f"Deposited: +{amount}")

    def withdraw(self, amount, pin):
        if self.pin == pin and amount % 100 == 0 and amount <= 10000 and self.balance - amount >= self.min_balance:
            self.balance -= amount
            self.add_log(f"Withdrawn: -{amount}")
            self.transaction_count += 1
            if self.transaction_count > 5:
                self.balance -= 10
                self.add_log("Extra charge of 10Rs for exceeding transaction limit")
            return True
        else:
            return False

    def add_log(self, transaction):
        self.logs.append(transaction)

    def balance_enquiry(self):
        return self.balance

    def get_statement(self):
        return self.logs

    def get_account_info(self):
        return f"Account Number: {self.account_no}\nName: {self.name}\nBalance: {self.balance}\nMinimum Balance: {self.min_balance}"

    

def mini_statement(account):
    statements = account.get_statement()
    if statements:
        print("Mini Statement:")
        for statement in statements[-5:]:
            print(statement)
    else:
        print("No transactions yet.") 
        
class SavingsAccount(Account):
    def __init__(self, account_no, name, initial_balance=0, pin=None):
        super().__init__(account_no, name, initial_balance, min_balance=0, pin=pin)


class CurrentAccount(Account):
    def __init__(self, account_no, name, initial_balance=0, company_name="", pin=None):
        super().__init__(account_no, name, initial_balance, min_balance=-1000, pin=pin)
        self.company_name = company_name


def create_account(account_type, name, initial_balance=0, company_name="", pin=None):
    account_no = random.randint(10000000, 99999999)
    if account_type.lower() == "savings":
        return SavingsAccount(account_no, name, initial_balance, pin=pin)
    elif account_type.lower() == "current":
        return CurrentAccount(account_no, name, initial_balance, company_name, pin=pin)
    else:
        print("Invalid account type. Please enter either 'Savings' or 'Current'.")
        return None

def main():
    for i in range(3):
        try:
            initial_balance = float(input("Enter Initial Balance: "))
            if initial_balance > 0:
                break
            else:
                print("Initial Balance should be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        account_type = input("Enter account type (Savings/Current): ")
        name = input("Enter your name: ")
        pin = input("Set PIN: ")  
        if account_type.lower() == "current":
            company_name = input("Enter company name: ")
            account = create_account(account_type, name, initial_balance, company_name, pin=pin)
        else:
            account = create_account(account_type, name, initial_balance, pin=pin)
        if account is not None:
            break

    while True:
        entered_pin = input("Enter PIN: ")
        if account.pin == entered_pin:
            break
        else:
            print("Incorrect PIN. Please try again.")

    while True:
        print("\n1. Deposit")
        print("2. Get Account Info")
        print("3. Balance Enquiry")
        print("4. Get Statement")
        print("5. Withdraw")
        print("6. Mini Statement")
        print("7. Exit")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            print("Deposit successful!")
        elif choice == 2:
            print(account.get_account_info())
        elif choice == 3:
            print(f"Current Balance: {account.balance_enquiry()}")
        elif choice == 4:
            print(account.get_statement())
        elif choice == 5:
            amount = float(input("Enter withdrawal amount: "))
            pin = input("Enter PIN for withdrawal: ")
            success = account.withdraw(amount, pin)
            if not success:
                print("Withdrawal failed. Please check amount, account balance, or PIN.")
        elif choice == 6:
            mini_statement(account)
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()