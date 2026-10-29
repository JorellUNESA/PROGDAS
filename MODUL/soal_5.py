# Nama: Jorell Ozora Jizraele
# File: soal5.py

failed_attempts = int(input("Masukkan jumlah percobaan login gagal sebelumnya: "))

# Evaluasi Short-Circuit, langsung berhenti jika percobaan gagal sudah 3
if failed_attempts >= 3:
    print("AKUN TERKUNCI")
else:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    if username == "admin" and password == "pass123":
        otp = input("Masukkan Kode OTP: ")
        ip_trusted_input = input("Login dari IP Terpercaya? (ya/tidak): ").lower()
        is_ip_trusted = ip_trusted_input == "ya"
        
        if otp == "123456" or is_ip_trusted:
            print("Akses diterima. Login berhasil.")
        else:
            print("Akses ditolak. OTP salah dan IP tidak terpercaya.")
    else:
        print("Akses ditolak. Username atau Password salah.")