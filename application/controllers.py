from flask import Flask, render_template, redirect, request
from flask import current_app as app
from .models import * 

@app.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(username=username).first()
        if this_user:
            if this_user.password == pwd:
                if this_user.type == "manager":
                    return redirect("/manager")
                else:
                    return render_template("user_dash.html", this_user=this_user)
            else:
                return render_template("incorrect_p.html")
        else:
            return render_template("not_exist.html")

    return render_template("login.html")

@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        pwd = request.form.get("pwd")
        user_name = User.query.filter_by(username = username).first()
        user_email = User.query.filter_by(email = email).first()
        if user_name or user_email:
            return render_template("already.html")
        else:
            new_user = User(username = username, email = email, password=pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")
        
    return render_template("register.html")
