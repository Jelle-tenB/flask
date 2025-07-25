from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# CREATING A DATABASE 
app = Flask(__name__)
 
class Base(DeclarativeBase):
    pass
 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# ---------------------------------------------------------------------------- #
# CREATE A NEW TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
 
with app.app_context():
    db.create_all()

# ---------------------------------------------------------------------------- #
# CREATE A NEW RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# ---------------------------------------------------------------------------- #
# READ ALL RECORDS
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    booklist = [book.title for book in all_books]
    print(booklist)
# scalarS for multiple, scalar for single

# ---------------------------------------------------------------------------- #
# READ A PARTICULAR RECORD BY QUERY
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

# ---------------------------------------------------------------------------- #
# UPDATE A PARTICULAR RECORD BY QUERY
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# ---------------------------------------------------------------------------- #
# UPDATE A RECORD BY PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
# extra query methods:
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/#queries-for-views

# ---------------------------------------------------------------------------- #
# DELETE A PARTICULAR RECORD BY PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
