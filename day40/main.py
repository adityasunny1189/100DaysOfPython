from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 align="center">Hello World</h1>'


def make_bold(function):
    def wrapper_function():
        return f"<strong>{function()}</strong>"
    return wrapper_function


def make_italic(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


def make_heading(function):
    def wrapper_function():
        return f"<h1>{function()}</h1>"
    return wrapper_function


@app.route('/bye')
@make_bold
@make_italic
@make_heading
@make_underline
def bye():
    return 'Bye'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name + '21'} how are you, your age is {number} old"


if __name__ == "__main__":
    app.run(debug=True)
