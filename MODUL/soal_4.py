# Nama: Jorell Ozora Jizraele
# File: soal4.py

ipk = float(input("Masukkan IPK: "))
penghasilan = int(input("Masukkan penghasilan orang tua: "))
prestasi_input = input("Memiliki Prestasi Nasional? (ya/tidak): ").lower()
pelanggaran_input = input("Memiliki Catatan Pelanggaran? (ya/tidak): ").lower()

prestasi = prestasi_input == "ya"
pelanggaran = pelanggaran_input == "ya"

# Menggabungkan operator and, or, dan not
if (ipk >= 3.50 and penghasilan < 5000000) or (prestasi and not pelanggaran):
    print("Status: LAYAK menerima beasiswa")
else:
    print("Status: TIDAK LAYAK menerima beasiswa")