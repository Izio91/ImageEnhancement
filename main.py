from Utilities import show_image
from Utilities import read_image
from Utilities import show_histogram
from Utilities import show_couple_of_images
from ImageEnhancement import make_image_negative
from ImageEnhancement import histogram_of_grayscale
import numpy as np
path= 'images/1577x1365.png'
path= 'images/745x419.jpg'
#path= 'images/columbia.jpg'
color_scale = "rgb"
image = read_image(path, color_scale)

N = image.shape[0] * image.shape[1]

#show_image(make_image_negative(image), color_scale)
show_couple_of_images(image, make_image_negative(image), "Original", "Negative", "rgb")
"""histogram = histogram_of_grayscale(image)
print(histogram)
show_histogram(histogram/N, "Pixel intensity", "Pixel frequency")"""