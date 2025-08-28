# File Read & Write Challenge 🖋️ + Error Handling Lab 🧪

This project is a simple Python exercise that combines **file I/O operations** with **error handling**.  
The program demonstrates how to:

1. **Read from a file** (`week3_assignment.py`).
2. **Write a modified version** of the file into a new file (`week3_assignment_modified.py`).
   - Each line from the original file is copied.
   - A separator (`*`) is added after each line.
3. **Handle user input safely** when searching for a file:
   - Prompts the user to enter a filename.
   - Tries to open and read the file.
   - Handles errors gracefully if the file does not exist, cannot be read, or other unexpected issues occur.

---

## 🔑 Features

- **File Read & Write Challenge 🖋️**  
  Reads all lines from a source file and writes them into a modified version with extra separators.

- **Error Handling Lab 🧪**  
  Uses `try` / `except` blocks to handle common errors:
  - `FileNotFoundError` → if the user enters a filename that does not exist.
  - `PermissionError` → if the program lacks permission to read the file.
  - `Exception` → catches any other unexpected errors.

---

## 🗂️ Files

- **`week3_assignment.py`** → Input file (original).
- **`week3_assignment_modified.py`** → Output file (modified).
- **`main.py`** (or the script you run) → Contains the logic for both challenges.

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Place a file named `week3_assignment.py` in the project directory (or edit the code to point to a different file).
3. Run the program:

```bash
python main.py
```
