# Prepare image to be proccessed 
import cv2
import numpy as np

def process(image):
  try:
    image = cv2.imread(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    no_noise_img = cv2.medianBlur(gray_image, 5)
    thresholding = cv2.threshold(no_noise_img, 0, 255, cv2.THRESH_OTSU)[1]
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(thresholding, kernel, iterations = 1)
  except:
    return 'image processing failed' 