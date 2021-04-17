class User:
    def __init__(self, name, email, no_of_accounts = 1):
        self.name = name
        self.email = email
        self.accounts = []
        for i in range(no_of_accounts):
            self.accounts.append(BankAccount(int_rate=0.02, balance=0))
        
    def make_deposit(self, amount):
        accountNo = self.choose_account()
        self.accounts[accountNo - 1].deposit(amount)
        return self

    def make_withdrawal(self, amount):
        accountNo = self.choose_account()
        self.accounts[accountNo - 1].withdraw(amount)
        return self
    
    def display_user_balance(self):
        accountNo = self.choose_account()
        print(f"User: {self.name} , Balance of Account number {accountNo}: {self.accounts[accountNo - 1].balance}")
        return self

    def transfer_money(self, other_user, amount):
        print("first user account to transfer money from: ")
        accountNo1 = self.choose_account()
        self.accounts[accountNo1 - 1].balance -= amount

        print("second user account to transfer money to: ")
        accountNo2 = other_user.choose_account()
        other_user.accounts[accountNo2 - 1].balance += amount
        return self

    def choose_account(self):
        print(f"{self.name} you have {len(self.accounts)} accounts, please choose the number of account you want to make a change to: ")
        for i in range(len(self.accounts)):
            print(f"{i + 1}. AccountNo {i + 1}")
        accountNo = input()
        return int(accountNo)

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance > amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.int_rate * self.balance
        return self

guido = User("Guido van Rossum", 'guido@python.com',2)
waleed = User("Waleed Almotairi", "AlmotairiWal@gmail.com", 3)

guido.make_deposit(500).display_user_balance()
guido.make_withdrawal(100).display_user_balance()

waleed.make_deposit(300).display_user_balance()
guido.transfer_money(waleed,200)
guido.display_user_balance()
waleed.display_user_balance()

