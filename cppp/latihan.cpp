#include <iostream>

int main() {
    int x;
    int s1 = 0; // Jumlah bilangan ganjil
    int s2 = 0; // Jumlah bilangan genap

    std::cout << "Masukkan sebuah angka bulat (x): ";
    std::cin >> x;

    // Menghitung s1 dan s2
    for (int i = 0; i <= x; ++i) {
        if (i % 2 == 0) { // Bilangan genap
            s2 += i;
        } else { // Bilangan ganjil
            s1 += i;
        }
    }

    // Menampilkan bilangan ganjil dan nilai s1
    std::cout << "Bilangan ganjil antara 0 dan " << x << " adalah: ";
    for (int i = 1; i <= x; i += 2) {
        std::cout << i << " ";
    }
    std::cout << "\nNilai s1: " << s1 << std::endl;

    // Menampilkan bilangan genap dan nilai s2
    std::cout << "Bilangan genap antara 0 dan " << x << " adalah: ";
    for (int i = 0; i <= x; i += 2) {
        std::cout << i << " ";
    }
    std::cout << "\nNilai s2: " << s2 << std::endl;

    return 0;
}
