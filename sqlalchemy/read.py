from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

#look up all Users
users = session.query(User).all()

print(f"this all users: {users}")

user = users[0]
print(f"this is one user: {user}")
print(user.name)
print(user.id)
print(user.age)

# Loop through all users
for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")

# Search through all users and select ALL with id of 1 and returns a list
all_user_id1 = session.query(User).filter_by(id=1).all()

# Search through all user and select 1 or none, this can only work if there is only 1 of its kind.
one_user_id1 = session.query(User).filter_by(id=1).one_or_none()

# Search through all user and select the first one.
first_user_id1 = session.query(User).filter_by(id=1).first()

# Changing values need a commit to change in the db
one_user_id1.name = "different"
session.commit()

# DELETING
# session.delete(one_user_id1)
