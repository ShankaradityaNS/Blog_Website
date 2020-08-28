from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LogInForm
from flask_sqlalchemy import SQLAlchemy
from models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '3337817fa603bc909ed5af2dfc488ec5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


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


if __name__ == '__main__':
    app.run(debug=True)
