
import mod1

users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

print("Adults:", mod1.age18(users))
print("Active Users:", mod1.actT(users))
print("Adult Active Users:", mod1.age_act(users))



# print(f"Adults: {[user for user in users if filter.is_adult(user)]}")
# print(f"Active Users: {[user for user in users if filter.is_active_user(user)]}")
# print(f"Adult Active Users: {[user for user in users if filter.is_adult_active_user(user)]}")