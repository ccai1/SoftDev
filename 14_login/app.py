#Cathy Cai and Emily Lee - CaiLee Cosmetics
#SoftDev1 pd6
#K14 -- Do I know You?
#2018-10-02

from flask import Flask, session, render_template, url_for, redirect, request
import os

app=Flask(__name__)
app.secret_key=os.urandom(32)


@app.route("/")
def login():

    #if logged in, welcome!
    if 'watermelon' in session:
        return render_template("/welcome.html",
                               user="Watermelon")

    #if not, log in!
    return render_template("/login.html")


@app.route("/welcome", methods=["POST"])
def auth():

    #add session
    session["watermelon"] = "juice"
    
    #wrong username/pass
    if request.form["user"]!="watermelon":
        return error('username or password')  
    if request.form["pass"]!=session["watermelon"]:
        return error('password')
    
    #right username and pass, go to welcome page!
    if request.form["pass"]==session["watermelon"]:
        return render_template("/welcome.html",
                               user="Watermelon"
                               )


#wrong credentials, try again!
def error(error):
    return render_template("/login.html",
                           error=error
                           )


@app.route("/logout")
#logging out removes the user from the current session
def logout():
    session.pop("watermelon")
    return redirect(url_for("login"))


if __name__=="__main__":
    app.debug=True
    app.run()
