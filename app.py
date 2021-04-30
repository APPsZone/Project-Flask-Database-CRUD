from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from flask_sqlalchemy import SQLAlchemy
from models import *
from passlib.hash import pbkdf2_sha256
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_script import Manager
from postgres import Postgres
from flask_migrate import Migrate, MigrateCommand
import psycopg2, psycopg2.extras

def invalid_credentials(form, field):
    """Username and password checker """
    
    username_entered = form.username.data
    password_entered = field.data
    
    #Check credentials is valid
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or password is incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username or password is incorrect")
    
class SignUpForm(FlaskForm):
    """ Sign Up Form """
    username = StringField('username_label', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password required"), Length(min=8, max=20, message="Password must be between 8 and 20 characters")])
    confirm_pswd = PasswordField('confirm_pswd_label', validators=[InputRequired(message=" Confirm Password required"), EqualTo('password', message="Password must match")])
    submit_button = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists.")
class LoginForm(FlaskForm):
    """ Login Form """
    username = StringField('username_label', validators=[InputRequired(message="Username required")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password required"), invalid_credentials])
    login_button = SubmitField('Login')

#configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:appjunior123@localhost:5432/Garage' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db = SQLAlchemy(app)

conn = psycopg2.connect(host="localhost", database="Garage", user="postgres", password="appjunior123", port = 5432)
mycursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Configure flask login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
def home():
    return render_template('home2.html')
        
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    reg_form = SignUpForm()
    
    #updated database if validation success
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        
        #Hash password 
        hashed_pwd = pbkdf2_sha256.hash(password)
        
        
        #Add user to DB
        user = User(username=username, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=reg_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)   
        return redirect(url_for('apps'))
 
    return render_template('login.html', form=login_form)

@app.route("/apps", methods=['GET', 'POST'])
@login_required
def apps():
    if not current_user.is_authenticated:
        return "Please login before.."
    
    return render_template('home.html')

@app.route('/jasaservis', methods=['GET', 'POST'])
def jasa():
    mycursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    mycursor.execute ("SELECT * FROM jasaservis")
    data = mycursor.fetchall()
    return render_template('jasaservis.html', data=data)
    mycursor.close()

@app.route('/simpan', methods=['GET', 'POST'])
def simpan():
    if request.method == 'POST':
        id_data = request.form['id']
        nama = request.form['nama']
        harga = request.form['harga']
        mycursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        mycursor.execute ("INSERT INTO jasaservis nama, harga) VALUES (%s, %s)", (id, nama, harga,))
        mycursor.commit()
        flash('Added successfully')
        return redirect(url_for('jasaservis'))

@app.route('/update', methods=['POST'])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    harga = request.form['harga']
    mycursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    mycursor.execute("UPDATE jasaservis SET nama=%s, harga=%s WHERE id=%s", (nama, harga))
    mycursor.commit()
    flash('Added successfully')
    return redirect(url_for('jasaservis'))

@app.route('/hapus/<string:id_data>', methods=['POST'])
def hapus(id_data):
    mycursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    mycursor.execute("DELETE FROM jasaservis WHERE id=%s", (id_data))
    mycursor.commit()
    flash('Removed Successfully')
    return redirect(url_for('jasaservis'))
    
@app.route('/sparepart', methods=['GET', 'POST'])
def spare():
    mycursor.execute ("SELECT * FROM sparepart")
    data = mycursor.fetchall()
    return render_template('sparepart.html', data=data)
    mycursor.close()
    
@app.route('/aksesoris', methods=['GET', 'POST'])
def aksesoris():
    mycursor.execute ("SELECT * FROM aksesoris")
    data = mycursor.fetchall()
    return render_template('aksesoris.html', data=data)
    mycursor.close()
    
@app.route("/logout", methods=['GET'])
def logout():
    
    logout_user()
    return render_template('home2.html')

if __name__ == '__main__':
    app.run(debug=True)