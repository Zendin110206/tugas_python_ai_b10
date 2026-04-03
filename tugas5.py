# tugas5.py

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
Task 5 - Python Function and Class
Infinite Learning Batch 10

Author: Muhammad Zaenal Abidin Abdurrahman
Description: This script demonstrates python function and class concepts in a clear and structured way.   
"""

# Latihan: Pengenalan Fungsi paling dasar
# Paling dasar terlebih dahulu sebagai awal pembelajaran fungsi

print("--- Latihan: Pengenalan Fungsi paling dasar ---")

def sapa(nama):
    """
    Fungsi untuk menyapa seseorang dengan nama yang diberikan.
    Parameter:
    nama (str): Nama orang yang akan disapa.
    
    Return:
    str: Pesan sapaan.
    """
    # Kegunaan dari """ .... """ (Docstring, biasanyaa bagus nih kalau mau vibe coding, kasih prompt ke AI yang kalian gunakan untuk jikalau membuat fungsi, suruh kasih docstringnya) adalah untuk memberikan dokumentasi pada fungsi, sehingga ketika kita memanggil help(sapa) akan muncul penjelasan tentang fungsi ini. Ini membantu kita memahami apa yang dilakukan fungsi, parameter yang dibutuhkan, dan apa yang dikembalikan oleh fungsi tersebut.
    return f"Halo, {nama}! Selamat belajar Python!"

print("Menampilkan Docstring dengan help()")
help(sapa)
sapaan = sapa("Muhammad Zaenal Abidin Abdurrahman")
print(sapaan)


# jika langsung dipanggil tanpa disimpan ke variabel. 
print(sapa("Infinite Learning Batch 10"))
sapa("Python Function and Class") # ini tidak akan menampilkan apa-apa, jika mau, di dalam fungsi sapa, kita bisa menambahkan print untuk menampilkan hasilnya, tapi karena kita sudah menggunakan return, maka kita bisa menyimpan hasilnya ke variabel dan mencetaknya seperti contoh pertama.

def sapa2(nama):
    """
    Fungsi untuk menyapa seseorang dengan nama yang diberikan.
    Parameter:
    nama (str): Nama orang yang akan disapa.
    
    Return:
    str: Pesan sapaan.
    """
    print(f"\nHalo, {nama}! Selamat belajar Python!")
    print("Ini adalah fungsi sapa2 yang menggunakan print di dalamnya, jadi langsung menampilkan hasilnya tanpa perlu menyimpan ke variabel.")

sapa2("Muhammad Zaenal Abidin Abdurrahman")


jeda(bersihkan_layar=True)


print("=== Tugas 5: PYTHON FUNCTION AND CLASS ===")

# Soal 1: Fungsi - definisi, parameter, return
print("\n--- Soal 1: Fungsi - definisi, parameter, return ---")

def greet(nama: str) -> str: # Bedannya dengan fungsi sapa sebelumnya, di sini kita menggunakan type hinting untuk memberikan informasi tentang tipe data parameter dan return value. Ini membantu kita memahami apa yang diharapkan dari fungsi ini.
    """
    Fungsi untuk menyapa seseorang dengan nama yang diberikan.
    Parameter:
    nama (str): Nama orang yang akan disapa.
    
    Return:
    str: Pesan sapaan.
    """
    return f"Halo, {nama}!"

print("Fungsi Sapa")
print(greet("Zaenal Abidin"))
print(greet(123)) # ini akan tetap bekerja karena Python adalah bahasa yang dinamis, tapi akan lebih baik jika kita mengikuti type hinting yang sudah kita buat untuk menjaga konsistensi dan menghindari error di masa depan.

def tambah(a: float, b: float = 0.0) -> float: # Just notes to remember : Type Hinting (Petunjuk) vs Type Casting (Pengubahan) is different. Don't get confused between these two.
    # Kita bisa nambahain docsting otomatis dengan menggunakan fitur yang ada di code editor kita, biasanya dengan mengetik tiga kali tanda kutip ganda """ dan tekan enter, maka akan otomatis muncul template docstring seperti ini:
    """_summary_ 

    Args:
        a (float): _description_
        b (float, optional): _description_. Defaults to 0.0.

    Returns:
        float: _description_
    """ # Dengan memberikan nilai default 0.0 pada parameter b, kita memungkinkan untuk memanggil fungsi tambah dengan hanya satu argumen, yaitu a. Jika kita tidak memberikan nilai untuk b saat memanggil fungsi, maka b akan otomatis diinisialisasi dengan nilai default 0.0.
    return a + b

