# Day 7 - Functions in Python

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to assign grade based on average
def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

# Function to print student report
def print_report(students):
    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = assign_grade(avg)
        print(f"Student: {name}, Average: {avg:.2f}, Grade: {grade}")

# Main program
students_data = {
    "Ravi": [85, 90, 78],
    "Sneha": [92, 88, 95],
    "Amit": [45, 50, 40],
    "Priya": [70, 75, 80]
}

print_report(students_data)
