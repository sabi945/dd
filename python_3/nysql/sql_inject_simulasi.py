import mysql.connector

def get_user_password(username):
    try:
        # Membuat koneksi ke database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="mahdi"
        )

        # Membuat kursor
        cursor = conn.cursor()

        # Membuat query SQL dengan menggunakan parameterized query
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))  # Menggunakan tupel untuk nilai parameter

        # Mendapatkan hasil query
        result = cursor.fetchone()
        
        if result:
            return result[0]  # Mengembalikan password
        else:
            return "User tidak ditemukan."

    except Exception as e:
        print("Error:", e)

    finally:
        # Menutup kursor dan koneksi
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Contoh penggunaan
username = input("Masukkan nama pengguna: ")
password = get_user_password(username)
print("Password:", password)
