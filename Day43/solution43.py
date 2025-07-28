def student_marks():
    marks_dict = {}
    while True:
        name = input("Enter student name: ").strip()
        if name.lower() == 'done':
            break
        try:
            marks = float(input("Enter marks: ").strip())
            marks_dict[name] = marks
        except ValueError:
            print("Please enter a valid number for marks.")
    return marks_dict

# To run the function and print the result
if __name__ == "__main__":
    result = student_marks()
    print(result)
