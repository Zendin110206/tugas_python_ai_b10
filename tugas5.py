# tugas5.py

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
Task 5 - Python Function and Class
Infinite Learning Batch 10

Author: Muhammad Zaenal Abidin Abdurrahman
Description: This script demonstrates python function and class concepts in a clear and structured way.   
"""

# Practice: Basic Function Introduction
# Starts with the simplest structure before moving to assignment-level function exercises.

print("--- Latihan: Pengenalan Fungsi paling dasar ---")

def greet_with_return(name):
    """
    Return a greeting message for a given name.

    Parameter:
    name (str): The name to greet.
    
    Return:
    str: Greeting message.
    """
    # A docstring documents the function so help() can explain its purpose, parameters, and return value.
    return f"Halo, {name}! Selamat belajar Python!"

print("Menampilkan Docstring dengan help()")
help(greet_with_return)
greeting_message = greet_with_return("Muhammad Zaenal Abidin Abdurrahman")
print(greeting_message)


# Directly calling a function with return still works when the returned value is printed.
print(greet_with_return("Infinite Learning Batch 10"))
greet_with_return("Python Function and Class") # This does not display output because the returned value is not printed or stored.

def greet_with_print(name):
    """
    Print a greeting message for a given name.

    Parameter:
    name (str): The name to greet.
    
    Return:
    None
    """
    print(f"\nHalo, {name}! Selamat belajar Python!")
    print("This is the greet_with_print function, which prints the result directly without storing it in a variable.")

greet_with_print("Muhammad Zaenal Abidin Abdurrahman")


pause_between_sections(clear_screen=True)


print("=== Tugas 5: PYTHON FUNCTION AND CLASS ===")

# Exercise 1: Functions - Definition, Parameters, and Return Values
print("\n--- Soal 1: Fungsi - definisi, parameter, return ---")

def greet(name: str) -> str: # Type hints clarify the expected parameter type and return type.
    """
    Return a greeting message for a given name.

    Parameter:
    name (str): The name to greet.
    
    Return:
    str: Greeting message.
    """
    return f"Halo, {name}!"

print("Fungsi Sapa")
print(greet("Zaenal Abidin"))
print(greet(123)) # Python still allows this dynamically, but following type hints keeps the code more consistent.

def add_numbers(a: float, b: float = 0.0) -> float: # Type hinting and type casting are different concepts.
    # Many editors can generate a docstring template automatically after typing triple quotes.
    """_summary_ 

    Args:
        a (float): _description_
        b (float, optional): _description_. Defaults to 0.0.

    Returns:
        float: _description_
    """ # The default value allows this function to be called with only one argument.
    return a + b

print("\nFungsi tambah dengan dua angka:")
print(add_numbers(5, 10))
result = add_numbers(3.5, 2.5)
print(result)

def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average value from a list of numbers.

    Parameter:
    numbers (list[float]): List of numeric values.
    
    Return:
    float: Average value from the list.
    """
    if len(numbers) == 0: # Guard against division by zero when the input list is empty.
        return 0.0
    return sum(numbers) / len(numbers)

print("\nFungsi rata_rata dengan list angka:")
print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([])) # This returns 0.0 because the empty-list case is handled inside calculate_average().

pause_between_sections(clear_screen=True)

# Practice: Basic Class Introduction
# Starts with the simplest structure before moving to assignment-level class exercises.

print("--- Latihan: Pengenalan Kelas paling dasar ---")

class Car: # Class names conventionally use CamelCase to distinguish them from functions and variables.
    def __init__(self, brand, model, year): # __init__ initializes each new object instance with the required data.
        self.brand = brand
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"{self.year} {self.brand} {self.model}"
    
car_1 = Car("Toyota", "Corolla", 2020) # All required constructor arguments must be provided when creating a Car object.
print("Informasi mobil:", car_1.get_car_info())

class StudentProfile:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def get_student_info(self):
        return f"Nama: {self.name}, NIM: {self.student_id}, Jurusan: {self.major}"

    def update_major(self, new_major):
        self.major = new_major
        print(f"Jurusan {self.name} telah diperbarui menjadi {self.major}.")
    
    def clear_student_id(self):
        self.student_id = None
        print(f"NIM {self.name} telah dihapus.")

