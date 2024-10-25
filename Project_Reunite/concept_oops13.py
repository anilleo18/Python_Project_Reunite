class Diploma:
    sub = ['english', 'hindi']

    def __init__(self):
        self.food = ['potato chips', 'Maggies']

    def method_v1(self):
        print("printing method_v1 method")

    @classmethod
    def method_v2(cls):
        print("printing Method_v2 method")

    @staticmethod
    def method_v3():
        print("pritning Method_v31111")


class Studies(Diploma):
    sub_new = ['townhouse', 'pinkies']

    def __init__(self):
        food_new = ['boodle', 'Raita']

    def method_c1(self):
        print("printing c1 method")
        super().method_v1()
        super().method_v2()
        super().method_v3()
        super().__init__()
        print(self.food)


    @classmethod
    def method_c2(cls):
        print("printing c2 method")

    @staticmethod
    def method_c3():
        print('printing c3')
        print(Diploma.sub)
        super(Studies, Studies).method_v3()




obj1 = Studies()
obj1.method_c1()
obj1.method_c3()
print(obj1.food)