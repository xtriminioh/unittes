
class Product:
    def __init__(self, name:str, price: float, discount:float = 0.0) -> None:
        self.name = name
        self.price = price
        self.discount = discount
