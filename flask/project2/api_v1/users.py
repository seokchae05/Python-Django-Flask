from . import api
from flask import jsonify
from flask import request
from models import Scuser, db

@api.route("/users",methods =["GET","POST"])
def users():
    if request.method == "POST":
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')
    
        if not (userid and username and password and re_password):
            return jsonify({"error: no argument"},400)
        
        if password != re_password:
            return jsonify({"error: Wrong password"},400)
    
        scuser = Scuser()
        scuser.userid = userid
        scuser.username = username           
        scuser.password = password


        db.session.add(scuser)
        db.session.commit()

        return jsonify(),201

    users = Scuser.query.all()


    return jsonify([user.serialize for user in users])


@api.route("/users/<uid>",methods =["GET","PUT","DELETE"])
def user_detail(uid):
    if request.method == "GET":
        user = Scuser.query.filter(Scuser.id == uid).first()
        return jsonify(user.serialize)
    elif request.method == "DELETE":
        Scuser.query.delete(Scuser.id == uid)
        return jsonify(),204

    data = request.get_json()
    Scuser.query.filter(Scuser.id == uid).update(data)
    user = Scuser.query.filter(Scuser.id == uid).first()
    return jsonify(user.serialize)
