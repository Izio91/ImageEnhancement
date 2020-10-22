from matplotlib import pyplot as plt
import cv2

def read_image(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return image


def show_image(image):
    plt.imshow(image, cmap='gray', interpolation='bicubic', vmin=0, vmax=255)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
