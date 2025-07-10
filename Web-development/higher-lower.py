from flask import Flask
import random

app = Flask(__name__)

def h1_wrap(function):
    def wrapper():
        return f"<h1>{function()}</h1>"
    return wrapper

@app.route("/")
def guess():
    global random_number
    random_number = random.randint(0, 9)
    return "<h1>Guess a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:user_number>")
def answer(user_number):
    global random_number
    if user_number < random_number:
        return "<h1>Too low, try again!</h1>" \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif user_number > random_number:
        return "<h1>Too high, try again!</h1>" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1>You found me!</h1>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
