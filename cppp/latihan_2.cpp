#include <iostream>

int main() {
    double bilangan1, bilangan2;
    char operasi, lanjut;

    do {
        std::cout << "Masukkan operasi yang diinginkan (+, -, *, /): ";
        std::cin >> operasi;
        std::cout << "Masukkan dua bilangan: ";
        std::cin >> bilangan1 >> bilangan2;
        

        switch (operasi) {
            case '+':
                std::cout << "Hasil: " << bilangan1 << " + " << bilangan2 << " = " << bilangan1 + bilangan2 << std::endl;
                break;
            case '-':
                std::cout << "Hasil: " << bilangan1 << " - " << bilangan2 << " = " << bilangan1 - bilangan2 << std::endl;
                break;
            case '*':
                std::cout << "Hasil: " << bilangan1 << " * " << bilangan2 << " = " << bilangan1 * bilangan2 << std::endl;
                break;
            case '/':
                if (bilangan2 != 0) {
                    std::cout << "Hasil: " << bilangan1 << " / " << bilangan2 << " = " << bilangan1 / bilangan2 << std::endl;
                } else {
                    std::cout << "Error: Pembagian dengan nol." << std::endl;
                }
                break;
            default:
                std::cout << "Operasi tidak dikenali." << std::endl;
        }

        std::cout << "Apakah Anda ingin melakukan operasi lain? (y/n): ";
        std::cin >> lanjut;
    } while (lanjut == 'y' || lanjut == 'Y');

    return 0;

}