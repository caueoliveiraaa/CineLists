from flask import Flask 
from views import views


# Create app 
app = Flask(__name__)
# Register the blueprint views
app.register_blueprint(views, url_prefix='/')


if __name__== '__main__':
    app.run()
