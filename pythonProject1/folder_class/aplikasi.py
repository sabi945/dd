

# root = Tk()
# labelnya = Label(root, text="halo selamat datang")
# labelnya_1 = Label(root, text="hai kawan lama tak jumpa")
# root.geometry("500x300+100+100")
# root.configure(bg="white")
# root.resizable(False,False)

# nilai_frame = ttk.Frame(root)
# nilai_frame.pack(padx=10,pady=10,fill="x",expand=True,ipady=20,)
# manambahkah = ttk.Label(nilai_frame, text="halo semuanya")
# manambahkah.pack()



# root.mainloop()

# belajar part 1



import tkinter as tk
from tkinter import Label

root = tk.Tk()
root.configure(bg="white")

# Membuat sebuah frame
frame = tk.Frame(root, bg="blue")
frame.configure( width=100, height=200)
frame.pack_propagate(False)

frame.pack(padx=10,pady=10,fill=tk.BOTH)
# Menambahkan teks ke dalam frame menggunakan widget Label
baso = Label(frame, text="halo")
baso.pack()

root.mainloop()



