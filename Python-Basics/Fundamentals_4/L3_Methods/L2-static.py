class Laptop:
    CPU = "Intel Core I5 9400f"
    GPU = "Nivdia GTX 1650"
    Storage_type = "SSD"
    Body = "Metalic"

    def __init__(self, Ram, Storage):
        self.Ram = Ram
        self.Storage = Storage

    @classmethod # decorator 
    def get_storage_type(cls):
        print(f"Stroage Type is {cls.Storage_type}")
        
    def get_info(self): #instance
        print(f"The Laptop Has {self.CPU} Processor, {self.GPU} GPU with {self.Body} Body and {self.Ram} Ram and {self.Storage} {self.Storage_type}")    
        
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - ((discount*price)/100)
        print(f"Discounted Price is = {final_price}")

        
l1 = Laptop("16gb","512gb")


#fnx => (price, discount) => final price
l1.calc_discount(50_000, 10)