from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''<b>Welcome to my page!</b><br><br>
            <button onclick="location.href='/fruits'">fruits</button>
            <button onclick="location.href='/drinks'">drinks</button>
            '''

@app.route('/fruits')
def food():
    return '''A list of fruits I love:
            <ul>
            <li>avocados</li>
            <li>strawberries</li>
            <li>mangosteens</li>
            </ul>
            <button onclick="location.href='/'">home</button>
            '''

@app.route('/drinks')
def drinks():
    return '''A list of drinks I love:
            <ul>
            <li>tea</li>
            <li>coffee</li>
            <li>smoothies</li>
            </ul>
            <button onclick="location.href='/'">home</button>
            '''


if __name__ == '__main__':
    app.debug = True
    app.run()
