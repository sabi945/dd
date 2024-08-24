#include <iostream>
using namespace std;

int main() {
    
    char hasil;
    int nilai_1;
    int nilai_2;
    cout << "masukkan keywoard : ";
    cin >> hasil;
    cout << "masukkan nilai pertama : ";
    cin >> nilai_1;
    cout << "masukkan nilai kedua : ";
    cin >> nilai_2;

    switch (hasil)
    {
        case '*':
            cout << nilai_1 * nilai_2 << endl;
    }
    
    
    
    return 0;
}