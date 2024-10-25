# class concept_1:
#
#     def __int__(self):
#         pass
#
#     def method_one(self, a, b):
#         print(a + b)
#
#     def method_two(self, mylist):
#         mylist_2 = sorted(mylist)
#         return mylist_2
#
#
# obj1 = concept_1()
# obj1.method_one(20, 30)
# mylist_3 = obj1.method_two([992, 22, 333, 45])
# print(mylist_3)
import sys


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def talking(self):
        print(self.name)
        print(self.age)
        print(self.gender)


obj1 = Student('anil', 35, 'male')
# Student.talking(obj1)
obj1.talking()


class Tester:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def m1(self):
        print(self.a)
        print(self.b)


obj2 = Tester(2, 3)
obj3 = Tester(30, 40)
obj2.a = 200
obj2.b = 300
obj2.m1()
obj3.m1()


class veggie:
    rate = 300

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        print("print it as veggie class ")

    def method_veggie(self):
        print("class veggie method")


obj1 = veggie("potato", "sonam brand")
obj1.method_veggie()
print(obj1.rate)

obj2 = veggie("potato", "sonam brand")


# class Banking:
#     Bank_name = "SBI"
#
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount:float):
#         self.balance = self.balance + amount
#         print("Deposited Amount:", self.balance)
#
#     def withdrwaw(self, amount:float):
#         if self.balance > amount:
#             self.balance = self.balance - amount
#         else:
#             sys.exit()
#         return self.balance
#
#
# print(Banking.Bank_name)
# obj1 = Banking("Anil")
#
# while True:
#
#     option = input("please enter the option :")
#     if option == 'D':
#         print("we are doing with deposit operation")
#         amount = input("enter the amount: ")
#         obj1.deposit(int(amount))
#     else:
#         print("we are doing withdraw deposits")
#         amount = input("enter the amount: ")
#         obj1.withdrwaw(int(amount))
#
#


class Student:
    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setsalary(self, salary):
        self.salary = salary

    def getsalary(self):
        return self.salary

    def setschool(self, school):
        self.school = school

    def getschool(self):
        return self.school


obj1 = Student()
obj1.setsalary("10000K")
obj1.setname("Anil")
obj1.setschool("MSRP")

print(obj1.getsalary())
print(obj1.getname())
print(obj1.getschool())

obj2 = Student();
obj2.setname("AK")
obj2.setsalary("900k")

print(obj2.getname())
print(obj2.getsalary())


class Banker:
    bank_name = "ADCB"

    def __init__(self, amount):
        self.amount = amount

    @classmethod
    def bank_waste(cls):
        cls.bank_name = "SBI"
        cls.amount = 500


obj1 = Banker(200)
print(obj1.bank_name)
print(obj1.amount)
obj1.bank_waste()
print("-----")
print(obj1.bank_name)
print(obj1.amount)  # with cls varaible we can change instance variables
print(Banker.amount)


class Checkers:
    legs_aninaml = 4

    @classmethod
    def legchecker(cls):
        print(f'legs of animal are {cls.legs_aninaml}')


Checkers.legchecker()


# Creation of objects

class ObjectChecker:
    counter = 0

    def __init__(self):
        self.a = 300
        ObjectChecker.counter += 1

    @classmethod
    def objectcheking(cls):
        print(f'the counter is comings as {ObjectChecker.counter}')

    @staticmethod
    def meth_m1(a, b):
        print(f'a * b is {a * b}')


obj1 = ObjectChecker()
obj2 = ObjectChecker()
obj3 = ObjectChecker()
obj4 = ObjectChecker()
ObjectChecker.objectcheking()
ObjectChecker.meth_m1(20, 30)


class Employee:

    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print(f'printing  {self.eno}')
        print(f'printing  {self.ename}')
        print(f'printing  {self.esal}')


class Test:

    def modify(emp):
        emp.esal = emp.esal + 10000
        emp.display()


e = Employee(111, "Anil", 5000)
Test.modify(e)
