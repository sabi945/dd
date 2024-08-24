import cv2

# Fungsi utama untuk membuka kamera dan menampilkan outputnya
def open_camera():
    # Membuka koneksi ke kamera (biasanya 0 untuk kamera bawaan)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Tidak dapat membuka kamera.")
        return

    while True:
        # Membaca frame dari kamera
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Tidak dapat membaca frame dari kamera.")
            break

        # Menampilkan frame di jendela 'Camera'
        cv2.imshow('Camera', frame)

        # Keluar dari loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Melepaskan objek capture dan menutup semua jendela OpenCV
    cap.release()
    cv2.destroyAllWindows()

# Memanggil fungsi untuk membuka kamera
open_camera()
