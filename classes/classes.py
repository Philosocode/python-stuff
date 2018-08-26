# Students List
students = []


# Student Class
class Student:

    def __init__(self, name, student_id):
        # Append unique 'student' to 'students' List
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name  # Text to display when printing Class

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


# Inherit from Student
class HighSchoolStudent(Student):

    school_name = "Beaver UniUniversity"

    def get_school_name(self):
        return "This is a high school student."



# Create 'student', an Instance of Student()
mark = Student('Mark', '123')
james = HighSchoolStudent('James', '222')

print(james.get_school_name())

print(students)
print(mark)
