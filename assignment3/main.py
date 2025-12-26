# main.py
"""
Student Management System - Main Program
Demonstrates modular programming by integrating all modules
"""

# Demonstration of different import methods (Requirement 5)
import student_data  # Standard import
from marks import add_marks, calculate_average, calculate_grade  # from...import
from attendance import *  # import all (use cautiously in production)
import fees as fee_module  # Module alias (Requirement 5)
from report_generator import StudentReport, BatchReport
import utils
import marks 
import math, random  # Multiple imports (Requirement 5, 8)
from datetime import datetime  # Predefined module (Requirement 8)


def display_main_menu():
    """Display the main menu"""
    options = [
        "Add Student",
        "Add Marks",
        "Mark Attendance",
        "Manage Fees",
        "Generate Report",
        "View All Students",
        "Exit"
    ]
    utils.display_menu(options)


def add_student_interactive():
    """Interactive function to add student"""
    print("\n--- Add New Student ---")
    
    # Generate student ID using utils module (Requirement 6)
    student_id = utils.generate_student_id()
    print(f"Generated Student ID: {student_id}")
    
    name = input("Enter student name: ")
    name = utils.sanitize_input(name)  # Using reusable utility
    
    age = int(input("Enter student age: "))
    course = input("Enter course: ")
    
    # Using student_data module (Requirement 2)
    success, message = student_data.add_student(student_id, name, age, course)
    print(message)
    
    return student_id if success else None


def add_marks_interactive(student_id=None):
    """Interactive function to add marks"""
    print("\n--- Add Marks ---")
    
    if student_id is None:
        student_id = input("Enter Student ID: ")
    
    # Check if student exists
    student = student_data.get_student(student_id)
    if not student:
        print("Student not found!")
        return
    
    print(f"Adding marks for: {student['name']}")
    subject = input("Enter subject: ")
    marks = float(input("Enter marks (0-100): "))
    
    # Using marks module (Requirement 3)
    success, message = add_marks(student_id, subject, marks)
    print(message)


def mark_attendance_interactive(student_id=None):
    """Interactive function to mark attendance"""
    print("\n--- Mark Attendance ---")
    
    if student_id is None:
        student_id = input("Enter Student ID: ")
    
    student = student_data.get_student(student_id)
    if not student:
        print("Student not found!")
        return
    
    print(f"Marking attendance for: {student['name']}")
    print("Status: 1. Present  2. Absent  3. Late")
    choice = input("Enter choice: ")
    
    status_map = {'1': 'Present', '2': 'Absent', '3': 'Late'}
    status = status_map.get(choice, 'Present')
    
    # Using attendance module (Requirement 7)
    success, message = mark_attendance(student_id, status)
    print(message)


def manage_fees_interactive(student_id=None):
    """Interactive function to manage fees"""
    print("\n--- Fee Management ---")
    
    if student_id is None:
        student_id = input("Enter Student ID: ")
    
    student = student_data.get_student(student_id)
    if not student:
        print("Student not found!")
        return
    
    print(f"Fee management for: {student['name']}")
    print("1. Set Fee Structure")
    print("2. Make Payment")
    print("3. View Fee Status")
    
    choice = input("Enter choice: ")
    
    # Using fees module with alias (Requirement 5, 7)
    if choice == '1':
        total_fee = float(input("Enter total fee: "))
        installments = int(input("Enter number of installments: "))
        success, message = fee_module.set_fee_structure(student_id, total_fee, installments)
        print(message)
    
    elif choice == '2':
        amount = float(input("Enter payment amount: "))
        success, message = fee_module.make_payment(student_id, amount)
        print(message)
    
    elif choice == '3':
        status = fee_module.get_fee_status(student_id)
        if status:
            print(f"Total Fee: {status['total_fee']}")
            print(f"Paid: {status['paid']}")
            print(f"Balance: {status['balance']}")
        else:
            print("No fee record found")


