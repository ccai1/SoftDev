from flask import Flask, render_template
import urllib.request
import json
import ssl

app=Flask(__name__)

@app.route("/")
def home():

    # accessing and reading api
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=qW3bb6KgHGBkm5oDsidiolh2VvzenUI4zFpIjObW")
    info = u.read()
    print (info)

    #converting the json object string into a dict
    info = json.loads(info)

    #passing in "url" value to template
    return render_template("index.html",
                           pic=info["url"]
                           )

if __name__=="__main__":
    app.debug=True
    app.run()
