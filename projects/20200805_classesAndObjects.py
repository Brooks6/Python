class Students:
    def __init__(self, name, major, gpa, isOnProbation):
        self.name = name#self is refer to actual object
        self.major = major
        self.gpa = gpa
        self.isOnprobation = isOnProbation

'''
from Students import Students
⬇
from student file, we want to import student class
'''
stu1 = Students("z23", "commerce", 3.8, False)
print(stu1.name)