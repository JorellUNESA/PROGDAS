for i in range(5):  
    print(i)
for i in range(2, 10, 2):  
    print(i)
# menghasilkan 2, 4, 6, 8

kelipatan = int(input("Masukkan batas kelipatan: "))
atas = int(input("Masukkan batas atas: "))
for a in range(kelipatan, atas + 1, kelipatan):
    print(a)

for char in 'saya belajar python':
    print(char)
    vocals = 'aiueo'
    jumlah_vocal = 0
    for char in kata:
        if char.lower() in vocals:
            jumlah_vocal += 1
    print("Jumlah huruf vokal dalam")


nama = ('Ahmad', 'Berry', 'Caca')
nama_yang_dicari = 'Caca'
for n in nama:
    if n == nama_yang_dicari:
        ada=True
        break
if ada:
    print (nama_yang_dicari,'ada dalam tuple.')
else:
    print (nama_yang_dicari,'tidak ada dalam tuple')

for i in range(20):
    if i ==2:
        continue
print(i)