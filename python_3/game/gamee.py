import pygame

# Inisialisasi Pygame
pygame.init()

# Atur lebar dan tinggi layar
lebar_layar = 800
tinggi_layar = 600

# Buat layar
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))

# Atur judul layar
pygame.display.set_caption("Game Bola Memantul")

# Definisikan warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
merah = (255, 0, 0)

# Definisikan bola
radius_bola = 20
x_bola = lebar_layar // 2
y_bola = tinggi_layar // 2
kecepatan_bola_x = 5
kecepatan_bola_y = 5

# Definisikan raket
lebar_raket = 100
tinggi_raket = 20
x_raket = lebar_layar // 2 - lebar_raket // 2
y_raket = tinggi_layar - tinggi_raket

# Jalankan game
berjalan = True
while berjalan:
    # Periksa event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    # Kontrol raket
    tombol_ditekan = pygame.key.get_pressed()
    if tombol_ditekan[pygame.K_LEFT]:
        x_raket -= 5
    if tombol_ditekan[pygame.K_RIGHT]:
        x_raket += 5

    # Batasi pergerakan raket
    if x_raket < 0:
        x_raket = 0
    elif x_raket > lebar_layar - lebar_raket:
        x_raket = lebar_layar - lebar_raket

    # Perbarui posisi bola
    x_bola += kecepatan_bola_x
    y_bola += kecepatan_bola_y

    # Pantulkan bola dari dinding
    if x_bola < 0 or x_bola > lebar_layar:
        kecepatan_bola_x *= -1

    if y_bola < 0:
        kecepatan_bola_y *= -1

    # Pantulkan bola dari raket
    if y_bola >= tinggi_layar - tinggi_raket and x_bola >= x_raket and x_bola <= x_raket + lebar_raket:
        kecepatan_bola_y *= -1

    # Periksa skor
    if y_bola > tinggi_layar:
        y_bola = tinggi_layar // 2
        kecepatan_bola_y *= -1

    # Isi layar dengan warna hitam
    layar.fill(hitam)

    # Gambar bola
    pygame.draw.circle(layar, merah, (x_bola, y_bola), radius_bola)

    # Gambar raket
    pygame.draw.rect(layar, putih, (x_raket, y_raket, lebar_raket, tinggi_raket))

    # Perbarui layar
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
