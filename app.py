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

@app.route('/<username>')
def userviews(username):
    return 'hello %s' % username

@app.route('/post/<int:post_id>')
def posts(post_id):
    return 'This is post %d' % post_id

if __name__ == 'main':
    app.run(debug=True)