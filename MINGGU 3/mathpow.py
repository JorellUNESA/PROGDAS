print("\n9.MENCARI PANGKAT BILANGAN")
print("-"*30)

bilangan = float(input("Masukkan bilangan: "))
pangkat = float(input("Masukkan pangkat: "))

import math
hasil = math.pow(bilangan, pangkat)
print(f"{bilangan} pangkat {pangkat} = {hasil:.2f}")