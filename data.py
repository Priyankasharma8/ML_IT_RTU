import csv
import random

branches = ['CIVIL', 'CSE', 'EE', 'ME', 'IT']
students = []

for i in range(100):
    student = {}
    student['10th Percentage'] = round(random.uniform(60, 100), 2)
    student['12th Percentage'] = round(random.uniform(60, 100), 2)
    student['Branch'] = random.choice(branches)
    students.append(student)

with open('students.csv', mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=['10th Percentage', '12th Percentage', 'Branch'])
    writer.writeheader()
    for student in students:
        writer.writerow(student)