from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('/hello.html', name=name)

@app.route('/')
def index():
    return 'Index'
@app.route('/search')
def search():
    return 'you can search for people here'
@app.route('/home/<username>')
def userviews(username):
    return 'hello %s' % username

@app.route('/<username>/<int:post_id>')
def posts(username, post_id):
    return 'This is post %d' % post_id

@app.route('/<username>')
def profile(username):
    return 'This is %s ' %username

if __name__ == 'main':
    app.run(debug=True)