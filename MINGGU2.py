print("="*50)
print("CONTOH PROGRAM PYTHON UNTUK PEMULA")
print("="*50)

#PROGRAM 1= MENGENAL VARIABEl DAN TIPE DATA
nama = "Budi"
umur = 20
tinggi = 175.5
menikah = False
print(f"Nama: {nama} (tipe: {type(nama)})")
print(f"Umur: {umur} (tipe: {type(umur)})")
print(f"Tinggi: {tinggi} (tipe: {type(tinggi)})")
print(f"Menikah: {menikah} (tipe: {type(menikah)})")
print(f"Status menikah: {menikah}")

#PROGRAM 2= KONVERSI TIPE DATA
print("\n2.KONVERSI TIPE DATA")
print("-"*30)
angka_string = "123"
angka_float = "45.67"

konversi_int = int(angka_string)
konversi_float = float(angka_float)
print(f"String '{angka_string}' menjadi integer: {konversi_int}")
print(f"String '{angka_float}' menjadi float: {konversi_float}")
print(f"Integer '{konversi_int} menjadi string: '{str(konversi_int)}'")


#PROGRAM 3= OPERASI ARITMATIKA
print("\n6.OPERASI ARITMATIKA DASAR")
print("-" * 30)
a = 15
b = 4
print(f"a = {a}, b = {b}")
print(f"Penjumlahan: {a} + {b} = {a + b}")
print(f"Pengurangan: {a} - {b} = {a - b}")
print(f"Perkalian: {a} * {b} = {a * b}")
print(f"Pembagian: {a} / {b} = {a / b}")
