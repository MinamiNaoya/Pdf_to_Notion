from pathlib import Path
import json
import PyPDF2
import copy

# Load configuration from config.json
with open("PdfToImage/config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_pdfdir_path = config["device"][0]["pdf_file_path"]
    input_abs_imgdir_path = config["device"][0]["image_file_path"]

# Get PDF file path from user input
abs_pdf_file_dirpath = Path(input_abs_pdfdir_path)
file_name = input("Enter pdf file name!:")
pdf_file_path = abs_pdf_file_dirpath.joinpath(str(file_name))

# Open the input PDF file
input_pdf = open(pdf_file_path, "rb")

# PDF reader object
pdf_reader = PyPDF2.PdfReader(input_pdf)

# Create a PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# Set padding values (adjust as needed)
padding_top = 10   # padding from the top
padding_bottom = 10  # padding from the bottom
padding_left = 10    # padding from the left
padding_right = 10   # padding from the right

for i in range(len(pdf_reader.pages)):
    # create multiple objects for each page
    page = pdf_reader.pages[i]

    # Get the coordinates of the page (paper size)
    x0 = page.mediabox.left
    y0 = page.mediabox.bottom
    x1 = page.mediabox.right
    y1 = page.mediabox.top

    # Adjust for padding
    x0 += padding_left
    y0 += padding_bottom
    x1 -= padding_right
    y1 -= padding_top

    # Calculate positions for 2 sections (top and bottom)
    mid_height = (y1 + y0) / 2

    coords = [
        ((x0, mid_height), (x1, y1)),  # Top half
        ((x0, y0), (x1, mid_height))  # Bottom half
    ]

    # Add each cropped section as a new page
    for lower_left, upper_right in coords:
        new_page = copy.copy(page)
        new_page.cropbox.lower_left = lower_left
        new_page.cropbox.upper_right = upper_right
        pdf_writer.add_page(new_page)

# Close the input PDF file
input_pdf.close()

# Save the output PDF file
output_pdf_path = f"PdfToImage/pdf_file/divided_two_{file_name}"

with open(output_pdf_path, "wb") as output_pdf:
    pdf_writer.write(output_pdf)

print("PDF page divided into two equal parts (top and bottom) with padding successfully!")

