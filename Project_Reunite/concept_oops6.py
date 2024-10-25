class Parent:
    parent_var = 90

    def __init__(self):
        print("parent Constructor")

    def m1(self):
        print("parent Instance method")

    @classmethod
    def m2(cls):
        print("parent class Method is running")

    @staticmethod
    def m3():
        print("parent Static Method is running")


class child(Parent):
    def __init__(self):

        super().__init__()
        print("child class constructor")

    def m1_child(self):
        print("child class Instance Methods")

    @classmethod
    def m2_child(cls):
        print("child class class Method")

    @staticmethod
    def m3_child():
        print("child static Method ")

c=child()
print(c.parent_var)
c.m1()
c.m2()
c.m3()

c.m1_child()
c.m2_child()
c.m3_child()
