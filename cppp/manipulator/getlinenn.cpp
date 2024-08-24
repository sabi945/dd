#include <iostream>
#include <cstdlib>

int main() {
    // Contoh perintah Nmap untuk memindai jaringan
    std::string command = "nmap -sP 203.190.242.211 /24";
    
    // Memanggil perintah Nmap dari C++
    int result = system(command.c_str());

    if (result != 0) {
        std::cerr << "Perintah Nmap gagal dijalankan." << std::endl;
    } else {
        std::cout << "Perintah Nmap berhasil dijalankan." << std::endl;
    }

    return 0;
}
