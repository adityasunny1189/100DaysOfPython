from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Guess a Number</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'


@app.route('/<int:num>')
def guess_num(num):
    if num > 8:
        return '<h2>Number too high</h2>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img>'
    elif num < 8:
        return '<h2>Number too low</h2>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>'
    return '<h2>Number guessed right</h2>' \
           '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img>'


if __name__ == "__main__":
    app.run(debug=True)




