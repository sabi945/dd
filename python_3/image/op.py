from PIL import Image
import numpy as np

# Persiapkan larik NumPy (misalnya, gambar 100x100 piksel dengan saluran RGB)
width, height = 100, 100
rgb_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)  # Data piksel acak untuk contoh

# Buat gambar dari larik NumPy
image = Image.fromarray(rgb_data)

# Tampilkan gambar
image.show()

# Atau simpan gambar ke file

