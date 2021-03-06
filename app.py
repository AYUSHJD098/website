from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))

# class Product(db.Model):
#     """
#     Database class
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     projectname = db.Column(db.String(50))
#     date_posted = db.Column(db.DateTime)
#     des = db.Column(db.Text)
#     repo = db.Column(db.String(50))


#     class LoginForm(FlaskForm):
#         username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
#         password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
#         remember = BooleanField('remember me')

#     class RegisterForm(FlaskForm):
#         email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
#         username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
#         password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def project():
    return render_template('project.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')


# not sure bout this 
# @app.route('/manage/projects')
# def manage_project():
#     return render_template('index.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user:
#             if check_password_hash(user.password, form.password.data):
#                 login_user(user, remember=form.remember.data)
#                 return redirect(url_for('home'))

#         return '<h1>Invalid username or password</h1>'
#         #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

#     return render_template('login.html', form=form)

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     form = RegisterForm()

#     if form.validate_on_submit():
#         hashed_password = generate_password_hash(form.password.data, method='sha256')
#         new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         return '<h1>New user has been created! <a href="/login">Login</a></h1>'
#             #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

#     return render_template('signup.html', form=form)

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))


# @app.route('/post/<int:post_id>')
# @login_required
# def post(post_id):
#     """
#     Post page route
#     """
#     pass


# @app.route('/addpost', methods=['POST', 'GET'])
# @login_required
# def addpost():
#     if request.method == "POST":
#         #request from form
#         pass
#     else:
#         #just render_template
#         pass



if __name__ == '__main__':
    app.run(debug=True)