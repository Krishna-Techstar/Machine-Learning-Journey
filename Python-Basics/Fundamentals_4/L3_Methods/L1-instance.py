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
        

l1 = Laptop("16gb","512gb")
l2= Laptop("32gb", "1tb") 

l1.get_info()
l2.get_info()

Laptop.get_storage_type() #this can be access by both class and instance methods
l1.get_storage_type()