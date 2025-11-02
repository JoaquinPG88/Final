class Product:
    """
    Clase para representar un producto.
    """
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        """
        Actualiza el stock del producto.
        :param quantity: La cantidad a añadir o restar del stock
        """
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock += quantity
    
    def __str__(self):
        return f"Producto {self.name} (ID: {self.product_id}) - Precio: {self.price} - Stock: {self.stock}"

class ProductManager:
    """
    Clase que gestiona la lista de productos y operaciones sobre ellos.
    """
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        """
        Añade un nuevo producto al inventario.
        :param product: Producto a añadir.
        """
        if product.product_id in self.products:
            raise ValueError(f"El producto con ID {product.product_id} ya existe.")
        self.products[product.product_id] = product
    
    def get_product(self, product_id):
        """
        Obtiene un producto por su ID.
        :param product_id: ID del producto a obtener.
        :return: Producto encontrado.
        """
        return self.products.get(product_id, None)
    
    def remove_product(self, product_id):
        """
        Elimina un producto del inventario.
        :param product_id: ID del producto a eliminar.
        """
        if product_id not in self.products:
            raise ValueError(f"El producto con ID {product_id} no existe.")
        del self.products[product_id]
 
