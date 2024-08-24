#include <iostream>

void baso(int arr[],int siji) {
    for (int i = 0; i< siji; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int sise = 4;   
    int penyimpanan[5] = {1,2,3,4,5};

    std::cout << "ini adalah hasilnya :  " << std::endl;
    baso(penyimpanan,sise);

}