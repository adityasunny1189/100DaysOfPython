from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    description = TextAreaField(label='Describe Yourself', validators=[DataRequired()])
    submit = SubmitField(label='Login')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'AdityaPathak1189'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        data = {
            "Email": login_form.email.data,
            "Password": login_form.password.data,
            "description": login_form.description.data
        }
        if data['Email'] == 'admin@gmail.com' and data['Password'] == '123456':
            return '<h1>Welcome Back Boss</h1>'
        elif data['Email'] == 'admin@gmail.com' and data['Password'] != '123456':
            return '<h1>Boss Please check your password</h1>'
        else:
            return f'<h1>Welcome {data["Email"]}</h1>'
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
