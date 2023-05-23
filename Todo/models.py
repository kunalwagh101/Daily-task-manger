from Todo import db,app,login_manager
from datetime import datetime
from flask_login import UserMixin


class Blognet(db.Model):

    Srno = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(200), nullable=False)
    Description = db.Column(db.String(500),nullable=False)
    owner = db.Column(db.Integer,nullable=False)
    time_stamp = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self) -> str:
        return f"{self.Srno} - {self.Title}"
    



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500),unique=True,nullable=False)
    password = db.Column(db.String(500),nullable=False)
    


    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"

  

with app.app_context():
    db.create_all()