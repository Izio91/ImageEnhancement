from matplotlib import pyplot as plt
import cv2
import numpy as np

def read_image(path, color_scale = 'gray'):
    color_scale_dictionary = {
        "gray": cv2.IMREAD_GRAYSCALE,
        "color": cv2.IMREAD_COLOR,
        "unchanged": cv2.IMREAD_UNCHANGED
    }
    scale = color_scale_dictionary.get(color_scale)
    if(scale == None):
        scale = cv2.IMREAD_GRAYSCALE

    image = cv2.imread(path, scale)
    return image


def show_image(image):
    image = resize_with_aspect_ratio(image, 600)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def show_histogram(histogram, x_label="", y_label=""):
    plt.plot(np.arange(histogram.size), histogram)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
