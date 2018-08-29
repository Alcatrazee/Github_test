import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    succ,frame = capture.read()
    
    result = cv2.GaussianBlur(frame,(7,7),10)

    cv2.imshow("img",result)
    if cv2.waitKey(20) == 32:
        break
cv2.destroyAllWindows()


