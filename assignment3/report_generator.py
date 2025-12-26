# report_generator.py
"""
Report Generation Module using Classes
Generates comprehensive student reports
"""

class StudentReport:
    """Class to generate student reports"""
    
    def __init__(self, student_id):
        self.student_id = student_id
        self.report_data = {}
    
    def add_section(self, section_name, data):
        """Add a section to the report"""
        self.report_data[section_name] = data
    
    def generate_text_report(self):
        """Generate a text-based report"""
        report = f"\n{'='*50}\n"
        report += f"STUDENT REPORT - ID: {self.student_id}\n"
        report += f"{'='*50}\n\n"
        
        for section, data in self.report_data.items():
            report += f"{section.upper()}:\n"
            report += f"{'-'*50}\n"
            
            if isinstance(data, dict):
                for key, value in data.items():
                    report += f"  {key}: {value}\n"
            else:
                report += f"  {data}\n"
            
            report += "\n"
        
        report += f"{'='*50}\n"
        return report
    
    def generate_summary(self):
        """Generate a summary report"""
        return f"Report for Student {self.student_id} with {len(self.report_data)} sections"


class BatchReport:
    """Class to generate reports for multiple students"""
    
    def __init__(self):
        self.reports = []
    
    def add_student_report(self, student_report):
        """Add a student report to batch"""
        self.reports.append(student_report)
    
    def generate_batch_summary(self):
        """Generate summary for all students"""
        summary = f"\nBATCH REPORT SUMMARY\n"
        summary += f"{'='*50}\n"
        summary += f"Total Students: {len(self.reports)}\n"
        
        for report in self.reports:
            summary += f"  - {report.generate_summary()}\n"
        
        return summary


# Testing the module independently (Requirement 9)
if __name__ == "__main__":
    print("Testing Report Generator Module")
    print(f"Module Name: {__name__}")
    print(f"Classes defined: StudentReport, BatchReport")
    
    # Create a test report
    test_report = StudentReport("TEST001")
    test_report.add_section("Student Info", {"Name": "Test Student", "Age": 20})
    test_report.add_section("Marks", {"Math": 95, "Science": 88})
    
    print("\n" + test_report.generate_text_report())
    print(test_report.generate_summary())