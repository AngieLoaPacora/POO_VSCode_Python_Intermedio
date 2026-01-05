class Vehiculo:
    def __init__(self,marca,modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año
    def mostrar_informacion(self):
        return f"{self.marca} {self.modelo} ({self.año})"
    
class Coche(Vehiculo):
    def __init__(self,marca,modelo,año,numero_puertas):
        super().__init__(marca,modelo,año)
        self.numero_puertas=numero_puertas
    def mostrar_informacion(self):
        base_info=super().mostrar_informacion()
        return f"{base_info}, Puertas {self.numero_puertas}"
    
class Motocicleta(Vehiculo):
    def __init__(self,marca,modelo,año,tipo_motor):
        super().__init__(marca,modelo,año)
        self.tipo_motor=tipo_motor
        
#Crear instancias de los vehiculos
mi_coche=Coche("Toyota","Corolla",2020,4)
mi_motocicleta=Motocicleta("Harley-Davidson","Iron 883", 2020, "V-TWIN")

#Mostrar la informacion de los vehiculos
print(mi_coche.mostrar_informacion())
print(mi_motocicleta.mostrar_informacion())
    