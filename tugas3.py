# tugas3.py

import os

# Fungsi untuk memberikan jeda antara soal-soal agar saya bisa membaca soal dengan lebih nyaman. Juga bisa membersihkan layar jika diperlukan.
def jeda(bersihkan_layar=False):
    """
    Fungsi untuk memberikan jeda.
    Parameter bersihkan_layar (opsional): Jika True, terminal akan dibersihkan.
    """
    print("\n" + "="*50)
    input("👉 Tekan [ENTER] untuk lanjut ke soal berikutnya...")
    
    # Mengecek apakah user minta layarnya dibersihkan
    if bersihkan_layar:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        # Kalau tidak dibersihkan, cetak garis penutup biar rapi
        print("="*50 + "\n")
        
"""
Task 3 - Python Basics
Infinite Learning Batch 10

Author: Muhammad Zaenal Abidin Abdurrahman
Description: This script demonstrates basic Python concepts in a clear and structured way.    
"""

print("=== Tugas 3: PYTHON BASICS ===")

# Soal 1: Variabel dan Tipe Data
print("\n--- Soal 1: Variabel dan Tipe Data ---")
nama = "Muhammad Zaenal Abidin Abdurrahman"
umur = 20
ipk = 3.91
sedang_belajar_python = True
hobi = ["ngoding", "belajar", "catur", "anime"]

print("Nama:", nama, "| Tipe:", type(nama))
print("Umur:", umur, "| Tipe:", type(umur))
print("IPK:", ipk, "| Tipe:", type(ipk))
print("Sedang Belajar Python:", sedang_belajar_python, "| Tipe:", type(sedang_belajar_python))
print("Hobi:", hobi, "| Tipe:", type(hobi))

jeda()

# Soal 2: Manipulasi String
print("\n--- Soal 2: Manipulasi String ---")
depan = "infinite"
belakang = "learning"
gabungan = depan + " " + belakang
print("Gabungan String:", gabungan)
print("Panjang String:", len(gabungan))
print("Huruf besar:", gabungan.upper())
print("Huruf kecil:", gabungan.lower())

jeda()

# Soal 3: Operasi Matematika sederhana
print("\n--- Soal 3: Operasi Matematika ---")
angka1 = 25
angka2 = 4

print(f"{angka1} + {angka2} =", angka1 + angka2)
print(f"{angka1} - {angka2} =", angka1 - angka2)
print(f"{angka1} * {angka2} =", angka1 * angka2)
print(f"{angka1} / {angka2} =", angka1 / angka2)
print(f"{angka1} // {angka2} =", angka1 // angka2)
print(f"{angka1} % {angka2} =", angka1 % angka2)

jeda()

# Soal 4: List dan akses elemen
print("\n--- Soal 4: List dan Akses Elemen ---")
buah = ["apel", "jeruk", "pisang", "mangga", "anggur"]
print("Daftar Buah:", buah)
print("Buah pertama (Elemen pertama):", buah[0])
print("Buah terakhir (Elemen terakhir):", buah[-1])

buah.append("semangka")
print("Setelah append 'semangka':", buah)

buah.remove("jeruk")
print("Setelah remove 'jeruk':", buah)

jeda()

# Soal 5: Input dari User
print("\n--- Soal 5: Input dari User ---")
nama_user = input("Masukkan nama Anda: ")
umur_user = int(input("Masukkan umur Anda: "))

print(f"Holaa amigoss, nama saya {nama_user} dan umur saya {umur_user} tahun.")
