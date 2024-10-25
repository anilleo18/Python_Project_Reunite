class Reserviour:
    Res = "ING"

    def __init__(self, company_name, company_city):
        self.company_name = company_name
        self.company_city = company_city

    def Reserviour_m1(self):
        print(f'the values of reservioir are {self.company_city} and {self.company_name}')


class well:
    well_var = "PNG"

    def __init__(self, core_mineral, Reserviour):
        self.core_mineral = core_mineral
        self.Reserviour = Reserviour

    def well_m1(self):
        print(f'{self.core_mineral}')
        print(f'{self.Reserviour.company_name}')
        print(f'{self.Reserviour.company_city}')
        self.Reserviour.Reserviour_m1()
        self.Reserviour.Res


obj1 = Reserviour("BPCL", "Guntur")
w = well('Bauxite', obj1)
w.well_m1()
print(obj1.Res)
w.Reserviour
