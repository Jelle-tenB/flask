from models2 import session, User

# Creating users
user1 = User(username="Zeq tech 1")
user2 = User(username="Zeq tech 2")
user3 = User(username="Zeq tech 3")

# Creating relationships
# because user1 and user3 are following each other, and because it shows who the other user follows that you follow, you get a Circular dependency error
# this is fixed by an association table
user1.following.append(user2)
user2.following.append(user3)
user3.following.append(user1)

# Adding users to the session and committing
session.add_all([user1, user2, user3])
session.commit()

print(f"{user1.following = }")
print(f"{user2.following = }")
print(f"{user3.following = }")
