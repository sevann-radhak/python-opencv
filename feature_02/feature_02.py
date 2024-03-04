import random
import cv2
import os
# print(os.getcwd())
img = cv2.imread('./assets/logo.jpg', cv2.IMREAD_COLOR)

if img is None:
    print("Could not open or find the image")
else:    
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] 

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()