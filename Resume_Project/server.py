from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


class ResumeForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    # will add later


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'Very_Hard_to_guess'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/resumeform', methods=['GET', 'POST'])
def fill_form():
    resume_form = ResumeForm()
    resume_form.validate_on_submit()
    data = {
        "name": resume_form.name.data
    }
    print(data)
    return render_template('resumeform.html', form=resume_form)


if __name__ == '__main__':
    app.run(debug=True)
