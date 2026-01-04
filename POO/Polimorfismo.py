#CLASE BASE
class Animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def hacer_sonido(self):
        raise NotImplementedError("Este Método debe ser sobreescrito por las subclases")
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
#SUBCLASES DERIVADAS DE LA CLASE BASE ANIMAL    

class Perro(Animal):
    def hacer_sonido(self):
        return 'Ladrido'
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Maullido"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"
    
#Función que acepte un objeto de tipo animal y llame el método hacer_sonido
def hacer_sonido_animal(animal):
    print(f"{animal} hace: {animal.hacer_sonido()}")
    
#Crear instancias de las subclases

mi_perro=Perro(nombre="Rex", edad=5)
mi_gato=Gato(nombre="Felix", edad=10)
mi_vaca=Vaca(nombre="Blanca", edad=7)

#Usar Polimorfismo para llamar al método hacer_sonido en diferentes tipos de animales
hacer_sonido_animal(mi_perro)
hacer_sonido_animal(mi_gato)
hacer_sonido_animal(mi_vaca)
