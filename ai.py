import cv2
import pytesseract
from pytesseract import Output
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\axian\AppData\Local\Tesseract-OCR\tesseract.exe";


#edit where image is found later
#proof = cv2.imread('test.jpg')
proof = cv2.imread(r"C:\Users\axian\OneDrive\Documents\CT AI\test.jpg", cv2.IMREAD_COLOR)
scale_percent = 25

width = int(proof.shape[1] * scale_percent / 100)
height = int(proof.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)
output = cv2.resize(proof, dsize)
cv2.imshow('img', output)
cv2.waitKey(0)
text = pytesseract.image_to_data(proof, output_type=Output.DICT)



keys = list(text.keys())

detect = "COVID-19 Vaccination Record Card"
search = len(text['text'])
print("YOSH")
#for i in range(search):
#   if re.match(detect, d['text'][i]):
#        print("Username is: ")
