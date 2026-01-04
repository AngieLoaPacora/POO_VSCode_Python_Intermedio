class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, quantity):
        self.quantity = quantity

    def update_price(self, price):
        self.price = price

    def __str__(self):
        return f"Producto: {self.name}, Cantidad: {self.quantity}, Precio: $ {self.price:.2f}"

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity, price):
        if name in self.inventory:
            print(f"El producto '{name}' ya existe. Actualizando datos.")
            self.inventory[name].update_quantity(quantity)
            self.inventory[name].update_price(price)
        else:
            self.inventory[name] = Product(name, quantity, price)
            print(f"Producto '{name}' agregado al inventario")

    def list_products(self):
        if not self.inventory:
            print("El inventario está vacío.")
            return
        print("\nLista de Productos en el Inventario:")
        for product in self.inventory.values():
            print(product)

    def search_product(self, name):
        if name in self.inventory:
            print(self.inventory[name])
        else:
            print(f"El producto '{name}' no se encuentra en el inventario")

    def update_product(self, name, quantity=None, price=None):
        if name in self.inventory:
            if quantity is not None:
                self.inventory[name].update_quantity(quantity)
                print(f"Cantidad actualizada a {quantity}")
            if price is not None:
                self.inventory[name].update_price(price)
                print(f"Precio actualizado a {price}")
        else:
            print(f"El producto '{name}' no existe")

    def delete_product(self,name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"Producto '{name}' eliminado del inventario.")
    
    def start(self):
        while True:
            print("\nGestor de Inventario")
            print("1.- Agregar Productos")
            print("2.- Listar Productos")
            print("3.- Buscar Producto")
            print("4.- Actualizar Producto")
            print("5.- Eliminar Producto")
            
            print("6.- Salir")

            choice = input("Seleccione una opción: ").strip()

            if choice == "1":
                name = input("Nombre del producto: ").strip()
                try:
                    quantity = int(input("Cantidad del producto: ").strip())
                    price = float(input("Precio del producto: ").strip())
                    self.add_product(name, quantity, price)
                except ValueError:
                    print("Ingrese valores numéricos válidos")

            elif choice == "2":
                self.list_products()

            elif choice == "3":
                name = input("Nombre del producto a buscar: ").strip()
                self.search_product(name)

            elif choice == "4":
                name = input("Nombre del producto a actualizar: ").strip()
                try:
                    quantity = input("Nueva cantidad (Enter para no cambiar): ").strip()
                    price = input("Nuevo precio (Enter para no cambiar): ").strip()
                    quantity = int(quantity) if quantity else None
                    price = float(price) if price else None
                    self.update_product(name, quantity, price)
                except ValueError:
                    print("Ingrese valores numéricos válidos")
            elif choice=="5":
                name=input("Nombre del producto a eliminar:").strip()
                self.delete_product(name)
            elif choice == "6":
                print("Saliendo del gestor de inventario. ¡Adiós!")
                break
            else:
                print("Opción no válida")



if __name__ == "__main__":
    inventory_manager = InventoryManager()
    inventory_manager.start()
