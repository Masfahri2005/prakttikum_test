import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def cek_kelulusan():
    try:
        nilai_akhir = float(entry_nilai.get())
        
        if nilai_akhir > 90:
            status = "Lulus dengan Pujian"
        elif 75 <= nilai_akhir <= 90:
            status = "Lulus"
        else:
            status = "Tidak Lulus"
        
        label_hasil.config(text=f"Status: {status}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai akhir yang valid.")

# Membuat tampilan aplikasi
window = tk.Tk()
window.title("Penentuan Kelulusan Siswa")
window.geometry("400x250")

label_judul = ttk.Label(window, text="Penentuan Kelulusan Siswa", font=("Arial", 16))
label_judul.pack(pady=10)

label_nilai = ttk.Label(window, text="Masukkan Nilai Akhir:")
label_nilai.pack()
entry_nilai = ttk.Entry(window)
entry_nilai.pack(pady=5)

button_cek = ttk.Button(window, text="Cek Kelulusan", command=cek_kelulusan)
button_cek.pack(pady=10)

label_hasil = ttk.Label(window, text="", font=("Arial", 12))
label_hasil.pack(pady=10)

# Menjalankan aplikasi tkinter python
window.mainloop()
