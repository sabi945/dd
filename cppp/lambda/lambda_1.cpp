#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
void siji(int a, int b) {
    int r = a + b;
    std::cout << r << std::endl;
}
template <class T>
T sum(T a, T b) {
    return a + b;
}
int main() {
    std::vector<int> angka = {5, 2, 8, 3, 1};
    std::sort(angka.begin(), angka.end());
    for (int num : angka) {
        std::cout << num << " ";

    }
     printf("halo kawan ku\n");

    siji(10,20);

    int baso = sum(10,20);
    cout << baso << endl;


    return 0;
}
