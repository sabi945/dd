#include <iostream>
using namespace std;

int main() {
            const int array = 5;
            int arr[array];

            cout << "maskkan " << array << " angka" << endl;
            for (int i = 0; i < array;  ++i) {
                cout << "masukkan angka " << i + 1 << " ";
                cin >> arr[i];
            }
            
            cout << "hasil dari array \n";
            for (int i =0; i < array; ++i) {
                cout << arr[i] << " ";
            }
            cout << endl;
        
        }
