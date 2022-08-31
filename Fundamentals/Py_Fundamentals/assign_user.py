from re import M


class User():

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
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
User_3 = User("Lydiaa", "Leigh", "none", 3)

User_1.enroll().spend_points(50)

User_2.enroll().spend_points(80)

# print(User_1.display_info())
# print(User_1.gold_card_points)

# print(User_2.display_info())
# print(User_2.gold_card_points)

# print(User_3.display_info())
# print(User_3.gold_card_points)

User_1.enroll()
User_3.spend_points(40)


