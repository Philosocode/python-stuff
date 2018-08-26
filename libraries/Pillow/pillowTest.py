from PIL import Image
catImg = Image.open('zophie.png')
print(catImg.size)
print(catImg.filename)
print(catImg.format)
print(catImg.format_description)
catImg.save("zophie.jpg")
