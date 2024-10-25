class IamtooyoungException(Exception):

    def __init__(self, args):
        self.args = args

90
class IamtoooldException(Exception):

    def __init__(self, args):
        self.args = args


age = int(input('enter number :'))
if age<90:
    raise IamtooyoungException('hello you are too young')
elif age>90:
    raise IamtoooldException('hello you are too old')
else:
    print('here corect age')
