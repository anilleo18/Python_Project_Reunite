class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + self.amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount

    def print_statement(self):
        return f'The balance amount in statement is  {self.balance}'


class Savings(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance)

    def __str__(self):
        return f'Balance amount is {self.balance}'


s = Savings('Anil', 1000)
s.deposit(2000)
print(s)
