from abc import *


# abc = Abstract base Class :
class I_phone:

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def ios_button(self):
        pass


class phone(I_phone):

    def screen(self):
        return 25


p = phone()
print(p.screen())


class Android(I_phone):
    def screen(self):
        return 3000;


a = Android()
print(a.screen())


class vechile:

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def Seats(self):
        pass

class car_lexus(vechile):

    def engine(self):
        return '2.5CC'
    def Seats(self):
        return '7 doors'

c=car_lexus()
print(c.engine())
print(c.Seats())



class DbInterface:

    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class sysInterface(DbInterface):

    def connect(self):
        print('connecting to sys database')

    def disconnect(self):
        print('dis connecting to sys base')

class AzureInterface(DbInterface):

    def connect(self):
        print('connecting the Azure interface')

    def disconnect(self):
        print('Dis connecting the Azure Interface  ')

dbname=input("enter the dbname :")
classname=globals()[dbname]  #here it is converting string into class name
obj1=classname() # After str converted to class name we are assigning it to objectvariable
obj1.connect()
obj1.disconnect()









