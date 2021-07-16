
import sys

class Student:
    """Lets see"""
    def __init__(self,num_students,grades,credits):
        self.num_students = num_students
        self.grades = grades
        self.credits = credits
    def CPI(self):
       i,sum = 0,0
       while i < len(grades) :
            sum = sum + grades[i]*credits[i]
       print("%.4d" %sum)


with open(sys.argv[1]) as f:
    for l in f:
        print l.strip().split("---")

