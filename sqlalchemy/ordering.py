import random
from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

names = ["Andrew Pip", "Iron Man", "John Doe", "Jane Doe"]
ages = [20, 21, 22, 23, 25, 27, 30, 35, 60]

for x in range(20):
    user = User(name=random.choice(names), age=random.choice(ages))
    session.add(user)

# query all users ordered by age (ascending)
users = session.query(User).order_by(User.age).all()

# query all users ordered by age (descending)
users = session.query(User).order_by(User.age.desc()).all()

# query all users ordered by age AND name (ascending)
# ordered First by age then Name
users = session.query(User).order_by(User.age, User.name).all()

for user in users:
    print(f"User age: {user.age}, name: {user.name}, id: {user.id}")
