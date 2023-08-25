from flask import request
from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import url_for


# Create flask app
app = Flask(__name__)


# Working with urls
# ("Uniform Resource Locator.")
@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/login_page', methods=['GET'])
def login_page():
    return render_template('login.html')


@app.route('/do_login', methods=['POST'])
def do_login():
    if request.method == 'POST':

        # AUTHENTICATION

        return render_template('index.html')


"""Converter types:
string: (default) accepts any text without a slash
int: accepts positive integers
float: accepts positive floating point values
path: like string but also accepts slashes
uuid: accepts UUID strings"""


if __name__ == '__main__':
    app.run(debug=True, port=8002)
    # run app on terminal: flask --app app run