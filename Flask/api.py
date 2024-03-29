from flask import Flask, jsonify, request, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def api_call():
    if request.method == 'POST':
        code = request.form['text_editor']
        d = {
            "code": f"{code}"
        }
        print(f'Code: {code}')
        d1 = json.dumps(d)
        data = json.loads(d1)
        api_end_point_get_id = f'https://codersapi.herokuapp.com/api/coderun/'
        response = requests.post(api_end_point_get_id, json=data)
        json_response = response.json()
        code_editor_id = json_response['id']
        api_end_point_get_output = f'https://codersapi.herokuapp.com/api/output/'
        di = {
            "id": f"{code_editor_id}"
        }
        print(f'ID: {code_editor_id}')
        di1 = json.dumps(di)
        data_id = json.loads(di1)
        response_output = requests.post(api_end_point_get_output, json=data_id)
        output = response_output.json()['output']
        print(output)
        error = response_output.json()['error']
        output = output.split('\n')
        print(output)
        return render_template('index.html', output=output, error=error)
    else:
        return render_template('index.html', output=[], error='')


if __name__ == '__main__':
    app.run(debug=True)
