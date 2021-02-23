from flask import Flask, render_template
from models import Scuser
from api_v1 import api as api_v1
import os
from models import db
app = Flask(__name__)
app.register_blueprint(api_v1,url_prefix = "/api/v1")

@app.route("/")
def hello():
    return "Hello world!"


@app.route("/register",methods = ["GET","POST"])
def register():

     
    return render_template("register.html")




if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir,'db.sqlite')


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dbfile
# DB와 연동
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# DB 에 반영
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SECRET_KEY"] = "asdoduahfoeafh"



    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host="127.0.0.1",port=5000,debug=True)