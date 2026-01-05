import tkinter as tk

def mostrar_texto():
    texto=entrada.get() #Capturar el texto ingresado
    etiqueta.config(text=f"texto ingresado:{texto}")

def mostrar_mensaje():
    etiqueta.config(text="Boton Presionado 🥳")

#Crear una Ventana Principal

ventana=tk.Tk()
ventana.title("Ventana Básica")

#Establecer el tamaño de la ventana
ventana.geometry("300x200")

#Crear Widget de tipo de etiqueta
etiqueta=tk.Label(ventana,text=" 👀 Hola usando la librería Tkinter  ☀️")
etiqueta.pack()

entrada=tk.Entry(ventana)
entrada.pack()

#Crear un boton
boton=tk.Button(ventana,text="Presioname 🟡",command=mostrar_texto)
boton.pack()

#Iniciar el bucle principal de la aplicación
ventana.mainloop()
