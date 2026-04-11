from flask import Flask

#  create a Flask application instance
app = Flask(__name__)

# define a route for the root URL
@app.route('/')
def home():
    return 'Hello, World1111!'

@app.route('/ping')
def ping():
    return {'message': 'run this '}