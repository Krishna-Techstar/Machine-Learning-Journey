class Product:
    Product="Details"
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Price of the product {self.name} is {self.price}.")

    @classmethod
    def get_count(cls):
        print(f"Total Product been created is {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - ((discount*price)/100)
        print(f"Discounted Price = {final_price}")

M1=Product("Iphone 15", 64999)
L1=Product("Lenovo Loq 15", 126999)

M1.get_info()
L1.get_info()
Product.get_count()

M1.calc_discount(M1.price,10)