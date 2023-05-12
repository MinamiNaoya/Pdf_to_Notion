from pikepdf import Pdf
from pathlib import Path

input_abs_pdfdir_path = r"C:\Users\owner\OneDrive\デスクトップ\PDF_TO_NOTION_project\Pdf_to_Notion\PdfToImage\pdf_file"
abs_pdf_file_dirpath = Path(input_abs_pdfdir_path)
file_name = str(input("Enter pdf file name!:"))
password = str(input("Please enter password!:"))

pdf_file_path = abs_pdf_file_dirpath.joinpath(file_name) # -> os.でファイル名を取ってきてもいいかも
unlocked_pdf_path = abs_pdf_file_dirpath.joinpath("unlocked" + file_name)

pdf = Pdf.open(pdf_file_path, password=password) # pdfを開く
pdf_unlock = Pdf.new() 
pdf_unlock.pages.extend(pdf.pages)
pdf_unlock.save(unlocked_pdf_path)