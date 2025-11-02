# main.py
from product_manager import Product, ProductManager
from cart_manager import Cart

def main():
    # Crear el gestor de productos y carrito
    product_manager = ProductManager()
    cart = Cart()

    # Crear productos
    product1 = Product(1, "Té de Romero", 5.0, 100)
    product2 = Product(2, "Café Orgánico", 3.0, 50)

    # Añadir productos al gestor de productos
    product_manager.add_product(product1)
    product_manager.add_product(product2)

    # Mostrar productos disponibles
    print("Productos disponibles:")
    print(product_manager.get_product(1))
    print(product_manager.get_product(2))

    # Añadir productos al carrito
    cart.add_item(product1, 2)
    cart.add_item(product2, 1)

    # Mostrar total del carrito
    print("\nTotal del carrito:", cart.calculate_total())

    # Realizar el checkout
    print("\nResultado del checkout:", cart.checkout())

if __name__ == "__main__":
    main()
 
