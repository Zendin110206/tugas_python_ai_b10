### TABEL PERBANDINGAN STRUKTUR DATA PYTHON

| Fitur / Karakteristik | `List` 📦 | `Tuple` 🔒 | `Set` 🔮 | `Dictionary` 📚 |
| :--- | :--- | :--- | :--- | :--- |
| **Simbol (Sintaks)** | Kurung siku `[ ]` | Kurung lengkung `( )` | Kurung kurawal `{ }` | Kurung kurawal `{key: value}` |
| **Bisa Diubah (Mutable)?** | **Ya** (Bisa nambah/hapus) | **Tidak** (Immutable/Terkunci) | **Ya** (Bisa nambah/hapus) | **Ya** (Value bisa diubah/ditambah) |
| **Berurutan (Ordered)?** | **Ya** (Punya indeks 0,1,2..) | **Ya** (Punya indeks 0,1,2..) | **Tidak** (Acak, tidak berindeks) | **Ya** (Sejak Python 3.7+) |
| **Boleh Duplikat?** | **Ya** (Bisa ada data kembar) | **Ya** (Bisa ada data kembar) | **Tidak** (Otomatis dihapus jika kembar) | **Key: Tidak**, **Value: Ya** |
| **Cara Akses Data** | Pakai Indeks `data[0]` | Pakai Indeks `data[0]` | Tidak bisa diakses satuan | Pakai Key `data["kunci"]` |
| **Kegunaan Utama** | Kumpulan data umum yang sering diubah. | Kumpulan data tetap yang pantang diubah (misal: koordinat GPS). | Mencari data unik / menghilangkan duplikat. | Menyimpan data berpasangan (seperti kamus/database). |

---

### 1. LIST `[ ]` (Si Fleksibel)

List adalah tempat penampungan paling umum. Kamu bisa menaruh tipe data apa saja di dalamnya (campur aduk angka, teks, boolean, dll), dan kamu bebas mengubah isinya kapan saja.

**Contoh Pembuatan:**

```python
buah = ["apel", "mangga", "jeruk", "apel"] # 'apel' boleh duplikat
```

**Fungsi-fungsi Lengkap List:**

* **Menambah Data:**
  * `.append(data)`: Menambah 1 data di posisi **paling belakang**.

    ```python
        buah.append("pisang") # Hasil: ['apel', 'mangga', 'jeruk', 'apel', 'pisang']
    ```

  * `.insert(indeks, data)`: Menyelipkan data di **posisi/indeks tertentu**.

    ```python
        buah.insert(1, "anggur") # Menyelipkan "anggur" di indeks ke-1
    ```

  * `.extend(list_lain)`: Memasukkan banyak data sekaligus dari list lain.

    ```python
        buah.extend(["melon", "kiwi"])
    ```

* **Menghapus Data:**

  * `.remove(data)`: Menghapus data berdasarkan **namanya** (hanya yang pertama ketemu).

    ```python
        buah.remove("apel")
    ```

  * `.pop(indeks)`: Menghapus data berdasarkan **indeks**, lalu mengembalikan nilainya. Jika kurung dikosongkan `pop()`, dia menghapus data paling belakang.

    ```python
        buah.pop(2)
    ```

  * `.clear()`: Menghapus **semua** isi list sampai kosong melompong `[]`.

* **Fungsi Lainnya:**
  * `.sort()` (mengurutkan A-Z), `.reverse()` (membalik urutan), `.count(data)` (menghitung jumlah kembaran).

---

### 2. TUPLE `( )` (Si Keras Kepala / Terkunci)

Tuple itu kembarannya List, bedanya cuma satu: **TIDAK BISA DIUBAH SAMA SEKALI (Immutable)** setelah dibuat. Kamu nggak bisa nambah, nggak bisa hapus, nggak bisa ubah urutan.

**Contoh Pembuatan:**

```python
koordinat = (10.5, 20.7, 10.5) 
```

**Fungsi-fungsi Tuple:**
Karena dia terkunci, fungsinya sangat sedikit. Dia tidak punya `.append()` atau `.remove()`.

* `.count(data)`: Menghitung berapa kali sebuah data muncul di dalam tuple.

    ```python
    koordinat.count(10.5) # Hasil: 2
    ```

* `.index(data)`: Mencari tahu posisi (indeks) ke-berapa sebuah data berada.

    ```python
    koordinat.index(20.7) # Hasil: 1
    ```

