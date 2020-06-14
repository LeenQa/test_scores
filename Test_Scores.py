import json

"""
class for students
"""
class Student:

    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    """
    function to calculate the avergae mark of a student
    """
    def average_mark(self, scores):
        sum = 0
        count = 0
        for score in scores:
            sum += score
            count += 1
        return sum / count

    """
    function to determine wether this student has failed or not
    """
    def failed(self):
        if self.average_mark(self.scores) < 50:
            return True
        else:
            return False

"""
class for subject
"""
class Subject:

    def __init__(self, title, teacher, students):
        self.title = title
        self.teacher = teacher
        self.students = students


    """
    function that returns the top student in this subject
    """
    def top_student(self, students):
        max = 0
        for student in students:
            if student.average_mark(student.scores) > max:
                top_std = student.name
                max = student.average_mark(student.scores)
        return top_std
    """
    function that returns the failed student in this subject
    """
    def failed_students(self, students):
        failed = []
        for student in students:
            if student.failed() == True:
                failed.append(student.name)
        return failed

    def calculate_avg(self,students):
        sum = 0
        count = 0
        for student in students:
            sum += student.average_mark(student.scores)
            count += 1
        return sum / count
"""
Opening JSON file
"""
f = open('test_scores.json', )

data = json.load(f)

subjects = []

for name, subject in data.items():
    teacher=subject['Teacher']
    students=subject['Students']
    studlist=[]
    for s in students:
        name1=s['name']
        scores=s['scores']
        stud=Student(name1,scores)
        studlist.append(stud)
    mat=Subject(name,teacher,studlist)
    subjects.append(mat)
statistics=""
for sub in subjects:
    result=f"The average mark of {sub.title} is:{str(int(sub.calculate_avg(sub.students)*100)/100)} \n"
    statistics+=result
    print(result)

print("")
for m in subjects:
    result=f"Top Student in {m.title} is: {m.top_student(m.students)}\n"
    statistics+=result
    print(result)

print("")
statistics+="list of Failing Students:"+"\n"
print("list of Failing Students:")
for m in subjects:
    for name in m.failed_students(m.students):
        statistics+=name+"\n"
        print(name)

# Closing file
f.close()

"""
writing statistics on a file
"""
with open('statistics.txt', "r+") as file:
    contents = file.writelines(statistics)