from pdf2image import convert_from_path
import os
from pathlib import Path
import json

import unlock_pdf

with open("PdfToImage\config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_pdfdir_path = config["device"][0]["pdf_file_path"]
    input_abs_imgdir_path = config["device"][0]["image_file_path"]
    

# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

HOME_DIR = os.path.expanduser("~")
# PDF -> Image に変換（150dpi）
pages = convert_from_path(str(unlock_pdf.unlocked_pdf_path), 150)

abs_image_dir_path = Path(input_abs_imgdir_path)

for i , page in enumerate(pages):
    file_name = unlock_pdf.unlocked_pdf_path.stem + "_{:02d}".format(i+1) + ".jpeg"
    image_path = abs_image_dir_path / file_name
    # JPEGで保存する。
    page.save(str(image_path), "JPEG")
    

print("success!")


    
