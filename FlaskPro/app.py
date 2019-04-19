from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'be653f60dd04eeef821c197690697c9f5587'

posts = [
    {
        'author': 'Chandra',
        'title': 'Blog post 1',
        'content': 'First Post content',
        'date_posted': 'April 10, 2019'
    },
    {
        'author': 'Suvro',
        'title': 'Blog post 2',
        'content': 'Second Post content',
        'date_posted': 'April 1, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title='Home')


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            redirect(url_for('home'))
        else:
            flash('Unsuccessful Login! Check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
