from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/account')
def account():
    # return render_template('index.html')
    import requests
    response = requests.get('https://neonmonkey.in/Nion/')
    if response.status_code == 200:
        return f'<hhtml>ello mastaruuuuu! how are you? Response data:{response.json}</html>'
    else:
        return f'<html>ello mastaruuuuu! how are you? Response data:{response.status_code}</html>'

@app.route('/username')
def username():
    # return render_template('index.html')
    return 'ello mastaruuuuu! how are you?'

@app.route('/settings')
def settings():
    # return render_template('index.html')
    return 'ello mastaruuuuu! how are you?'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1269)
