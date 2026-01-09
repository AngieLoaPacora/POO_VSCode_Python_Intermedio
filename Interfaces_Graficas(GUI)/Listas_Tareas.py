import tkinter as tk
from tkinter import messagebox

def agregar_tarea(entrada, lista):
    tarea=entrada.get()
    if tarea:
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)

def eliminar_tarea(lista):
    tarea_seleccionada=lista.curselection()
    if tarea_seleccionada:
        lista.delete(tarea_seleccionada)
        
def salir(ventana):
    if messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?"):
        ventana.destroy()

def principal():
    ventana=tk.Tk()
    ventana.title("Listas Tareas")
    
    #Creando los Widget
    marco_lista=tk.Frame(ventana)
    marco_lista.pack(pady=10)
    
    listas_tareas=tk.Listbox(marco_lista, width=50, height=10)
    listas_tareas.pack(side=tk.LEFT, fill=tk.BOTH)
    
    scrollbar=tk.Scrollbar(marco_lista, orient=tk.VERTICAL)
    scrollbar.config(command=listas_tareas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listas_tareas.config(yscrollcommand=scrollbar.set)
    
    marco_entrada=tk.Frame(ventana)
    marco_entrada.pack(pady=5)
    
    etiqueta_tarea=tk.Label(marco_entrada, text="Nueva Tarea")
    etiqueta_tarea.pack(side=tk.LEFT)
    entrada_tarea=tk.Entry(marco_entrada, width=40)
    entrada_tarea.pack(side=tk.LEFT)
    
    boton_agregar=tk.Button(ventana, text="Agregar Tarea", command=lambda:agregar_tarea(entrada_tarea, listas_tareas))
    boton_agregar.pack(pady=5)
    
    boton_eliminar=tk.Button(ventana, text="Eliminar Tarea", command=lambda:eliminar_tarea(listas_tareas))
    boton_eliminar.pack(pady=5)
    
    boton_salir=tk.Button(ventana, text="Salir", command=lambda:salir(ventana))
    boton_salir.pack(pady=5)
    ventana.mainloop()
    
if __name__=="__main__":
        principal()
        
    
    