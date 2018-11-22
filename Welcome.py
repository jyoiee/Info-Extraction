from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract'
print(pytesseract.image_to_string(Image.open("D:/Jyoti-backup/python-project_folders/Info-Extraction/img1.jpg")))

# pytesseract.pytesseract.run_tesseract('D:/Jyoti-backup/python-project_folders/Info-Extraction/eng2.jpg', 'output', lang=None, extension="hocr" )
# print(pytesseract.image_to_string(Image.open("D:/Jyoti-backup/python-project_folders/Info-Extraction/hindi.jpg"), lang="hin"))