#Cathy Cai
#SoftDev1 pd06
#K09 -- Solidify
#2018-09-20

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''<a href="/static/index.html">click here</a>'''

if __name__ == '__main__':
    app.debug = True
    app.run()
