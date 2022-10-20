class ProductDiscountError(Exception):
    """Esta clase esta creada realizar los errores.
        Ejemplo: que un descuento sea mayor al precio del producto."""
    pass

class Product:
    def __init__(self, name:str, price: float, discount:float = 0.0) -> None:
        self.name = name
        self.price = price

        if discount > price:
            raise ProductDiscountError('Lo sentimos, el descuento no puede ser mayor al precio.')
        self.discount = discount
