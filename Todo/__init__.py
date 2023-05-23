from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blognet.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "kunal@123"

db = SQLAlchemy(app)
login_manager = LoginManager()
bcrypt = Bcrypt(app)

login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = u"Please Login "
login_manager.login_message_category = "danger"





from Todo import routes


app.app_context().push()