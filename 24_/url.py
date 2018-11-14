from flask import Flask, render_template
import urllib.request
import json
import ssl

app=Flask(__name__)

@app.route("/")
def home():

    # Python 3.6 on OSX has no certificates at all, and can't validate any SSL connections

    # accessing and reading api
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=qW3bb6KgHGBkm5oDsidiolh2VvzenUI4zFpIjObw")
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
