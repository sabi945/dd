import pygame
import av

# Inisialisasi Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PyAV Kamera dengan Menu")

# Membuka kamera
container = av.open("0", format="dshow", options={'video_size': '640x480'})

# Fungsi untuk menampilkan menu
def draw_menu(screen):
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 640, 50))  # Latar belakang menu
    font = pygame.font.Font(None, 36)
    text = font.render('Tekan "q" untuk keluar', True, (0, 0, 0))
    screen.blit(text, (10, 10))

running = True
while running:
    for frame in container.decode(video=0):
        # Mengonversi frame ke format yang dapat digunakan Pygame
        image = frame.to_image()
        mode = image.mode
        size = image.size
        data = image.tobytes()

        # Membuat surface Pygame dari frame
        frame_surface = pygame.image.fromstring(data, size, mode)

        # Menampilkan frame di window
        screen.blit(frame_surface, (0, 50))

        # Menambahkan menu ke frame
        draw_menu(screen)

        # Memperbarui display
        pygame.display.flip()

        # Mengambil event Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
          
