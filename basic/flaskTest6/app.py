from flask import Flask,make_response, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        user =request.form['name']
        res = make_response("Created cookie!")
        res.set_cookie("userID", user)
        print(user)
        return res

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    print(name)
    return name

if __name__ == '__main__':
    app.run(debug=True)
    