student_profile_1 = StudentProfile("Zaenal", "101012300153", "Teknik Telekomunikasi")
student_profile_info = student_profile_1.get_student_info()
print("\nInformasi mahasiswa:", student_profile_info)
student_profile_1.update_major("Teknik Informatika")
print("Informasi mahasiswa setelah update jurusan:", student_profile_1.get_student_info())
student_profile_1.clear_student_id()
print("Informasi mahasiswa setelah hapus NIM:", student_profile_1.get_student_info())

class Book: # Publication year may be empty.
    def __init__(self, title, author, publication_year=None): # A default value allows a Book object to be created without publication-year data.
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_book_info(self):
        if self.publication_year: # This compact truthiness check is enough for the current optional-year example.
            return f"'{self.title}' oleh {self.author}, diterbitkan pada tahun {self.publication_year}."
        else:
            return f"'{self.title}' oleh {self.author}, tahun terbit tidak tersedia."
        
book_1 = Book("Atomic Habits", "James Clear", 2018)
print("\nInformasi buku:", book_1.get_book_info())
book_2 = Book("Deep Work", "Cal Newport") # The default publication_year value handles books without year data.
print("Informasi buku tanpa tahun terbit:", book_2.get_book_info())

pause_between_sections(clear_screen=True)

# Exercise 2: Classes - Attributes, Methods, and Inheritance
print("\n--- Soal 2: Class - atribut, method, inheritance ---")

class Student: 
    
    def __init__ (self, name: str, student_id: str, scores: list[float] | None = None) -> None: # Type hints document the expected parameter types and return value.
        # The None default keeps scores optional while still initializing the attribute as an empty list.
        self.name = name
        self.student_id = student_id
        self.scores = scores if scores is not None else []
        
    def add_score(self, score: float) -> None:
        self.scores.append(score)
    
    def average_score(self) -> float:
        if not self.scores: # Return 0.0 when the score list is empty to avoid division by zero.
            return 0.0
        return round(sum(self.scores) / len(self.scores), 2) # Round the average to two decimal places for cleaner output.
    
    def passing_status(self, threshold: float = 70.9) -> str:
        average_value = self.average_score()
        if average_value >= threshold:
            return "LULUS"
        
        # In this implementation, an empty score list returns 0.0 and therefore maps to "TIDAK LULUS".
        
        else:
            return "TIDAK LULUS"
        
    def __str__(self) -> str: 
        return f"Student(nama='{self.name}', nim='{self.student_id}', nilai={self.scores}, status_kelulusan='{self.passing_status()}')"
    
    # __str__ controls how the object is represented when passed to print() or str().
        

print("Percobaan kelas Student secara bertahap:")

student1 = Student("Zaenal", "101012300153")
print("Informasi student1:", student1) # Printing student1 calls __str__ and displays the formatted object summary.
student1.add_score(85.5)
student1.add_score(90.0)
print("Informasi student1 setelah menambahkan nilai:", student1)
print("Rata-rata nilai student1:", student1.average_score())

student2 = Student("Abidin", "101012300154", [60.0, 65.0, 70.0])
print("\nInformasi student2:", student2)
print("Rata-rata nilai student2:", student2.average_score())
print("Status kelulusan student2:", student2.passing_status())

pause_between_sections(clear_screen=True)

# Exercise 3: Full Function and Class Testing in if __name__ == "__main__"

print("\n--- Soal 3: Pengujian fungsi dan kelas secara keseluruhan di dalam if __name__ == \"__main__\": ---")

if __name__ == "__main__": # This block runs only when the file is executed directly, not when imported as a module.
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print("add_numbers(5, 7):", add_numbers(5, 7))
    print("add_numbers(10) =", add_numbers(10)) # The default second argument keeps this call valid.
    print("calculate_average([80, 90, 100]):", calculate_average([80, 90, 100]))
    print("calculate_average([]):", calculate_average([]))
    
    print("\n=== CLASSES ===")  
    student_a = Student("Budi", "A123")
    student_a.add_score(80)
    student_a.add_score(85)
    student_a.add_score(90)
    
    student_b = Student("Siti", "B456")
    student_b.add_score(60)
    student_b.add_score(65)
    student_b.add_score(70)
    
    print(student_a)
    print("Rata-rata nilai mhs1:", student_a.average_score())
    print("Status kelulusan mhs1:", student_a.passing_status())

    print(student_b)
    print("Rata-rata nilai mhs2:", student_b.average_score())
    print("Status kelulusan mhs2:", student_b.passing_status())
