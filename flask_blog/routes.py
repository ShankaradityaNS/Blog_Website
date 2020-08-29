from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LogInForm
from flask_blog.models import User, Post


data = [
    {
        'author': 'J R Tolken',
        'title': 'Lord of the Rings: The Fellowship of the Ring',
        'content': 'A historic epic that everyone would have loved to experience',
        'date_posted': '29 July 1954'
    },
    {
        'author': 'J K Rowling',
        'title': 'Harry Potter: The Sorcers Stone',
        'content': 'Magical Relm everyone would love to be part of!!',
        'date_posted': '26 June 1997'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=data)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Log In Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Log In', form=form)
