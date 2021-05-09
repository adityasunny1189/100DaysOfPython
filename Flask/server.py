from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'<h1>Your browser is {user_agent}</h1>'


@app.route('/galary')
def get_images():
    return render_template('images.html')


if __name__ == '__main__':
    app.run(debug=True)
