#include <iostream>
using namespace std;
void pengulagan(int arr[], int siji) {
    for (int a = 0;a < siji; ++a) {
        cout << arr[a] << " ";
    }
    cout << endl;
}

int main()
{

    int satu = 4;
    int pemersatu[5] = {1,2,3,4,5};

    pengulagan(pemersatu,satu);



    return 0;

}