#include <iostream>
#include <string>

int main() {
    std::string baso = "halo";

    char akses = baso[0];

    std::cout << "karakter pertama : " << akses << std::endl;

    baso[0] = 'j';
    std::cout << baso << std::endl;
    

}