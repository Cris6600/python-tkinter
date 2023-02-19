from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3

def conexionBBDD():

    con = sqlite3.connect("mi_usuario")

    cur = con.cursor()

    try:

        cur.execute('''
            CREATE TABLE usuarios(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre VARCHAR(50), 
            apellido VARCHAR(50))
            ''')

        messagebox.showinfo("BBDD", "BBDD creada con exito")

    except:
        messagebox.showinfo("Atencion", "La BBDD ya existe")

def limpiarCampos():
    id.set("")
    nombres.set("")
    apellido.set("")

def crearBBDD():
    con = sqlite3.connect("mi_usuario")
    
    cur = con.cursor()
    cur.execute("INSERT INTO usuarios VALUES(NULL, '" + nombres.get()+ 
                "','" + apellido.get()+ "')")
                
        
    con.commit()

    messagebox.showinfo("BBDD", "Registro insertado con exito")

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

id=StringVar()
nombres=StringVar()
apellido= StringVar()



ttk.Label(frm, text="ID").grid(column=0, row=0)
ttk.Entry(frm,textvariable = id).grid(column=1, row=0)
ttk.Label(frm, text="Nombre").grid(column=0, row=1)
ttk.Entry(frm, textvariable=nombres).grid(column=1, row=1)
ttk.Label(frm, text="Apellido").grid(column=0, row=2)
ttk.Entry(frm, textvariable=apellido).grid(column=1, row=2)
ttk.Button(frm, text="Conectar", command=conexionBBDD).grid(column=0, row=3)
ttk.Button(frm, text="Guardar", command=crearBBDD).grid(column=1, row=3)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=2, row=3)
ttk.Button(frm, text="Limpiar", command=limpiarCampos).grid(column=3, row=3)



root.mainloop()