from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def home():
    return "Hello, GitHub Pages with Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1269)
