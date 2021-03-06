from Utilities import show_image
from Utilities import read_image
from Utilities import show_histogram
from Utilities import show_couple_of_images
from ImageEnhancement import make_image_negative
from ImageEnhancement import histogram_of_grayscale
from ImageEnhancement import local_thresholding
from ImageEnhancement import histogram_equalization
import numpy as np
import cv2

path= 'images/1577x1365.png'
#path= 'images/745x419.jpg'
#path = 'images/402x588.png'
path= 'images/columbia.jpg'
#path= 'images/306x341.png'
#path= 'images/sonnet.png'
color_scale = "rgb"
image = read_image(path, color_scale)

# Threshold
output = local_thresholding(image, 7)
show_couple_of_images(image, output, "Original", "Local Thresholding", color_scale)

# Negative
"""
show_couple_of_images(image, make_image_negative(image), "Original", "Negative", "rgb")"""

# Histogram
"""
N = image.shape[0] * image.shape[1]
histogram = histogram_of_grayscale(image)
show_histogram(histogram/N, "Pixel intensity", "Pixel frequency")"""

# Histogram equalization
"""output = histogram_equalization(image)
show_couple_of_images(image, output, "Original", "Equalized", color_scale)"""
