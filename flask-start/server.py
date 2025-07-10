from flask import Flask, render_template
import random
from datetime import datetime
import requests

AGIFY = "https://api.agify.io?name="
GENDERIZE = "https://api.genderize.io?name="

app = Flask(__name__)
current_year = datetime.now().year

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, current_year=current_year)


@app.route('/guess/<string:name>')
def name_check(name):
    #age
    age_response = requests.get(url=AGIFY+name)
    age_data = age_response.json()
    age = age_data['age']
    #gender
    gender_response = requests.get(url=GENDERIZE+name)
    gender_data = gender_response.json()
    gender = gender_data['gender']
    return render_template("guess.html", age=age, gender=gender, name=name)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
