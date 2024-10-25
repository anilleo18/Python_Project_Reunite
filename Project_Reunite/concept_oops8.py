class Bicycle:
    a = 999;

    def __init__(self):
        self.b = 888

    def m1(self):
        pass


class Cycle(Bicycle):
    def __init__(self):
        super().__init__()
        self.c = 777

    def m2(self):
        pass


obj1 = Cycle()
obj1.m2()
obj1.m1()
print(obj1.a)
print(obj1.c)
print(obj1.b)
