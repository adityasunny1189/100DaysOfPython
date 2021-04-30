from flask import Flask, render_template
import requests

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     random_number = random.randint(1, 10)
#     return render_template('index.html', num=random_number, cur_year=2021)


@app.route('/guess/<username>')
def guess_sex_age(username):
    # Get Age
    response = requests.get(url=f'https://api.agify.io?name={username}')
    age = response.json()['age']
    # Get Gender
    response = requests.get(f'https://api.genderize.io?name={username}')
    gender = response.json()['gender']
    return render_template('index.html', username=username, user_age=age, user_gender=gender)


if __name__ == '__main__':
    app.run(debug=True)
