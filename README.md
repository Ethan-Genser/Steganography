# Steganography.py

Steganography.py is an entry-level steganography project by Ethan Genser. It encodes the color values for each pixel on the secret image in the last bit of the color values in the coresponding pixels on the cover image.

# Image Format
Steganography.py is based on PIL v5.0.0. As such, the program is only capable of loading images with PIL compatible file extensions. In addition, some image formats that are supported by the PIL library may not be supported by Steganography.py. Listed bellow are the currently supported file extension supported by Steganography.py (Attempt to load any file not included in the list bellow, may cause the program to not function properly or crash). A full list of the PIL library's compatible image formats can be found at http://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html.
<ul>
  <li>PNG</li>
</ul>

Note that Steganography.py will normalize the dimensions of both the cover image and hidden image before encoding. This means the resulting encoded image will have the width of the thinnest image and the height of the shortest image.

# File Summaries
<ul>
  <li><b>Implementation.py:</b> This is an example of how Steganography.py can be implemented in a project.</li>
  <li><b>Steganography.py:</b> This is the main module.</li>
</ul>
