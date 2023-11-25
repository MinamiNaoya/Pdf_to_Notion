import os
import shutil

def delete_pdfs():
    shutil.rmtree('PdfToImage/pdf_file')
    os.makedirs('PdfToImage/pdf_file', exist_ok=True)

delete_pdfs()
print("success!")