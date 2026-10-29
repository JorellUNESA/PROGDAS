# Nama: Jorell Ozora Jizraele
# File: soal2.py

usia = int(input("Masukkan usia Anda: "))
disabilitas = input("Apakah Anda penyandang disabilitas? (ya/tidak): ").lower()

# Menggunakan operator or untuk kondisi salah satu terpenuhi
if usia < 5 or usia > 65 or disabilitas == "ya":
    print("TIKET GRATIS")
else:
    print("TIKET NORMAL (Rp 50.000)")