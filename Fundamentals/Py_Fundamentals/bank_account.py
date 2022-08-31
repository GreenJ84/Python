class Bank_Account():
    all_accounts=[]

    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
        Bank_Account.all_accounts.append(self)
        print(Bank_Account.all_accounts)


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if amount > self.balance:
            print("You do not have enough funds.")
        else:
            self.balance -= amount
            return self
    
    def display_account(self):
        print(self.balance)
        print(self.interest)
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.interest)
        return self

    @classmethod
    def display_accounts(cls):
        for instances in Bank_Account.all_accounts:
            print(instances.balance)
            print(instances.interest)


Account1 = Bank_Account(50000, .05)
print(Account1.display_account())
Account2 = Bank_Account(500000, .08)

# Account1.deposit(10000).deposit(20000).deposit(5000).withdrawl(22000).yield_interest().display_account()

# Account2.deposit(25000).deposit(20000).withdrawl(100000).withdrawl(100000).withdrawl(200000).withdrawl(120000).yield_interest().display_account()

# Bank_Account.display_accounts()