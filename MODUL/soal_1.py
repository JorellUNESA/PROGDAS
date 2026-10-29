# Nama: Jorell Ozora Jizraele
# File: soal1.py

toefl = int(input("Masukkan nilai TOEFL (0-677): "))
ipk = float(input("Masukkan nilai IPK (0.00-4.00): "))

# Menggunakan operator and karena kedua syarat harus terpenuhi
if toefl >= 500 and ipk >= 3.25:
    print("LULUS SELEKSI")
else:
    print("TIDAK LULUS SELEKSI")