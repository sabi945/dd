#include <iostream>
#include <iomanip> // Include library untuk manipulator setw

int main() {
    int rows, cols;     

    // Meminta pengguna untuk memasukkan jumlah baris dan kolom tabel
    std::cout << "Masukkan jumlah baris: ";
    std::cin >> rows;
    std::cout << "Masukkan jumlah kolom: ";
    std::cin >> cols;

    // Meminta pengguna untuk memasukkan nilai untuk setiap sel tabel
    int table[rows][cols];
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            std::cout << "Masukkan nilai untuk baris " << i + 1 << ", kolom " << j + 1 << ": ";
            std::cin >> table[i][j];
        }
    }

    // Menampilkan tabel
    std::cout << "\nTabel yang dimasukkan:\n";
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            // Menampilkan nilai dari setiap sel tabel dengan lebar yang sama
            std::cout << std::setw(5) << table[i][j];
        }
        std::cout << std::endl; // Pindah ke baris berikutnya setelah selesai mencetak baris
    }

    return 0;
}
