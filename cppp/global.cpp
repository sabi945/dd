#include <iostream>
#include <thread>
#include <vector>
#include <atomic>
#include <chrono>
#include <signal.h>

using namespace std;

atomic<bool> keepRunning(true);

void signal_handler(int signal) {
    if (signal == SIGINT) {
        cout << "SIGINT diterima. Menyelesaikan program..." << endl;
        keepRunning = false;
    }
}

void heavy_computation() {
    while (keepRunning) {
        // Tugas berat yang akan memaksimalkan penggunaan CPU
        volatile double x = 0.0;
        for (int i = 0; i < 1000000; ++i) {
            x += i * i;
        }
    }
}

int main() {
    // Menangani sinyal SIGINT (Command + C)
    signal(SIGINT, signal_handler);

    // Dapatkan jumlah core CPU.
    unsigned int numCores = thread::hardware_concurrency();

    // Cetak jumlah core.
    cout << "Jumlah Core: " << numCores << endl;

    // Buat thread sebanyak jumlah core CPU.
    vector<thread> threads;
    for (unsigned int i = 0; i < numCores; ++i) {
        threads.push_back(thread(heavy_computation));
    }

    // Tunggu sinyal untuk keluar
    while (keepRunning) {
        this_thread::sleep_for(chrono::seconds(1)); // Istirahat sejenak
    }

    // Hentikan semua thread
    for (auto& t : threads) {
        t.join();
    }

    return 0;
}



