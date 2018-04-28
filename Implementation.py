# Copyright 2018 Ethan P. Genser
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PIL import Image
import Steganography as sg

# Functions as the basic XNOR logic gate.
def XNOR(leftSide, rightSide):
    if bool(leftSide) == True and bool(rightSide) == True:
        return True
    elif bool(leftSide) == False and bool(rightSide) == True:
        return False
    elif bool(leftSide) == True and bool(rightSide) == False:
        return False
    else:
        return True

# The main entry point for the program
def main():

    # User sets the mode to either encypt an image or decrypt a previously
	# encypted image.
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

        # Creates encrypted image.
        print("\nProcessing...\n")
        encryptedImage = sg.encrypt(originalImage, secretImage)
        encryptedImage.save('Encrypted_Image.png')

    # Begins the decryption process.
    elif mode == 'decrypt':
        # Creates decrypted image.
        print("\nProcessing...\n")
        decryptedImage = sg.decrypt(originalImage)
        decryptedImage.save("Decrypted_Image.png")

    print(mode + 'ion was completed successfully!\n')

# Calls main function
if __name__=='__main__':main()
