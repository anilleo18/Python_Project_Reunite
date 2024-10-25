class Parent1:
    def m1(self):
        print('parent 1 M1 method')


class Parent2:
    def m1(self):
        print('parent 2 M1 method')


class Kid(Parent2, Parent1):
    def m3(self):
        pass


k = Kid();
k.m1()


# ===============


class Sum_test:
    Total = 0

    def summer(self, *a):
        for x in a:
            Sum_test.Total = Sum_test.Total + x
        print(Sum_test.Total)


s = Sum_test()
s.summer(200, 3, 6)


class Sum_cons:
    conter = 0

    def __init__(self):
        Sum_cons.conter = Sum_cons.conter + 1


s = Sum_cons()
s2 = Sum_cons()
s3 = Sum_cons()
print(Sum_cons.conter)


# constructor Overloading

class cons_con:

    def __init__(self, *a):
        print("constructor with elements")


obj1 = cons_con()
obj2 = cons_con(90, 88)
obj3 = cons_con(90, 90000, 88)





