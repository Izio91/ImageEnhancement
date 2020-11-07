from matplotlib import pyplot as plt
import cv2
import numpy as np

def read_image(path, color_scale = 'gray'):
    scale = 0
    if(color_scale == 'rgb'):
        scale = 1
    image = cv2.imread(path, scale)
    return image

def show_image(image, color_scale = 'gray'):
    image, color = adapt_image_to_color_scale(image, color_scale)
    plt.imshow(image, cmap=color, interpolation='bicubic', vmin=0, vmax=255)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def adapt_image_to_color_scale(image, color_scale):
    color = None
    if(color_scale != 'gray'):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        color = "gray"
    return image, color

def show_couple_of_images(image1, image2, title1 = None, title2 = None, color_scale = 'gray'):
    image1, color = adapt_image_to_color_scale(image1, color_scale)
    image2, color = adapt_image_to_color_scale(image2, color_scale)
    plt.subplot(121), plt.imshow(image1, cmap=color, interpolation='bicubic', vmin=0, vmax=255), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(image2, cmap=color, interpolation='bicubic', vmin=0, vmax=255), plt.title(title2)
    plt.xticks([]), plt.yticks([])
    plt.show()

def show_histogram(histogram, x_label="", y_label=""):
    plt.plot(np.arange(histogram.size), histogram)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
