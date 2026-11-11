
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def show_person_details(self):
        print("Name :", self.name)
        print("Email :", self.email)
        print("Phone :", self.phone)


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

    # Attendance validation using encapsulation
    @property
    def attendance(self):
        return self.__attendance

    @attendance.setter
    def attendance(self, value):
        if 0 <= value <= 100:
            self.__attendance = value
        else:
            raise ValueError("Attendance must be between 0 and 100")

    def attendance_validate(self):
        return 0 <= self.attendance <= 100

    # Academic calculations
    def total_mark(self):
        return self.python_mark + self.sql_mark + self.excel_mark

    def average_mark(self):
        return self.total_mark() / 3

    def grade(self):
        avg = self.average_mark()

        if avg >= 80:
            return "Grade A"
        elif avg >= 70:
            return "Grade B"
        elif avg >= 60:
            return "Grade C"
        elif avg >= 50:
            return "Grade D"
        elif avg >= 40:
            return "Grade E"
        else:
            return "Grade F"

    def result(self):
        if self.average_mark() >= 50:
            return "Pass"
        else:
            return "Fail"

    # Checking attendance eligibility
    def attendance_eligible(self):
        if self.attendance >= 75:
            return "Eligible For Examination"
        else:
            return "Not Eligible For Examination"

    def academic_details(self):
        print("\nACADEMIC INFORMATION")
        print("Python Mark :", self.python_mark)
        print("SQL Mark :", self.sql_mark)
        print("Excel Mark :", self.excel_mark)
        print("Total Mark :", self.total_mark())
        print("Average Mark :", round(self.average_mark(), 2))
        print("Grade :", self.grade())
        print("Result :", self.result())

    def student_details_show(self):
        print("\nSTUDENT INFORMATION")
        print("Student ID :", self.student_id)
        self.show_person_details()
        print("Department :", self.department)
        print("Attendance :", self.attendance)
        print("Attendance Status :", self.attendance_eligible())
        self.academic_details()

    def role_information(self):
        print("\nStudent Role")
        print("Student ID :", self.student_id)
        print("Department :", self.department)


class Faculty(Person):
    def __init__(self, name, email, phone, faculty_id, department, designation):
        super().__init__(name, email, phone)

        self.faculty_id = faculty_id
        self.department = department
        self.designation = designation

    def faculty_details_show(self):
        print("\nFACULTY INFORMATION")
        print("Faculty ID :", self.faculty_id)
        self.show_person_details()
        print("Department :", self.department)
        print("Designation :", self.designation)

    def role_information(self):
        print("\nFaculty Role")
        print("Faculty ID :", self.faculty_id)
        print("Department :", self.department)
        print("Designation :", self.designation)


# Storing student and faculty records
students = {}
faculties = {}


# Function to get valid numeric input
def get_number(message, minimum, maximum, decimal=False):
    while True:
        try:
            if decimal:
                value = float(input(message))
            else:
                value = int(input(message))

            if minimum <= value <= maximum:
                return value
            else:
                print("Please enter a value between", minimum, "and", maximum)

        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to avoid empty inputs
def get_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value
        else:
            print("This field cannot be empty.")


# Adding a student
def add_student():
    print("\nADD STUDENT")

    student_id = get_input("Enter Student ID :")

    if student_id in students:
        print("Student ID already exists.")
        return

    name = get_input("Enter Student Name :")
    email = get_input("Enter Student Email :")
    phone = get_input("Enter Student Phone :")
    department = get_input("Enter Department :")

    attendance = get_number("Enter Attendance Percentage :", 0, 100, True)

    python_mark = get_number("Enter Python Mark :", 0, 100)
    sql_mark = get_number("Enter SQL Mark :", 0, 100)
    excel_mark = get_number("Enter Excel Mark :", 0, 100)

    student = Student(
        name, email, phone, student_id, department,
        attendance, python_mark, sql_mark, excel_mark
    )

    students[student_id] = student

    print("Student Added Successfully!")


# Displaying all students
def view_student():
    print("\nVIEW STUDENTS")

    if len(students) == 0:
        print("No student records found.")
    else:
        for student in students.values():
            student.student_details_show()


# Checking attendance
def check_attendance():
    print("\nCHECK ATTENDANCE")

    student_id = get_input("Enter Student ID :")

    if student_id in students:
        student = students[student_id]

        print("Student Name :", student.name)
        print("Attendance :", student.attendance, "%")
        print("Attendance Status :", student.attendance_eligible())

    else:
        print("Student Not Found.")


# Displaying academic result
def view_result():
    print("\nVIEW ACADEMIC RESULT")

    student_id = get_input("Enter Student ID :")

    if student_id in students:
        student = students[student_id]

        print("Student Name :", student.name)
        student.academic_details()

    else:
        print("Student Not Found.")


# Adding faculty
def add_faculty():
    print("\nADD FACULTY")

    faculty_id = get_input("Enter Faculty ID :")

    if faculty_id in faculties:
        print("Faculty ID already exists.")
        return

    name = get_input("Enter Faculty Name :")
    email = get_input("Enter Faculty Email :")
    phone = get_input("Enter Faculty Phone :")
    department = get_input("Enter Department :")
    designation = get_input("Enter Designation :")

    faculty = Faculty(
        name, email, phone, faculty_id, department, designation
    )

    faculties[faculty_id] = faculty

    print("Faculty Added Successfully!")


# Displaying faculty information
def view_faculty():
    print("\nVIEW FACULTY")

    if len(faculties) == 0:
        print("No faculty records found.")
    else:
        for faculty in faculties.values():
            faculty.faculty_details_show()


# Displaying information according to the role
def role_information():
    print("\n1. Student")
    print("2. Faculty")

    choice = get_number("Enter Your Choice :", 1, 2)

    if choice == 1:
        student_id = get_input("Enter Student ID :")

        if student_id in students:
            students[student_id].role_information()
        else:
            print("Student Not Found.")

    elif choice == 2:
        faculty_id = get_input("Enter Faculty ID :")

        if faculty_id in faculties:
            faculties[faculty_id].role_information()
        else:
            print("Faculty Not Found.")


# Main menu
def main_menu():
    while True:
        print("\n------- NOVA UNIVERSITY -------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Check Attendance Eligibility")
        print("4. View Academic Result")
        print("5. Add Faculty")
        print("6. View Faculty")
        print("7. Role Information")
        print("8. Exit")

        choice = get_number("Enter Your Choice :", 1, 8)

        if choice == 1:
            add_student()

        elif choice == 2:
            view_student()

        elif choice == 3:
            check_attendance()

        elif choice == 4:
            view_result()

        elif choice == 5:
            add_faculty()

        elif choice == 6:
            view_faculty()

        elif choice == 7:
            role_information()

        elif choice == 8:
            print("Thank You!")
            break


main_menu()
