#Definición de una clase

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    
    #Creación de un objeto de la clase persona
persona1=Persona("Angie",34)
persona2=Persona("Regina", 35)
print(persona2.nombre)
print(persona2.edad)
print(persona2.saludar())
print(persona2.__dict__)



