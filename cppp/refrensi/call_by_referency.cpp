#include <iostream>
using namespace std;
int basow = 10;
void umpan(int &baso) {
    basow = 19;
}
int main() {
    umpan(basow);
 cout << "hasil dari umpan " <<  basow << endl;
}   