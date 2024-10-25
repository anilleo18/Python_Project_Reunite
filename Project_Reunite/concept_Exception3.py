from abc import *


class Exception_demo:

    @abstractmethod
    def excep_m1(self):
        pass

    @abstractmethod
    def excep_m2(self):
        pass


class Exception_main(Exception_demo):

    def excep_m1(self):
        print('providing implemenetation excep_m1')

    def excep_m2(self):
        print('providing implementation excep_m2')

    def excep_m3(self, input, output):

        try:
            val = input / output
            print(f'val is : {val} ')
        except (Exception) as msg:

            print(f'it is providing some execpetion{msg}')
        finally:
            print('code clean up happening')

        return val


e = Exception_main()
x = int(input('enter the number x :'))
y = int(input('enter the number y :'))
value = e.excep_m3(x, y)
print(f'hey this is value {value}')
