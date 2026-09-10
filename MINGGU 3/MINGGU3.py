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
print(f"jari-jari lingkaran: {radius}")
print(f"Luas lingkaran: {luas:.2f}")
print(f"Keliling lingkaran: {keliling:.2f}")  


#PROGRAM 10: KONVERSI SUHU
print("\n10.KONVERSI SUHU CELCIUS KE FAHRENHEIT")
print("-"*30)
celcius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15
print(f"{celcius}°C = {fahrenheit:.2f}°F")
print(f"{celcius}°C = {kelvin:.2f} K")

#PROGRAM 11: OPERATOR PEMBANDING DASAR
print("\n11.OPERATOR PEMBANDING DASAR")
print("-"*30)
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}") #sama dengan
print(f"x != y: {x != y}") #tidak sama dengan
print(f"x > y: {x > y}") #lebih besar dari
print(f"x < y: {x < y}") #lebih kecil dari
print(f"x >= y: {x >= y}") #lebih besar atau sama dengan
print(f"x <= y: {x <= y}") #lebih kecil atau sama dengan

#PROGRAM 12: OPERATOR LOGIKA DASAR
print("\n16.OPERATOR LOGIKA DASAR")
