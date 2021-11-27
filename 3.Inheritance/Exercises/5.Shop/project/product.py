class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, new_quantity: int):
        if self.quantity >= new_quantity:
            self.quantity -= new_quantity

    def increase(self, new_quantity: int):
        self.quantity += new_quantity

    def __repr__(self):
        return self.name
