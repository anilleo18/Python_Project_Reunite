class outer:
    def __init__(self):
        print("outer class constructor")

    def meth_outer(self):
        print("outer class method")

    class inner:
        def __init__(self):
            print("inner class constructor")

        def meth_inner(self):
            print("Inner class method")


obj1 = outer()

obj2 = outer().inner()
obj2.meth_inner()


##########################################


class Animal:

    def __init__(self):
        self.legs = "4"
        self.type = self.TypesofAnimals()
        self.food = self.foodtakenbyAnimal()
        print("Animal class const")

    class TypesofAnimals:

        def animaltypes(self):
            print("Animal are carnivor,omnivoures")

    class foodtakenbyAnimal:

        def foodeatenbyanimal(self):
            print("Animal eat beg and non veg foods")

        def fornoteaten(self):
            print("animal dont eat metals")


obj5 = Animal()
obj5.type.animaltypes()
obj5.food.foodeatenbyanimal()

obj6 = Animal()
obj6.food.fornoteaten()


class Student:

    def __init__(self):
        self.name = "anil"
        self.subjects = self.Studies()
        self.universities = self.Colleges()
        print("Hello this is student class Constructor")

    class Studies:

        def social(self):
            print("I want to read social")

        def science(self):
            print("i want to read science")

    class Colleges:

        def litam(self):
            print("college name is litam")

        def klu(self):
            print("college name in KLU")


s=Student()
print(s.name)
s.subjects.social()
s.universities.litam()
s.universities.klu()
