#include <iostream>
#include <memory>
using namespace std;

int main()
{
    unique_ptr<int> ptr = make_unique<int>(40);

    cout << *ptr << " ini adalah hasilnya " << endl;
    return 0;
}