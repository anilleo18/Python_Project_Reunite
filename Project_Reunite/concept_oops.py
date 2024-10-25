class University:
    university_course = "GRAD"

    def __init__(self):
        print("university constructor")
        self.departmets = "ECE"
        self.doors='5-doors'

    def method_university(self):
        print("this is the Method university")


class Schools:

    def __init__(self):
        print("schools Constructor")
        self.university = University()

    def method_school(self):
        print("Schools Method")
        print(f'{self.university.departmets} and {self.university.university_course}')
        print(f'{self.university.doors}')


obj1 = Schools()
obj1.method_school()
