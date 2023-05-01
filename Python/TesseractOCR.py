import cv2
import time
import pytesseract
start = time.time()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
end = time.time()
print('finished library loaded')
print(end-start)
print("----------------------------------------")
while(True):
    img = cv2.imread('BCQR.jpg')
    r = cv2.selectROI("select OCR area to Read", img)
    cropped_image = img[int(r[1]):int(r[1]+r[3]),
    int(r[0]):int(r[0]+r[2])]
    start = time.time()
    readfromtess = pytesseract.image_to_string(cropped_image, lang='tha+eng')
    print("result------")
    print(readfromtess.replace(" ", ""))
    end = time.time()
    print('processing time')
    print(end-start)
    print('Pieces / minute')
    print(int(1000/((end-start)*1000))*60)
    input('Please press Anykey')