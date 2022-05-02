import pytesseract
import cv2
import csv
from pytesseract.pytesseract import Output
id_no="306629406413"

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img1=cv2.imread('c:/Users/BISWAJIT/OneDrive/Desktop/voter1.jpg')
color=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cus_conf=r'--oem 3 --psm 6 '
th=cv2.threshold(color,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
detail=pytesseract.image_to_data(th,output_type=Output.DICT,config=cus_conf)
parse_text=[]
word_list=[]
last_word=''
for word in detail['text']:
    if word!='':
        word_list.append(word)
        last_word=word
    if (last_word!='' and word=='') or (word==detail['text'][-1]) :
        parse_text.append(word_list)
        word_list=[]

for i in parse_text:
    data=",".join(i)
    data=data.replace(",","")
    print(data)
    if data==id_no:
        print("found : ",id_no)


