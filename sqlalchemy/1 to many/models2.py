from sqlalchemy import (create_engine, Column, Integer, String, MetaData, Table, ForeignKey)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column

db_url = "sqlite:///sqlite/1 to many/database2.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class BaseModel(Base):
    # allows other classes to inheret from this
    __abstract__ = True
    # allow the unmapped method
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)


class FollowingAssociation(BaseModel):
    __tablename__ = "following_association"
    
    user_id = Column(Integer, ForeignKey('users.id'))
    following_id = Column(Integer, ForeignKey('users.id'))


class User(BaseModel):
    __tablename__ = "users"
    
    username = Column(String)
    
    #following_id = Column(Integer, ForeignKey('users.id'))
    # relationships in the same table within the same class need "remote_side=[]" with the name of the foreignkey
    # uselist=True makes it a list so you can get multiple items back
    #following = relationship('User', remote_side=[id], uselist=True)
    following = relationship('User', secondary="following_association",
                            primaryjoin=("FollowingAssociation.user_id==User.id"),
                            secondaryjoin=("FollowingAssociation.following_id==User.id")
                            )
    # secondary allows for a second relationship
    # primaryjoin links the current user to the table
    # secondaryjoin links the table to the Other user
    
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}, following={self.following}')>"

Base.metadata.create_all(engine)
