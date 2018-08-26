# Create an empty List
students = []


# Get Title Case For Students
def get_students_titlecase():
    # We'll be storing the Title Case in a new List
    students_titlecase = []
    # For each Student in Students:
    for student in students:
        # Add the student's title case name to "students_titlecase" List
        students_titlecase.append(student['name'].title())
    return students_titlecase


# Same as above, but prints "students_titlecase" List
def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id):
    # Append student's name to "students" List
    student = {'name': name, 'student_id': student_id}
    students.append(student)


def save_file(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + '\n')
        f.close()
    except Exception:
        print("Could not save file.")


def read_file():
    try:
        f = open('students.txt', 'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file.")


read_file()
print_students_titlecase()

student_name = input("Enter student name:\n> ")
student_id = input("Enter student ID:\n> ")

add_student(student_name, student_id)
save_file(student_name)
