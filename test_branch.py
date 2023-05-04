import random, string
print("hi")
# user_id = []
# for i in range(1, 11):
#     user_id.append(random.choice(string.digits))
# user_id = ''.join(user_id)

user_id = [str(random.randint(0, 9)) for x in range(10)]
print(user_id)
