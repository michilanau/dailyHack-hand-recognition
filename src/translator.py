from translation import translation
from classifier import classifyImage

# Array de imagenes Hello World
imagesHelloWorld = [
    'image_tests/frame_00_02_0011.png', # H
    'image_tests/frame_00_09_0018.png',

    'image_tests/frame_00_02_0011.png', # E
    'image_tests/frame_00_06_0001.png',
    
    'image_tests/frame_00_03_0001.png', # L
    'image_tests/frame_00_04_0001.png',

    'image_tests/frame_00_03_0001.png', # L
    'image_tests/frame_00_04_0001.png',

    'image_tests/frame_00_03_0001.png', # O
    'image_tests/frame_00_08_0017.png',

    'image_tests/frame_00_01_0017.png', # ' '

    'image_tests/frame_00_05_0012.png', # W
    'image_tests/frame_00_07_0010.png',

    'image_tests/frame_00_03_0001.png', # O
    'image_tests/frame_00_08_0017.png',
    
    'image_tests/frame_00_05_0010.png', # R
    'image_tests/frame_00_02_0057.png',

    'image_tests/frame_00_03_0001.png', # L
    'image_tests/frame_00_04_0001.png',

    'image_tests/frame_00_02_0005.png', # D
    'image_tests/frame_00_05_0003.png'
]

def getTextFromImages(images):

    text = ""
    index = 0

    while index < len(images):
        gesture = classifyImage(images[index])
        index += 1

        if(gesture == 'palm'):
            word = translation[gesture]
            text += word
            continue

        if(index < len(images)):
            gesture += "+" + classifyImage(images[index])
            index += 1
        else:
            break;
        
        if gesture in translation:
            word = translation[gesture]
            text += word
        else:
            print("Error: Lenguaje de imagenes incorrecto\n")
            return -1
    return text
    
#print(getTextFromImages(imagesHelloWorld))

