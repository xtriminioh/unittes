from product import Product

class ShoppingCart:
    def __init__(self) -> None:
        self.__products: List[Product] = []

    @property
    def products(self):
        """Se crea una propiedad para mostrar los productos
            que contenga el carrito de compras - decorado @propety"""
        return self.__products.copy()

    def add_product(self, product: Product) -> None:
        if isinstance(product,Product):
            self.__products.append(product)

    def empty(self) -> bool:
        return len(self.__products) == 0

    def has_products(self) -> bool:
        return not self.empty()


    
