class Student:

    students = []

    def __init__(self, name, student_id):
        # Append unique 'student' to 'students' List
        self.name = name
        self.student_id = student_id
        self.students.append(self)

    def __str__(self):
        return "Student " + self.name  # Text to display when printing Class

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):

    school_name = "Beaver UniUniversity"

    def get_school_name(self):
        return "This is a high school student."
