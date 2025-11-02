class Cart:
    """
    Clase que representa un carrito de compras.
    """
    def __init__(self):
        self.items = []  # Lista de productos en el carrito

    def add_item(self, product, quantity):
        """
        Añade un producto al carrito con la cantidad indicada.
        :param product: Producto a añadir
        :param quantity: Cantidad del producto
        """
        for item in self.items:
            if item.product_id == product.product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def calculate_total(self):
        """
        Calcula el total del carrito sumando los precios de los productos.
        :return: Total del carrito
        """
        return sum(item.get_total() for item in self.items)

    def checkout(self):
        """
        Realiza el pago y vacía el carrito.
        :return: Resultado de la compra.
        """
        total = self.calculate_total()
        if total > 0:
            self.items.clear()  # Vaciar el carrito
            return f"Compra realizada con éxito. Total: {total}"
        return "El carrito está vacío."

class CartItem:
    """
    Representa un ítem en el carrito, que es un producto con una cantidad específica.
    """
    def __init__(self, product, quantity):
        self.product_id = product.product_id
        self.name = product.name
        self.price = product.price
        self.quantity = quantity

    def get_total(self):
        """
        Calcula el total del ítem (precio * cantidad).
        :return: Total del ítem.
        """
        return self.price * self.quantity
 
