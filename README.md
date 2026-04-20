<div align="center">

# Python Assignments — Infinite Learning Batch 10

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Conda](https://img.shields.io/badge/conda-environment-green)
![Course](https://img.shields.io/badge/course-AI%20Development-orange)
![Progress](https://img.shields.io/badge/tasks-5%2F31-informational)

Structured Python assignment repository for Infinite Learning Batch 10.  
This repository documents my progress from Python fundamentals toward more applied topics such as data structures, object-oriented programming, exploratory data analysis, and notebook-based data science workflows.

</div>

---

## Overview

This repository contains my Python assignments for the **AI Development** program at **Infinite Learning Batch 10**.  
The main purpose of this repository remains the official assignment track from the program, which documents my progress from Python fundamentals toward more applied topics.

In addition to the coursework, I also include selected practice from **FreeCodeCamp** and **HackerRank**. These materials are intentionally kept in the same repository as supporting evidence of continuous learning, concept reinforcement, and hands-on problem solving beyond mandatory submissions.

As a result, this repository serves two related purposes:

- Primary archive for Infinite Learning assignments
- Structured record of independent Python practice and review

This approach helps present a clearer picture of how I study, apply, and revisit Python concepts over time.

The progress indicator at the top of this README refers to the official Infinite Learning assignment track only.

---

## Learning Scope

### Primary Track: Infinite Learning

The central part of this repository is the assignment work completed as part of the **AI Development program at Infinite Learning Batch 10**.  
These files represent formal coursework and remain the main context of the repository.
The track now includes both script-based Python assignments and notebook-based data analysis work.

### Supplementary Track: FreeCodeCamp and HackerRank

The **FreeCodeCamp** and **HackerRank** folders are included as complementary study material.  
They show how I strengthen core Python concepts through extra exercises, review notes, small projects, debugging practice, and problem-solving drills outside the required assignment flow.

This combination makes the repository more representative of my actual learning process: not only completing assigned work, but also building consistency through self-directed practice.

---

## Repository Structure

```bash
├── README.md
├── .gitignore
├── environment.yml
├── tugas3.py
├── tugas4.py
├── tugas5.py
├── tugas6.py
├── tugas7_eda.ipynb
├── ringkasaan_tugas6.txt
├── assets/
│   └── screenshots/
├── docs/
├── FreeCodeCamp Certifications Python/
│   ├── Python Basics/
│   ├── Loops and Sequences/
│   ├── Dictionary and Sets/
│   ├── Error Handling/
│   ├── Classes and Objects/
│   └── Certification Projects/
└── HackerRank/
    ├── introduction/
    └── python/
```

---

## Current Coverage

### Infinite Learning Assignments

- [x] **Task 3 — Python Basics**
  Covers variables, data types, string manipulation, mathematical operations, list operations, and user input.

- [x] **Task 4 — Python Data Structures**
  Covers list, tuple, set, dictionary, nested structures, comprehensions, and membership checking.

- [x] **Task 5 — Python Function and Class**
  Covers function definitions, default arguments, return values, class design, methods, and `__str__`.

- [x] **Task 6 — Python Modules, File I/O, & Simple OOP**
  Covers NumPy statistics, pandas DataFrame usage, text file output, and an OOP-based `GradeBook` class.

- [x] **Task 7 — Mini Project: Exploratory Data Analysis (EDA)**
  Covers notebook-based exploratory analysis of a 209-country Worldometer COVID-19 dataset snapshot, including data structure inspection, missing-value auditing, distribution analysis, continent-level aggregation, positivity-rate cleaning, death and recovery outcome metrics, serious/critical case analysis, country-level benchmarking, and correlation heatmaps. Each major step is accompanied by written analytical insight, with particular emphasis on data integrity issues, testing-capacity disparities, and observation bias in reported global case counts.

- [ ] **Task 8 - 31 — Upcoming**

---

### FreeCodeCamp Practice

- **Python Basics**
  Covers review notes and small Python projects focused on core syntax, conditions, strings, and introductory logic.

- **Loops and Sequences**
  Covers repetition, iteration patterns, and sequence-based exercises.

- **Dictionary and Sets**
  Covers dictionary operations, set usage, validation logic, and additional topic notes.

- **Error Handling**
  Covers exception handling review material and debugging-focused exercises.

- **Classes and Objects**
  Covers class design, object behavior, and small object-oriented Python projects.

- **Certification Projects**
  Stores project-style exercises related to FreeCodeCamp Python certification preparation.

### HackerRank Practice

- **Introduction**
  Contains introductory Python problem-solving exercises used to strengthen syntax fluency and coding consistency.

---

## Key Files and Directories

- `tugas3.py` to `tugas6.py`
  Core Infinite Learning assignment files.

- `tugas7_eda.ipynb`
  Notebook-based Infinite Learning assignment for Task 7 EDA, containing step-by-step analysis, visualizations, and written insights.

- `ringkasaan_tugas6.txt`
  Output or supporting text file related to Task 6.

- `FreeCodeCamp Certifications Python/`
  Topic-based review notes and coding exercises completed as supplementary structured study.

- `HackerRank/`
  Short problem-solving exercises that support Python fundamentals and programming fluency.

- `assets/screenshots/`
  Reserved for supporting visuals when needed.

- `docs/`
  Reserved for additional project documentation.

- `environment.yml`
  Conda environment definition for reproducible local setup across script, notebook, data science, machine learning, and TensorFlow/Keras-based assignments.

- `.gitignore`
  Repository ignore rules for local files and generated artifacts.

---

## Tech Stack

- **Python 3.12**
- **Conda** (Environment Management)
- **Jupyter Notebook / Google Colab**
- **NumPy**
- **pandas**
- **Matplotlib**
- **Seaborn**
- **scikit-learn**
- **TensorFlow / Keras**

---

## How to Run

This project uses Conda for environment management to ensure consistency across different machines.

**1. Clone the repository:**

```bash
git clone https://github.com/Zendin110206/tugas_python_ai_b10.git
cd tugas_python_ai_b10
```

**2. Setup the Conda Environment:**
Create the environment and install all dependencies automatically using the provided configuration file:

```bash
conda env create -f environment.yml
```

**3. Activate the environment:**

```bash
conda activate env_daily_use
```

**4. Run the script-based files you want to review:**

```bash
python tugas3.py
python tugas4.py
python tugas5.py
python tugas6.py
python "FreeCodeCamp Certifications Python/Classes and Objects/Build_an_Email_Simulator.py"
python "HackerRank/introduction/python_if_else.py"
```

**5. Access notebook-based assignments:**

- **Task 7 EDA notebook:** [Open in Google Colab](https://colab.research.google.com/drive/1wtv8ZXdOkMeRhzEmK7W9CZ2DpTFmRc-o?usp=sharing)
- The repository keeps the Task 7 notebook file as `tugas7_eda.ipynb` for documentation and versioning purposes.
- The current Task 7 notebook is best reviewed through Google Colab because it depends on an external dataset file, `worldometer_data.csv`, which is intentionally not stored in this repository to keep the repository lighter.
- A fresh local clone of this repository does **not** include that dataset by default, so running the notebook locally requires downloading the Worldometer dataset separately and adjusting the notebook file path as needed.
- Upcoming notebook-heavy coursework, especially Tasks 8 through 12, may also continue to use a Colab-first workflow when the course provides external templates, datasets, or hosted notebook references.

---

## Learning Goals

Through this repository, I aim to:

- strengthen my Python fundamentals
- practice writing clearer and more structured code
- build consistency in documenting technical work
- reinforce coursework with additional self-directed exercises
- maintain a single organized record of formal and independent learning
- prepare a solid foundation for future AI and data-related projects

---

## Notes

This repository is part of my ongoing learning journey in programming and AI development.  
While the primary focus is still the official **Infinite Learning Batch 10** assignment path, the inclusion of **FreeCodeCamp** and **HackerRank** work is deliberate.

These additional folders show that I do not rely only on mandatory coursework. I also spend time reinforcing concepts independently through guided practice, review material, debugging exercises, and small coding projects.

Some notebook-based assignments also depend on external datasets and are therefore referenced through Google Colab links when that provides a cleaner and lighter repository structure.

I organize everything in one repository to reflect discipline, continuity, and a professional record of how I learn and improve over time.

---

## Author

**Muhammad Zaenal Abidin Abdurrahman** Telecommunication Engineering Undergraduate — Telkom University

- GitHub: [Zendin110206](https://github.com/Zendin110206)
- LinkedIn: [zendin1102](https://www.linkedin.com/in/zendin1102/)
