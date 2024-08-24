#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
int main()
{
    int baso = 10;
    int siji = 20;

    cout << baso << siji << endl;

    swap(baso,siji);
    cout << "a " << baso << " b "  << siji << endl;

int angka;

    do {
        std::cout << "Masukkan angka antara 1 dan 10: ";
        std::cin >> angka;
    } while (angka < 1 || angka > 10); // Loop akan terus berjalan jika angka tidak berada di antara 1 dan 10

    std::cout << "Angka yang dimasukkan adalah: " << angka << std::endl;

 // Header untuk manipulasi output, seperti setw()
    clog << "ini adalah pesan saya ya " << endl;

    return 0;
    // Mencetak header tabel


    // Mencetak baris data




}