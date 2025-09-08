class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following = self.following + 1
        user.followers += 1

    def unfollow(self, user):
        self.followers = self.followers - 1
        user.followers -= 1



user_1 = User("001", "zeinab")
user_2 = User("002", "sata")
user_3 = User("003", "sara")

user_1.follow(user_2)
user_2.follow(user_3)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
print(user_3.followers)
print(user_3.following)