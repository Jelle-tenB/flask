from models import User, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

# group users by age
users = session.query(User.name, func.count(User.id)).group_by(User.name).all()
# print(users)

users_tuple = (
    session.query(User.age, func.count(User.id))
    .filter(User.age > 24)
    .order_by(User.age)
    .filter(User.age < 50)
    .group_by(User.age)
    .all()
)

# for age, count in users_tuple:
#     print(f"Age: {age} - {count} users")

only_iron_man = False
group_by_age = True

users = session.query(User)

if only_iron_man:
    users = users.filter(User.name == "Iron Man")

if group_by_age:
    users = users.group_by(User.age)

users = users.all()

for user in users:
    print(f"User age: {user.age}, name: {user.name}")
