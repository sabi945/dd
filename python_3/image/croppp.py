from PIL import Image

baso = Image.open("/Users/mahdi/Desktop/pemograman/python_3/image/baso.png")

drop = (100,110,200,250)
hasil = baso.crop(drop)

hasil.show()