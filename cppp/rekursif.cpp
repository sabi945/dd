#include <iostream>

inline int baso(int n) {
    if (n == 0 ) {
        return 1;
    }
    else {
        return n * baso(n - 1);
    }

}
int main() {
    int pembungkus = 5;
    std::cout << "nilai dari factorial " << pembungkus << " adalah " << baso(pembungkus) << std::endl;
}
