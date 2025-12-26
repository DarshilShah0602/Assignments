# attendance.py
"""
Attendance Management Module
Tracks student attendance separately
"""

from datetime import datetime, date  # Predefined module (Requirement 8)
import random  # Predefined module (Requirement 8)

attendance_records = {}

def mark_attendance(student_id, status='Present'):
    """Mark attendance for a student"""
    today = date.today().strftime("%Y-%m-%d")
    
    if student_id not in attendance_records:
        attendance_records[student_id] = {}
    
    attendance_records[student_id][today] = {
        'status': status,
        'timestamp': datetime.now().strftime("%H:%M:%S")
    }
    return True, f"Attendance marked as {status}"

def get_attendance(student_id):
    """Get attendance records for a student"""
    return attendance_records.get(student_id, {})

def calculate_attendance_percentage(student_id):
    """Calculate attendance percentage"""
    if student_id not in attendance_records:
        return 0
    
    records = attendance_records[student_id]
    total_days = len(records)
    present_days = sum(1 for record in records.values() if record['status'] == 'Present')
    
    if total_days == 0:
        return 0
    
    return round((present_days / total_days) * 100, 2)

def get_all_attendance():
    """Get all attendance records"""
    return attendance_records