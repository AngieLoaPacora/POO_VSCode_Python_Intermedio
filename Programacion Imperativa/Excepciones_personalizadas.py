"""
Raise; se utiliza para lanzar excepciones de forma explicita y puede ser usado para manejar errores
o controlar el flujo del programa
"""

#Definicion de la excepción personalizada
class Mierror(Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)
        
        
#Función que lanza laexcepción personalizada
def verificar_edad(edad):
    if edad <0:
        raise Mierror("La edad no puede ser negativa")        
    return edad

# #Ejecución de la funcion
# try:
#     print(verificar_edad(25)) #Imprimir edad
#     print(verificar_edad(-5)) #Lanzar Mierror
# except Mierror as err:
#     print(f"Error {err}")
def dividir(a,b):
    if b==0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a/b

try:
    resultado=dividir(10,0)
except ZeroDivisionError as err:
    print(f"Error {err}")

"""
Assert; se usa para comprobar condiciones que deberian ser verdaderas en tiempo de desarrolla  puede ayudar a detectar errores en etapas tempranas
"""

def calcular_media(lista):
    assert len(lista)>0, "La lista no puede estar vacia"
    return sum(lista)/len(lista)
# print(calcular_media([1,2,3,4,5])) #3.0
# print(calcular_media([])) #Lanza AssertionError

try:
    edad=int(input("Ingrese la edad:"))
    assert edad>0, "Error: La edad No puede ser negativa"
    print(f"edad ingresada correctamente")
except (ValueError, AssertionError) as err:
    print(f"{err}")
    