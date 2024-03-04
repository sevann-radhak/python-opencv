import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True: 
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    img = np.zeros(frame.shape, dtype=np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    img[:height//2, :width//2] = smaller_frame  
    img[height//2:, :width//2] = smaller_frame  
    img[:height//2, width//2:] = smaller_frame  
    img[height//2:, width//2:] = smaller_frame  
    
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
