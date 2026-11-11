# Nova University OOP Project

This folder contains a single Python script **`student_management.py`** that demonstrates object‑oriented programming concepts for a simple university management system.  The script provides:

- **Base class `Person`** – stores common attributes (`name`, `email`, `phone`) and a method to display them.
- **`Student` class** – inherits from `Person` and adds student‑specific data such as `student_id`, `department`, attendance and marks for Python, SQL, and Excel.
  - Encapsulated attendance with a property validator.
  - Helper methods to compute total/average marks, assign a grade, determine pass/fail, and check examination eligibility.
  - Presentation helpers that print both personal and academic details.
- **`Faculty` class** – also inherits from `Person` and stores faculty‑specific fields (`faculty_id`, `department`, `designation`).
- **In‑memory dictionaries** `students` and `faculties` that act as simple data stores.
- **Utility functions** for robust user input (`get_number`, `get_input`).
- **Menu‑driven CLI** (add, view, update, delete students/faculties, etc.) – the script prompts the user via the console.

---

## Quick Start

1. **Prerequisites**
   - Python 3.8+ installed and added to your `PATH`.
   - No external dependencies; the script uses only the standard library.

2. **Run the program**

   ```powershell
   cd C:\\nova-university-oop
   python student_management.py
   ```

   You will be presented with a text‑based menu.  Follow the prompts to add students, view records, or manage faculty members.

3. **Typical workflow**
   - **Add a student** – provide ID, personal details, attendance (0‑100), and marks for the three subjects.
   - **View students** – the program prints each student's personal information, attendance status, academic details, grade, and pass/fail result.
   - **Add a faculty** – similar to students but with faculty‑specific fields.
   - **View faculties** – displays faculty information.

---

## Code Overview

### Classes

```python
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def show_person_details(self):
        print("Name :", self.name)
        print("Email :", self.email)
        print("Phone :", self.phone)
```

```python
class Student(Person):
    def __init__(self, name, email, phone, student_id, department,
                 attendance, python_mark, sql_mark, excel_mark):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.department = department
        self.__attendance = attendance
        self.python_mark = python_mark
        self.sql_mark = sql_mark
        self.excel_mark = excel_mark

    # Attendance property with validation
    @property
    def attendance(self):
        return self.__attendance

    @attendance.setter
    def attendance(self, value):
        if 0 <= value <= 100:
            self.__attendance = value
        else:
            raise ValueError("Attendance must be between 0 and 100")
```

Key methods inside `Student` include:
- `total_mark`, `average_mark`, `grade`, `result`
- `attendance_eligible` – checks if attendance ≥ 75 %.
- `academic_details` and `student_details_show` – formatted console output.

```python
class Faculty(Person):
    def __init__(self, name, email, phone, faculty_id, department, designation):
        super().__init__(name, email, phone)
        self.faculty_id = faculty_id
        self.department = department
        self.designation = designation
```

### Helper Functions

- `get_number(message, minimum, maximum, decimal=False)` – repeatedly asks for numeric input until a valid value is supplied.
- `get_input(message)` – ensures non‑empty string input.

### Data Stores

```python
students = {}   # key: student_id, value: Student instance
faculties = {}  # key: faculty_id, value: Faculty instance
```

---

## Extending the Project

- **Persistence** – replace the in‑memory dictionaries with a simple JSON file or SQLite database.
- **GUI / Web UI** – wrap the core logic with a Flask/Django app or a desktop UI framework (Tkinter, PyQt).
- **Additional roles** – add `Staff`, `Course`, `Enrollment` classes to model a fuller university system.

---

## Screenshots

![Add Student Menu](/c:/nova-university-oop/Screenshots/Screenshot%202026-11-11%20114240.png)

![View Students Output](/c:/nova-university-oop/Screenshots/Screenshot%202026-11-11%20114442.png)

---

## License

This educational example is provided **as‑is** under the MIT License. Feel free to modify and reuse it for learning purposes.
