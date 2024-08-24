import openpyxl

# Membuat workbook baru
workbook = openpyxl.Workbook()

# Membuka worksheet yang ada atau membuat yang baru
sheet = workbook.active
sheet.title = "Data"

# Menerima input dari client
data = input("Masukkan data: ")

# Menyimpan input ke dalam file Excel
sheet.append([data])

# Menyimpan workbook ke dalam file Excel
workbook.save("data_excel.xlsx")
