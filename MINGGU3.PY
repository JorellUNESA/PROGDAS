#PROGRAM 5: INPUT DARI USER
print("\n5.INPUT DARI USER")
print("-"*30)
print("Masukkan nama Data Anda:")
nama_user = input("Nama: ")
umur_user = int(input("Umur: "))
print(f"Halo: {nama_user}, umur Anda {umur_user} tahun")

print("\n9.MENGHITUNG LUAS DAN KELILING PERSEGI LINGKARAN")
print("-"*30) 
import math
radius = float(input("Masukkan jari-jari lingkaran: "))
luas = math.pi * radius ** 2
keliling = 2 * math.pi * radius
print(f"Luas lingkaran dengan jari-jari {radius} adalah: {luas:.2f}")
print(f"Keliling lingkaran dengan jari-jari {radius} adalah: {keliling:.2f}")