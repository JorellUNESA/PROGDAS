# Nama: Jorell Ozora Jizraele
# File: soal3.py

keranjang = input("Masukkan daftar barang belanjaan (pisahkan dengan koma): ").strip()

# Memeriksa Falsy value (string kosong)
if not keranjang:
    print("Keranjang belanja Anda masih kosong!")
else:
    # Menghitung jumlah item berdasarkan pemisah koma
    jumlah_item = len(keranjang.split(","))
    print(f"Total variasi item barang yang dibeli: {jumlah_item}")