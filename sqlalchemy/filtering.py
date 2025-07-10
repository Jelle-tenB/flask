import random
from models import User, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_, not_

Session = sessionmaker(bind=engine)
session = Session()

# query all users
users_all = session.query(User).all()

# query all users with age greater than or equal to 25
users_filtered = session.query(User).filter(User.age >= 25).all()

# query all users with age greater than or equal to 25 and named Iron Man
users_filtered = session.query(User).filter(User.age >= 25, User.name == "Iron Man").all()

# query all users with age is equal to 30
# Does NOT work with >= or other conditionals
users = session.query(User).filter_by(age=30).all()

# for user in users:
#     print(f"User age: {user.age}")

other_users = session.query(User).where(User.age >= 30).order_by(User.age).all()

# for user in other_users:
#     print(f"User age: {user.age}")

# OR Filter from sqlalchemy
# query all users with age over 30 OR name is equal to Iron Man
or_users = session.query(User).where(or_(User.age >= 30, User.name == "Iron Man")).all()

#Or Filter within Python with |
or_users = session.query(User).where((User.age >= 30) | (User.name == "Iron Man")).all()

# for user in or_users:
#     print(f"{user.age} - {user.name}")

# query all users and find all NOT named Iron Man. Can be combined with and_ and or_
not_users = session.query(User).where(not_(User.name == "Iron Man")).all()

for user in not_users:
    print(f"{user.age} - {user.name}")
