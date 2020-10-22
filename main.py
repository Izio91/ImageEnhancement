from Utilities import show_image
from Utilities import read_image
from ImageEnhancement import make_image_negative

path= 'images/1577x1365.png'
image = read_image(path)
show_image(image)

show_image(make_image_negative(image))