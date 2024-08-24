#include <iostream>

int menghitungLuas(int panjang, int luas ) {
    return panjang * luas;
}

int main() {
    int panjang, lebar;
    std::cout << "masukkan panjangnya : ";
    std::cin >> panjang;
    std::cout << "masukkan lebar : ";
    std::cin >> lebar;

    int hasil = menghitungLuas(panjang, lebar);
    std::cout << "hasilnya adalah : " << hasil << std::endl;

}

