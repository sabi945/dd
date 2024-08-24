#include <iostream>
#include <vector>
#include <algorithm>

class ComplexNumber {
private:
    double real;
    double imaginary;
public:
    ComplexNumber(double r, double i) : real(r), imaginary(i) {}

    ComplexNumber operator+(const ComplexNumber& other) const {
        return ComplexNumber(real + other.real, imaginary + other.imaginary);
    }

    ComplexNumber operator*(const ComplexNumber& other) const {
        return ComplexNumber(real * other.real - imaginary * other.imaginary,
                             real * other.imaginary + imaginary * other.real);
    }

    friend std::ostream& operator<<(std::ostream& out, const ComplexNumber& complex) {
        out << complex.real << " + " << complex.imaginary << "i";
        return out;
    }
};

int main() {
    std::vector<ComplexNumber> complexNumbers;
    complexNumbers.push_back(ComplexNumber(1.0, 2.0));
    complexNumbers.push_back(ComplexNumber(3.0, 4.0));
    complexNumbers.push_back(ComplexNumber(5.0, 6.0));

    // Menjumlahkan semua bilangan kompleks
    ComplexNumber sum = std::accumulate(complexNumbers.begin(), complexNumbers.end(), ComplexNumber(0.0, 0.0));
    std::cout << "Jumlah semua bilangan kompleks: " << sum << std::endl;

    // Mengalikan semua bilangan kompleks
    ComplexNumber product = std::accumulate(complexNumbers.begin(), complexNumbers.end(), ComplexNumber(1.0, 0.0),
                                            [](const ComplexNumber& a, const ComplexNumber& b) { return a * b; });
    std::cout << "Perkalian semua bilangan kompleks: " << product << std::endl;

    return 0;
}
