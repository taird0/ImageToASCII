from PIL import Image, ImageOps 
import numpy as np

imColour = Image.open('unionj.jpg')
imGrey = ImageOps.grayscale(imColour)

imGrey.show()

with Image.open('unionj.jpg') as im:
    Image.ImageOps.greyscale(im)