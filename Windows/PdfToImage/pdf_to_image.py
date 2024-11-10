from pdf2image import convert_from_path
import os
from pathlib import Path
import json
import socket
import zipfile
import logging

with open(r"PdfToImage/config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_pdfdir_path = config["device"][0]["pdf_file_path"]
    input_abs_imgdir_path = config["device"][0]["image_file_path"]
    is_server = config["server"][0]["is_server"]


# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

HOME_DIR = os.path.expanduser("~")

abs_pdf_file_dirpath = Path(input_abs_pdfdir_path)
pdf_file_path = abs_pdf_file_dirpath.joinpath(str(input("Enter pdf file name!:"))) # -> os.でファイル名を取ってきてもいいかも
# PDF -> Image に変換（150dpi）
pages = convert_from_path(str(pdf_file_path), 150)


abs_image_dir_path = Path(input_abs_imgdir_path)




def save_images():
    if is_server:
        # zipオブジェクト新規作成
        with zipfile.ZipFile('images.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            logging.info("zipオブジェクトの作成")  
                         
    for i , page in enumerate(pages):
        file_name = pdf_file_path.stem + "_{:02d}".format(i+1) + ".jpeg"
        image_path = abs_image_dir_path / file_name
        
        # サーバーで実行された場合はjpegファイルを圧縮してzipファイルに圧縮してreturnする。
        if is_server:
            zipf.write(file_name)
        # ローカルの場合はJPEGでimage_fileディレクトリに保存する。   
        elif not is_server:
            page.save(str(image_path), "JPEG")

    if not is_server:  
        print("success!")
        return
    if is_server:
        return zipf
    


save_images()
    
