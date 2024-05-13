data = [ (1,90), (2,60), (1,80), (2,50), (3,70), (3,85)]


students = {}

for rollno, marks in data:
    if rollno in students:
        students[rollno] = students[rollno] + marks 
    else:
        students[rollno] = marks
    


print(students)
