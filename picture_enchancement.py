import cv2
import numpy as np

capture = cv2.VideoCapture(0)
succ,frame = capture.read()
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
rows,cols = gray.shape
gray2 = np.zeros((rows,cols))
contrast=1.1
brightness=0
while True:
    succ,frame = capture.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    for i in range(rows):
        for j in range(cols):
            gray2[i,j]=gray[i,j]*contrast + brightness
            if gray2[i,j]>255:
                gray2[i,j]=255
            elif gray2[i,j]<0:
                gray2[i,j]=0
    print (gray2[300,300])
    
    #result = cv2.GaussianBlur(frame,(7,7),10)

    #cv2.imshow("img",result)
    gray2 = np.uint8(gray2)
    cv2.imshow("gray",gray2)
    if cv2.waitKey(20) == 32:
        break
    
cv2.destroyAllWindows()


