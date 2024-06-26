from PIL import Image, ImageOps
import numpy as np

asciiChars = '!"£$%^&*)]#~;@?'

def resizeImage(jpg, newWidth):
    width, height = jpg.size
    aspectRatio = height / width

    return jpg.resize((newWidth, int(aspectRatio * newWidth)))

# imColour = Image.open('unionj.jpg')
# imGrey = ImageOps.grayscale(imColour)

# imGrey.show()

# imGreySmall = resizeImage(imGrey, 200)

# imGreySmall.show()



with Image.open('unionj.jpg') as im:
    Image.ImageOps.greyscale(im)

    im = resizeImage(im, 200)
