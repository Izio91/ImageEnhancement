import numpy as np

def make_image_negative(image):
    return np.subtract(255, image)

def histogram_of_grayscale(image):
    histogram = np.zeros(256)
    for row in image:
        for pixel in row:
            histogram[pixel] = histogram[pixel] + 1
    return histogram.astype(int)