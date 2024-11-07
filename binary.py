import random
import PIL
import PIL.Image

with open("binary.txt", "r") as binary:
    binary_text = binary.read()
    
binary_pos = -1

REDUCTION_FACTOR = 0.8

img = PIL.Image.open("crow2.png")

img = img.resize((img.width, int(img.height/2)))
img.thumbnail((
    int(img.width * REDUCTION_FACTOR),
    int(img.height * REDUCTION_FACTOR)
))

output = []

def get_output(pixel):
    global binary_pos
    if pixel[3] >= 125:
        binary_pos += 1
        if binary_pos >= len(binary_text):
            binary_pos = 0
        return binary_text[binary_pos]
    return " "

for y in range(0, img.height):
    
    characters = []
    
    for x in range(0, img.width):
        character = get_output(img.getpixel((x, y)))
        characters.append(character)
    
    output.append(characters)

for row in output:
    print("".join(row))