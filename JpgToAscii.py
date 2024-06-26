from PIL import Image, ImageOps
import numpy as np

asciiChars = '@$%#"&"£)]!;^*"~?'

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
    im = ImageOps.grayscale(im)
    
    im = resizeImage(im, 20)

    width, height = im.size 

    pixels = im.load()

    asciiString = ''
    asciiArt = []

    for y in range(height):
        for x in range(width):
            pixel_value = pixels[x, y]
            
            asciiString += asciiChars[pixel_value // 17]
        asciiArt.append(asciiString)
    
for asciiStr in asciiArt:
    print(asciiString)


with open('unionj.txt', 'w') as out:
    for asciiStr in asciiArt:
        out.write(asciiStr + '\n')
    
    
