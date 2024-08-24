#include <iostream>

int main() {
    // Membuat lambda yang tidak memiliki parameter
    auto sayHello = []() {
        std::cout << "Hello, World!" << std::endl;
    };

    // Memanggil lambda untuk menampilkan pesan
    sayHello();

    // Membuat lambda dengan satu parameter
    auto square = [](int x) {
        return x * x;
    };

    // Memanggil lambda untuk menghitung kuadrat dari 5
    int result = square(5);
    std::cout << "Square of 5 is: " << result << std::endl;

    return 0;
}
