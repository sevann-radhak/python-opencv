import random
import cv2
import numpy as np

def create_colored_images(frame):
    col_b, col_g, col_r = cv2.split(frame)
    img_red = cv2.merge([col_b * 0, col_g * 0, col_r])        
    img_blue = cv2.merge([col_b, col_g * 0, col_r * 0])      
    img_green = cv2.merge([col_b * 0, col_g, col_r * 0])
    return [img_red, img_blue, img_green]

def resize_image(image):
    return cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

def main():
    cap = cv2.VideoCapture(0)

    while True: 
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        colored_images = create_colored_images(frame)
        random_images = random.choices(colored_images, k=4)
        resized_images = [resize_image(img) for img in random_images]

        img = np.zeros(frame.shape, dtype=np.uint8)
        img[:height//2, :width//2] = resized_images[0]
        img[height//2:, :width//2] = resized_images[1]
        img[:height//2, width//2:] = resized_images[2]
        img[height//2:, width//2:] = resized_images[3]

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()