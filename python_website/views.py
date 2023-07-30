from flask import Blueprint, render_template, request


# Create a bluprint 
views = Blueprint(__name__, 'views')

# Create route
@views.route('/')
def home():
    # Send variables to template and render it 
    return render_template('index.html', name='Robot')


# Create another route for user names getting the user name after /
# @views.route('/profile/<username>')
# def profile(username):
#     args = request.args
#     name = args.get('name')
#     return render_template('index.html', name=username)


# Get username with ?name=user_name_here
@views.route('/profile/')
def profile():
    args = request.args
    name = args.get('name')
    return render_template('index.html', name=name)