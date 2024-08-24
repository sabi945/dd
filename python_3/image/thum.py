# from PIL import Image


# path_nya = Image.open("/Users/mahdi/Desktop/pemograman/python_3/image/mahdi.png")

# thumbnail = (100,100)
# path_nya.thumbnail(thumbnail)
# path_nya.save("/Users/mahdi/Desktop/pemograman/python_3/image/basi.png")

from PIL import Image, ImageFilter

# Membaca gambar
image = Image.open('/Users/mahdi/Desktop/pemograman/python_3/image/basi.png')

# Memperjelas gambar dengan filter sharpen
sharpened_image = image.filter(ImageFilter.SHARPEN)

# Menyimpan gambar yang telah dipertajam
sharpened_image.save('/Users/mahdi/Desktop/pemograman/python_3/image/hama.png')
