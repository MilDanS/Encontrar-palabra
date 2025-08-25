from sqlite3 import *
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

#def agregarpalabras ():

baseDeDatos = connect("EncontrarPalabra.db")
cr =baseDeDatos.cursor()

app = Tk()
app.title("Juego Adivina Palabra")

neword =Label(app, text="Ingrese una palabra")
descripcion =Label(app, text="Ingrese la descripción")

palabra = Entry(app)
Descrip = Text(app, width=15, height=3)

neword.grid(row=0, column=0, pady=5, padx=5)
descripcion.grid(row=1, column=0, pady=5, padx=5)
palabra.grid(row=0, column=1, pady=5, padx=5)
Descrip.grid(row=1, column=1, pady=5, padx=5)

app.mainloop()