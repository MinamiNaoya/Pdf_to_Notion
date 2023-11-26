import os
import shutil
import json

with open("PdfToImage/config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_imgdir_path = config["device"][0]["image_file_path"]
    
def delete_images():
    shutil.rmtree(input_abs_imgdir_path)
    os.makedirs(input_abs_imgdir_path, exist_ok=True)

delete_images()

print("success!")