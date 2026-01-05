import tkinter as tk
from tkinter import messagebox

class SumadorApp:
    def __init__(self,master):
        self.master=master
        master.title("Sumador")
        
        self.label1=tk.Label(master, text="Número 1")
        self.label1.grid(row=0, column=0)
        
        self.entry1=tk.Entry(master)
        self.entry1.grid(row=0, column=1)
        
        self.label2=tk.Label(master, text="Número 2")
        self.label2.grid(row=1, column=0)
        
        self.entry2=tk.Entry(master)
        self.entry2.grid(row=1, column=1)
        
        self.result_label=tk.Label(master, text="")
        self.result_label.grid(row=2, columnspan=2)
        
        self.sumar_buton=tk.Button(master, text="Sumar", command=self.sumar)
        self.sumar_buton.grid(row=3, columnspan=2)
        
        self.boton_salir=tk.Button(master, text="Salir", command=self.salir)
        self.boton_salir.grid(row=4, columnspan=2)
        
        
    def sumar(self):
        num1=float(self.entry1.get())
        num2=float(self.entry2.get())
        reusltado=num1+num2
        self.result_label.config(text=f"La suma es {reusltado}")
    
    def salir(self):
        if messagebox.askokcancel("Salir", "¿Está seguro de que quieres salir?"):
            self.master.destroy()
        
if __name__=="__main__":
    root=tk.Tk()
    app=SumadorApp(root)
    root.mainloop()
            