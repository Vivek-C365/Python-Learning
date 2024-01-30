import random
class Account:
    def __init__(self, account_number, name, account_type):
        self.account = account_number
        self.name = name
        self._balance = 0 
        self.transaction_count = 0 
        self.account_type = account_type
        self.logs = []

    def get_balance(self):
        return self._balance

    def deposit(self, transaction):
        self._balance += transaction
        log_entry = dict(Deposited=f"+{transaction}")
        self.logs.append(log_entry)

    def withdraw(self, transaction):
        self.transaction_count += 1
        if self.transaction_count<=2:
            self._balance -= transaction
            log_entry = dict(Withdrawn=f"-{transaction}")
            print(self.transaction_count)
            self.logs.append(log_entry)
        else:
            self._balance -= transaction
            self._balance -= 10
            log_entry = dict(Withdrawn=f"-{transaction}" ,Extra_Charges = f"-10" )
            self.logs.append(log_entry)
            print("extra charges of 10Rs appliled for exeeding transaction limit")
         
    def account_info(self):
        print(f"\nAccount Number: {self.account}\nAccount Type: {self.account_type}\nName: {self.name}\nBalance: {self._balance}\n")

    def get_statement(self):
        print("\nTransactions:")
        for log_entry in self.logs:
            print(log_entry)

def create_account(name, account_type):
    account_number = random.randint(100000000, 999999999)
    if account_type == 'Savings':
        return Saving_account(account_number, name)
    elif account_type == 'Current':
        return Current_account(account_number, name)
    else:
        print("Error! Wrong account type.")

class Saving_account(Account):
    def __init__(self, account_number, name):
        super().__init__(account_number, name, account_type='Savings')  

class Current_account(Account):
    def __init__(self, account_number, name):
        super().__init__(account_number, name, account_type='Current')  

def main():
    while True:
        print("Type 1 for Savings account")
        print("Type 2 for Current Account")
        acc_choice = int(input("Enter your choice: "))
        if acc_choice == 1:
            name = input("Enter your name: ")
            account_detail = create_account(name, 'Savings')
        elif acc_choice == 2:
            name = input("Enter your Company name: ")
            account_detail = create_account(name, 'Current')
        else:
            print('Invalid choice. Please enter a number')
            break
        count = 0
        while True and count < 3:
            print("1. Deposit in Account")
            print("2. Withdraw from Account")
            print("3. Get Account Info")
            print("4. Get Statement")
            print("5. Balance Enquiry")
            print("0. for Exit")
            choice = int(input("Enter your Choice"))
            if choice == 1:
                amount = float(input("Enter the Amount to be deposited: "))
                account_detail.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter the Amount to be withdrawn: "))
                account_detail.withdraw(amount)
            elif choice == 3:
                account_detail.account_info()
            elif choice == 4:
                account_detail.get_statement()
            elif choice == 5:
                print("Current Balance : ", account_detail.get_balance())
            elif choice == 0:
                exit()
            else:
                if count < 3:
                    print("Invalid choice. Please try again.")
                    count += 1
                elif count == 3:
                    print("You entered the wrong input 3 times")
                    exit()
                    
if __name__ == "__main__":
    main()