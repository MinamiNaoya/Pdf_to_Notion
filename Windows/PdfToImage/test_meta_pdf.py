import pypdf

pdf = pypdf.PdfReader(r'パス')

print(type(pdf.metadata))
print(pdf.metadata)
