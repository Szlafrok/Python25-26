filepath = "Lekcja40 - Przetwarzanie obrazow/"

import cv2
import numpy as np # py -m pip install numpy
from PIL import Image

def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image_cv(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img)
    print(img.shape)
    print(type(img))
    return img

image = read_image_cv(f"{filepath}goku.jpg")
show_image(image)

def grayscale(img):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            pixel = img[row][column].astype(np.uint16)
            gray = int(sum(pixel) / 3)
            img[row][column] = np.array([gray, gray, gray])
    return np.array(img, dtype = np.uint8)

img = grayscale(image)
show_image(img)