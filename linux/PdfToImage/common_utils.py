import zipfile
import logging


class FileExtentionError(Exception):
    pass


def is_pdf_file(pdf_file_name):
    if str(pdf_file_name).endswith('.pdf'):
        return True
    else:
        return False

def save_images(is_server, pdf_file_path, abs_image_dir_path, pages):
    """
    pages: pdfが画像ファイルに変換されたオブジェクト

    """
    if is_server:
        # zipオブジェクト新規作成
        with zipfile.ZipFile('images.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            logging.info("zipオブジェクトの作成")  
                         
    for i , page in enumerate(pages):
        file_name = pdf_file_path.stem + "_{:02d}".format(i+1) + ".jpeg"
        image_path = abs_image_dir_path / file_name
        
        # サーバーで実行された場合はjpegファイルを圧縮してzipファイルに圧縮してreturnする。
        if is_server:
            zipf.write(file_name)
        # ローカルの場合はJPEGでimage_fileディレクトリに保存する。   
        elif not is_server:
            page.save(str(image_path), "JPEG")

    if not is_server:  
        print("success!")
        return
    if is_server:
        return zipf


