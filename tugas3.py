# tugas3.py

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
Task 3 - Python Basics
Infinite Learning Batch 10

Author: Muhammad Zaenal Abidin Abdurrahman
Description: This script demonstrates basic Python concepts in a clear and structured way.    
"""

print("=== Tugas 3: PYTHON BASICS ===")

# Exercise 1: Variables and Data Types
print("\n--- Soal 1: Variabel dan Tipe Data ---")
full_name = "Muhammad Zaenal Abidin Abdurrahman"
age = 20
gpa = 3.91
is_learning_python = True
hobbies = ["ngoding", "belajar", "catur", "anime"]

print("Nama:", full_name, "| Tipe:", type(full_name))
print("Umur:", age, "| Tipe:", type(age))
print("IPK:", gpa, "| Tipe:", type(gpa))
print("Sedang Belajar Python:", is_learning_python, "| Tipe:", type(is_learning_python))
print("Hobi:", hobbies, "| Tipe:", type(hobbies))

pause_between_sections()

# Exercise 2: String Manipulation
print("\n--- Soal 2: Manipulasi String ---")
first_word = "infinite"
second_word = "learning"
combined_text = first_word + " " + second_word
print("Gabungan String:", combined_text)
print("Panjang String:", len(combined_text))
print("Huruf besar:", combined_text.upper())
print("Huruf kecil:", combined_text.lower())

pause_between_sections()

# Exercise 3: Basic Mathematical Operations
print("\n--- Soal 3: Operasi Matematika ---")
number_1 = 25
number_2 = 4

print(f"{number_1} + {number_2} =", number_1 + number_2)
print(f"{number_1} - {number_2} =", number_1 - number_2)
print(f"{number_1} * {number_2} =", number_1 * number_2)
print(f"{number_1} / {number_2} =", number_1 / number_2)
print(f"{number_1} // {number_2} =", number_1 // number_2)
print(f"{number_1} % {number_2} =", number_1 % number_2)

pause_between_sections()

# Exercise 4: Lists and Element Access
print("\n--- Soal 4: List dan Akses Elemen ---")
fruits = ["apel", "jeruk", "pisang", "mangga", "anggur"]
print("Daftar Buah:", fruits)
print("Buah pertama (Elemen pertama):", fruits[0])
print("Buah terakhir (Elemen terakhir):", fruits[-1])

fruits.append("semangka")
print("Setelah append 'semangka':", fruits)

fruits.remove("jeruk")
print("Setelah remove 'jeruk':", fruits)

pause_between_sections()

# Exercise 5: User Input
print("\n--- Soal 5: Input dari User ---")
user_name = input("Masukkan nama Anda: ")
user_age = int(input("Masukkan umur Anda: "))

print(f"Holaa amigoss, nama saya {user_name} dan umur saya {user_age} tahun.")
