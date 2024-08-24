#include <mysqlx/xdevapi.h>
#include <iostream>

using namespace std;
using namespace mysqlx;

int main() {
    try {
        // Buat koneksi ke database
        Session sess("localhost", 33060, "root", "1234567");
        Schema db = sess.getSchema("mahdi");
        
        // Input data ke tabel produk
        Table produkTable = db.getTable("produk");
        RowResult result = produkTable.insert("id", "nama").values(1, "Produk A").execute();
        
        cout << "Data telah dimasukkan ke tabel produk." << endl;
        
    } catch (const mysqlx::Error &e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }
    
    return 0;
}
