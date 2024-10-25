class Student:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def m1(self):
        return 'This is method one'
    
    def __str__(self):
        return f'hey this is student name {self.name} and salary is {self.salary}'


s=Student('anil',90000)

print(s)


