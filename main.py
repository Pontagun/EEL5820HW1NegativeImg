import cv2
import numpy
import numpy as np
from PIL import Image
import math

path1 = r'ot.jpg'
# path2 = r'img2.jpg'

img1 = cv2.imread(path1, 0)

img = 255 - img1

im = Image.fromarray(img)
im.save("ot_invert.jpg")

# img2 = cv2.imread(path2, 0)
#
# img = 255 - img2
#
# im = Image.fromarray(img)
# im.save("invert2.jpg")
