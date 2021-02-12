import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from models import db

from models import Fcuser

app = Flask(__name__)





@app.route('/register',methods = ["GET","POST"])
def register():
    if request.method =="GET":
        return render_template("register.html")
    else:
        userid = request.form.get("userid")
        username = request.form.get("username")
        password = request.form.get("passsword")
        re_password = request.form.get("re-passsword")

        if not userid and username and password and re_password:
            return render_template("register.html")

        if password != re_password:
            return render_template("register.html")
        
        fcuser = Fcuser()
        fcuser.userid = userid
        fcuser.username = username
        fcuser.password = password

        db.session.add(fcuser)
        db.session.commit()

        return redirect("/")

@app.route('/')
def hello():
    return render_template("hello.html")
    #라우트 안에 컨트롤러 역할을 하는 기능이 담길 예정
    #분리해서 담아준다.
    #컨트롤러와 뷰의 분리

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir,'db.sqlite')


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dbfile
# DB와 연동
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# DB 에 반영
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    db.app = app
    db.create_all()


    app.run(host="127.0.0.1",port=5000, debug=True)


 
