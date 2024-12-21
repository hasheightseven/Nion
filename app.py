from flask import Flask, render_template

@app.route('/')
def home():
    return "Hello, GitHub Pages with Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1269)
