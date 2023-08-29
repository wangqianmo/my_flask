from app import *
from flask import render_template


@app.route('/')
def index():
    # return Markup('<div>Hello %s</div>') % '<em>Flask</em>'
    # return '<div>Hello %s</div>'  % '<em>Flask</em>'
    # return escape('<div>Hello %s</div>') % '<em>Flask</em>'
    return render_template("index.html")
#等价下面代码
# hello_world=app.route('/')(hello_world)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_name(name=None):
    return render_template("hello.html", name=name)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post : {post_id}'

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        print(request.form)
        if request.form["user_name"]=="admin":
            return "Admin Login Successfully!!"
        else:
            return "Invalid username/password!!"
    title = request.args.get("title","World")
    return render_template("login.html", title=title)

@app.route("/login_new",methods=["POST","GET"])
def login_new():
    form = LoginForm()
    # if request.method=="POST":
    #     print(request.form)
    #     if request.form["user_name"]=="admin":
    #         return "Admin Login Successfully!!"
    #     else:
    #         return "Invalid username/password!!"
    title = request.args.get("title","Hello,World")
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for("hello_name"))
    return render_template("login.html", title=title, form=form)

@app.route("/user")
def user_says():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('user.html', title='Home', user=user, posts=posts)

# with app.test_request_context():
#     print(url_for('hello_world',name="jone"))


