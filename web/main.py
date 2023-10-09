from flask import Flask, render_template, redirect, request, flash , url_for, send_from_directory, send_file
import subprocess
import os
import platform
from werkzeug.utils import secure_filename
import socket
import logging
import json


UPLOAD_FOLDER = 'PdfToImage\pdf_file'
ALLOWED_EXTENSIONS = {'pdf'} # 拡張子の設定

pf = platform.system()
if pf == 'Windows':
    OS = 'Windows'
elif pf == 'Darwin':
    OS = 'Mac'
elif pf == 'Linux':
    OS = 'Linux'

with open("PdfToImage\config.json", encoding='utf-8') as f:
    config = json.load(f)
    is_server = config["server"][0]["is_server"]
    



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/exec_command/<string:cmd>")
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

@app.route('/convert_pdf_to_image', methods=['POST'])
def convert_pdf_to_image():
    # フォームからアップロードされたファイルを取得
    uploaded_file = request.files['pdf_file']
    if not upload_file:
        raise FileNotFoundError('File Not Found Error')
    
    # 一時的なディレクトリの作成
    temp_directory = os.path.join(os.environ['TEMP'], 'uploads')
    os.makedirs(temp_directory, exist_ok=True)

    # 一時的なファイルパスの作成
    temp_filepath = os.path.join(temp_directory, 'uploaded_pdf.pdf')
        
    uploaded_file.save(temp_filepath)
    
    # コマンドを実行してPDFから画像に変換
    try:
        result = subprocess.Popen(['pipenv', 'run', 'pdf_to_image'], stdin=subprocess.PIPE, shell=True)
        result.communicate(input=temp_filepath.encode())
        
        
        if is_server:
            return send_file(result, as_attachment=True, download_name='images.zip', mimetype='application/zip')
            
        if not is_server:
            return render_template("/pdf_to_image/pdf_to_image_successed.html")
            
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode()}"
    
@app.route('/delete_images', methods=['POST'])
def delete_images():
    try:
        subprocess.run(['pipenv', 'run', 'delete_images'], shell=True)
        return("delete images successfully!")
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode()}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
