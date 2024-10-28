import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung harga akhir
def hitung_diskon():
    try:
        total_belanja = float(entry_total.get())
        
        if total_belanja > 1000000:
            diskon = 0.20
        elif 500000 <= total_belanja <= 1000000:
            diskon = 0.10
        else:
            diskon = 0.0
        harga_akhir = total_belanja - (total_belanja * diskon)
        label_hasil.config(text=f"Harga akhir setelah diskon: Rp {harga_akhir:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan jumlah total belanja yang valid.")

# Membuat Tampilan Aplikasi
window = tk.Tk()
window.title("Diskon Toko Elektronik")
window.geometry("400x250")

label_judul = tk.Label(window, text="Diskon Toko Elektronik", font=("Arial", 16))
label_judul.pack(pady=10)

# Label input untuk total belanja
label_total = tk.Label(window, text="Masukkan Total Belanja (Rp):")
label_total.pack()
entry_total = tk.Entry(window)
entry_total.pack(pady=5)

# Tombol untuk menghitung
button_hitung = tk.Button(window, text="Hitung Diskon", command=hitung_diskon)
button_hitung.pack(pady=10)

# Label hasil
label_hasil = tk.Label(window, text="", font=("Arial", 12))
label_hasil.pack(pady=10)

# Menjalankan aplikasi tkinter
window.mainloop()
