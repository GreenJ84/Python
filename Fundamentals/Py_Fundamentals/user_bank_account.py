class Bank_Account():
    all_accounts=[]

    def __init__(self, name, balance, interest):
        self.name = name
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
    
    def display_account_info(self):
            print(self.balance)
            print(self.interest)
            return self

    def yield_interest(self):
        self.balance += (self.balance * self.interest)
        return self


class User():

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.accounts = {}
        self.rewards_member = False
        self.gold_card_points = 0
        print(self)

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        for key in self.accounts:
            print(self.accounts[key].display_account_info())
        return self

    def create_account(self, account_name, intitial):
        self.accounts[account_name] = Bank_Account(account_name, intitial, 0.02)
        print(self.accounts[account_name].display_account_info())

    def addto_account(self, account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self

    def takefrom_acount(self, account_name, amount):
        self.accounts[account_name].withdrawl(amount)
        return self

    def transfer_accounts(self, from_account, to_account, amount):
        if amount > self.account[from_account].balance:
            print('You cannot afford this transfer!')
        else:
            self.accounts[from_account].balance -= amount
            self.accounts[to_account].balance += amount

    def transfer_touser(self,from_account, amount, other_user, account_name):
        if amount > self.accounts[from_account].balance:
            print('You cannot afford this transfer!')
        else:
            self.accounts[from_account].balance -= amount
            other_user.accounts[account_name].balance += amount
        print(self.accounts[from_account].balance)
        print(other_user.accounts[account_name].balance)

    def display_account(self, account_name):
        self.accounts[account_name].display_account_info()
        return self

    def enroll(self):
        if self.rewards_member == True:
            print('You are already enrolled!')
        else:
            self.rewards_member = True
            self.gold_card_points = 200
            return self

    def spend_points(self, amount):
        if (amount > self.gold_card_points):
            print('Not enough points for purchase')
        else:
            self.gold_card_points -= amount
        return self

User_1 = User("Jesse", "Greenough", "@gmail.com", 24)
User_2 = User("Danika", "Kraft", "@yahoo.com", 32)


User_1.create_account('checkings', 1000)
User_1.create_account('savings', 0)

User_2.create_account('checkings', 1000)
User_2.create_account('savings', 1000)

User_1.display_info()
User_2.display_info()

User_1.transfer_touser('checkings', 500, User_2, 'checkings')

