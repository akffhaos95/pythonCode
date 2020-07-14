from flask import Flask, render_template, jinja2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return "yummy cakse"

if __name__ == '__main__':
    app.run(debug = True)