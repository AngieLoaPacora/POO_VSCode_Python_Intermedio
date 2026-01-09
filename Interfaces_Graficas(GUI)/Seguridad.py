import tkinter as tk
from tkinter import messagebox
import sqlite3

class LogiApp:
    def __init__(self, root):
        self.root=root
        self.root.title("Sistema de seguridad")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")
        
        #Mostrar la pantalla de login
        self.show_login_screen()
        
    def show_login_screen(self):
        self.clear_screen()
        self.login_frame=tk.Frame(self.root, bg="white", bd=2, relief=tk.SOLID, padx=10, pady=10)
        self.login_frame.pack(padx=20, pady=20)
        
        tk.Label(self.login_frame, text="Iniciar sesión", font=("Comics sans", 18), bg="red").grid(row=0, columnspan=2, pady=10)
        
        tk.Label(self.login_frame, text="Usuario", bg="white").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_login_username=tk.Entry(self.login_frame, width=30)
        self.entry_login_username.grid(row=1, column=1, pady=5)
        
        tk.Label(self.login_frame, text="Contraseña", bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_login_username=tk.Entry(self.login_frame, show="*", width=30)
        self.entry_login_username.grid(row=2, column=1, pady=5)
        
        tk.Button(self.login_frame, text="Iniciar Sesión", command="",  bg="#007bff", fg="white", width=15).grid(row=3, columnspan=2, pady=10)
        
        tk.Button(self.login_frame, text="Registrarse", command="",  bg="#28a745", fg="white", width=15).grid(row=4, columnspan=2, pady=10)
        
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()    
        
if __name__=="__main__":
    root=tk.Tk()
    app=LogiApp(root)
    root.mainloop()