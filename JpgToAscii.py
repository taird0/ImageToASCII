from PIL import Image, ImageOps
import argparse

asciiChars = '@$%#"&"£)]!;^*"~?'

def resizeImage(jpg, newWidth):
    width, height = jpg.size
    aspectRatio = height / width

    return jpg.resize((newWidth, int(aspectRatio * newWidth)))

def main(image_path, output_path):
    with Image.open(image_path) as im:
        im = ImageOps.grayscale(im)
        
        im = resizeImage(im, 200)

        width, height = im.size 

        pixels = im.load()

        asciiString = ''
        asciiArt = []

        for y in range(height):
            for x in range(width):
                pixel_value = pixels[x, y]
                
                asciiString += asciiChars[pixel_value // len(asciiChars)]
            asciiArt.append(asciiString)
            asciiString = ''
        
    for asciiStr in asciiArt:
        print(asciiString)


    with open(output_path, 'w') as out:
        for asciiStr in asciiArt:
            out.write(asciiStr + '\n')
        
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a jpg Image to ASCII Art")
    parser.add_argument('input_image', help="Image file to be converted")
    parser.add_argument('output_path', help="Path to create text file containing art")

    args = parser.parse_args()
    main(args.input_image, args.output_path)
