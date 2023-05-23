from flask_wtf import FlaskForm 
from Todo.models import User
from wtforms import StringField ,PasswordField ,SubmitField ,EmailField

from wtforms.validators import DataRequired ,Length,Email,InputRequired,EqualTo,ValidationError



def validate_email(self, email) :
         
        if User.query.filter_by(email = email.data).first() :
                  print("email is already register")
                  raise ValidationError("email is already register")
   
def validate_username(self, username) :
         
        if User.query.filter_by(name = username.data).first() :
                  print("username is already register")
                  raise ValidationError("username is already register")   





class RegistrationForm(FlaskForm) :

      username = StringField('Username',validators=[DataRequired(),validate_username,Length(min=2, max=25)])
      email = EmailField('Email address', validators=[Email(),InputRequired(), validate_email,Length(4, 128)])
      password = PasswordField('Password :', validators=[DataRequired(),Length(4, 128) ])
      confirm = PasswordField('Confirm Password: ',validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

      submit = SubmitField('Sign In')


    

    

class LoginForm(FlaskForm) :
        email = EmailField('Email', validators=[Email(),InputRequired(), Length(4, 128)])
        password = PasswordField('Password :', validators=[DataRequired(),Length(4, 128) ])
        submit = SubmitField('Login')