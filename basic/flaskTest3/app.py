from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form_input.html')

@app.route('/login', methods=['POST'])
def login():
    result = request.form
    return render_template('form_result.html', result = result)

if __name__ == '__main__':
    app.run(debug = True, port = 8089)