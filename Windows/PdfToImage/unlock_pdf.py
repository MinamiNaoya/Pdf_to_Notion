from pikepdf import Pdf
from pathlib import Path
import json

with open("PdfToImage\config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_pdfdir_path = config["device"][0]["pdf_file_path"]
    input_abs_imgdir_path = config["device"][0]["image_file_path"]
  
abs_pdf_file_dirpath = Path(input_abs_pdfdir_path)
file_name = str(input("Enter pdf file name!:"))
password = str(input("Please enter password!:"))

pdf_file_path = abs_pdf_file_dirpath.joinpath(file_name) # -> os.でファイル名を取ってきてもいいかも
unlocked_pdf_path = abs_pdf_file_dirpath.joinpath("unlocked" + file_name)

pdf = Pdf.open(pdf_file_path, password=password) # pdfを開く
pdf_unlock = Pdf.new() 
pdf_unlock.pages.extend(pdf.pages)
pdf_unlock.save(unlocked_pdf_path)