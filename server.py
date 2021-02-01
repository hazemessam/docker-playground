from os import environ
from flask import Flask


app = Flask(__name__)
USER = environ.get('USER', None)

@app.route('/')
def index():
    print('Server is running...')
    return f'<h1>Server is running...</h1><h2>Welcome {USER}!</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)