#PROGRAM 10: KONVERSI SUHU
print("\n10.KONVERSI SUHU CELCIUS KE FAHRENHEIT")
print("-"*30)
celcius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15
print(f"{celcius}°C = {fahrenheit:.2f}°F")
print(f"{celcius}°C = {kelvin:.2f} K")