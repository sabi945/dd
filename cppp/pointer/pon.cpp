#include <iostream>
using namespace std;

int main() {
     
     int baso = 10;
    auto siji = &baso;
    *siji = 20;
    cout << baso << endl;
     
     
     return 0;
}