"""
Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.
"""

def student_data(student_id, student_name=None, student_class=None):
    if student_name:
        return f"Student ID: {student_id}\nStudent name: {student_name}\n"
    if student_class:
        return f"\nStudent ID: {student_id}\nClass: {student_class}\n"
    if student_name and student_class:
        return f"\nStudent ID: {student_id}\nStudent name: {student_name}\nClass: {student_class}\n"
    return f"\nStudent_ID: {student_id}\n"

print(student_data(student_id = 576, student_name="Mike Hodge"))
print(student_data(student_id = 68741))
print(student_data(student_id = 1234, student_class = "VI"))
print(student_data(student_id = 48965, student_name = "James Bond", student_class = "II"))