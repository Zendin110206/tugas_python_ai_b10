# tugas4.py

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
Task 4 - Python Data Structures
Infinite Learning Batch 10

Author: Muhammad Zaenal Abidin Abdurrahman
Description: This script demonstrates python data structures concepts in a clear and structured way.    
"""

print("=== Tugas 4: PYTHON DATA STRUCTURES ===")

# Soal 1: List - akses & manipulasi
print("\n--- Soal 1: List - akses & manipulasi ---")
data_list = ["Python", "Numpy", 10, 3.14, True, "AI", 2026]
print("List:", data_list)
print("Elemen pertama:", data_list[0])
print("Elemen terakhir:", data_list[-1])
print("Slice [1:4]:", data_list[1:4])
print("Slicing dengan step [::2]:", data_list[::2])

print("\nManipuasi List:")
print("Sebelum:", data_list)

data_list.append("Machine Learning")
print("Setelah append:", data_list)

data_list.insert(2, "Data Science")
print("Setelah insert:", data_list)

data_list.extend(["Deep Learning", "Big Data"])
print("Setelah extend:", data_list)

data_list.remove(10)
print("Setelah remove:", data_list)

data_list[2] = "Data Analysis"
print("Setelah update index 2:", data_list)

elemen_pop = data_list.pop()
print("Setelah pop:", data_list)
print("Elemen yang dipop:", elemen_pop)

print("\n\nSetelah proses manipulasi, List sekarang:", data_list)

jeda()

# Soal 2: Tuple - immutability & unpacking
print("\n--- Soal 2: Tuple - immutability & unpacking ---")
data_tuple = ("Bandung", "Jakarta", "Surabaya", "Malang", "Yogyakarta")
print("Tuple:", data_tuple)
print("Panjang Tuple:", len(data_tuple))
print("Elemen pertama:", data_tuple[0])
print("Elemen indeks ke-2:", data_tuple[2])

kota1, kota2, *kota_lain = data_tuple
print("Unpacking Tuple:")
print("Kota 1:", kota1)
print("Kota 2:", kota2)
print("Kota lain:", kota_lain) 
# Tuple tidak bisa diubah, jadi kita tidak bisa melakukan operasi seperti append atau insert. Kita hanya bisa membuat tuple baru jika ingin mengubah isinya.

jeda()

# Soal 3: Set - uniqueness & operasi himpunan
print("\n--- Soal 3: Set - uniqueness & operasi himpunan ---")
set_a = {1, 2, 3, 4, 4, 5}
set_b = {4, 5, 6, 7, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union (A ∪ B):", set_a.union(set_b))
print("Intersection (A ∩ B):", set_a.intersection(set_b))
print("Difference (A - B):", set_a.difference(set_b))
print("Symmetric Difference (A Δ B):", set_a.symmetric_difference(set_b))

print("\nOperasi himpunan dengan operator:")
print("Union (A ∪ B) dengan operator |:", set_a | set_b)
print("Intersection (A ∩ B) dengan operator &:", set_a & set_b)
print("Difference (A - B) dengan operator -:", set_a - set_b)
print("Symmetric Difference (A Δ B) dengan operator ^:", set_a ^ set_b) # Symmetric difference menghasilkan elemen yang hanya ada di salah satu set, tapi tidak di kedua set.

jeda()

# Soal 4: Dictionary - akses & manipulasi
print("\n--- Soal 4: Dictionary - akses & manipulasi ---")
mahasiswa = {
    "nama": "Muhammad Zaenal Abidin Abdurrahman",
    "umur": 20,
    "nim" : "101012300153",
    "angkatan": 2023,
    "kota": "Bandung"
    }
print("Dictionary awal:", mahasiswa)

mahasiswa["prodi"] = "S1 Teknik Telekomunikasi"
mahasiswa["kota"] = "Pasuruan"
del mahasiswa["nim"]
print("Dictionary setelah manipulasi:", mahasiswa)

print("\nAkses nilai dengan key 'nama':", mahasiswa["nama"])
print("Akses nilai dengan key 'umur':", mahasiswa.get("umur")) # get dipakai untuk mengakses nilai dengan key, tapi kalau key tidak ada, dia akan mengembalikan None, bukan error seperti kalau kita akses langsung dengan tanda kurung siku. Lebih aman aja kalau kita tidak yakin keynya ada atau tidak.
print("\nKeys:", mahasiswa.keys())
print("Keys (list):", list(mahasiswa.keys()))
print("Values:", mahasiswa.values())
print("Items (key-value pairs):", mahasiswa.items())

print("\nIterasi dictionary:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
    
jeda()

# Soal 5: Nested Structures
print("\n--- Soal 5: Nested Structures ---")
daftar_buku = [
    {"judul": "Atomic Habits", "penulis": "James Clear", "tahun": 2018},
    {"judul": "Deep Work", "penulis": "Cal Newport", "tahun": 2016},
    {"judul": "Python Crash Course", "penulis": "Eric Matthes", "tahun": 2019},
    {"judul": "The Pragmatic Programmer", "penulis": "Andrew Hunt", "tahun": 1999}
]

print("Semua judul buku:")
for buku in daftar_buku:
    # print(buku) # Kalau kita print buku, dia akan print seluruh dictionarynya, tapi kalau kita print buku["judul"], dia akan print hanya judulnya saja. Kita bisa akses nilai di dalam dictionary dengan menggunakan keynya.
    print("-", buku["judul"])
    
buku_terbaru = [buku for buku in daftar_buku if buku["tahun"] >= 2017]
print("\nBuku yang diterbitkan tahun 2017 atau lebih baru:")
for buku in buku_terbaru:
    print(f"- {buku['judul']} ({buku['tahun']})")
    
jeda()

# Soal 6: Comprehensions & utilitas
print("\n--- Soal 6: Comprehensions & utilitas ---")
angka = list(range(1, 21))
print("List angka 1-20:", angka)

angka_kuadrat = [x**2 for x in angka]
print("List kuadrat angka 1-20:", angka_kuadrat)

angka_genap = [x for x in angka if x % 2 == 0]
print("List angka genap 1-20:", angka_genap)

status_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("\nDictionary status angka 1-10:", status_angka)

kalimat = "Python Data Structures"
huruf_unik = {huruf.lower() for huruf in kalimat if huruf != " "} # Cara kerjanya adalah dengan membuat set comprehension yang iterasi setiap huruf dalam kalimat, lalu kita ubah hurufnya menjadi lowercase dan kita filter agar tidak memasukkan spasi. Hasilnya adalah set yang berisi huruf-huruf unik dalam kalimat tersebut. Kita pakai set karena set otomatis akan menghilangkan duplikat, jadi kita akan mendapatkan hanya huruf unik saja.
print("Set comprehension huruf unik:", huruf_unik)

jeda()

# Soal 7: Keanggotaan & pencarian sederhana
print("\n--- Soal 7: Keanggotaan & pencarian sederhana ---")
# data_list sudah didefinisikan di soal 1, yaitu : data_list = ["Python", "Numpy", 10, 3.14, True, "AI", 2026]
print("List untuk pencarian:", data_list)
print("'Python' ada di list?", "Python" in data_list)
print("3.14 ada di list?", 3.14 in data_list)
print("Angka 10 ada di set A?", 10 in set_a)

if "AI" in data_list:
    print("AI ditemukan di list! Posisi indeks:", data_list.index("AI"))
else:
    print("AI tak de lah di list.")
    





