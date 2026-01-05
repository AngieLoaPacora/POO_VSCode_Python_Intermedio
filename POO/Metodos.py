class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        import math
        return math.pi * (self.radio ** 2)

    # Método para cambiar el radio
    def cambiar_radio(self, nuevo_radio):
        self.radio = nuevo_radio

# Crear objeto
mi_circulo = Circulo(5)
print(f"Área del círculo: {mi_circulo.area()}")

# Cambiar el radio
mi_circulo.cambiar_radio(10)
print(f"Nuevo área del círculo: {mi_circulo.area()}")

"""
Métodos de Clase
"""

class Circulo():
    pi=3.14159
    
    def __init__(self,radio):
        self.radio=radio
        
    @classmethod
    def crear_unidad(cls):
        return cls(1) #Crea un circulo con radio1
    
    def area(self):
        return Circulo.pi * (self.radio **2)
    
#Crear un objeto usando el método de clase
circulo_unidad=Circulo.crear_unidad()
print(f"Area del circulo unidad {circulo_unidad.area()}")

"""
Métodos estáticos
"""

class Calculadora():
    @staticmethod
    def sumar(a,b):
        return a+b
    @staticmethod
    def restar(a,b):
        return a-b

#Llamar a los métodos estáticos sin crear una instancia
print(f"Suma {Calculadora.sumar(5,3)}")
print(f"Resta {Calculadora.restar(5,3)}")
