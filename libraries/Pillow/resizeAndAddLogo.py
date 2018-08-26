#! python3
# resizeAndAddLogo.py - Resizes all images in CWD to fit in a 300x300 square
# and adds catlogo.png to the lower-right corner
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"

logoImg = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoImg.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all the files in the CWD
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('jpg')) \
       or filename == LOGO_FILENAME:
        continue  # Skip non-image files and the logo file itself

    img = Image.open(filename)
    width, height = img.size

    # Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image
        print("Resizing %s..." % (filename))
        img = img.resize((width, height))

        # Add Logo
        print("Adding the logo to %s..." % (filename))
        img.paste(logoImg, (width - logoWidth, height - logoHeight), logoImg)

        # Save Changes
        img.save(os.path.join("withLogo", filename))
