from flask import Flask, render_template,request,url_for

app = Flask(__name__,static_folder="assets")

from extensions import *
from models import *
from controller import *
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123@127.0.0.1:3307/book"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
app.config["SECRET_KEY"]="myproject"
