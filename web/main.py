from flask import Flask, render_template, redirect, request, flash , url_for
import subprocess
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = 'PdfToImage\pdf_file'
ALLOWED_EXTENSIONS = {'pdf'} # 拡張子の設定


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/exec_command")
def exec_command(cmd):
    subprocess.run('pipenv run ' + cmd, shell=True)
    
@app.route("/pdf_to_image")
def pdf_to_image():
    print("Rendaring pdf_to_image.html")
    return render_template("/pdf_to_image/pdf_to_image.html")

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDR'], filename))
        return redirect(url_for('download_file', name=filename))
    return render_template("/pdf_to_image/upload_pdf_file.html")

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
