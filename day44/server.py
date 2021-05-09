from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'very-hard-to-guess'

# Open the csv file and read the data
with open() as file:
    pass


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        data = {
            # Data from the form
        }
        # Add the data to the csv file
        return render_template('cafe_list.html')
    else:
        return render_template('add_cafe.html', form=cafe_form)


if __name__ == '__main__':
    app.run(debug=True)
