from PIL import Image
import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract'
# print(pytesseract.image_to_string(Image.open("D:/Jyoti-backup/python-project_folders/Info-Extraction/mixed.png")))

# pytesseract.pytesseract.run_tesseract('D:/Jyoti-backup/python-project_folders/Info-Extraction/eng2.jpg', 'out1', lang=None, extension="hocr")
# print(pytesseract.image_to_string(Image.open("D:/Jyoti-backup/python-project_folders/Info-Extraction/hindi.jpg"), lang="hin"))


import codecs
import pyocr.builders

builder = pyocr.builders.LineBoxBuilder()
with codecs.open("out1.html", 'r', encoding='utf-8') as file_descriptor:
    line_boxes = builder.read_file(file_descriptor)
