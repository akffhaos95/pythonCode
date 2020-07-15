from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os

UPLOAD_DIRECTORY = os.path.dirname(__file__) + "/files"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/fileUpload', methods=['POST'])
def fileUpload():
    if request.method == 'POST':
        result = request.form
        f = request.files['file']
        dirname = os.path.dirname(__file__) + '/files/' + f.filename
        print(result)
        print(dirname) 
        f.save(dirname)
    return render_template('list.html', result=result, dir=f.filename)

@app.route('/files')
def list_files():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return render_template('list.html', files=files)

@app.route('/files/<path:path>')
def get_file(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug = True, port = 8089)