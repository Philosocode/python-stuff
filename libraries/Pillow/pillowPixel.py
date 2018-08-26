from PIL import Image
img = Image.new("RGBA", (100, 100))
for x in range(100):
    for y in range(50):
        img.putpixel((x, y), (210, 210, 210))

from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
        img.putpixel((x, y), ImageColor.getcolor("darkgray", "RGBA"))
img.save("putPixel.png")
