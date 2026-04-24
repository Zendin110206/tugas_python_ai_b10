# tugas6.py

# Note: This file is intentionally filled with comments to explain the code in detail. The comments are meant to help me understand the code better and to make it easier for me to review it later. I hope you don't mind the abundance of comments in this file. Thank you for your understanding.

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
Task 6 - Python Function and Class
Infinite Learning Batch 10

Author: Muhammad Zaenal Abidin Abdurrahman
Description: This script demonstrates Python modules, File I/O, and OOP concepts in a clear and structured way.
"""

import numpy as np
import pandas as pd

# Exercise 4: Basic OOP class, defined before main to keep the script structured.
# OOP (Object-Oriented Programming) is a programming paradigm that uses objects to organize code around data and behavior.
# A simple analogy for OOP is like a blueprint for a house. The blueprint (class) defines the structure and features of the house, such as the number of rooms, doors, and windows. When you build a house based on that blueprint, you create an object (instance) of the class. Each house (object) can have its own unique characteristics (like color or size), but they all share the same structure defined by the blueprint (class). This allows us to create multiple houses (objects) from the same blueprint (class) without having to rewrite the code for each house.

class GradeBook:
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Constructor for the GradeBook class.
        Parameter df: DataFrame containing student data and scores.
        """
        self.df = df
        
    def average(self) -> float:
        """Calculate the average score."""
        return float(self.df["nilai"].mean())
    
    def pass_rate(self, threshold: float = 70.0) -> float:
        """Calculate the passing percentage based on a score threshold."""
        total_students = len(self.df)
        if total_students == 0:
            return 0.0
        passed_students = len(self.df[self.df["nilai"] >= threshold])
        return float((passed_students / total_students) * 100)
    
    def save_summary(self, filename: str) -> None:
        """Save the statistical summary to a file."""
        # Two equivalent counting approaches:
        # first way:
        passed_count = (self.df["status"] == "LULUS").sum()
        # second way:
        failed_count = len(self.df[self.df["status"] == "TIDAK LULUS"])
         
        with open(filename, "w") as file:
            file.write("=== Ringkasan GradeBook ===\n\n")
            file.write(f"Jumlah mahasiswa: {len(self.df)}\n")
            file.write(f"Rata-rata nilai: {self.average():.2f}\n")
            file.write(f"Persentase lulus (threshold 70): {self.pass_rate():.2f}%\n")
            file.write(f"Jumlah mahasiswa yang lulus: {passed_count}\n")
            file.write(f"Jumlah mahasiswa yang tidak lulus: {failed_count}\n")
            file.write("\nData Mahasiswa:\n")
            file.write(self.df.to_string(index=False))
    
    def __str__(self):
        # Represent the object with a concise summary string.
        return f"[GradeBook Info] Jumlah Data: {len(self.df)} Mahasiswa | Rata-rata Kelas: {self.average():.2f}"

