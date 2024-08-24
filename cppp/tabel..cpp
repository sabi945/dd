#include <iostream>
#include <iomanip> // Untuk manipulator setw

int main() {
    int rows;

    // Meminta pengguna untuk memasukkan jumlah baris tabel
    std::cout << "Masukkan jumlah baris tabel: ";
    std::cin >> rows;

    // Membersihkan input buffer
    std::cin.ignore();

    // Membuat tabel untuk menyimpan data
    std::string nama[rows];
    std::string ip[rows];

    // Meminta pengguna untuk memasukkan data untuk setiap baris tabel
    for (int i = 0; i < rows; ++i) {
        std::cout << "Masukkan Nama untuk baris " << i + 1 << ": ";
        std::getline(std::cin, nama[i]);
        std::cout << "Masukkan IP untuk baris " << i + 1 << ": ";
        std::getline(std::cin, ip[i]);
    } 

    // Menampilkan tabel dengan judul kolom "Nama" dan "IP"
    std::cout << "\nTabel yang dimasukkan:\n";
    std::cout << std::left << std::setw(20) << "Nama" << " | " << std::setw(15) << "IP" << std::endl;
    std::cout << std::setfill('-') << std::setw(20) << "-" << " | " << std::setw(15) << "-" << std::endl;
    std::cout << std::setfill(' ');

    for (int i = 0; i < rows; ++i) {
        std::cout << std::left << std::setw(20) << nama[i] << " | " << std::setw(15) << ip[i] << std::endl;
    }

    return 0;
}
