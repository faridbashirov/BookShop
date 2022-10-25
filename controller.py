from crypt import methods
from app import app
from flask import redirect, render_template,url_for,request
from models import *
from forms import MyForm,RegisterForm,LoginForm
from flask_login import login_user,login_required, logout_user
from datetime import datetime

@app.route("/product",methods=["POST","GET"])
def prodcut():
    book_name="İncognito(beyinin gizli həyatı)"
    book_price=12
    book_old_price=15
    book_description="Tanınmış nevroloq D.İqlmenin 20-dən çox dilə tərcümə edilən və indidən klassik əsərə çevrilən bu kitabı beynin sirli dünyasına təcrübələr, elmi biliklər və tarixi faktlar işığında səyahət edir.Kitab tibbi mövzuda olsa da, müəllif yazarlıq məharətini və zəngin biliyini birləşdirərək elmi faktları sadə və müqayisəli dillə oxucularına təqdim edir. Müəllif əsər boyu sədaqət geni, qumarbazlara çevrilən parkinson xəstələri, gen-mühit əlaqəsi, \"yaxşı\" və \"pis\" gen, şüuraltı və qərarvermə mexanizmi, məsuliyyət anlayışı, beynin insan həyatında rolu kimi bir çox mövzulara toxunur. Alim bu mövzuların beyinlə əlaqəsini izah etməklə kifayətlənmir, beyinlə bağlı müxtəlif formullar və modellər irəli sürür. İnsan psixologiyası və davranışlarına neyron və gen prizmasından baxmağı öyrədir. Elmi-populyar dildə yazılmış bu kitab xüsusən müəllimlər, psixoloqlar, valideynlər, həkimlər üçün mühüm bilikləri ehtiva edir."
    book_image_path=url_for('static',filename='images/Inkognito.png')
    book_quantity=2
    book_language="Azərbaycanca"
    book_genre="Psixologiya"
    book_author="David Eagleman"
    book_published_at="Qanun Nəşriyyatı"
    form=MyForm()
    post_data=request.form
    
    if request.method =="POST":
        form=MyForm(data=post_data)
        if form.validate_on_submit():
            datetimes=datetime.now()
            comment=Comments(full_name=form.full_name.data,comment=form.comment.data,date_of_comment=datetimes)
            comment.save()
            form.full_name.data=""
            form.comment.data= ""
    comments=Comments.query.all()
    return render_template('product.html',show_block=True,name=book_name,price=book_price,old_price=book_old_price,description=book_description,image=book_image_path,quantity=book_quantity,language=book_language,genre=book_genre,author=book_author,published_at=book_published_at,form=form,comments=comments)
@app.route("/")
def index():
    books=Book.query.all()
    return render_template("index.html",books=books,show_block=False)
@app.route("/book/<int:book_id>",methods=["POST","GET"])
def show_book(book_id):
    books=Book.query.all()
    langs=Language.query.all()
    genres=Genre.query.all()
    form=MyForm()
    post_data=request.form
    
    if request.method =="POST":
        form=MyForm(data=post_data)
        if form.validate_on_submit():
            datetimes=datetime.now()
            comment=Comments(full_name=form.full_name.data,comment=form.comment.data,date_of_comment=datetimes)
            comment.save()
            form.full_name.data=""
            form.comment.data=""
    comments=Comments.query.all()
    
    return render_template("book.html",book=books[book_id-1],langs=langs,genres=genres,show_nav=True,form=form,comments=comments)
@app.route("/register",methods=["POST","GET"])
def Register():
    form=RegisterForm()
    post_data=request.form
    print(post_data)
    if request.method =="POST":
        form=RegisterForm(data=post_data)
        if form.validate_on_submit():
            user=User(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data,username=form.username.data,password=form.password.data)
            user.save()
    return render_template("sign_up.html",form=form)
@app.route("/login",methods=["POST","GET"])
def Login():
    form=LoginForm()
    post_data=request.form
    if request.method =="POST":
         form=LoginForm(data=post_data)
         if form.validate_on_submit():
          form=LoginForm(data=post_data)
          user=User.query.filter_by(username=form.username.data).first()
         if user and check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect("/user-profile")
    return render_template("sign_in.html",form=form)
@app.route("/user-profile")
@login_required
def  user_profile():
    books=Book.query.all()
    
    return render_template("user-profile.html",is_active=True,books=books)