#include <iostream>

int& getReference() {
    static int x = 5;
    static int y = 10;
    static int result = x + y; // Menambahkan kedua variabel
    return result; // Mengembalikan referensi ke hasil penambahan
}

int main() {
    int& ref = getReference(); // Mendapatkan referensi ke hasil penambahan dari fungsi
    std::cout << "Nilai sebelum diubah: " << ref << std::endl; // Akan mencetak hasil penambahan
    ref = 20; // Mengubah nilai hasil penambahan melalui referensi ref
    std::cout << "Nilai setelah diubah: " << ref << std::endl; // Akan mencetak nilai yang telah diubah
    return 0;
}
