# Assignment_5


This program:

Creates a dictionary with student names as keys and their marks as values

Takes a student’s name as input from the user

Displays the student’s marks if found

Shows an error message if the student does not exist



Task_1
Student_marks={"Alice":85,
               "Bob":78,
               "Charlie":92}

name=input("Enter the name: ")


if name in Student_marks:
    print(f"{name}'s  marks: {Student_marks[name]}")
    
else:
    print("Student not found: ")
    


This program:

Creates a list of numbers from 1 to 10

Extracts the first five elements

Reverses the extracted elements

Prints all results





Task_2

original_list=[1,2,3,4,5,6,7,8,9,10]

Extracted_first_five_elements=original_list[0:5]



reversed_extracted_elements=Extracted_first_five_elements[::-1]






print(f"original_lists: {original_list}")
print(f"Extracted_first_five_elements: {Extracted_first_five_elements}")
print(f"reversed_extracted_elements: {reversed_extracted_elements}")