print("\nFungsi tambah dengan dua angka:")
print(tambah(5, 10))
hasil = tambah(3.5, 2.5)
print(hasil)

def rata_rata(angka: list[float]) -> float:
    """
    Fungsi untuk menghitung rata-rata dari sebuah list angka.
    Parameter:
    angka (list[float]): List yang berisi angka-angka.
    
    Return:
    float: Rata-rata dari angka-angka dalam list.
    """
    if len(angka) == 0: # why? Karena jika kita mencoba menghitung rata-rata dari list kosong, kita akan mendapatkan error pembagian dengan nol. Oleh karena itu, kita perlu memeriksa apakah list tersebut kosong sebelum melakukan perhitungan rata-rata. Jika list kosong, kita bisa mengembalikan nilai default seperti 0.0 atau memberikan pesan bahwa tidak ada angka untuk dihitung rata-ratanya.
        return 0.0
    return sum(angka) / len(angka)

print("\nFungsi rata_rata dengan list angka:")
print(rata_rata([1, 2, 3, 4, 5]))
print(rata_rata([])) # ini akan mengembalikan 0.0 karena kita sudah menangani kasus list kosong di dalam fungsi rata_rata.

jeda(bersihkan_layar=True)

# Latihan: Pengenalan Kelas paling dasar
# Paling dasar terlebih dahulu sebagai awal pembelajaran kelas

print("--- Latihan: Pengenalan Kelas paling dasar ---")

class Mobil: # type convention untuk nama kelas adalah menggunakan CamelCase, jadi setiap kata diawali dengan huruf kapital tanpa spasi. Ini membantu membedakan kelas dari fungsi atau variabel biasa yang biasanya menggunakan snake_case.
    def __init__(self, merek, model, tahun): # __init__ adalah method khusus yang digunakan untuk menginisialisasi objek ketika kita membuat instance dari kelas tersebut. Method ini akan dipanggil secara otomatis setiap kali kita membuat objek baru dari kelas Mobil. Parameter self adalah referensi ke instance objek yang sedang dibuat, dan parameter lainnya (merek, model, tahun) adalah data yang kita ingin simpan di dalam objek tersebut.
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def info_mobil(self):
        return f"{self.tahun} {self.merek} {self.model}"
    
mobil1 = Mobil("Toyota", "Corolla", 2020) # Penjelasan singkat : Jika tidak mengisi salah satu dari parameter merek, model, atau tahun saat membuat instance mobil1, maka kita akan mendapatkan error karena __init__ method mengharuskan kita untuk memberikan nilai untuk ketiga parameter tersebut. Misalnya, jika kita mencoba membuat mobil1 dengan hanya memberikan merek dan model seperti ini: mobil1 = Mobil("Toyota", "Corolla"), maka kita akan mendapatkan error TypeError yang mengatakan bahwa __init__() missing 1 required positional argument: 'tahun'. Oleh karena itu, kita harus memastikan untuk memberikan semua parameter yang diperlukan saat membuat instance dari kelas Mobil.
print("Informasi mobil:", mobil1.info_mobil())

class Mahasiswa: 
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def info_mahasiswa(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}"
    
    def update_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru
        print(f"Jurusan {self.nama} telah diperbarui menjadi {self.jurusan}.")
    
    def hapus_nim(self):
        self.nim = None
        print(f"NIM {self.nama} telah dihapus.")

mahasiswa1 = Mahasiswa("Zaenal", "101012300153", "Teknik Telekomunikasi")
info_mahasiswa1 = mahasiswa1.info_mahasiswa()
print("\nInformasi mahasiswa:", info_mahasiswa1)
mahasiswa1.update_jurusan("Teknik Informatika")
print("Informasi mahasiswa setelah update jurusan:", mahasiswa1.info_mahasiswa())
mahasiswa1.hapus_nim()
print("Informasi mahasiswa setelah hapus NIM:", mahasiswa1.info_mahasiswa())

