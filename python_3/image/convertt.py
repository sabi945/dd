from PIL import Image

path_nya = Image.open("/Users/mahdi/Desktop/pemograman/python_3/image/baso.png")

hasil = path_nya.convert("1")


hasil.save("a.png")
