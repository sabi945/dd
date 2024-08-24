#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int rows;

    std::cout << "masukkan jumlah baaris : ";   
    std::cin >> rows;
    std::cin.ignore();

    std::string nama[rows];
    std::string ip[rows];

    for (int i = 0; i < rows; i++)
    {
        std::cout << "masukkan nama " << i + 1 << ": ";
        std::getline(std::cin, nama[i]);
        std::cout << "masukkan ip " << i + 1 << ": ";
        std::getline(std::cin, ip[i]);
    }

    std::cout << "tabel yang ada masukkan :\n";
    std::cout << std::left << std::setw(20) << "nama" << "|" << std::setw(15) << "ip" << std::endl;
    std::cout << std::setfill('-') << std::setw(20) << "-" << "|" << std::setw(15) << "-" << std::endl;
    std::cout << std::setfill(' ');

    for (int i = 0; i < rows; ++i)
    {
        std::cout << std::left << std::setw(20) << nama[i] << "|" << std::setw(15) << ip[i] << std::endl;
    }
}