import mysql.connector

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="penyimpanan_file"
)
cursor = conn.cursor()

# Fungsi untuk menyimpan file
def save_file(file_path):
    with open(file_path, "rb") as file:
        binary_data = file.read()
    sql = "INSERT INTO files (name, data) VALUES (%s, %s)"
    cursor.execute(sql, (file_path, binary_data))
    conn.commit()

# Contoh penggunaan
save_file("/Users/mahdi/Desktop/pemograman/python_3/nysql/ha.pdf")

# Tutup koneksi
cursor.close()
conn.close()
