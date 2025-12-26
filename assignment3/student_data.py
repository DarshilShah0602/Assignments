# student_data.py
"""
Student Data Management Module
This module handles all student-related data operations
"""

# Dictionary to store student records
students = {}

def add_student(student_id, name, age, course):
    """Add a new student to the system"""
    if student_id in students:
        return False, "Student ID already exists"
    
    students[student_id] = {
        'name': name,
        'age': age,
        'course': course
    }
    return True, f"Student {name} added successfully"

def get_student(student_id):
    """Retrieve student information"""
    return students.get(student_id, None)

def get_all_students():
    """Get all students"""
    return students

def update_student(student_id, **kwargs):
    """Update student information"""
    if student_id not in students:
        return False, "Student not found"
    
    students[student_id].update(kwargs)
    return True, "Student updated successfully"

def delete_student(student_id):
    """Delete a student record"""
    if student_id in students:
        del students[student_id]
        return True, "Student deleted successfully"
    return False, "Student not found"
print("Module Name:", __name__)
# Module metadata (Requirement 9)
__name__ = "student_data"
__file__ = "student_data.py"
__dict__ = students
print("Module Name:", __name__)
print("File Name:", __file__)
print("Module Dictionary:", __dict__)
if __name__ == "__main__":
    # Testing the module independently
    print("Testing Student Data Module")
    add_student("S001", "John Doe", 20, "Computer Science")
    print(get_student("S001"))
