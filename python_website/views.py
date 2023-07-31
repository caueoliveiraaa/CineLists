from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for


# Create a bluprint 
views = Blueprint(__name__, 'views')

# Create route
@views.route('/')
def home():
    # Send variables to template and render it 
    return render_template('index.html', name='Robot')


# Return json data
@views.route('/json')
def get_json():
    return jsonify({'name': 'bot', 'version': 1.5})


# Get username with ?name=user_name_here
@views.route('/profile/')
def profile():
    args = request.args
    name = args.get('name')
    return render_template('index.html', name=name)


# Return to home route
@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))