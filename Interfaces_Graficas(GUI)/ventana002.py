import tkinter as tk

ventana=tk.Tk()
ventana.title("Uso de Frame y Grid")

#Crear un marco
frame=tk.Frame(ventana, borderwidth=2, relief="groove")
frame.pack(padx=10, pady=10, fill="both", expand=True)

#Crear widgets en el marco
etiqueta1=tk.Label(frame,text="Etiqueta 1")
etiqueta1.grid(row=0, column=0)

etiqueta2=tk.Label(frame,text="Etiqueta 2")
etiqueta2.grid(row=0,column=1)

boton1=tk.Button(frame, text="Botón 1")
boton1.grid(row=1,column=0)

boton2=tk.Button(frame, text="Botón 2")
boton2.grid(row=1, column=1)

ventana.mainloop()