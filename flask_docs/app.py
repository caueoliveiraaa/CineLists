from flask import Flask
from markupsafe import escape

# Create flask app
app = Flask(__name__)

# Working with urls ("Uniform Resource Locator.")
@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/<name>')
def greet(name):
    return f'Wellcome {escape(name)}'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


"""Converter types:
string: (default) accepts any text without a slash
int: accepts positive integers
float: accepts positive floating point values
path: like string but also accepts slashes
uuid: accepts UUID strings"""


if __name__ == '__main__':
    app.run(debug=True, port=8002)
    # run app on terminal: flask --app app run