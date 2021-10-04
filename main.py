import cv2
from PIL import Image
path1 = r'ot.jpg'
img1 = cv2.imread(path1, 0)
img = 255 - img1
im = Image.fromarray(img)
im.save("ot_invert.jpg")

