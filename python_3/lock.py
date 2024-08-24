from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Nama", "Umur", "Kota"]
table.add_row(["Alice", 30, "New York"])
table.add_row(["Bob", 25, "San Francisco"])
table.add_row(["Charlie", 35, "Los Angeles"])

print(table)
