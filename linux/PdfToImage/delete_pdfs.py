import os
import shutil
import json

with open("PdfToImage/config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_pdfdir_path = config["device"][0]["pdf_file_path"]

def delete_pdfs():
    shutil.rmtree(input_abs_pdfdir_path)
    os.makedirs(input_abs_pdfdir_path, exist_ok=True)

delete_pdfs()
print("success!")