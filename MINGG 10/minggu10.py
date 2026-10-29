angka = [10, 20, 30, 40, 50]
print (angka[1:4])  # Output: [20, 30, 40]
print (angka[:2])   # Output: [10, 20]

#menambahkan elemen di paling akhir
buah = ['apel', 'jeruk',]
buah.append('pisang')
print(buah)  # Output: ['apel', 'jeruk', 'pisang']

#peringatan: mengembalikan none
hasil = buah.append('mangga')
print(hasil)  # Output: None

nilai = [70,80,100]
#sisipkan angak 90 pada indeks ke 2
nilai.insert(0,60)
print(nilai)  # Output: [60, 70, 80, 90, 100]