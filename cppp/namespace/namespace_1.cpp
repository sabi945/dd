namespace math
{
    int tambah(int a, int b)
    {
        return a + b;
    }
    int kali(int a, int b)
    {
        return a * b;
    }
}
namespace warna {

}
#include <iostream>
using namespace std;
using namespace math;


int main()
{
    int siji = tambah(10,10);
    cout << siji << endl;


    return 0;
}