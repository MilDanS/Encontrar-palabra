from sqlite3 import *
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

#def agregarpalabras ():

baseDeDatos = connect("EncontrarPalabra.db")
cr =baseDeDatos.cursor()

app = Tk()
app.title("Juego Adivina Palabra")

