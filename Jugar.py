from random import *
from sqlite3 import *
from customtkinter import *

baseDeDatos = connect("EncontrarPalabra.db")
cr = baseDeDatos.cursor()

app = CTk()
app.title("Juego Adivina Palabra")

Intentos = 3
Fallos = 0
Word = " "
Desc = " "






