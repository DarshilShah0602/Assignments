# marks.py
"""
Marks Processing System Module
Handles all marks-related operations separately
"""

import math  # Predefined module usage (Requirement 8)
from datetime import datetime  # Predefined module (Requirement 8)

# Store marks data
marks_database = {}

def add_marks(student_id, subject, marks):
    """Add marks for a student"""
    if marks < 0 or marks > 100:
        return False, "Invalid marks range"
    
    if student_id not in marks_database:
        marks_database[student_id] = {}
    
    marks_database[student_id][subject] = {
        'marks': marks,
        'date': datetime.now().strftime("%Y-%m-%d"),
        'percentage': marks  # Direct percentage if out of 100
    }
    return True, "Marks added successfully"

def get_student_marks(student_id):
    """Get all marks for a student"""
    return marks_database.get(student_id, {})

def calculate_average(student_id):
    """Calculate average marks using math module"""
    if student_id not in marks_database:
        return 0
    
    marks_list = [data['marks'] for data in marks_database[student_id].values()]
    if not marks_list:
        return 0
    
    average = sum(marks_list) / len(marks_list)
    return math.ceil(average)  # Using math module (Requirement 8)

def calculate_grade(average):
    """Calculate grade based on average"""
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

def get_all_marks():
    """Get all marks records"""
    return marks_database