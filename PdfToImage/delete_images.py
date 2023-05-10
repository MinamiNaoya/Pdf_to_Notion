import os
import shutil

def delete_images():
    shutil.rmtree('PdfToImage/image_file')
    os.makedirs('PdfToImage/image_file', exist_ok=True)

delete_images()
