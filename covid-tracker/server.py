from flask import Flask, render_template, request
import requests


app = Flask(__name__)


response = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
data = response.json()['data']
regional_data_list = data['regional']


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        state = request.form['text']
        for i in regional_data_list:
            if i['loc'] == state:
                return render_template('statedata.html', data=i)
        return render_template('state.html')
    else:
        return render_template('index.html', state_input=state_input)


@app.route('/<state>')
def covid_case(state):
    for i in regional_data_list:
        if i['loc'] == state:
            return render_template('statedata.html', data=i)
    return render_template('state.html')


@app.route('/allstates')
def display_report():
    return render_template('allstates.html', regional_data_list=regional_data_list)


if __name__ == '__main__':
    app.run(debug=True)
