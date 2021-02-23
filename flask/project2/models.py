import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Scuser(db.Model):
    __tablename__="Scuser"
    id = db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(32))
    
    @property
    def serialize(self):
        return {
            "id" : self.id ,
            "password" : self.password,
            "userid" : self.userid ,
            "username" : self.username ,
        }