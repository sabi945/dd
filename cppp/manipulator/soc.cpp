#include <iostream>
#include <netdb.h>
#include <arpa/inet.h>
#include <cstring>

int main() {
    const char* hostname = "www.detik.com"; // Ganti dengan nama website yang ingin Anda cari IP-nya
    struct hostent* host = gethostbyname(hostname);

    if (host == nullptr) {
        std::cerr << "Error: Could not resolve hostname." << std::endl;
        return 1;
    }

    struct in_addr** addr_list = (struct in_addr**)host->h_addr_list;

    for(int i = 0; addr_list[i] != nullptr; i++) {
        std::cout << "IP Address: " << inet_ntoa(*addr_list[i]) << std::endl;
    }

    return 0;
}
