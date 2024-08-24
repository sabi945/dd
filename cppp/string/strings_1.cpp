#include <iostream>
#include <string>
using namespace std;

int main()
{
    string baso = "halo siji";

    int panjang = baso.length();
    cout << panjang << endl;
    
    string sub = baso.substr(6,5);

    cout << sub << endl;

    
    return 0;
}