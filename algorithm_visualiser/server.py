from flask import Flask, render_template, request

app = Flask(__name__)

arr = [2, 3]


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        value = int(request.form['value'])
        position = int(request.form['position'])
        arr.insert(position, value)
        return render_template('index.html', arr=arr)
    else:
        return render_template('index.html', arr=arr)


if __name__ == '__main__':
    app.run(debug=True)
