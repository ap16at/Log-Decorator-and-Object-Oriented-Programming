# Andrew Perez-Napan
# ap16at
# Due Date: 1-29-21
# The program in this file is the individual work of Andrew Perez-Napan

import math


class Student(object):
    def __init__(self, firstname, lastname, gender, status, gpa):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.status = status
        self.gpa = gpa

    def show_myself(self):
        print('Firstname: {0} | Lastname: {1} | Gender: {2} | Status: {3} | Gpa: {4:.2f}'
              .format(str(self.firstname), str(self.lastname), str(self.gender), str(self.status), self.gpa))

    def study_time(self, study_time):
        self.gpa = self.gpa + math.log10(study_time)
        if self.gpa > 4.0:
            self.gpa = 4.0
            return self.gpa
        else:
            return self.gpa


if __name__ == "__main__":
    student_list = [Student('Mike', 'Barnes', 'Male', 'Freshman', 4),
                    Student('Jim', 'Nickerson', 'Male', 'Sophomore', 3),
                    Student('Jack', 'Indabox', 'Male', 'Junior', 2.5),
                    Student('Jane', 'Miller', 'Female', 'Senior', 3.6),
                    Student('Mary', 'Scott', 'Female', 'Senior', 2.7)]

    for student in student_list:
        student.show_myself()
