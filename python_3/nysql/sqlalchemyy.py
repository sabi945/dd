from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Konfigurasi database
DATABASE_URL = "mysql+mysqlconnector://root:12345678@localhost/baso"

# Membuat engine dan sesi koneksi
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Mendefinisikan model User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(100), nullable=False)

# Fungsi untuk membuat pengguna baru
def create_user(db, username: str, email: str, full_name: str):
    db_user = User(username=username, email=email, full_name=full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Fungsi utama untuk menerima input pengguna dan memasukkan data ke database
def main():
    # Membuat sesi koneksi database
    db = SessionLocal()

    # Menerima inputan pengguna
    username = input("Enter username: ")
    email = input("Enter email: ")
    full_name = input("Enter full name: ")

    # Memasukkan data ke database
    try:
        user = create_user(db, username, email, full_name)
        print(f"User created with ID: {user.id}")
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")

    # Menutup sesi koneksi
    db.close()

if __name__ == "__main__":
    # Membuat tabel jika belum ada
    Base.metadata.create_all(bind=engine)
    main()
