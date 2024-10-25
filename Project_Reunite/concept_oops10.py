class car:
    car_Model = 'LC'

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def m1(self):
        print(f'car details :{self.color} and {self.name}')


class Person:
    person_Gender = 'Female'

    def __init__(self, person_name, person_age):
        self.person_name = person_name
        self.person_age = person_age

    def person_m1(self):
        print("person name name and age is :")
        print(f'{self.person_name} and {self.person_name}')


class Employee(Person):
    employee_company = "HSBC"

    def __init__(self, esal, emobile_num, car):
        self.esal = esal
        self.emobile_num = emobile_num
        self.car = car

    def employee_m1(self):
        print(f'{self.car.color} and {self.car.name}')
        self.car.m1()
        print(self.car.car_Model)


obj1 = car('white', 'Merc')

e = Employee('100k', '99124', obj1)

e.employee_m1()

print(e.employee_company)

print(e.person_Gender)


class KID :

    college_name="LITAM"

    def __init__(self,Buses):
        self.Buses =Buses

print(KID.college_name)
obj1 =KID('5')




class Parent_1:

    def m1(self):
        pass
    def m2(self):
        pass
class parent_2(Parent_1):

    def m3(self):
        pass
    def m4(self):
        pass

class child(parent_2):
    def m5(self):
        pass


c=child()
c.m1()













