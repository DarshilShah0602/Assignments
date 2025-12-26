# utils.py
"""
Utility Module - Reusable Functions
Can be used across multiple student applications
"""

import random
from datetime import datetime

def generate_student_id():
    """Generate a unique student ID"""
    prefix = "STU"
    number = random.randint(1000, 9999)
    return f"{prefix}{number}"

def validate_email(email):
    """Validate email format"""
    return '@' in email and '.' in email.split('@')[1]

def format_date(date_string=None):
    """Format date in readable format"""
    if date_string is None:
        return datetime.now().strftime("%B %d, %Y")
    return date_string

def calculate_age(birth_year):
    """Calculate age from birth year"""
    current_year = datetime.now().year
    return current_year - birth_year

def sanitize_input(text):
    """Sanitize user input"""
    return text.strip().title()

def display_menu(options):
    """Display a menu with options"""
    print("\n" + "="*50)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("="*50)

# Module properties demonstration (Requirement 9)
if __name__ == "__main__":
    print(f"Module Name: {__name__}")
    print(f"Module File: {__file__}")