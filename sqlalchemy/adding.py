from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

user = User(name="John", age=30)
user2 = User(name="Bob", age=44)
user3 = User(name="Henk", age=16)

session.add(user)
session.add_all([user2, user3])

session.commit()
