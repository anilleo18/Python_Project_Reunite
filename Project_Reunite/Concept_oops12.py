class Rider_P:

    def __init__(self):
        print("parent constructor")

    def car_rider(self):
        print("Car Rider")

    def bike_rider(self):
        print("bike Rider ")


class Rider_c(Rider_P):

    def __init__(self):
        super().__init__()
        print("child constructor")

    def bullock_rider(self):
        print("buklocks Rider ")

    def bike_rider(self):
        print("bike_rider+KTM Rider")


obj1 = Rider_c()
obj1.bike_rider()


###########

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def m1(self):
        print(self.name)
        print(self.age)


class Employee:

    def __init__(self, salary, person):
        self.salary = salary
        self.person = person

    def display(self):
        print(f'Employees are {person.name},{person.age},{self.salary}')


person = Person('ameer', 40)
e = Employee(200, person)
e.display()

mydict_details = {

    'car': ['audi', 'Benz'],
    'players': ['sachin', 'dravid', 'Noel'],
    'food': ['fish', 'chicken']

}

for k, v in mydict_details.items():
    print(f'{k}  and {v}')

for key, value in mydict_details.items():

    for val in value:

        if val in 'Noel':
            print("hey 'Noel is available here !!!")




