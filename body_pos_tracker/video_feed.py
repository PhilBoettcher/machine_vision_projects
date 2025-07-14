import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot Open Camera")
    exit()
while True:
    ret, frame = cap.read()
    
    # ret is True when frame is read correctly
    if not ret:
        print("Cannot read frame. Exiting...")
        break
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
