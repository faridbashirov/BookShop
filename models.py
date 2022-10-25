from app import app
from extensions import *
from extensions import LoginManager
from extensions import LoginManager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)
class Language(db.Model):
     id=db.Column(db.Integer,primary_key=True )
     lang_name=db.Column(db.String(250),nullable=False )
     lang_code=db.Column(db.String(2),nullable=False )
     def __init__(self,lang_name,lang_code):
         self.lang_name=lang_name
         self.lang_code=lang_code
        
     def __repr__(self):
            return self.lang_name
     def save(self):
            db.session.add(self)
            db.session.commit()
  

class Genre(db.Model):
     id=db.Column(db.Integer,primary_key=True )
     name=db.Column(db.String(250),nullable=False )
     def __init__(self,name):
         self.name=name
        
     def __repr__(self):
            return self.name
     def save(self):
            db.session.add(self)
            db.session.commit()
class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True )
    title=db.Column(db.String(250),nullable=False )
    author=db.Column(db.String(250),nullable=False )
    price=db.Column(db.Float,default=10.00 )
    description=db.Column(db.Text,nullable=False )
    image_url=db.Column(db.String(250),nullable=False )
    stock=db.Column(db.Integer)
    genre_id=db.Column(db.Integer,db.ForeignKey("genre.id"),nullable=False)
    language_id=db.Column(db.Integer,db.ForeignKey("language.id"),nullable=False)
    publisher=db.Column(db.String(250),nullable=False)
    def __init__(self,title,author,price,desciption,image_url,stock,genre_id,language_id,publisher):
         self.title=title
         self.author=author
         self.price=price
         self.description=desciption
         self.image_url=image_url
         self.stock=stock
         self.genre_id=genre_id
         self.language_id=language_id
         self.publisher=publisher
    def __repr__(self):
        return self.title
    def save(self):
        db.session.add(self)
        db.session.commit()
class Comments(db.Model):
      id=db.Column(db.Integer,primary_key=True )
      full_name=db.Column(db.String(250),nullable=False )
      comment=db.Column(db.Text,nullable=False )
      date_of_comment=db.Column(db.DateTime)
      def __repr__(self):
          self.full_name
      def __init__(self,full_name,comment,date_of_comment):
          self.full_name=full_name
          self.comment=comment
          self.date_of_comment=date_of_comment
      def save(self):
          db.session.add(self)
          db.session.commit()
    
    
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30),nullable=False)
    last_name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    username = db.Column(db.String(30),nullable=False)
    password=db.Column(db.String(255),nullable=False)
    is_active=db.Column(db.Boolean,nullable=False)
    is_superuser=db.Column(db.Boolean,nullable=False)
    def __init__(self,first_name,last_name,email,username,password,is_active=True,is_superuser=False):
      self.first_name=first_name
      self.last_name=last_name
      self.email=email
      self.password=generate_password_hash(password)
      self.username=username
      self.is_active=is_active
      self.is_superuser=is_superuser   
    def set_password(self,new_password):
          self.password=generate_password_hash(new_password)
    def check_password(self,password):
        return  check_password_hash(self.password,password)
    def save(self):
        db.session.add(self)
        db.session.commit()
