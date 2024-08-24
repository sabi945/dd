import ssl
import urllib.request

# Lokasi file cacert.pem yang telah Anda unduh
cacert_path = '/Users/mahdi/Desktop/pemograman/pp/cacert.pem'

# Buat konteks SSL yang menggunakan cacert.pem
ssl_context = ssl.create_default_context(cafile=cacert_path)

# Contoh permintaan HTTPS menggunakan konteks SSL yang baru
url = 'https://www.wikipedia.org'

try:
    print("Opening URL")
    with urllib.request.urlopen(url, context=ssl_context) as response:
        print("Response opened")
        html = response.read()
        print("Read HTML")
        print(html)
except Exception as e:
    print(f"An error occurred: {e}")
