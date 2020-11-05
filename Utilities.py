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
    if(color_scale == 'rgb'):
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), interpolation='bicubic', vmin=0, vmax=255)
    else:
        plt.imshow(image, cmap="gray", interpolation='bicubic', vmin=0, vmax=255)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


def show_histogram(histogram, x_label="", y_label=""):
    plt.plot(np.arange(histogram.size), histogram)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
