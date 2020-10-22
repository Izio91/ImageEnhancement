from Utilities import show_image
from Utilities import read_image
from Utilities import show_histogram
from ImageEnhancement import make_image_negative
from ImageEnhancement import histogram_of_grayscale
import numpy as np
path= 'images/1577x1365.png'
image = read_image(path)
N = image.shape[0] * image.shape[1]
"""show_image(image)

show_image(make_image_negative(image))"""
histogram = histogram_of_grayscale(image)
print(histogram)
show_histogram(histogram/N, "Pixel intensity", "Pixel frequency")