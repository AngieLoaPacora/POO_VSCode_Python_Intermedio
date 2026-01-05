from empleados import leer_empleados, crear_empleado, actualizar_empleado, eliminar_empleado
from colorama import Fore,Style,init

init(autoreset=True)

def mostrar_menu():
    while True:
        print(Fore.MAGENTA+"\n-------Menu Crud de Empleados------")
        print(Fore.MAGENTA+"1-Leer todos los empleados")
        print(Fore.MAGENTA+"2-Crear un nuevo empleados")
        print(Fore.MAGENTA+"3-Actualizar todos los empleados")
        print(Fore.MAGENTA+"4-Eliminar Empleados")
        print(Fore.MAGENTA+"5-Salir")
        opcion=input(Fore.YELLOW+"\nElige una opción:")
        if opcion=="1":
            leer_empleados()
        elif opcion=="2":
            crear_empleado()
        elif opcion=="3":
            actualizar_empleado()
        elif opcion=="4":
            eliminar_empleado()
        elif opcion=="5":
            print(Fore.CYAN+"Saliendo del programa...")
            break
        else:
            print(Fore.RED+"Opción no Valida. Inténtelo de nuevo")
            