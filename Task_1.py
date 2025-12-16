Student_marks={"Alice":85,
               "Bob":78,
               "Charlie":92}

name=input("Enter the name: ")


if name in Student_marks:
    print(f"{name}'s  marks: {Student_marks[name]}")
    
else:
    print("Student not found: ")
    
    