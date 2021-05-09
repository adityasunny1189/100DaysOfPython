from flask import Flask, request, render_template

app = Flask(__name__)


database = {}


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        try:
            if database[user_email] == user_password:
                return f'Welcome {user_email}'
            else:
                return f'Your entered password is incorrect'
        except KeyError:
            return 'Account does not exist'
    else:
        return render_template('login.html', title='Login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        try:
            if database[user_email]:
                return f'Account already exist, try another'
        except KeyError:
            database[user_email] = user_password
            return f'Account created'
    else:
        return render_template('signup.html', title='Sign-Up')


if __name__ == '__main__':
    app.run(debug=True)
