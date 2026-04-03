# tugas6.py

# Note: This file is intentionally filled with comments to explain the code in detail. The comments are meant to help me understand the code better and to make it easier for me to review it later. I hope you don't mind the abundance of comments in this file. Thank you for your understanding.

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
Task 6 - Python Function and Class
Infinite Learning Batch 10

Author: Muhammad Zaenal Abidin Abdurrahman
Description: This script demonstrates python Python Modules, File I/O, & OOP concepts in a clear and structured way.
"""

import os
import numpy as np
import pandas as pd

# Soal 4: Class OOP sederhana (Dibuat sebelum main agar lebih terstruktur)
# What is OOP? OOP (Object-Oriented Programming) adalah paradigma pemrograman yang menggunakan "objek" untuk merancang aplikasi dan program. OOP memungkinkan kita untuk membuat kelas (class) yang merupakan blueprint untuk objek, dan objek adalah instance dari kelas tersebut. Dengan OOP, kita bisa mengorganisir kode dengan lebih baik, membuatnya lebih modular, dan memudahkan pemeliharaan serta pengembangan di masa depan.
# A simple analogy for OOP is like a blueprint for a house. The blueprint (class) defines the structure and features of the house, such as the number of rooms, doors, and windows. When you build a house based on that blueprint, you create an object (instance) of the class. Each house (object) can have its own unique characteristics (like color or size), but they all share the same structure defined by the blueprint (class). This allows us to create multiple houses (objects) from the same blueprint (class) without having to rewrite the code for each house.

class GradeBook:
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Konstruktor untuk kelas GradeBook.
        Parameter df: DataFrame yang berisi data mahasiswa dan nilai mereka.
        """
        self.df = df
        
    def average(self) -> float:
        """Menghitung rata-rata nilai."""
        return float(self.df["nilai"].mean())
    
    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase mahasiswa yang lulus berdasarkan threshold."""
        total_students = len(self.df)
        if total_students == 0:
            return 0.0
        passed_students = len(self.df[self.df["nilai"] >= threshold])
        return float((passed_students / total_students) * 100)
    
    def save_summary(self, filename: str) -> None:
        """Menyimpan ringkasan statistik ke file."""
        #Two way of doing this:
        # first way:
        jumlah_lulus = (self.df["status"] == "LULUS").sum()
        # second way:
        jumlah_tidak_lulus = len(self.df[self.df["status"] == "TIDAK LULUS"])
         
        with open(filename, "w") as file:
            file.write("=== Ringkasan GradeBook ===\n\n")
            file.write(f"Jumlah mahasiswa: {len(self.df)}\n")
            file.write(f"Rata-rata nilai: {self.average():.2f}\n")
            file.write(f"Persentase lulus (threshold 70): {self.pass_rate():.2f}%\n")
            file.write(f"Jumlah mahasiswa yang lulus: {jumlah_lulus}\n")
            file.write(f"Jumlah mahasiswa yang tidak lulus: {jumlah_tidak_lulus}\n")
            file.write("\nData Mahasiswa:\n")
            file.write(self.df.to_string(index=False))
    
    def __str__(self):
        # Merepresentasikan object dalam bentuk string yang rapi
        return f"[GradeBook Info] Jumlah Data: {len(self.df)} Mahasiswa | Rata-rata Kelas: {self.average():.2f}"

if __name__ == "__main__":
    # Agar output konsisten, kita set random seed untuk numpy
    np.random.seed(42)
    
    print("=== Tugas 6: PYTHON FUNCTION AND CLASS ===")
    
    # Soal 1: Numpy - Array Creation & Manipulation
    print("\n--- Soal 1: Numpy - Array Creation & Manipulation ---")
    
    nilai_ujian = np.random.randint(50, 101, size=10)  # Membuat array dengan 10 nilai acak antara 50 dan 100
    print("Data Array Nilai Ujian:", nilai_ujian) # Here is the output for this session: Data Array Nilai Ujian: [88 78 64 92 57 70 88 68 72 60]
    
    rata2 = np.mean(nilai_ujian)
    median = np.median(nilai_ujian)
    std_dev = np.std(nilai_ujian)
    nilai_min = np.min(nilai_ujian)
    nilai_max = np.max(nilai_ujian)

    print("\nStatistik Deskriptif:")
    print(f"Rata-rata        : {rata2:.2f}")
    print(f"Median           : {median:.2f}")
    print(f"Standar deviasi  : {std_dev:.2f}")
    print(f"Nilai minimum    : {nilai_min}")
    print(f"Nilai maksimum   : {nilai_max}")
    
    jeda()
    
    # Soal 2: Pandas - DataFrame Creation & Manipulation
    print("\n--- Soal 2: Pandas - DataFrame Creation & Manipulation ---")
    
    data_mahasiswa = {
        "nama" : ["Alice", "Bob", "Charlie", "David", "Eve"],
        "nim": ["IL1001", "IL1002", "IL1003", "IL1004", "IL1005"],
        "nilai": nilai_ujian[:5]  # Menggunakan 5 nilai pertama untuk mahasiswa yaitu : [88 78 64 92 57]
        
    }
    
    print("Data Mahasiswa (Dictionary):")
    for key, value in data_mahasiswa.items():
        print(f"  {key}: {value}") # Just checking the output for this part, to make sure everything is correct
        
    df = pd.DataFrame(data_mahasiswa)
    print("\nDataFrame Mahasiswa:")
    print(df)
    
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS") # Menambahkan kolom status berdasarkan nilai dengan threshold 70. Lambda secara sederhana dan mudah dipahami untuk pemula adalah fungsi anonim yang digunakan untuk menerapkan logika sederhana langsung pada kolom DataFrame. Dalam hal ini, lambda digunakan untuk menentukan apakah seorang mahasiswa lulus atau tidak berdasarkan nilai ujian mereka. Jika nilai 70 atau lebih, maka statusnya "LULUS", jika kurang dari 70, maka statusnya "TIDAK LULUS". Penggunaan lambda membuat kode lebih ringkas dan mudah dibaca, terutama untuk operasi sederhana seperti ini.
    # Bentuk panjang dari lambda di atas bisa ditulis sebagai berikut:
    # def tentukan_status(x):
    #     if x >= 70:
    #         return "LULUS"
    #     else:
    #         return "TIDAK LULUS"
    # df["status"] = df["nilai"].apply(tentukan_status)
    
    # Another way to add the status column without using lambda is by using np.where, which is also a common method in pandas for conditional assignment:
    # df["status"] = np.where(df["nilai"] >= 70, "LULUS", "TIDAK LULUS")
    
    print("5 Baris pertama setelah menambahkan kolom status:")
    print(df.head())
    
    jeda()
    
    # Soal 3: FILE I/O - Menulis dan Membaca File .txt
    print("\n--- Soal 3: FILE I/O - Menulis dan Membaca File .txt ---")
    nama_file = "ringkasaan_tugas6.txt"
    
    # two way of doinnt this: 
    jumlah_lulus = len(df[df["status"] == "LULUS"]) # Kode ini berjalan dengan bertingkat, kode pertama yaitu df["status"] == "LULUS" akan menghasilkan Series boolean yang menunjukkan baris mana yang memiliki status "LULUS". Kemudian, df[df["status"] == "LULUS"] akan menghasilkan DataFrame baru yang hanya berisi baris-baris tersebut. Terakhir, len() digunakan untuk menghitung jumlah baris dalam DataFrame baru tersebut, yang sama dengan jumlah mahasiswa yang lulus.
    jumlah_tidak_lulus = (df["status"] == "TIDAK LULUS").sum() # Kode ini bekerja dengan memeriksa setiap elemen dalam kolom "status" untuk melihat apakah nilainya adalah "TIDAK LULUS". Hasilnya adalah Series boolean yang menunjukkan True untuk baris yang tidak lulus dan False untuk yang lulus. Kemudian, dengan menggunakan .sum(), kita menghitung jumlah True dalam Series tersebut, yang sama dengan jumlah mahasiswa yang tidak lulus. TRUE dihitung sebagai 1 dan FALSE dihitung sebagai 0, sehingga hasil akhirnya adalah jumlah mahasiswa yang tidak lulus.
    
    with open(nama_file, "w") as file:
        # Menulis ringkasan keseluruhan kode dari awal hingga titik ini dan outputnya.
        file.write("=== Ringkasan Tugas 6: Python Function and Class ===\n\n")
        file.write("1. Numpy - Array Creation & Manipulation:\n")
        file.write(f"  Data Array Nilai Ujian: {nilai_ujian}\n")
        file.write(f"  Rata-rata: {rata2:.2f}\n")
        file.write(f"  Median: {median:.2f}\n")
        file.write(f"  Standar deviasi: {std_dev:.2f}\n")
        file.write(f"  Nilai minimum: {nilai_min}\n")
        file.write(f"  Nilai maksimum: {nilai_max}\n\n")

        file.write("2. Pandas - DataFrame Creation & Manipulation:\n")
        file.write("  Data Mahasiswa (Dictionary):\n")
        for key, value in data_mahasiswa.items():
            file.write(f"    {key}: {value}\n")
        file.write("\n  DataFrame Mahasiswa:\n")
        file.write(df.to_string(index=False)) # Menulis DataFrame ke file tanpa index
        
        file.write("\n\n3. FILE I/O - Menulis dan Membaca File .txt:\n")
        file.write(f"  Jumlah baris dalam DataFrame: {len(df)}\n")
        file.write(f"  Jumlah mahasiswa yang lulus: {jumlah_lulus}\n")
        file.write(f"  Jumlah mahasiswa yang tidak lulus: {jumlah_tidak_lulus}\n")
        
    print(f"File '{nama_file}' berhasil dibuat di: {os.path.abspath(nama_file)}")
    
    jeda()
    
    # Soal 4: OOP - Membuat kelas GradeBook
    print("\n--- Soal 4: OOP - Membuat kelas GradeBook ---")
    gradebook = GradeBook(df)
    print(gradebook) # Output dari print(gradebook) akan menampilkan informasi tentang jumlah data mahasiswa dan rata-rata nilai kelas, yang dihasilkan dari metode __str__ yang telah kita definisikan dalam kelas GradeBook. Outputnya akan terlihat seperti ini: [GradeBook Info] Jumlah Data: 5 Mahasiswa | Rata-rata Kelas: 75.00
    print(f"\nAverage\t\t: {gradebook.average():.2f}")
    print(f"Pass Rate\t: {gradebook.pass_rate():.2f}%")
    
    # This will rewrite the previous file.
    gradebook.save_summary(nama_file)
    print(f"Ringkasan tambahan berhasil disimpan ke '{nama_file}'")    
    

        

    
    
    




