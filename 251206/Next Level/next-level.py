user2_id, level2 = input().split()
level2 = int(level2)

class User:
    def __init__(self, user_id = "codetree", level = 10):
        self.user_id = user_id
        self.level = level
    
user1 = User()
print(f"user {user1.user_id} lv {user1.level}")

user2 = User(user2_id, level2)
print(f"user {user2.user_id} lv {user2.level}")