class Buku: # tahun terbit boleh kosong
    def __init__(self, judul, penulis, tahun_terbit=None): # Dengan memberikan nilai default None pada parameter tahun_terbit, kita memungkinkan untuk membuat instance dari kelas Buku tanpa harus memberikan nilai untuk tahun terbit. Jika kita tidak memberikan nilai untuk tahun_terbit saat membuat objek, maka atribut tahun_terbit akan diinisialisasi dengan nilai None. Ini berguna jika kita ingin menyimpan informasi tentang buku yang mungkin tidak memiliki data tahun terbit atau jika kita ingin menambahkan informasi tersebut nanti setelah objek dibuat.
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def info_buku(self):
        if self.tahun_terbit: # Penulisan singkat seperti ini (tanpa is not None) sudah cukup untuk memeriksa apakah tahun_terbit memiliki nilai yang valid atau tidak. Jika tahun_terbit memiliki nilai yang dianggap "truthy" (seperti angka selain 0, string non-kosong, dll.), maka kondisi ini akan terpenuhi dan kita akan mengembalikan informasi lengkap tentang buku. Namun, jika tahun_terbit adalah None atau nilai "falsy" lainnya, maka kita akan mengembalikan informasi tentang buku tanpa menyertakan tahun terbit.
            return f"'{self.judul}' oleh {self.penulis}, diterbitkan pada tahun {self.tahun_terbit}."
        else:
            return f"'{self.judul}' oleh {self.penulis}, tahun terbit tidak tersedia."
        
buku1 = Buku("Atomic Habits", "James Clear", 2018)
print("\nInformasi buku:", buku1.info_buku())
buku2 = Buku("Deep Work", "Cal Newport") # Karena kita memberikan nilai default None pada parameter tahun_terbit, kita bisa membuat instance buku2 tanpa menyertakan tahun terbit. Dalam hal ini, atribut tahun_terbit untuk buku2 akan diinisialisasi dengan nilai None, dan ketika kita memanggil metode info_buku(), itu akan mengembalikan informasi tentang buku tanpa menyertakan tahun terbit karena kondisi if self.tahun_terbit tidak terpenuhi.
print("Informasi buku tanpa tahun terbit:", buku2.info_buku())

jeda(bersihkan_layar=True)

# Soal 2: Class - atribut, method, inheritance
print("\n--- Soal 2: Class - atribut, method, inheritance ---")

class Student: 
    
    def __init__ (self, nama: str, nim: str, nilai: list[float] | None = None) -> None: # Maksud syntax panjang seperti ini adalah untuk memberikan type hinting pada parameter dan return value dari method __init__. Dengan menggunakan type hinting, kita memberikan informasi tentang tipe data yang diharapkan untuk setiap parameter dan apa yang dikembalikan oleh method tersebut. Dalam hal ini, kita menyatakan bahwa nama harus berupa string, nim harus berupa string, dan nilai harus berupa list yang berisi float atau bisa juga None (jika tidak diberikan). Return type None menunjukkan bahwa method ini tidak mengembalikan nilai apa pun. Type hinting ini membantu meningkatkan keterbacaan kode dan memudahkan pengembangan serta pemeliharaan kode di masa depan.
        # Kalau misalnya kamu cuman nulis nilai: List[float] | None gitu doank, tanpa None = None, maka kitaa wajibb memberikan nilai untuk parameter nilai setiap kali kita membuat instance dari kelas Student.
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else [] # Dengan menggunakan nilai if nilai is not None else [], kita memastikan bahwa jika parameter nilai tidak diberikan saat membuat instance Student, maka atribut nilai akan diinisialisasi sebagai list kosong. Ini mencegah masalah yang mungkin timbul jika kita mencoba mengakses atau memodifikasi atribut nilai yang belum diinisialisasi dengan benar.
        
    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)
    
    def rata_nilai(self) -> float:
        if not self.nilai: # Dengan menggunakan if not self.nilai, kita memeriksa apakah list nilai kosong. Jika list nilai kosong, maka kondisi ini akan terpenuhi dan kita akan mengembalikan 0.0 sebagai rata-rata. Ini mencegah error pembagian dengan nol yang akan terjadi jika kita mencoba menghitung rata-rata dari list kosong.
            return 0.0
        return round(sum(self.nilai) / len(self.nilai), 2) # Dengan menggunakan round(..., 2), kita membulatkan hasil rata-rata ke dua angka desimal. Ini membuat output lebih rapi dan mudah dibaca, terutama jika rata-rata memiliki banyak angka di belakang koma. Misalnya, jika rata-rata adalah 85.66666666666667, dengan menggunakan round(..., 2), hasilnya akan menjadi 85.67.
    
    def status_kelulusan(self, threshold: float = 70.9) -> str:
        rata = self.rata_nilai()
        if rata >= threshold:
            return "LULUS"
        
        # Jika rata_nilai tidak memiliki nilai (list kosong), lebih baik dibuat sendiri kondisi untuk menangani kasus tersebut, misalnya dengan mengembalikan "NILAI TIDAK TERSEDIA" atau sesuatu yang serupa, daripada langsung mengembalikan "TIDAK LULUS". 
        # Namun, dalam implementasi saat ini, jika rata_nilai mengembalikan 0.0 karena list nilai kosong, maka status_kelulusan akan mengembalikan "TIDAK LULUS". Jadi, dalam konteks ini, kita bisa menganggap bahwa jika tidak ada nilai yang diberikan, maka mahasiswa dianggap tidak lulus.
        
        else:
            return "TIDAK LULUS"
        
    def __str__(self) -> str: 
        return f"Student(nama='{self.nama}', nim='{self.nim}', nilai={self.nilai}, status_kelulusan='{self.status_kelulusan()}')"
    
    # Penjelasan singkat tentang __str__: Method __str__ adalah method khusus dalam Python yang digunakan untuk menentukan representasi string dari sebuah objek. Ketika kita menggunakan fungsi print() atau str() pada sebuah objek, Python akan memanggil method __str__ untuk mendapatkan representasi string dari objek tersebut. Dengan mengimplementasikan method __str__, kita dapat mengontrol bagaimana objek kita ditampilkan ketika dicetak, sehingga membuat output lebih informatif dan mudah dipahami. Dalam contoh ini, method __str__ memberikan informasi lengkap tentang nama, nim, nilai, dan status kelulusan dari objek Student ketika dicetak.    
        

