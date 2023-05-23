from flask import Flask ,render_template ,request,redirect,url_for,flash
from Todo import db,app 
from Todo.models import Blognet ,User
from Todo.form import RegistrationForm,LoginForm
from flask_login import login_user, current_user, logout_user, login_required



from Todo import bcrypt

@app.route("/", methods=["GET", "POST"]) 
def index():
    if not current_user.is_authenticated :

        return render_template('index.html')
    
    if request.method  == "POST" :
        Title = request.form["Title"]
        Description = request.form["Description"]
        
        owner = current_user.id
        print("current user i =", owner)


        blognet = Blognet(Title = Title ,Description = Description ,owner =owner) 
        db.session.add(blognet)
        db.session.commit()

    
    blognet_new = Blognet.query.filter_by(owner = current_user.id).all()
    return render_template('index.html',blognet_new= blognet_new)


# app.route("/users/create", methods=["GET", "POST"])


# @app.route("/show") 
# def show():
#     show_time = Blognet.query.all()
    
#     print(show_time )
#     return "thsis is the minimal app"


@app.route("/delete/<int:Srno>") 
def delete(Srno):
    delete = Blognet.query.filter_by(Srno=Srno).first()

    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/update/<int:Srno>", methods = ["GET","POST"]) 
def update(Srno):
    if request.method == "POST" :
        Title = request.form["Title"]
        Description = request.form["Description"]
        blognet = Blognet.query.filter_by(Srno =Srno).first()
        blognet.Title = Title
        blognet.Description = Description
        db.session.add(blognet)
        db.session.commit()
        return redirect(url_for("index"))
 






    update = Blognet.query.filter_by(Srno = Srno).first()
    
    
    return render_template("update.html",update = update)


# @app.route("/submit",methods=["POST","GET"]) 
# def submit():
#     if request.method  == "POST" :
#         Title = request.form["Title"]
#         Description = request.form["Description"]



#     return redirect(url_for("index"),Title =Title ,Description =Description  )




@app.route("/register", methods = ['POST','GET']) 
def register():
    form  = RegistrationForm()
    if request.method == 'POST' and form.validate():
      
        try:
            username = form.username.data
            email = form.email.data
            password = form.password.data
            pw_hash = bcrypt.generate_password_hash(password)
            
            users = User(name = username , email = email , password=pw_hash )
            db.session.add(users)
            flash(f'{username} u have been register succesfully',"success")
            db.session.commit()
            return redirect(url_for('Login'))
        
        except Exception as e :
             flash(f'error occured {e}')

    # if form.errors != {}:
    #     for error_msg in form.errors.values():
    #         flash(f'{ error_msg}',category='danger')

           
   
    
        
    #if form.errors != {}:
    #     for error_msg in form.errors.values():
    #         flash(f'this is the error: { error_msg}',category='danger') 
    #         print("error_msg = ", error_msg)   

    
    return render_template("/register.html",form = form )
    
    
@app.route("/Login", methods = ['POST','GET']) 
def Login():
    # a
    
    form  = LoginForm()
    if request.method == "POST" and form.validate():
        try:
           user =  User.query.filter_by(email = form.email.data).first() 
           if user and bcrypt.check_password_hash(user.password, form.password.data) :
               login_user(user)
               next_page = request.args.get('next')

               flash(f'{user.name} u are now logged in ',"success")
               return redirect(next_page or url_for('index'))
           else:
               flash('Email or Password is incorrect ',"danger")


        except Exception as e  :
            print(e)
    return render_template("/login.html",form = form )
    
    
        
@app.route("/Logout", methods = ['POST','GET']) 
def Logout():
     
     logout_user()
     flash('Your are logged out ! ','success')
     return redirect(url_for('index'))
    