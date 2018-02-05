from PIL import Image

# Constants
IMAGE_WIDTH = 800
IMAGE_HEIGHT = 400
IMAGE_SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)
BYTE_MAX = 255
COLOR_THRESHOLD = BYTE_MAX/2
RED_CHANNEL = 0
GREEN_CHANNEL = 1
BLUE_CHANNEL = 2
ALPHA_CHANEL = 3


# The main entry point for the program
def main():

    # User sets the mode to either encypt an image or decrypt a previously encypted image.
    mode = ''
    while XNOR(mode != 'encrypt', mode != 'decrypt'):
        mode = input('Would you like to encrypt or decrypt an image? ')

    # Loading the original image from a user-defined directory path.
    originalDir = input('What image would you like to ' + mode + '? ')
    try:
        originalImage = Image.open(originalDir)
    except:
        raise Exception('Image could not be loaded at the specified file directory.')

    # Begins the encyption process.
    if mode == 'encrypt':

        # Loading secret image for encryption.
        secretDir = input('What image would you like to hide inside `' + originalDir + '`? ')
        try:
            secretImage = Image.open(secretDir)
        except:
            raise Exception('Image could not be loaded at the specified file directory.')

        encryptedImage = encrypt(originalImage, secretImage)
        encryptedImage.save("C:/Users/Ethans Laptop/Desktop/Encrypted_Image.png")

    # Begins the decryption process.
    elif mode == 'decrypt':
        decryptedImage = decrypt(originalImage)
        decryptedImage.save("C:/Users/Ethans Laptop/Desktop/Decrypted_Image.png")

# Functions as the basic XNOR logic gate.
def XNOR(leftSide, rightSide):
    if leftSide == True and rightSide == True:
        return True
    elif leftSide == False and rightSide == True:
        return False
    elif leftSide == True and rightSide == False:
        return False
    else:
        return True

# Returns true if number is odd, and false if number is even.
IsOdd = lambda x: bool(x % 2)

# Returns the last bit of the specified value
getLastBit = lambda x: int(x > COLOR_THRESHOLD)

# Hides the secret image inside the original image and returns the product.
def encrypt(originalImage, secretImage):

    # Sets the last bit of a value equal to the specified bit
    def setLastBit(value, bit):
        if IsOdd(value):
            if bit == 1:
                return value;
            elif value + 1 > BYTE_MAX:
                return value - 1;
            else:
                return value + 1;
        else:
            if value + bit > 255:
                return value - bit;
            else:
                return value + bit;

    # Returns a pixel whose last bit for each color chanel coresponds to the secret image's color level
    def encodePixel(originalPixel, secretPixel):
        lastRedBit = getLastBit(secretPixel[RED_CHANNEL])
        lastGreenBit = getLastBit(secretPixel[GREEN_CHANNEL])
        lastBlueBit = getLastBit(secretPixel[BLUE_CHANNEL])

        newRedValue = setLastBit(originalPixel[RED_CHANNEL], lastRedBit)
        newGreenValue = setLastBit(originalPixel[GREEN_CHANNEL], lastGreenBit)
        newBlueValue = setLastBit(originalPixel[BLUE_CHANNEL], lastBlueBit)

        return (newRedValue, newGreenValue, newBlueValue)

    originalImage = originalImage.resize(IMAGE_SIZE)
    secretImage = secretImage.resize(IMAGE_SIZE)
    originalData = originalImage.load()
    secretData = secretImage.load()

    for x in range(0, IMAGE_WIDTH):
        for y in range(0, IMAGE_HEIGHT):
            newPixel = encodePixel(originalData[x,y], secretData[x,y])
            originalData[x,y] = newPixel

    return originalImage

# Extracts the hidden image from an encrypted image.
def decrypt(originalImage):

    # Returns either 0 or byte.maxValue depending on the last bit of the color value
    def decodeColor(byte):
        if IsOdd(byte):
            return BYTE_MAX
        else:
            return 0

    def decodePixel(pixel):
        red = decodeColor(pixel[RED_CHANNEL])
        green = decodeColor(pixel[GREEN_CHANNEL])
        blue = decodeColor(pixel[BLUE_CHANNEL])

        return (red, green, blue)

    originalData = originalImage.load()
    imageWidth = originalImage.size[0]
    imageHeight = originalImage.size[1]

    for x in range(0,imageWidth):
        for y in range(0,imageHeight):
            newPixel = decodePixel(originalData[x,y])
            originalData[x,y] = newPixel

    return originalImage

# Calls main function
main()