#include <iostream>
#include <iomanip> // Header untuk manipulasi output, seperti setw()

int main() {
    // Mencetak header tabel
    std::cout << std::setw(10) << "Nama" << std::setw(10) << "Usia" << std::setw(10) << "Kota" << std::endl;
    std::cout << std::setw(10) << "--------" << std::setw(9) << "--------" << std::setw(10) << "--------" << std::endl;

    // Mencetak baris data
    std::cout << std::setw(10) << "John" << std::setw(10) << "30" << std::setw(10) << "New York" << std::endl;
    std::cout << std::setw(10) << "Alice" << std::setw(10) << "25" << std::setw(10) << "London" << std::endl;
    std::cout << std::setw(10) << "Bob" << std::setw(10) << "40" << std::setw(10) << "Paris" << std::endl;


 std::cout << std::setw(13) << std::left << "Kanan" <<  std::setw(10) << std::left << "baso" << std::endl;
    std::cout << std::setw(10) << std::left << "----------" << std::endl;
    return 0;
}
