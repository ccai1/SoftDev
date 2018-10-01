#Cathy Cai and Emily Lee - CaiLee Cosmetics
#SoftDev1 pd6
#K14 -- Do I know You?
#2018-10-02

from flask import Flask #, render_template
#from util import

app=Flask(__name__)
from flask import Flask, session, render_template, url_for, redirect, request
import os

app=Flask(__name__)
app.secret_key=os.urandom(32)

@app.route("/")
def login():
    if request.cookies.get('session'):
        return render_template ("/welcome.html",
                               user="Watermelon"
                               )
    else:
        return render_template("/login.html")

@app.route("/welcome", methods=["POST"])
def auth():
    session["watermelon"]="juice"
    if request.form["user"]!="watermelon":
        return error('username or password')
    if request.form["pass"]!=session["watermelon"]:
        return error('password')
    if request.form["pass"]==session["watermelon"]:
        return render_template("/welcome.html",
                               user="Watermelon"
                               )

@app.route("/error")
def error(error):
    return render_template("/login.html",
                           error=error
                           )

@app.route("/logout")
def logout():
    session.pop('watermelon')
    return redirect(url_for("login"))
        
if __name__=="__main__":
    app.debug=True
    app.run()
