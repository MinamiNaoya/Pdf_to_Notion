from pathlib import Path
import json

import PyPDF2
import copy


with open("PdfToImage/config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_pdfdir_path = config["device"][0]["pdf_file_path"]
    input_abs_imgdir_path = config["device"][0]["image_file_path"]

# Open the input PDF file   
abs_pdf_file_dirpath = Path(input_abs_pdfdir_path)
file_name = input("Enter pdf file name!:")
pdf_file_path = abs_pdf_file_dirpath.joinpath(str(file_name))

input_pdf = open(pdf_file_path, "rb")

# PDF reader object
pdf_reader = PyPDF2.PdfReader(input_pdf)

page = pdf_reader.pages[0]

# Create a PDF writer object
pdf_writer = PyPDF2.PdfWriter()


for i in range(len(pdf_reader.pages)):
    # create two object for each page
    p1 = pdf_reader.pages[i]
    p2 = copy.copy(p1)
    p3 = copy.copy(p1)
    p4 = copy.copy(p1)
    p5 = copy.copy(p1)
    p6 = copy.copy(p1)
    
    # 対角の頂点の座標を取得(用紙サイズ)
    x0 = p1.mediabox.left
    y0 = p1.mediabox.bottom
    x1 = p1.mediabox.right
    y1 = p1.mediabox.top
    
    lower_left = (x0, y0)
    lower_medium = ((x0 + x1) / 2, y0)
    lower_right = (x1, y0)
    one_second_left = (x0, (y1 + y0) / 2)
    one_second_medium = ((x0 + x1) / 2, (y0 + y1) / 2)
    one_second_right = (x1, (y0 + y1) / 2)
    upper_left = (x0, y1)
    upper_medium = ((x0 + x1) / 2, y1)
    upper_right = (x1, y1)
    
    # 4つの領域に分割
    p1.cropbox.lower_left = one_second_left
    p1.cropbox.upper_right = upper_medium
    p2.cropbox.lower_left = one_second_medium
    p2.cropbox.upper_right = upper_right
    p3.cropbox.lower_left = lower_left
    p3.cropbox.upper_right = one_second_medium
    p4.cropbox.lower_left = lower_medium
    p4.cropbox.upper_right = one_second_right
    pdf_writer.add_page(p1)
    pdf_writer.add_page(p2)
    pdf_writer.add_page(p3)
    pdf_writer.add_page(p4)
        

    
    
    
    
# Close the input PDF file
input_pdf.close()

# Save the output PDF file
output_pdf_path = "PdfToImage\pdf_file" + "\divided_four" + str(file_name)

with open(output_pdf_path, "wb") as output_pdf:
    pdf_writer.write(output_pdf)



print("PDF page divided into four equal parts successfully!")

