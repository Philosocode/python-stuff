from PIL import Image
import os

size_300 = (300, 300)

for file in os.listdir('.'):
    if file.endswith('.jpg'):
        i = Image.open(file)
        filename, fileext = os.path.splittext(file)

        i.thumbnail(size_300)
        file.save('300/{}_300{}'.format(filename, fileext))

#  image1 = Image.open('putPixel.png')
#  image1.show()
