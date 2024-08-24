import os


# pathnya = "/Users/mahdi/Desktop/pemograman/pythonProject1/libyrary os/popen.py"
# baso = os.path.getsize(pathnya)
# print(baso)
# basis = os.getgid()
# print(basis)


file_path =  "/Users/mahdi/Desktop/pemograman/pythonProject1/libyrary os/popen.py"

if os.access(file_path, os.X_OK):
    print(f"File dapat ditulisi.")
else:
    print(f"File '{file_path}' tidak dapat ditulisi atau tidak ada.")
