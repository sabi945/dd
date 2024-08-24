#include <iostream>

struct Mahasiswa {
    std::string nama;
    std::string baso;
    int umur;
};

int main() {
    Mahasiswa baso;
    baso.nama = "halo semuanya";
    baso.umur = 18;
    baso.baso = "halo semuanya";

    std::cout << baso.nama << std::endl;
    return 0;
     
}