print("Percobaan kelas Student secara bertahap:")

student1 = Student("Zaenal", "101012300153")
print("Informasi student1:", student1) # dengan _str__, ketika kita print student1, itu akan memanggil method __str__ dan menampilkan informasi lengkap tentang student1 sesuai dengan format yang kita tentukan di dalam method __str__.
student1.tambah_nilai(85.5)
student1.tambah_nilai(90.0)
print("Informasi student1 setelah menambahkan nilai:", student1)
print("Rata-rata nilai student1:", student1.rata_nilai())

student2 = Student("Abidin", "101012300154", [60.0, 65.0, 70.0])
print("\nInformasi student2:", student2)
print("Rata-rata nilai student2:", student2.rata_nilai())
print("Status kelulusan student2:", student2.status_kelulusan())

jeda(bersihkan_layar=True)

# Soal 3: Pengujian fungsi dan kelas secara keseluruan di dalam if __name__ == "__main__":

print("\n--- Soal 3: Pengujian fungsi dan kelas secara keseluruan di dalam if __name__ == \"__main__\": ---")

if __name__ == "__main__": # Kegunaan __name__ == "__main__" adalah untuk memastikan bahwa kode di dalam blok ini hanya akan dieksekusi jika script dijalankan secara langsung, bukan ketika diimpor sebagai modul di script lain. Ini memungkinkan kita untuk menulis kode pengujian atau contoh penggunaan fungsi dan kelas tanpa khawatir akan dieksekusi saat modul tersebut diimpor. Dengan menggunakan if __name__ == "__main__", kita dapat menjaga agar kode pengujian tetap terpisah dari definisi fungsi dan kelas, sehingga membuat kode lebih bersih dan mudah dipelihara. 
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10) =", tambah(10)) # Karena parameter b memiliki nilai default 0.0, kita bisa memanggil fungsi tambah dengan hanya memberikan satu argumen, yaitu a. Dalam hal ini, b akan otomatis diinisialisasi dengan nilai default 0.0, sehingga hasilnya adalah 10 + 0.0 = 10.0.
    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([]):", rata_rata([]))
    
    print("\n=== CLASSES ===")  
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(85)
    mhs1.tambah_nilai(90)
    
    mhs2 = Student("Siti", "B456")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(65)
    mhs2.tambah_nilai(70)
    
    print(mhs1)
    print("Rata-rata nilai mhs1:", mhs1.rata_nilai())
    print("Status kelulusan mhs1:", mhs1.status_kelulusan())
    
    print(mhs2)
    print("Rata-rata nilai mhs2:", mhs2.rata_nilai())
    print("Status kelulusan mhs2:", mhs2.status_kelulusan())
    

    
    