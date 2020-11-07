import numpy as np
import cv2

def image_is_in_gray_scale(image):
    return len(image.shape) == 2

def make_image_negative(image):
    if not image_is_in_gray_scale(image):
        """image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        output = np.subtract([179, 255, 255], image)
        output = output.astype(np.uint8)
        output = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)"""
        output = np.subtract([255, 255, 255], image)
        return output.astype(np.uint8)
    else:
        return np.subtract(255, image)

def histogram_of_grayscale(image):
    histogram = np.zeros(256)
    for row in image:
        for pixel in row:
            histogram[pixel] = histogram[pixel] + 1
    return histogram.astype(int)