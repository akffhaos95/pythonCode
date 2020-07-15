from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello '+guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

if __name__ == '__main__':
    app.run()