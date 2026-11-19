
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = {}


class Course:
    def __init__(self, course_code, title, credit):
        self.course_code = course_code
        self.title = title
        self.credit = credit


def calculate_grade(mark):
    if mark < 0 or mark > 100:
        raise ValueError("Marks must be between 0 and 100.")

    if mark >= 80:
        return "A+", 4.00
    elif mark >= 75:
        return "A", 3.75
    elif mark >= 70:
        return "A-", 3.50
    elif mark >= 65:
        return "B+", 3.25
    elif mark >= 60:
        return "B", 3.00
    elif mark >= 55:
        return "B-", 2.75
    elif mark >= 50:
        return "C+", 2.50
    elif mark >= 45:
        return "C", 2.25
    elif mark >= 40:
        return "D", 2.00
    else:
        return "F", 0.00


class ResultManager:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name):
        if not student_id or not name.strip():
            print("Student ID and name are required.")
            return

        if student_id in self.students:
            print("Student ID already exists.")
            return

        self.students[student_id] = Student(student_id, name)
        print("Student added successfully.")

    def add_course(self, course_code, title, credit):
        if not course_code or not title.strip():
            print("Course code and title are required.")
            return

        if course_code in self.courses:
            print("Course code already exists.")
            return

        if credit <= 0:
            print("Credit must be greater than zero.")
            return

        self.courses[course_code] = Course(
            course_code, title, credit
        )
        print("Course added successfully.")

    def enter_marks(self, student_id, course_code, mark):
        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter marks from 0 to 100.")
            return

        self.students[student_id].marks[course_code] = mark
        print("Marks entered successfully.")

    def calculate_cgpa(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")

        student = self.students[student_id]

        total_points = 0
        total_credits = 0

        for course_code, mark in student.marks.items():
            course = self.courses[course_code]
            grade, point = calculate_grade(mark)

            total_points += point * course.credit
            total_credits += course.credit

        if total_credits == 0:
            return 0.00

        return total_points / total_credits

    def get_result_sheet(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        print("\n========== STUDENT RESULT SHEET ==========")
        print("Student ID:", student.student_id)
        print("Student Name:", student.name)

        print("-" * 65)
        print(f"{'Course':<12}{'Marks':<10}{'Grade':<10}{'Point':<10}{'Credit'}")
        print("-" * 65)

        if not student.marks:
            print("No marks have been entered yet.")

        for course_code, mark in student.marks.items():
            course = self.courses[course_code]
            grade, point = calculate_grade(mark)

            print(
                f"{course_code:<12}{mark:<10.2f}"
                f"{grade:<10}{point:<10.2f}{course.credit}"
            )

        cgpa = self.calculate_cgpa(student_id)

        print("-" * 65)
        print(f"CGPA: {cgpa:.2f}")
        print("==========================================\n")


def main():
    manager = ResultManager()

    while True:
        print("\n===== STUDENT RESULT MANAGER =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enter Marks")
        print("4. Show Result Sheet")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            manager.add_student(student_id, name)

        elif choice == "2":
            course_code = input("Enter Course Code: ").strip()
            title = input("Enter Course Title: ").strip()

            try:
                credit = float(input("Enter Course Credit: "))
                manager.add_course(course_code, title, credit)
            except ValueError:
                print("Please enter a valid credit value.")

        elif choice == "3":
            student_id = input("Enter Student ID: ").strip()
            course_code = input("Enter Course Code: ").strip()

            try:
                mark = float(input("Enter Marks (0-100): "))
                manager.enter_marks(student_id, course_code, mark)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            student_id = input("Enter Student ID: ").strip()
            manager.get_result_sheet(student_id)

        elif choice == "5":
            print("Thank you for using Student Result Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
  
