#include <iostream>

int rekursif(int a) {
    if (a == 0 ) {
        return 1;
    }
    return a * rekursif(a - 1);
}
int main() {
    int pengambilan = 5;
    std::cout << "ini adalah nilai awal "<< pengambilan << " nilai rekursif "<< rekursif(pengambilan)<<"\n";
    return 0;

}