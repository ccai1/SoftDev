from flask import Flask, render_template
import urllib.request
import json
import ssl

app=Flask(__name__)

@app.route("/")
def home():

    # accessing and reading api
    u = urllib.request.urlopen("http://api.nytimes.com/svc/search/v2/articlesearch.json?web_url=https://www.nytimes.com/interactive/2018/06/25/us/politics/midterm-primaries-voter-turnout.html&api-key=57dd2d5912f741448596f2d6aae17114")
    info = u.read()

    #converting the json object string into a dict
    info = json.loads(info)

    print ("------------")
    print (info)
    print ("------------")

    #passing in api values to template
    return render_template("index.html",
                           headline=info["response"]["docs"][0]["headline"]["main"],
                           date=info["response"]["docs"][0]["pub_date"],
                           content=info["response"]["docs"][0]["snippet"],
                           link=info["response"]["docs"][0]["web_url"]
                           )

if __name__=="__main__":
    app.debug=True
    app.run()
