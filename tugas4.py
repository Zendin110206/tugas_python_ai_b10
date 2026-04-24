# tugas4.py

import os

# Adds a pause between exercises and optionally clears the terminal.
def pause_between_sections(clear_screen=False):
    """
    Pause before continuing to the next exercise.
    Parameter clear_screen (optional): Clear the terminal when set to True.
    """
    print("\n" + "="*50)
    input("👉 Tekan [ENTER] untuk lanjut ke soal berikutnya...")
    
    # Check whether the user requested a clean terminal screen.
    if clear_screen:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        # Print a closing separator when the screen is not cleared.
        print("="*50 + "\n")
        
"""
Task 4 - Python Data Structures
Infinite Learning Batch 10

Author: Muhammad Zaenal Abidin Abdurrahman
Description: This script demonstrates python data structures concepts in a clear and structured way.    
"""

print("=== Tugas 4: PYTHON DATA STRUCTURES ===")

# Exercise 1: Lists - Access and Manipulation
print("\n--- Soal 1: List - akses & manipulasi ---")
data_list = ["Python", "Numpy", 10, 3.14, True, "AI", 2026]
print("List:", data_list)
print("Elemen pertama:", data_list[0])
print("Elemen terakhir:", data_list[-1])
print("Slice [1:4]:", data_list[1:4])
print("Slicing dengan step [::2]:", data_list[::2])

print("\nManipulasi List:")
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

popped_element = data_list.pop()
print("Setelah pop:", data_list)
print("Elemen yang dipop:", popped_element)

print("\n\nSetelah proses manipulasi, List sekarang:", data_list)

pause_between_sections()

# Exercise 2: Tuples - Immutability and Unpacking
print("\n--- Soal 2: Tuple - immutability & unpacking ---")
data_tuple = ("Bandung", "Jakarta", "Surabaya", "Malang", "Yogyakarta")
print("Tuple:", data_tuple)
print("Panjang Tuple:", len(data_tuple))
print("Elemen pertama:", data_tuple[0])
print("Elemen indeks ke-2:", data_tuple[2])

city_one, city_two, *other_cities = data_tuple
print("Unpacking Tuple:")
print("Kota 1:", city_one)
print("Kota 2:", city_two)
print("Kota lain:", other_cities)
# Tuples are immutable, so append and insert operations are not available. Create a new tuple when changes are needed.

pause_between_sections()

# Exercise 3: Sets - Uniqueness and Set Operations
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
print("Symmetric Difference (A Δ B) dengan operator ^:", set_a ^ set_b) # Symmetric difference returns elements that exist in only one set, not both.

pause_between_sections()

# Exercise 4: Dictionaries - Access and Manipulation
print("\n--- Soal 4: Dictionary - akses & manipulasi ---")
student_profile = {
    "nama": "Muhammad Zaenal Abidin Abdurrahman",
    "umur": 20,
    "nim" : "101012300153",
    "angkatan": 2023,
    "kota": "Bandung"
    }
print("Dictionary awal:", student_profile)

student_profile["prodi"] = "S1 Teknik Telekomunikasi"
student_profile["kota"] = "Pasuruan"
del student_profile["nim"]
print("Dictionary setelah manipulasi:", student_profile)

print("\nAkses nilai dengan key 'nama':", student_profile["nama"])
print("Akses nilai dengan key 'umur':", student_profile.get("umur")) # get() safely returns None when the key does not exist instead of raising an error.
print("\nKeys:", student_profile.keys())
print("Keys (list):", list(student_profile.keys()))
print("Values:", student_profile.values())
print("Items (key-value pairs):", student_profile.items())

print("\nIterasi dictionary:")
for key, value in student_profile.items():
    print(f"{key}: {value}")
    
pause_between_sections()

# Exercise 5: Nested Structures
print("\n--- Soal 5: Nested Structures ---")
book_list = [
    {"judul": "Atomic Habits", "penulis": "James Clear", "tahun": 2018},
    {"judul": "Deep Work", "penulis": "Cal Newport", "tahun": 2016},
    {"judul": "Python Crash Course", "penulis": "Eric Matthes", "tahun": 2019},
    {"judul": "The Pragmatic Programmer", "penulis": "Andrew Hunt", "tahun": 1999}
]

print("Semua judul buku:")
for book in book_list:
    # print(book) would display the full dictionary, while book["judul"] displays only the title value.
    print("-", book["judul"])
    
recent_books = [book for book in book_list if book["tahun"] >= 2017]
print("\nBuku yang diterbitkan tahun 2017 atau lebih baru:")
for book in recent_books:
    print(f"- {book['judul']} ({book['tahun']})")
    
pause_between_sections()

# Exercise 6: Comprehensions and Utilities
print("\n--- Soal 6: Comprehensions & utilitas ---")
numbers = list(range(1, 21))
print("List angka 1-20:", numbers)

squared_numbers = [x**2 for x in numbers]
print("List kuadrat angka 1-20:", squared_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
print("List angka genap 1-20:", even_numbers)

number_status = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("\nDictionary status angka 1-10:", number_status)

sentence = "Python Data Structures"
unique_letters = {letter.lower() for letter in sentence if letter != " "} # This set comprehension converts each non-space character to lowercase and keeps only unique letters.
print("Set comprehension huruf unik:", unique_letters)

pause_between_sections()

# Exercise 7: Membership and Basic Search
print("\n--- Soal 7: Keanggotaan & pencarian sederhana ---")
# data_list was defined in exercise 1: data_list = ["Python", "Numpy", 10, 3.14, True, "AI", 2026]
print("List untuk pencarian:", data_list)
print("'Python' ada di list?", "Python" in data_list)
print("3.14 ada di list?", 3.14 in data_list)
print("Angka 10 ada di set A?", 10 in set_a)

if "AI" in data_list:
    print("AI ditemukan di list! Posisi indeks:", data_list.index("AI"))
else:
    print("AI tak de lah di list.")
    





