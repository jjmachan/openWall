from flask import Flask
from flask import render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('/hello.html', name=name)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('index.html')
    else: 
        return redirect(url_for('home'))

@app.route('/search')
def search():
    return 'you can search for people here'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method=='POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/u/<username>/<int:post_id>')
def posts(username, post_id):
    return 'This is post %d' % post_id

@app.route('/u/<username>')
def profile(username):
    return 'This is %s ' %username

if __name__ == 'main':
    app.run(debug=True)