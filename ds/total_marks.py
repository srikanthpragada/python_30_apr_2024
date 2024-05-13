data = [ (1,90), (2,60), (1,80), (2,50), (3,70), (3,85)]


students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks 


print(students)
