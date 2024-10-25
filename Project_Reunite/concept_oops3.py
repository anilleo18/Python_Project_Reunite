class Lover:
    Lover_Name = "Navya"

    def __init__(self):
        self.Lover_Age = 60

    def m1(self):
        print("M1 Method")


class Friend:
    Friend_name = 'Aanya'

    def __init__(self):
        self.Friend_age = 90

    def m2(self):
        obj1 = Lover()
        obj1.m1()
        print(obj1.Lover_Age)
        print(self.Friend_age)
        print('M2 Method')


f = Friend()
f.m2()
