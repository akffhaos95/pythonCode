from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/method', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Post'
    elif request.method == 'GET':
        return 'Get'

@app.route('/login', methods=['GET'])
def login1():
    user = request.args.get('username')
    return 'name %s'%user

@app.route('/login', methods=['POST'])
def login2():
    username = request.form['username']
    password = request.form['password']
    return "username : %s password: %s"%(username,password)

if __name__ == '__main__':
    app.run(debug=True, port=8089)