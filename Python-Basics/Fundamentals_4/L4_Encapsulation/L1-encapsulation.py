class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        self._balance = balance #private - data mangaing

acc1 = BankAccount("Krishna", 10_00000)

print(acc1.name, acc1._balance)