*(Lalu gimana kalau kepepet mau ubah Tuple? Trick-nya: Ubah dulu jadi List pakai `list()`, ubah isinya, lalu ubah balik jadi Tuple pakai `tuple()`)*.

---

### 3. SET `{ }` (Si Unik & Acak)

Set adalah himpunan matematika. Ciri khas utamanya: **Anti Duplikat** dan **Tidak Punya Urutan (Acak)**. Kalau kamu masukin data kembar, Python akan diam-diam membuang salah satunya. Karena acak, kamu tidak bisa memanggil data pakai indeks seperti `data[0]`.

**Contoh Pembuatan:**

```python
angka_unik = {1, 2, 3, 3, 3, 4}
print(angka_unik) # Hasil: {1, 2, 3, 4} (Angka 3 yang kembar lenyap)
```

**Fungsi-fungsi Lengkap Set:**

* **Menambah Data:**
  * `.add(data)`: Menambahkan 1 data baru ke dalam set.

    ```python
        angka_unik.add(5)
    ```

  * `.update(set_lain)`: Menambahkan banyak data sekaligus (bisa dari list atau set lain).

    ```python
        angka_unik.update([6, 7, 8])
    ```

* **Menghapus Data:**

  * `.remove(data)`: Menghapus data. **Penting:** Kalau datanya ternyata nggak ada, program bakal *Error/Crash*.
  * `.discard(data)`: Menghapus data. **Penting:** Kalau datanya nggak ada, program *santai saja* dan tidak error (Lebih aman dari `.remove`).
  * `.pop()`: Menghapus data secara **ACAK** (karena set tidak punya urutan, kita nggak tahu data mana yang bakal terhapus).
* **Fungsi Khusus Matematika (Himpunan):**
  * `.union()` (Gabungan), `.intersection()` (Irisan / mencari yang sama), `.difference()` (Mencari perbedaan).

---

### 4. DICTIONARY `{key: value}` (Si Buku Kamus)

Dictionary menyimpan data secara **berpasangan**. Ada Kunci (`Key`) dan ada Nilai (`Value`). Ibarat menyimpan kontak di HP: Namanya adalah *Key*, dan Nomor HP-nya adalah *Value*.
*Catatan:* `Key` tidak boleh duplikat, tapi `Value` boleh duplikat.

**Contoh Pembuatan:**

```python
biodata = {
    "nama": "Budi",
    "umur": 20,
    "hobi": "Coding"
}
```

**Fungsi-fungsi Lengkap Dictionary:**

* **Mengakses / Melihat Data:**
  * Pakai kurung siku: `biodata["nama"]` (Kalau key-nya nggak ada, bakal *Error*).
  * Pakai fungsi `.get()`: `biodata.get("nama")` (Lebih aman, kalau key-nya nggak ada dia cuma membalas `None`, tidak error).
* **Menambah / Mengubah Data:**
  * Cara langsung:

    ```python
        biodata["asal"] = "Jakarta" # Karena "asal" belum ada, ini akan MENAMBAH data baru.
        biodata["umur"] = 21 # Karena "umur" sudah ada, ini akan MENGUBAH nilainya jadi 21.
    ```

  * `.update()`: Menambah/mengubah banyak data sekaligus.

    ```python
        biodata.update({"tinggi": 170, "berat": 65})
    ```

* **Menghapus Data:**

  * `.pop(key)`: Menghapus pasangan berdasarkan nama Kunci (*Key*).

    ```python
        biodata.pop("hobi") # Maka "hobi": "Coding" akan lenyap
    ```

  * `.popitem()`: Menghapus pasangan data yang **paling terakhir** dimasukkan.

* **Membongkar Isi Dictionary:**
  * `.keys()`: Mengambil semua nama *Key*-nya saja (nama, umur, hobi).
  * `.values()`: Mengambil semua nilainya saja (Budi, 20, Coding).
  * `.items()`: Mengambil semuanya secara berpasangan. Sangat berguna untuk di-looping pakai `for`.

---

Nah, ini sudah yang paling komplit! Mulai dari sintaks, sifat (mutable/ordered), sampai operasi-operasi bawaannya yang paling sering dipakai *programmer* Python. Ada bagian dari struktur data ini yang bikin kamu penasaran atau mau dikasih contoh kode yang lebih rumit?
