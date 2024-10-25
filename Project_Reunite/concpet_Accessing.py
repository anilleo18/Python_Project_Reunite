class Tester:
    alpha = 100
    _beta = 900  # Protected variable
    __gamma = 1000  ## Private Variable

    def __init__(self):
        self.delta = 1500

    def Tester_m1(self):
        penta = 800


class QA(Tester):

    def qa_m1(self):
        print(Tester.alpha)
        print(Tester._beta)
        print(self.delta)


class Assurance:

    def Ass_m1(self):
        print(Tester.alpha)
        print(Tester._beta)


obj2 = Assurance()
obj2.Ass_m1()
