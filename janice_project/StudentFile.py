import sys
from DataFile import *

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

def getStudentInfo(student_id):
    student_info = getStudentList()
    selected_student = []
    for i in range(len(student_info)):
        if (student_info[i][0] == student_id):
            selected_student.extend(student_info[i])
            return selected_student

def inputStdId(inId):
        try:
            student_id = input(inId)
            if student_id.strip() == "":
                color.write("Student Id must not be empty\n","COMMENT")
                return inputStdId(inId)
            elif len(student_id) > 15:
                color.write("Invalid format\n","COMMENT")
                return inputStdId(inId)
            else:
                return student_id
        except ValueError:
            color.write("Exception in inputStdId(inId)\n","COMMENT")
            return inputStdId(inId)

def inputStudentAge(inAge):
        try:
            student_age = int(input(inAge))
            if student_age < 18:
                color.write("Age must not be below 18\n","COMMENT")
                return inputStudentAge(inAge)
            elif student_age > 120:
                color.write("Invalid age\n","COMMENT")
                return inputStudentAge(inAge)
            else:
                return student_age
        except ValueError:
            color.write("Please enter Numbers only without decimal\n","COMMENT")
            return inputStudentAge(inAge)
