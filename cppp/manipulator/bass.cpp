#include <iostream>
using namespace std;

int factorial(int n) {
    if (n <= 1) // Basis rekursi
        return 1;
    else
        return n * factorial(n - 1); // Panggilan rekursif
}

int main() {
    int result = factorial(5); // Memanggil fungsi
    cout << "Factorial of 5: " << result << endl;
    return 0;
}