if __name__ == "__main__":
    # Set a random seed to keep the output consistent.
    np.random.seed(42)
    
    print("=== Tugas 6: PYTHON FUNCTION AND CLASS ===")
    
    # Exercise 1: NumPy - Array Creation and Manipulation
    print("\n--- Soal 1: Numpy - Array Creation & Manipulation ---")
    
    exam_scores = np.random.randint(50, 101, size=10)  # Create an array with 10 random scores between 50 and 100.
    print("Data Array Nilai Ujian:", exam_scores) # Here is the output for this session: Data Array Nilai Ujian: [88 78 64 92 57 70 88 68 72 60]
    
    mean_score = np.mean(exam_scores)
    median = np.median(exam_scores)
    std_dev = np.std(exam_scores)
    min_score = np.min(exam_scores)
    max_score = np.max(exam_scores)

    print("\nStatistik Deskriptif:")
    print(f"Rata-rata        : {mean_score:.2f}")
    print(f"Median           : {median:.2f}")
    print(f"Standar deviasi  : {std_dev:.2f}")
    print(f"Nilai minimum    : {min_score}")
    print(f"Nilai maksimum   : {max_score}")
    
    pause_between_sections()
    
    # Exercise 2: pandas - DataFrame Creation and Manipulation
    print("\n--- Soal 2: Pandas - DataFrame Creation & Manipulation ---")
    
    student_data = {
        "nama" : ["Alice", "Bob", "Charlie", "David", "Eve"],
        "nim": ["IL1001", "IL1002", "IL1003", "IL1004", "IL1005"],
        "nilai": exam_scores[:5]  # Use the first five scores for the student dataset.
        
    }
    
    print("Data Mahasiswa (Dictionary):")
    for key, value in student_data.items():
        print(f"  {key}: {value}") # Just checking the output for this part, to make sure everything is correct
        
    df = pd.DataFrame(student_data)
    print("\nDataFrame Mahasiswa:")
    print(df)
    
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS") # Add the status column based on a score threshold of 70.
    # The longer form of the lambda expression above could be written as follows:
    # def determine_status(x):
    #     if x >= 70:
    #         return "LULUS"
    #     else:
    #         return "TIDAK LULUS"
    # df["status"] = df["nilai"].apply(determine_status)
    
    # Another way to add the status column without using lambda is by using np.where, which is also a common method in pandas for conditional assignment:
    # df["status"] = np.where(df["nilai"] >= 70, "LULUS", "TIDAK LULUS")
    
    print("5 Baris pertama setelah menambahkan kolom status:")
    print(df.head())
    
    pause_between_sections()
    
    # Exercise 3: File I/O - Writing and Reading a .txt File
    print("\n--- Soal 3: FILE I/O - Menulis dan Membaca File .txt ---")
    output_filename = "ringkasaan_tugas6.txt"
    
    # Two ways to count rows by status:
    passed_count = len(df[df["status"] == "LULUS"]) # Filter rows with passing status and count the resulting DataFrame length.
    failed_count = (df["status"] == "TIDAK LULUS").sum() # Boolean True values are counted as 1, so sum() gives the failed-student count.
    
    with open(output_filename, "w") as file:
        # Write the script summary and the generated output up to this point.
        file.write("=== Ringkasan Tugas 6: Python Function and Class ===\n\n")
        file.write("1. Numpy - Array Creation & Manipulation:\n")
        file.write(f"  Data Array Nilai Ujian: {exam_scores}\n")
        file.write(f"  Rata-rata: {mean_score:.2f}\n")
        file.write(f"  Median: {median:.2f}\n")
        file.write(f"  Standar deviasi: {std_dev:.2f}\n")
        file.write(f"  Nilai minimum: {min_score}\n")
        file.write(f"  Nilai maksimum: {max_score}\n\n")

        file.write("2. Pandas - DataFrame Creation & Manipulation:\n")
        file.write("  Data Mahasiswa (Dictionary):\n")
        for key, value in student_data.items():
            file.write(f"    {key}: {value}\n")
        file.write("\n  DataFrame Mahasiswa:\n")
        file.write(df.to_string(index=False)) # Write the DataFrame without the index column.
        
        file.write("\n\n3. FILE I/O - Menulis dan Membaca File .txt:\n")
        file.write(f"  Jumlah baris dalam DataFrame: {len(df)}\n")
        file.write(f"  Jumlah mahasiswa yang lulus: {passed_count}\n")
        file.write(f"  Jumlah mahasiswa yang tidak lulus: {failed_count}\n")
        
    print(f"File '{output_filename}' berhasil dibuat di: {os.path.abspath(output_filename)}")
    
    pause_between_sections()
    
    # Exercise 4: OOP - Creating the GradeBook Class
    print("\n--- Soal 4: OOP - Membuat kelas GradeBook ---")
    gradebook = GradeBook(df)
    print(gradebook) # Printing gradebook calls __str__ and displays the formatted GradeBook summary.
    print(f"\nAverage\t\t: {gradebook.average():.2f}")
    print(f"Pass Rate\t: {gradebook.pass_rate():.2f}%")
    
    # This will rewrite the previous file.
    gradebook.save_summary(output_filename)
    print(f"Ringkasan tambahan berhasil disimpan ke '{output_filename}'")
    

        

    
    
    




