import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir,'db.sqlite')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dbfile
# DB와 연동
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# DB 에 반영
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

#
#class Test(db.Model):
#    __tablename__ = "test_table"  #하나의 모델이 된다.
#    id = db.Column(db.Integer, primary_key = True) 
#    name = db.Column(db.String(32), unique = True) 


#db.create_all()



@app.route('/')
def hello():
    return "오늘의 교훈: 강사보다 공식문서가 백 배 낫다...."

 
