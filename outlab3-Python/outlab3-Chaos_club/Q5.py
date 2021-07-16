import argparse
import csv
import os
import sys

class NewParser(argparse.ArgumentParser):
    def error(self,message):
        sys.stderr.write('%s\n' %message)
        sys.exit(2)

def createDefFile(name_csv):
    if not os.path.exists(name_csv):
        with open(name_csv,'a') as f:
            writer = csv.writer(f)
            writer.writerow(['First Name',' Last Name',' Roll Number',' Gender',' Mobile',' Dept',' CGPA'])

parser = NewParser()
parser.add_argument("--first_name",required=True)
parser.add_argument("--last_name",required=True)
parser.add_argument("--roll_no",required=True)
parser.add_argument("--gender",required=True)
parser.add_argument("--mobile",required=True)
parser.add_argument("--dept",required=True)
parser.add_argument("--CGPA",required=True)

args = parser.parse_args()

fields = []
for arg in vars(args):
    fields.append(" "+getattr(args,arg))
fields[0] = fields[0][1:]
createDefFile('student_database.csv')
with open('student_database.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
print("Sucessfully Added!!")

