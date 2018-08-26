from PIL import Image
catImg = Image.open('zophie.jpg')
width, height = catImg.size
svelteImg = catImg.resize((width, height + 300))
svelteImg.save("svelte.png")
