# Copyright 2018 Ethan P. Genser

from PIL import Image

# Constants
BYTE_MAX = 255
COLOR_THRESHOLD = BYTE_MAX/2
RED_CHANNEL = 0
GREEN_CHANNEL = 1
BLUE_CHANNEL = 2
ALPHA_CHANEL = 3

# Returns true if number is odd, and false if number is even.
IsOdd = lambda x: bool(x % 2)

# Returns the last bit of the specified value.
getLastBit = lambda x: int(x > COLOR_THRESHOLD)

# Hides the secret image inside the original image and returns the product.
def encrypt(originalImage:Image, secretImage:Image)->Image:

    # Sets the last bit of a value equal to the specified bit.
    def setLastBit(value:int, bit)->int:
        # If the last bit is 1...
        if IsOdd(value):
            if int(bit) == 1:
                return value
            elif value + 1 > BYTE_MAX:
                return value - 1
            else:
                return value + 1
        # If the last bit is 0...
        else:
            if value + int(bit) > BYTE_MAX:
                return value - int(bit)
            else:
                return value + int(bit)

    # Returns a pixel whose last bit for each color chanel coresponds to the
    # secret image's color level.
    def encodePixel(originalPixel:tuple, secretPixel:tuple)->tuple:
        # Finds what the secret bit for each color channel should be.
        lastRedBit = getLastBit(secretPixel[RED_CHANNEL])
        lastGreenBit = getLastBit(secretPixel[GREEN_CHANNEL])
        lastBlueBit = getLastBit(secretPixel[BLUE_CHANNEL])

        # Sets the value of each color channel to end with the secret bit
        newRedValue = setLastBit(originalPixel[RED_CHANNEL], lastRedBit)
        newGreenValue = setLastBit(originalPixel[GREEN_CHANNEL], lastGreenBit)
        newBlueValue = setLastBit(originalPixel[BLUE_CHANNEL], lastBlueBit)

        return (newRedValue, newGreenValue, newBlueValue)

    imageSize = (min(originalImage.size[0], secretImage.size[0]), 
                    min(originalImage.size[1], secretImage.size[1]))
    originalImage = originalImage.resize(imageSize)
    secretImage = secretImage.resize(imageSize)
    originalData = originalImage.load()
    secretData = secretImage.load()

    # Iterates over the image's pixels, encrypting them.
    for x in range(0, imageSize[0]):
        for y in range(0, imageSize[1]):
            newPixel = encodePixel(originalData[x,y], secretData[x,y])
            originalData[x,y] = newPixel

    return originalImage

# Extracts the hidden image from an encrypted image.
def decrypt(originalImage:Image)->Image:

    # Returns either 0 or 255 depending on the last bit of the color value.
    def decodeColor(byte:int)->int:
        if IsOdd(byte):
            return BYTE_MAX
        else:
            return 0

    # Uses the secret bits from the pixel to set the decoded pixel's colors.
    def decodePixel(pixel:tuple)->tuple:
        red = decodeColor(pixel[RED_CHANNEL])
        green = decodeColor(pixel[GREEN_CHANNEL])
        blue = decodeColor(pixel[BLUE_CHANNEL])

        return (red, green, blue)

    originalData = originalImage.load()
    imageWidth = originalImage.size[0]
    imageHeight = originalImage.size[1]

    # Iterates over the image's pixels, decrypting them.
    for x in range(0,imageWidth):
        for y in range(0,imageHeight):
            newPixel = decodePixel(originalData[x,y])
            originalData[x,y] = newPixel

    return originalImage
