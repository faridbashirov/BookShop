from email import message
from tabnanny import check
from flask_wtf import FlaskForm
from extensions import *
from models import User

from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired,email,Length,ValidationError
def check(form,field):
        
        
        for i in User.query.all():
          if field.data ==i.username:
            raise ValidationError("exists")
class MyForm(FlaskForm):
        full_name=StringField(label="full_name",validators=[DataRequired(),Length(min=3,max=30)])
        comment=TextAreaField(label="comment",validators=[DataRequired() ])
class LoginForm(FlaskForm):
        username=StringField(label="username",validators=[DataRequired(),Length(min=3,max=30)])
        password=StringField(label="password", validators=[DataRequired()])
class RegisterForm(FlaskForm):
        first_name=StringField(label="first_name",validators=[DataRequired(),Length(min=3,max=30)])
        username=StringField(label="username",validators=[DataRequired(),Length(min=3,max=30),check])
        last_name=StringField(label="last_name",validators=[DataRequired(),Length(min=3,max=30)])
        password=StringField(label="password",validators=[DataRequired(),Length(min=3,max=30)])
        email=StringField(label="email", validators=[DataRequired(),email(),])
        
        
        