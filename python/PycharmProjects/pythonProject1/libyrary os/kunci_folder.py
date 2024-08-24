
# Buat prompt untuk meminta nama folder
question = pyinquirer.prompt([
    pyinquirer.Text("Masukkan nama folder: ")
])

# Kunci folder yang dipilih
folder_name = question["Masukkan nama folder: "]
pylock.lock(folder_name)
