import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import io
import fitz  # PyMuPD

# Firefoxの設定オプションを作成
firefox_options = Options()
firefox_options.headless = False  # ヘッドレスモードを有効にする（画面を表示しない）


# Firefox WebDriverを起動
driver = webdriver.Firefox(options=firefox_options)

# PDFファイルのURL
abs_path = os.getcwd()
pdf_file_name = input("Enter PDF file name!:")
pdf_url = f"file:///{abs_path}/PdfToImage/pdf_file/{pdf_file_name}"
print(pdf_url)
# PDFファイルを開く
driver.get(pdf_url)

# ページ数を取得
pdf_data = driver.page_source.encode('utf-8')
pdf_file = io.BytesIO(pdf_data)
pdf_file_path = f"{abs_path}/PdfToImage/pdf_file/{pdf_file_name}"

# PyMuPDFを使用してPDFファイルを開く
pdf_document = fitz.open(pdf_file_path)

# ページ数を取得
page_count = pdf_document.page_count

print(f"PDFファイルのページ数: {page_count}")

# 各ページをスクリーンショットに保存
for page_number in range(page_count):
    driver.save_screenshot(f'/page_{page_number}.png')


# PyMuPDFを閉じる
pdf_document.close()
# WebDriverを終了
driver.quit()

    