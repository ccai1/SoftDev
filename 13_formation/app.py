#Cathy Cai
#SoftDev1 pd06
#K13: Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
    
def home():
    print (app)
    return '''home<br>
              <a href='/form'>form</a><br>
    '''

@app.route('/form')
    
def form():
    return render_template('/index.html')

@app.route('/auth', methods=["GET", "POST"])

def authenticate():
    print ('start')
##    print (app)
##    print (request)
##    print (request.headers)
##    print (request.method)
##    print (request.args)
##    print (request.form)
    name = request.form['first'] + ' ' + request.form['last'] 
    return 'POST Request...<br>Hi ' +  name + ', do you like mangos?' + '<br><a href="/">home</a><br>'

if __name__ == '__main__':
    app.debug = True
    app.run()

