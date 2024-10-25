class Avaiation_animals:

    def __init__(self, fly, color):
        self.fly = fly
        self.color = color
        self.carrots=90



    def m1(self):
        print(f'{self.fly} and {self.color}')



class birds(Avaiation_animals):


    def __init__(self, legs):
        self.legs = legs
        super().__init__(True, 'white')

    def m2(self):
        print(f'{self.legs + 10}')
        print(f'{self.fly}')
        print(f'{self.color}')
        print(f'{self.carrots}')



b = birds(10)
b.m2()





class Test:

    def __init__(self):
        print(id(self))


class Piss(Test):

    def m1(self):
        pass


p=Piss()
print(id(p))
