#include <iostream>

void baso(int arr[],int bass) {
    for (int i = 0; i < bass; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}
void doubleArray(int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        arr[i] *= 2;
    }
}

int main() {
    const int sise = 5;
    int penyimpanan[sise] =  {1,2,3,4,5};

    std::cout << "panggilana awal " << std::endl;
    baso(penyimpanan, sise);

    doubleArray(penyimpanan, sise);

    std::cout << "setelah array " << std::endl;
    baso(penyimpanan,sise);

}