from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)


response = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
data = response.json()
posts = []
for post in data:
    posts.append(Post(post['id'], post['title'], post['subtitle'], post['body']))


@app.route('/')
def home():
    return render_template("index.html", blogs=posts)


@app.route('/posts/<int:id>')
def get_posts(id):
    return render_template('post.html', blog_post=posts[id - 1])


if __name__ == "__main__":
    app.run(debug=True)