def generate_comprehensive_report(student_id=None):
    """Generate comprehensive report using report_generator module"""
    print("\n--- Generate Report ---")
    
    if student_id is None:
        student_id = input("Enter Student ID: ")
    
    student = student_data.get_student(student_id)
    if not student:
        print("Student not found!")
        return
    
    # Using class-based report generator (Requirement 4)
    report = StudentReport(student_id)
    
    # Add student information section
    report.add_section("Student Information", student)
    
    # Add marks section (Requirement 7 - integration)
    student_marks = marks.get_student_marks(student_id)
    if student_marks:
        average = calculate_average(student_id)
        grade = calculate_grade(average)
        marks_data = {
            'Subjects': student_marks,
            'Average': average,
            'Grade': grade
        }
        report.add_section("Academic Performance", marks_data)
    
    # Add attendance section (Requirement 7 - integration)
    attendance_data = get_attendance(student_id)
    if attendance_data:
        percentage = calculate_attendance_percentage(student_id)
        attendance_info = {
            'Total Days': len(attendance_data),
            'Attendance Percentage': f"{percentage}%"
        }
        report.add_section("Attendance", attendance_info)
    
    # Add fee section (Requirement 7 - integration)
    fee_status = fee_module.get_fee_status(student_id)
    if fee_status:
        report.add_section("Fee Status", {
            'Total Fee': fee_status['total_fee'],
            'Paid': fee_status['paid'],
            'Balance': fee_status['balance']
        })
    
    # Generate and display report
    print(report.generate_text_report())


def view_all_students():
    """View all students in the system"""
    print("\n--- All Students ---")
    students = student_data.get_all_students()
    
    if not students:
        print("No students found!")
        return
    
    for student_id, info in students.items():
        print(f"\nID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Course: {info['course']}")
        print("-" * 50)


def demonstrate_module_properties():
    """Demonstrate built-in module properties (Requirement 9)"""
    print("\n--- Module Properties Demonstration ---")
    print(f"Main module name: {__name__}")
    print(f"Main module file: {__file__}")
    print(f"Student data module: {student_data.__name__}")
    print(f"Available modules: student_data, marks, attendance, fees, report_generator, utils")
    print(f"Math module constants: Pi = {math.pi}, E = {math.e}")
    print(f"Current datetime: {datetime.now()}")


def quick_demo():
    """Quick demonstration of the complete system (Requirement 10)"""
    print("\n" + "="*50)
    print("QUICK DEMO - Complete Modular Student Management System")
    print("="*50)
    
    # Add sample students
    print("\n1. Adding students...")
    student_data.add_student("S001", "Alice Johnson", 20, "Computer Science")
    student_data.add_student("S002", "Bob Smith", 21, "Mathematics")
    print("✓ Students added")
    
    # Add marks
    print("\n2. Adding marks...")
    add_marks("S001", "Python Programming", 95)
    add_marks("S001", "Data Structures", 88)
    add_marks("S002", "Calculus", 92)
    print("✓ Marks added")
    
    # Mark attendance
    print("\n3. Marking attendance...")
    mark_attendance("S001", "Present")
    mark_attendance("S002", "Present")
    print("✓ Attendance marked")
    
    # Set fees
    print("\n4. Setting up fees...")
    fee_module.set_fee_structure("S001", 50000, 4)
    fee_module.make_payment("S001", 12500)
    print("✓ Fees configured")
    
    # Generate report
    print("\n5. Generating comprehensive report...")
    generate_comprehensive_report("S001")
    
    # Demonstrate module properties
    demonstrate_module_properties()
    
    print("\n" + "="*50)
    print("Demo completed successfully!")
    print("="*50)


def main():
    """Main function - Entry point of the program"""
    print("\n" + "="*60)
    print(" STUDENT MANAGEMENT SYSTEM - MODULAR ARCHITECTURE")
    print("="*60)
    
    # Ask if user wants quick demo
    demo_choice = input("\nWould you like to see a quick demo? (y/n): ").lower()
    if demo_choice == 'y':
        quick_demo()
        print("\nPress Enter to continue to interactive mode...")
        input()
    
    # Interactive mode
    while True:
        display_main_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            add_student_interactive()
        elif choice == '2':
            add_marks_interactive()
        elif choice == '3':
            mark_attendance_interactive()
        elif choice == '4':
            manage_fees_interactive()
        elif choice == '5':
            generate_comprehensive_report()
        elif choice == '6':
            view_all_students()
        elif choice == '7':
            print("\nThank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


# Entry point check (Requirement 10)
if __name__ == "__main__":
    main()