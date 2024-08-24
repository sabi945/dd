#include <iostream>
#include <string>

int main() {
    std::string str = "Jika Anda menggunakan";
    str.reserve(50);
    std::cout << "Kapasitas: " << str.capacity() << std::endl;
    return 0;
}
