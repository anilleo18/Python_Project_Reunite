class Country:
    place = 'Gulmarg'

    def __init__(self, hotel, season):
        self.hotel = hotel
        self.season = season

    def country_m1(self):
        print(f'{self.hotel} and {self.season}')


class State:
    place_state = "Kashmir"

    def __init__(self, no_of_days, Country):
        self.no_of_days = no_of_days
        self.Country = Country

    def State_methodm2(self):
        print(f'{self.no_of_days} and {self.Country.place} and {self.Country.season}')
        print(self.Country.season)


obj1 = Country('ITC-Welcome', 'Winter')
s = State(90, obj1)
s.State_methodm2()

