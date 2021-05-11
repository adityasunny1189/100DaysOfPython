from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap
import csv


class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name', validators=[DataRequired()])
    cafe_location = StringField(label='Cafe Location', validators=[DataRequired()])
    opening_time = TimeField(label='Opening Time', validators=[DataRequired()])
    closing_time = TimeField(label='Closing Time', validators=[DataRequired()])
    coffee_rating = StringField(label='Coffee Rating', validators=[DataRequired()])
    wifi_strength = StringField(label='Wifi Strength', validators=[DataRequired()])
    no_of_sockets = StringField(label='No of sockets', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'very-hard-to-guess'


def get_cafe_list():
    with open('cafes.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = []                         # Data = {1:{}, 2:{}, 3:{}, ...}
        for row in reader:
            info = {
                'cafe_name': row['cafe_name'],
                'cafe_location': row['cafe_location'],
                'opening_time': row['opening_time'],
                'closing_time': row['closing_time'],
                'coffee_rating': row['coffee_rating'],
                'wifi_strength': row['wifi_strength'],
                'no_of_sockets': row['no_of_sockets']
            }
            data.append(info)
        return data


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        data = {
            'cafe_name': cafe_form.cafe_name.data,
            'cafe_location': cafe_form.cafe_location.data,
            'opening_time': cafe_form.opening_time.data,
            'closing_time': cafe_form.closing_time.data,
            'coffee_rating': cafe_form.coffee_rating.data,
            'wifi_strength': cafe_form.wifi_strength.data,
            'no_of_sockets': cafe_form.no_of_sockets.data
        }
        with open('cafes.csv', 'a') as file:
            field_names = ['cafe_name', 'cafe_location', 'opening_time', 'closing_time',
                           'coffee_rating', 'wifi_strength', 'no_of_sockets']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writerow(data)
        cafe_list = get_cafe_list()
        return render_template('cafe_list.html', cafe_list=cafe_list)
    else:
        return render_template('add_cafe.html', form=cafe_form)


@app.route('/cafes')
def show_cafes():
    cafe_list = get_cafe_list()
    return render_template('cafe_list.html', cafe_list=cafe_list)


if __name__ == '__main__':
    app.run(debug=True)
