import numpy as np
import cv2
imBGR =cv2.imread("test1.jpg",1)
im = cv2.imread("test1.jpg",0)
tresh,BW_im = cv2.threshold(im,150,255,cv2.THRESH_BINARY_INV)
im2 = BW_im.copy()


contours,hi =cv2.findContours(BW_im,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
i=0
for con in contours:
    x,y,w,h = cv2.boundingRect(con)
    cv2.rectangle(imBGR,(x,y),(x+w,y+h),(0,255,0),1)
    cv2.imshow("data",imBGR)
    letter = BW_im[y:y+h,x:x+w]
    letter = cv2.resize(letter,[15,20])#[w,h]
    f_name = "dbase/l"+str(26-i)+".jpg"
    cv2.imwrite(f_name,letter)
    cv2.waitKey(500)
    i=i+1
cv2.destroyAllWindows()
