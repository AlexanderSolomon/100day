# Input a Python list of student heights
student_heights = [156, 178, 165, 171, 187]

print (len(student_heights))
print(sum(student_heights))


m = 0
s = 0
f = 0
for student in student_heights: 
    m += student
    s += 1
    f = m/s
print(m)
print(s)
print(f)
    
# Example Output 1
# total height = 857
# number of students = 5
# average height = 171