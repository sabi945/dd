import os
import stat


# penggunaan UF_IMMUTABLE dan untuk non IMMUTABLE
"""
inputan = str(input("masukkan inputan : "))

if inputan == "imun":
    pathss = '/Users/mahdi/Desktop/pemograman/pythonProject1/libyrary os/walkk.py'
    baso = os.chflags(pathss, stat.UF_IMMUTABLE)
    print("berhasil")
else:
    print("masukkan input yang benar")

# untuk menghapus immutable
if inputan == "immutable":
    file_path = '/Users/mahdi/Desktop/pemograman/pythonProject1/libyrary os/walkk.py'
    try:
        # Menghapus bendera UF_IMMUTABLE pada file
        os.chflags(file_path, ~stat.UF_IMMUTABLE & os.stat(file_path).st_flags)
        print("Bendera UF_IMMUTABLE berhasil dihapus.")
    except PermissionError:
        print("Tidak memiliki izin untuk menghapus bendera UF_IMMUTABLE.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
"""

# pathh = "/Users/mahdi/Desktop/pemograman/pythonProject1/libyrary os/stat.py"

# baso = os.chflags(pathh, stat.UF_NOUNLINK)
# print(baso)
"""
source_path = "/Users/mahdi/Desktop/pemograman/pythonProject1/lambdaa/lambdaa_1.py"
symlink_path = "/Users/mahdi/Desktop/pemograman/pythonProject1/lambdaa/lambda__1.py"

try:
    os.symlink(source_path, symlink_path, target_is_directory=False, dir_fd=None)
    print(f"Symlink created successfully at {symlink_path}.")
except OSError as e:
    print(f"Error creating symlink: {e}")
"""

path_string = "/Users/mahdi/Desktop/pemograman/pythonProject1/lambdaa/lambdaa_1.py"
converted_path = os.fspath(path_string)
print(f"Converted path (string): {converted_path}")