from PIL import Image, ImageDraw, ImageFont

# Membaca gambar
image = Image.open('/Users/mahdi/Desktop/pemograman/python_3/image/mahdi.png')

# Membuat objek draw
draw = ImageDraw.Draw(image)

# Menentukan path lengkap ke font di MacOS
font_path = '/Library/Fonts/Arial.ttf'  # Path font di MacOS
# Anda bisa menyesuaikan path ini jika font berada di lokasi yang berbeda, misalnya:
# font_path = '/System/Library/Fonts/Helvetica.ttc'
# atau font_path = '~/Library/Fonts/custom_font.ttf'

# Menentukan font dan ukuran
font = ImageFont.truetype(font_path, size=45)

# Menentukan posisi dan teks
position = (100, 100)
text = "Hello, World!"

# Menambahkan teks ke gambar
draw.text(position, text, fill="white", font=font)

# Menyimpan gambar
image.save('/Users/mahdi/Desktop/pemograman/python_3/image/bass.png')
