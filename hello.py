from flask import Flask, render_template, request, url_for
from markupsafe import escape
from markupsafe import Markup

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

# 1. HTML Escaping
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

# 2. Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# 3. URL Building
@app.route('/register')
def register():
    print(url_for('index'))
    print(url_for('register'))
    print(url_for('register', next='/'))
    print(url_for('show_user_profile', username='John Doe'))
    return 'register'

# 4. HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login'
    else:
        return 'show_the_login_form'

@app.post('/login2')
def login_post():
    return 'do_the_login2'

@app.get('/login2')
def login_get():
    return 'show_the_login_form2'

# 5. Static Files
@app.get('/static/<filename>')
def get_static(filename):
    return f'src/static/{filename}'

@app.get('/static-file')
def get_static_file():
    url = url_for('static', filename='style.css')
    return url

# 6. Rendering Templates
@app.route('/template/')
@app.route('/template/<name>')
def show_template(name=None):
    # hello.html in /templates
    return render_template('hello.html', name=name)

@app.get('/markup')
def show_markup():
    return Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink> - ' + Markup.escape('<blink>hacker</blink> - ') + Markup('<em>Marked up</em> &raquo; HTML').striptags()

# 7. Accessing Request Data
# 7.1 Request object
@app.route('/form-login', methods=['POST', 'GET'])
def form_login():
    error = None
    paramsQuery = request.args
    searchKey = request.args.get('q', '')
    if request.method == 'POST':
        print(request.form['username'], request.form['password'])
        return {
            "params": request.form,
            "paramsQuery": paramsQuery,
            "searchKey": searchKey,
        }
    return render_template('login.html', error=error)
