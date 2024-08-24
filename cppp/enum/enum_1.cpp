#include <iostream>

enum class Days {
    SUNDAY,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY
};

int main() {
    Days today = Days::MONDAY;

    // Menggunakan switch untuk memproses nilai enum

    // Penugasan nilai enum ke nilai yang tidak valid
    today = Days::SUNDAY; // Ini benar
    switch (today) {
        case Days::FRIDAY:
            std::cout << "Hari ini adalah Minggu." << std::endl;
            break;
        case Days::SUNDAY:
            std::cout << "Hari ini adalah Senin." << std::endl;
            break;
        default:
            std::cout << "ini hasilnya salah ya" << std::endl;
        // Kasus lainnya...
    }
    // today = 5; // Ini akan menyebabkan kesalahan kompilasi karena Days::FRIDAY bukanlah integer
    return 0;
}
