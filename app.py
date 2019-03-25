from flask import Flask, url_for
from flask import render_template
import fibo

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    pass

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    pass

with app.test_request_context():
    s = url_for('index')
    print(s)
    s2 = url_for('hello') 
    print(s2)



if __name__ == "__main__":
    app.run(host="0.0.0.0")

