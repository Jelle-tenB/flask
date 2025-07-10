from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/bye")
@make_italic
@make_underline
@make_bold
def bye():
    return "Bye!"

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
        "<p>This is a paragraph</p>" \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<name>")
def greet(name):
    return f"hello {name + '12'}"

@app.route("/username/<path:name>")
def groet(name):
    return f"hello {name}"

@app.route("/<name>/<int:number>")
def great(name, number):
    return f"hello {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
