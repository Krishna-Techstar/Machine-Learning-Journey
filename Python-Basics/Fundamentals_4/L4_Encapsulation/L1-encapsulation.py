class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        self._balance = balance #private - data mangaing

    def get_balance(self):
        return self.__balance 
    
    def set_balance(self, newBalance):
        self.__balance = newBalance

acc1 = BankAccount("Krishna", 10_00000)


acc1.set_balance(80000)
print(acc1.name, acc1.get_balance())

