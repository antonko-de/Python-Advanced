'''Write a program that reads students' names and their grades and adds them to the student record.
On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and grade.
For each student print all his/her grades and finally his/her average grade, 
formatted to the second decimal point in the format: "{student's name} -> 
{grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter.
'''
from statistics import mean

GRADES_RECEIVED  = int(input())

stud_dict = {}

for _ in range(GRADES_RECEIVED):
   name, grade = input().split()

   if stud_dict.get(name) == None:
        stud_dict[name] = [float(grade)]
   
   else:
        stud_dict[name].append(float(grade)) 





for student, records in stud_dict.items():
    grades = ' '.join(map(lambda x: f"{x:.2f}",records))
    avg = sum(records) / len(records)
    print(f"{student} -> {grades} (avg: {avg:.2f})")