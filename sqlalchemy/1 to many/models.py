from sqlalchemy import (create_engine, Column, Integer, String, MetaData, Table, ForeignKey)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column

db_url = "sqlite:///sqlalchemy/1 to many/database.db"

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

class Address(BaseModel):
    __tablename__ = "adresses"
    
    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    # foreignkey sets the relationship
    # Mapped adds type hints to make relationships better possible
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # Now you can acces a user through adress
    # back_populates links the two items together
    user: Mapped["User"] = relationship(back_populates="addresses")
    
    def __repr__(self):
        return f"<Address(id={self.id}, city='{self.city}')>"

class User(BaseModel):
    __tablename__ = "users"
    
    name = Column(String)
    age = Column(Integer)
    # users can have multiple adresses and this make a list of adresses per user
    addresses: Mapped[list["Address"]] = relationship()
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.name}')>"

Base.metadata.create_all(engine)
