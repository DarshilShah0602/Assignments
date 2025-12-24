students = {}

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

name1 = input("Enter student 1 name: ")
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
avg1 = calculate_average(m1, m2, m3)
students[name1] = avg1

name2 = input("Enter student 2 name: ")
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
avg2 = calculate_average(m1, m2, m3)
students[name2] = avg2

name3 = input("Enter student 3 name: ")
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
avg3 = calculate_average(m1, m2, m3)
students[name3] = avg3

for name in students:
    avg = students[name]
    grade = assign_grade(avg)
    print("Student:", name)
    print("Average:", avg)
    print("Grade:", grade)
    print()

top_student = max(students, key=students.get)
top_average = students[top_student]
print("Top Scorer:", top_student)
print("Top Average:", top_average)