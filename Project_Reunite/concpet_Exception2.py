class Exception_2:

    def __init__(self):
        self.a = 90

    def m1(self, input, output):

        try:
            val = input / output

        except (Exception) as msg:

            print(f'we are in catch block {msg}')

        finally:
            print(f'we are inside finally block to perform code clean up ')

        return val


obj1 = Exception_2()
value = obj1.m1(300, 10)
print(value)
