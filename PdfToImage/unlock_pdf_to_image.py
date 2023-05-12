import unlock_pdf
from pdf2image import convert_from_path
import os
from pathlib import Path

# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

HOME_DIR = os.path.expanduser("~")

# reprは変数に対するraw文字列のようなもの、エクスプローラーを起動

# PDF -> Image に変換（150dpi）
pages = convert_from_path(str(unlock_pdf.unlocked_pdf_path), 150)

# image_fileの絶対パスをここに入力

input_abs_imgdir_path = r"C:\Users\owner\OneDrive\デスクトップ\PDF_TO_NOTION_project\Pdf_to_Notion\PdfToImage\image_file"

abs_image_dir_path = Path(input_abs_imgdir_path)

for i , page in enumerate(pages):
    file_name = unlock_pdf.unlocked_pdf_path.stem + "_{:02d}".format(i+1) + ".jpeg"
    image_path = abs_image_dir_path / file_name
    # JPEGで保存する。
    page.save(str(image_path), "JPEG")
    




    
