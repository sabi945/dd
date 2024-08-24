#include <iostream>

int main() {
    int dvinisi = 0;
    int baso =10;

    if(dvinisi == 0){
        std::cerr << "EROR:nol tidak bisa di bagikan" << std::endl;
        return 1;
    }

    int hasil = dvinisi / baso;
    std::cout << "hasil pembagian " << hasil << std::endl; 
    return 0;
}