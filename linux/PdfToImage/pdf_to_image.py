from pdf2image import convert_from_path
import os
from pathlib import Path
import json
import socket
import zipfile
import logging

import common_utils as co

with open("PdfToImage/config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_pdfdir_path = config["device"][0]["pdf_file_path"]
    input_abs_imgdir_path = config["device"][0]["image_file_path"]
    is_server = config["server"][0]["is_server"]


# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler\bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

HOME_DIR = os.path.expanduser("~")

abs_pdf_file_dirpath = Path(input_abs_pdfdir_path)
pdf_file_path = abs_pdf_file_dirpath.joinpath(str(input("Enter pdf file name!:"))) # -> os.でファイル名を取ってきてもいいかも
if not co.is_pdf_file(pdf_file_path):
    raise co.FileExtentionError
    
# PDF -> Image に変換（150dpi）
pages = convert_from_path(str(pdf_file_path), 150)


abs_image_dir_path = Path(input_abs_imgdir_path)


co.save_images(is_server, pdf_file_path, abs_image_dir_path, pages)
