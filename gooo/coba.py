from PIL import Image
from rembg import remove
image = Image.open("BBH_7601-removebg-preview-min.png")
image_without_background = remove(image)
image_without_background.save("gambar_tanpa_background.png")
