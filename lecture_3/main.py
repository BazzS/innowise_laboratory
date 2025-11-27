def main():
    # 1. Student Data (The Starting Point)
    students = []
    
    # 2. Main Program Loop (The Menu)
    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")
        
        try:
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                add_new_student(students)
            elif choice == '2':
                add_grades_for_student(students)
            elif choice == '3':
                show_report(students)
            elif choice == '4':
                find_top_performer(students)
            elif choice == '5':
                print("Exiting program")
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

def add_new_student(students):
    """Option 1: Add a new student"""
    name = input("Enter student name: ").strip()
    
    # Check if student already exists
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student '{name}' already exists!")
            return
    
    # Create new student dictionary
    new_student = {
        "name": name,
        "grades": []
    }
    students.append(new_student)
    #print(f"Student '{name}' added successfully!")

def add_grades_for_student(students):
    """Option 2: Add grades for a student"""
    if not students:
        print("No students available. Please add a student first.")
        return
    
    name = input("Enter student name: ").strip()
    
    # Find the student
    student_found = None
    for student in students:
        if student["name"].lower() == name.lower():
            student_found = student
            break
    
    if not student_found:
        print(f"Student '{name}' not found!")
        return
        
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()
        
        if grade_input == 'done':
            break
            
        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student_found["grades"].append(grade)
            else:
                print("Invalid input. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def show_report(students):
    """Option 3: Show report (all students)"""
    if not students:
        print("No students available.")
        return
    
    print("\n--- Student Report ---")
    #print("-" * 40)
    all_average = []
    
    for student in students:
        name = student["name"]
        grades = student["grades"]
        
        if grades:
            average = sum(grades) / len(grades)
            all_average.append(average)

            print(f"{name}'s average grade is: {average}")
        else:
            print(f"{name} has not grades.")

        
        print("-" * 40)
        print(f"Max Average: {max[all_average]}")
        print(f"Min Average: {min[all_average]}")
        average_average = sum(all_average) / len(all_average)
        print(f"Overall Average: {average_average}")

def find_top_performer(students):
    """Option 4: Find top performer"""
    if not students:
        print("No students available.")
        return
    
    top_student = None
    top_average = -1
    
    for student in students:
        grades = student["grades"]
        if grades:
            average = sum(grades) / len(grades)
            if average > top_average:
                top_average = average
                top_student = student
    
    if top_student:
        print(f"The student with the highest average is {top_student['name']} with a grade of {top_average}")
    else:
        print("No students with grades available.")

if __name__ == "__main__":
    main()