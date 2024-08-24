import os
import requests
from bs4 import BeautifulSoup
import random
import shutil
from urllib.parse import urlparse

# Fungsi untuk mendapatkan URL gambar acak dari Pixabay
def get_random_image_url():
    url = 'https://indonesiakaya.com/pustaka-indonesia/pegunungan-latimojong-satu-dari-tujuh-gunung-tertinggi-di-indonesia/'
    response = requests.get(url)
    response.raise_for_status()  # Menambahkan penanganan error untuk respons HTTP
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    if not images:
        raise ValueError("Tidak ada gambar yang ditemukan pada halaman web")
    random_image = random.choice(images)
    image_url = random_image['src']
    return image_url

# Fungsi untuk menyimpan gambar ke dalam folder Documents
def save_image_to_documents(image_url):
    response = requests.get(image_url, stream=True)
    response.raise_for_status()  # Menambahkan penanganan error untuk respons HTTP
    if response.headers.get('Content-Length') == '0':
        raise ValueError("Ukuran gambar tidak valid atau gambar tidak berhasil diunduh")
    
    # Mendapatkan nama file dan format dari URL gambar
    parsed_url = urlparse(image_url)
    image_name = os.path.basename(parsed_url.path)
    image_format = os.path.splitext(image_name)[1]
    
    # Menyimpan gambar dengan nama dan format yang sama




    documents_path = os.path.expanduser("~/Documents/baso")
    image_path = os.path.join(documents_path, image_name)
    with open(image_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

try:
    # Mendapatkan URL gambar acak
    random_image_url = get_random_image_url()

    # Menyimpan gambar ke dalam folder Documents dengan nama dan format yang sama
    save_image_to_documents(random_image_url)

    print("Gambar acak telah disimpan di dalam folder Documents.")
except ValueError as e:
    print("Terjadi kesalahan:", e)
except Exception as e:
    print("Terjadi kesalahan yang tidak diketahui:", e)
