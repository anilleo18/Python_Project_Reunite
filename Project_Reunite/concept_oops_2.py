class University:
    departments = 'EEE'

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def method_university(self):
        print(f'{self.name} and {self.courses}')


class college:
    collge_dep = 'Inter'

    def __init__(self, grades, University):
        self.grades = grades
        self.University = University

    def college_method(self):
        print(f'printing {self.grades}')
        print(f'{self.University.departments}')
        self.University.method_university()
        print(self.University.name)
        print(self.University.courses)


obj1 = University('JNU', 'Mechanical courses')
c = college('A+', obj1)
c.college_method()
print(c.University.name)
print(c.University.courses)
