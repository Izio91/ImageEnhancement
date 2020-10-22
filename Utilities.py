from matplotlib import pyplot as plt
import cv2
import numpy as np

def read_image(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return image


def show_image(image):
    plt.imshow(image, cmap='gray', interpolation='bicubic', vmin=0, vmax=255)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def show_histogram(histogram, x_label="", y_label=""):
    plt.plot(np.arange(histogram.size), histogram)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
