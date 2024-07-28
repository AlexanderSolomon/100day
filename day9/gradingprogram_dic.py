# Write a program that converts their scores to grades. 
# By the end of your program, you should have a new dictionary called student_grades 
# that should contain student names for keys and their grades for values.

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# The final version of the student_grades dictionary will be checked.

# DO NOT modify lines 1-7 to change the existing student_scores dictionary.

# DO NOT write any print statements.
# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] < 91 and student_scores[key] >= 81 :
        student_grades[key] = "Exceeds Expectations"    
    elif student_scores[key] < 81 and student_scores[key] >= 71 :
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
    
        
     
        
print(student_grades)