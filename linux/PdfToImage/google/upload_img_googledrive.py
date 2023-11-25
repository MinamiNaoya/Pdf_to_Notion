import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


os.chdir(os.path.dirname(os.path.abspath(__file__)))

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': 'TEST.TXT'})
f.SetContentString('Hello')
f.Upload()

os.chdir('.\PdfToImage\image_file')
image_list = []
for images in os.listdir():
    image_list.append(images)


